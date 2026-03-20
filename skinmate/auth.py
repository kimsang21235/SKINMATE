
from __future__ import annotations

import sqlite3
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from skinmate.db import get_db


def init_auth_routes(app):
    @app.route('/register', methods=['GET', 'POST'], endpoint='register')
    def register():
        if request.method == 'POST':
            username = request.form.get('username', '').strip()
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '')
            error = None

            if not username:
                error = '이름을 입력해주세요.'
            elif not email:
                error = '이메일을 입력해주세요.'
            elif not password:
                error = '비밀번호를 입력해주세요.'

            if error is None:
                db = get_db()
                try:
                    db.execute(
                        'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                        (username, email, generate_password_hash(password)),
                    )
                    db.commit()
                except sqlite3.IntegrityError:
                    error = f'이미 등록된 이메일입니다: {email}'
                else:
                    flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
                    return redirect(url_for('login'))

            flash(error, 'danger')
        return render_template('login.html')

    @app.route('/login', methods=['GET', 'POST'], endpoint='login')
    def login():
        if request.method == 'POST':
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '')
            db = get_db()
            user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

            if user is None or not check_password_hash(user['password_hash'], password):
                flash('잘못된 이메일 또는 비밀번호입니다.', 'danger')
            else:
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('로그인 성공!', 'success')
                return redirect(url_for('index'))

        return render_template('login.html')

    @app.route('/logout', endpoint='logout')
    def logout():
        session.clear()
        flash('로그아웃되었습니다.', 'info')
        return redirect(url_for('index'))
