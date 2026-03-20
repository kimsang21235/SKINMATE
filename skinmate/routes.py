
from __future__ import annotations

import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from flask import current_app, flash, jsonify, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename

from skinmate.db import get_db
from skinmate.services.analysis_service import get_skin_scores
from skinmate.services.recommendation_service import generate_recommendations, generate_result_summary
from skinmate.services.routine_service import build_recommendations_payload
from skinmate.utils.image_utils import allowed_file, is_face_image, resize_image_if_needed


def init_main_routes(app):
    @app.route('/', endpoint='index')
    def index():
        return render_template('index.html')

    @app.route('/introduction', endpoint='introduction')
    def introduction():
        return render_template('introduction.html')

    @app.route('/analysis', endpoint='analysis')
    def analysis():
        return render_template('analysis.html')

    @app.route('/history', endpoint='history')
    def history():
        if 'user_id' not in session:
            flash('기록을 보려면 먼저 로그인해주세요.')
            return redirect(url_for('login'))

        db = get_db()
        rows = db.execute('SELECT * FROM analyses WHERE user_id = ? ORDER BY analysis_timestamp DESC', (session['user_id'],)).fetchall()
        processed = []
        for row in rows:
            item = dict(row)
            try:
                scores = json.loads(item.get('scores_json') or '{}')
            except Exception:
                scores = {}
            numeric_scores = [scores.get(k, 0) for k in ('moisture', 'elasticity', 'wrinkle') if isinstance(scores.get(k), (int, float))]
            item['main_score'] = round(sum(numeric_scores) / len(numeric_scores), 1) if numeric_scores else 0
            processed.append(item)
        return render_template('history.html', analyses=processed)

    @app.route('/skin_diary', endpoint='skin_diary')
    def skin_diary():
        if 'user_id' not in session:
            flash('피부 일지를 보려면 먼저 로그인해주세요.')
            return redirect(url_for('login'))
        return render_template('skin_diary.html')

    @app.route('/api/history')
    def api_history():
        if 'user_id' not in session:
            return jsonify({'error': 'User not logged in'}), 401

        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
        except Exception:
            end_date = datetime.now().replace(hour=23, minute=59, second=59)
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
        except Exception:
            start_date = (end_date - timedelta(days=6)).replace(hour=0, minute=0, second=0)

        db = get_db()
        analyses = db.execute(
            'SELECT analysis_timestamp, scores_json FROM analyses WHERE user_id = ? AND analysis_timestamp BETWEEN ? AND ? ORDER BY analysis_timestamp ASC',
            (session['user_id'], start_date, end_date),
        ).fetchall()

        buckets = {}
        current = start_date.date()
        while current <= end_date.date():
            buckets[current.strftime('%Y-%m-%d')] = {'moisture': [], 'elasticity': [], 'wrinkle': []}
            current += timedelta(days=1)

        for row in analyses:
            key = row['analysis_timestamp'].strftime('%Y-%m-%d')
            try:
                scores = json.loads(row['scores_json'])
            except Exception:
                continue
            for metric in ('moisture', 'elasticity', 'wrinkle'):
                if isinstance(scores.get(metric), (int, float)):
                    buckets[key][metric].append(scores[metric])

        graph_dates, graph_moisture, graph_elasticity, graph_wrinkle = [], [], [], []
        for key, values in buckets.items():
            graph_dates.append(datetime.strptime(key, '%Y-%m-%d').strftime('%m-%d'))
            graph_moisture.append(round(sum(values['moisture']) / len(values['moisture']), 1) if values['moisture'] else 0)
            graph_elasticity.append(round(sum(values['elasticity']) / len(values['elasticity']), 1) if values['elasticity'] else 0)
            graph_wrinkle.append(round(sum(values['wrinkle']) / len(values['wrinkle']), 1) if values['wrinkle'] else 0)

        return jsonify(
            graph_dates=graph_dates,
            graph_moisture=graph_moisture,
            graph_elasticity=graph_elasticity,
            graph_wrinkle=graph_wrinkle,
        )

    @app.route('/delete_analysis/<int:analysis_id>', methods=['POST'], endpoint='delete_analysis')
    def delete_analysis(analysis_id: int):
        if 'user_id' not in session:
            flash('권한이 없습니다.', 'danger')
            return redirect(url_for('login'))
        db = get_db()
        row = db.execute('SELECT * FROM analyses WHERE id = ? AND user_id = ?', (analysis_id, session['user_id'])).fetchone()
        if row is None:
            flash('존재하지 않는 분석 기록입니다.', 'danger')
        else:
            db.execute('DELETE FROM analyses WHERE id = ?', (analysis_id,))
            db.commit()
            flash('분석 기록이 삭제되었습니다.', 'success')
        return redirect(url_for('history'))

    @app.route('/delete_selected_analyses', methods=['POST'], endpoint='delete_selected_analyses')
    def delete_selected_analyses():
        if 'user_id' not in session:
            flash('권한이 없습니다.', 'danger')
            return redirect(url_for('login'))
        ids = request.form.getlist('analysis_ids')
        if not ids:
            flash('삭제할 기록을 선택해주세요.', 'info')
            return redirect(url_for('history'))
        db = get_db()
        placeholders = ','.join('?' for _ in ids)
        db.execute(f'DELETE FROM analyses WHERE id IN ({placeholders}) AND user_id = ?', [*ids, session['user_id']])
        db.commit()
        flash('선택한 분석 기록이 삭제되었습니다.', 'success')
        return redirect(url_for('history'))

    @app.route('/analyze', methods=['POST'], endpoint='analyze_image')
    def analyze_image():
        if 'user_id' not in session:
            flash('분석을 진행하려면 먼저 로그인해주세요.', 'info')
            return redirect(url_for('login'))

        file = request.files.get('image')
        if file is None or file.filename == '':
            flash('파일이 선택되지 않았습니다.', 'danger')
            return redirect(url_for('analysis'))

        if not allowed_file(file.filename, current_app.config['ALLOWED_EXTENSIONS']):
            flash('허용되지 않는 파일 형식입니다.', 'danger')
            return redirect(url_for('analysis'))

        filename = secure_filename(file.filename)
        upload_dir = Path(current_app.config['UPLOAD_DIR'])
        upload_dir.mkdir(parents=True, exist_ok=True)
        temp_path = upload_dir / filename
        file.save(temp_path)

        resize_image_if_needed(temp_path, max_size_mb=1.0)
        if not is_face_image(temp_path):
            temp_path.unlink(missing_ok=True)
            flash('얼굴이 인식되지 않습니다. 얼굴이 보이는 사진을 업로드해주세요.', 'danger')
            return redirect(url_for('analysis'))

        scores = get_skin_scores(temp_path)
        reco_data = generate_recommendations(scores, session.get('username', '방문자'))
        skin_type = scores.get('skin_type', '알 수 없음')
        concerns = reco_data['concerns_for_template']
        recommendations_data = build_recommendations_payload(session.get('username', '방문자'), skin_type, concerns)
        session['recommendations_data'] = recommendations_data

        db = get_db()
        scores_serializable = {
            'moisture': float(scores.get('moisture', 55.0)),
            'elasticity': float(scores.get('elasticity', 58.0)),
            'wrinkle': float(scores.get('wrinkle', 52.0)),
            'skin_type': skin_type,
        }
        db.execute(
            'INSERT INTO analyses (user_id, skin_type, recommendation_text, scores_json, concerns_json, image_filename) VALUES (?, ?, ?, ?, ?, ?)',
            (session['user_id'], skin_type, reco_data['recommendation_text'], json.dumps(scores_serializable, ensure_ascii=False), json.dumps(concerns, ensure_ascii=False), filename),
        )
        db.commit()

        static_upload_dir = Path(current_app.config['STATIC_UPLOADS_DIR'])
        static_upload_dir.mkdir(parents=True, exist_ok=True)
        final_path = static_upload_dir / filename
        if final_path.exists():
            final_path.unlink()
        shutil.move(str(temp_path), str(final_path))

        concern_scores = {k: scores_serializable[k] for k in ('moisture', 'elasticity', 'wrinkle')}
        main_score = sum(concern_scores.values()) / len(concern_scores)
        result_summary = generate_result_summary(session.get('username', '방문자'), main_score, skin_type, reco_data['top_concerns_names'])

        return render_template(
            'result.html',
            main_score=main_score,
            scores=concern_scores,
            uploaded_image=url_for('static', filename=f'uploads_temp/{filename}'),
            result_summary=result_summary,
            recommendations=recommendations_data,
            skin_type=skin_type,
            original_scores=scores_serializable,
        )

    @app.route('/routines', endpoint='routines')
    def routines():
        recommendations_data = session.get('recommendations_data')
        if not recommendations_data:
            flash('먼저 피부 분석을 진행해주세요.', 'info')
            return redirect(url_for('analysis'))
        return render_template('routines.html', recommendations=recommendations_data)

    @app.route('/recommendations', endpoint='recommendations')
    def recommendations():
        recommendations_data = session.get('recommendations_data')
        if not recommendations_data:
            flash('먼저 피부 분석을 진행해주세요.', 'info')
            return redirect(url_for('analysis'))
        return render_template('recommendations.html', recommendations=recommendations_data)

    @app.route('/healthz')
    def healthz():
        return {'status': 'ok'}
