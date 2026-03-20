# SKINMATE

사진 기반 피부 상태 점수화와 스킨케어 루틴 추천을 제공하는 Flask 기반 AI 피부 분석 서비스입니다. 기존 클라우드 의존형 프로토타입을 **로컬 실행 가능한 포트폴리오 프로젝트** 형태로 재구성했습니다.

## What this project does
- 회원가입 / 로그인 기반 사용자 세션 관리
- 얼굴 이미지 업로드 및 기본 검증
- TFLite 모델 기반 피부 점수 예측
- 피부 고민 요약 및 맞춤형 루틴 추천
- 분석 결과 저장 및 히스토리 조회

## Tech Stack
- Python, Flask
- SQLite
- TensorFlow Lite
- HTML / CSS / Jinja2

## Repository Structure
```text
SKINMATE/
├── app.py                     # Flask 실행 엔트리포인트
├── requirements.txt
├── .env.example
├── docs/
│   ├── ARCHITECTURE.md        # 요청 흐름 / 설계 의도
│   └── REPOSITORY_GUIDE.md    # GitHub 정리 가이드
├── tests/
│   └── smoke_test.py          # 간단 실행 점검 스크립트
├── uploads/                   # 업로드 임시 저장소 (gitkeep only)
└── skinmate/
    ├── __init__.py            # create_app
    ├── config.py              # 경로 / 설정값
    ├── db.py                  # SQLite 연결 / 초기화
    ├── auth.py                # 로그인 / 회원가입 / 로그아웃
    ├── routes.py              # 페이지 / 분석 / 기록 라우트
    ├── services/
    │   ├── analysis_service.py
    │   ├── recommendation_service.py
    │   └── routine_service.py
    ├── utils/
    │   ├── image_utils.py
    │   └── template_filters.py
    ├── templates/
    ├── static/
    │   ├── css/
    │   ├── images/
    │   └── uploads_temp/      # 런타임에만 사용
    └── resources/
        ├── models/
        ├── routine_rules.py
        └── seed/
```

## Local Run
```bash
pip install -r requirements.txt
python app.py
```

접속 주소:
```text
http://127.0.0.1:5001
```

## Demo Flow
1. 회원가입
2. 로그인
3. 피부 이미지 업로드
4. 분석 결과 확인
5. 추천 루틴 확인
6. 히스토리 조회

## Portfolio Highlights
- Vertex AI 의존성을 제거하고 로컬 재현이 가능하도록 리팩토링
- 기능별 책임을 인증 / 분석 / 추천 / 기록으로 분리
- 업로드부터 결과 저장까지 하나의 사용자 흐름으로 연결
- 포트폴리오 제출용으로 불필요한 런타임 산출물과 테스트 데이터를 제거

## Notes
- 피부 타입은 로컬 점수 기반 규칙으로 추정합니다.
- TensorFlow Lite 환경이 제한되면 fallback 점수를 사용하도록 설계되어 있습니다.
- 이 프로젝트는 상용 배포보다 포트폴리오 시연과 구조 설명에 초점을 둔 버전입니다.

## Security & GitHub Upload Notes
- `.env`, runtime database, uploaded images, and temporary files are excluded from version control.
- OAuth/API-related values belong in local environment variables only. The repository includes placeholders in `.env.example` instead of real keys.
- Before pushing, run a quick check such as `git status` and confirm that no secret files or personal data are staged.
