# 🌟 SKINMATE (Refactored Portfolio Version)

![SKINMATE Banner](./docs/screenshots/skinmate_시연.gif)

## ✨ 프로젝트 소개

SKINMATE는 AI 기반 피부 분석을 통해 사용자에게 맞춤형 스킨케어 루틴과
제품을 추천하는 서비스입니다.

기존 피부 분석 서비스는 단순 분류에 그치는 경우가 많아
정량적인 피부 상태 분석과 개인화된 해석이 부족하다는 문제를 해결하고자 했습니다.

본 프로젝트는 **팀 프로젝트로 개발한 클라우드 기반 AI 서비스**를
👉 **개인 포트폴리오용으로 리팩토링하여 로컬에서도 실행 가능하도록 재구성한 버전**입니다.

---

## 🧑‍💻 역할

* 팀장으로서 프로젝트 전체 설계 및 진행 총괄
* AI 모델 파이프라인 구조 설계 (Detection + Regression)
* 피부 상태 회귀 모델 개발 및 Feature Selection 수행
* 모델 결과 해석 로직 설계 및 서비스 반영
* 데이터 특성 분석 및 일반화 한계(domain shift) 도출
* Flask 기반 서비스 구조 리팩토링

---

## 🔥 프로젝트 배경 및 리팩토링

### ✔ Original Team Project

* Google Cloud Vertex AI 기반 피부 타입 분류
* Cloud Run 배포 환경
* 4개 AI 모델 통합 분석 파이프라인

### ✔ Refactored Portfolio Version

* Vertex AI 제거 → **로컬 실행 가능 구조로 변경**
* Flask 기반 모듈 구조 재설계
* 분석 → 추천 → 기록 흐름 통합
* 외부 의존성 없이 실행 가능한 데모 서비스 구현

---

## 🧠 AI 모델 설계 및 분석 과정

> 단순 모델 사용이 아닌, **서비스 관점에서의 AI 파이프라인 설계**를 수행했습니다.

### 📌 전체 파이프라인

```
이미지 입력 → 얼굴 부위 탐지 → 부위별 이미지 추출 → 임베딩 → 회귀 예측 → 상태 해석
```

---

### 1️⃣ 얼굴 부위 탐지 (Detection)

**사용 기술**

* Object Detection (Bounding Box 기반 영역 분리)
* 이미지 좌표 정규화 (0~1 scaling)

**설명**

* 얼굴 영역을 이마, 볼, 턱 등으로 분리
* 부위별 피부 상태 분석을 위한 전처리 단계

👉 단순 전체 얼굴 분석이 아닌 **부위별 분석 구조 설계**

---

### 2️⃣ 피부 상태 회귀 모델 (Regression)

**사용 기술**

* CNN 기반 Feature Embedding (2048-dim)
* Feature Selection (차원 축소: 2048 → 38)
* Regression Model (정량값 예측)

**설명**

* AIHub 피부 데이터 기반 학습
* 이미지 → 임베딩 벡터 변환 → 회귀 예측
* 출력: 피부 수분 등 연속적인 수치 값

---

### 3️⃣ 결과 해석 로직

**사용 기술**

* 통계 기반 구간화 (평균, 표준편차 활용)
* Rule-based Mapping

**설명**

* 예측값을 기반으로 상태 구간 정의
* 사용자에게 직관적인 상태 제공

예:

* Very Dry / Dry / Normal / Moist / Very Moist

👉 **AI 결과를 사용자 친화적으로 변환**

---

## 📊 Dataset & Training

* 데이터: **AIHub 한국인 피부 상태 측정 데이터**

**특징**

* 전문 장비 기반 정량 데이터 (수분, 탄력, 주름 등)
* 지도학습 기반 회귀 모델 학습 가능

---

## ⚠️ Model Performance & Limitation

* R² Score ≈ 0.97
* MAE ≈ 0.83

학습 데이터 기준으로는 높은 성능을 보였으나,
외부 이미지 입력 시 성능 저하가 발생했습니다.

### 📌 원인 분석

* 데이터는 **전문 장비 + 통제된 환경**
* 실제 사용자 이미지와의 **도메인 차이(domain shift)** 존재
* 모델이 피부 상태보다 **데이터셋 패턴을 학습했을 가능성**

---

### 📌 개선 방향

* 다양한 환경 데이터 확보
* 이미지 augmentation 및 normalization 개선
* 도메인 일반화 고려한 모델 개선

👉 **데이터와 일반화 성능의 중요성을 경험적으로 학습**

---

## 🔑 주요 기능

* AI 피부 분석 (TFLite 기반)
* 맞춤형 스킨케어 루틴 추천
* 피부 상태 점수 시각화
* 분석 기록 저장 및 조회
* 직관적인 UI/UX

---

## 🛠 기술 스택

### Backend

* Python, Flask (REST API 설계)
* Service Layer / Route Layer 분리 구조

### Frontend

* HTML, CSS, JavaScript

### Database

* SQLite (사용자 기록 및 분석 결과 저장)

### AI / 분석

* TensorFlow Lite (경량 모델 서빙)
* CNN Feature Embedding
* Regression 기반 피부 상태 예측
* Feature Selection
* Object Detection 기반 부위 분리

---

## ⚙️ 예외 처리 및 안정성 설계

실제 서비스 환경을 고려하여 다음과 같은 예외 처리를 적용했습니다.

* 얼굴 인식 실패 시 분석 중단 및 사용자 안내
* 모델 추론 실패 시 fallback 로직 적용
* 입력 이미지 품질이 낮을 경우 예외 처리

### 📌 Fallback Heuristic Logic

* 모델 예측이 불가능한 경우
  👉 **기본 규칙 기반 피부 상태 추정 로직 적용**

예:

* 평균값 기반 점수 보정
* 기본 피부 타입 기준 추천 제공

👉 AI 모델 의존도를 낮추고 **서비스 안정성 확보**

---

## ⚙️ 실행 방법

```bash
pip install -r requirements.txt
python app.py
```

접속: http://127.0.0.1:5001

---

## 📸 실행 화면

### 메인

![메인](./docs/screenshots/01-main.png)

### 분석 결과

![결과](./docs/screenshots/03-result.png)

### 루틴 추천

![루틴](./docs/screenshots/04-morning-routine.png)

---

## 🚀 핵심 포인트

* 클라우드 기반 AI 서비스 → 로컬 실행형으로 리팩토링
* 객체 탐지 + 회귀 기반 AI 파이프라인 설계
* 데이터 기반 모델의 한계(domain shift) 분석
* 예외 처리 및 fallback 로직을 통한 서비스 안정성 확보

---

## 📌 한 줄 요약

AI 피부 분석 서비스를 단순 모델 구현이 아닌
👉 **서비스 관점에서 설계하고, 데이터 한계와 안정성까지 고려한 프로젝트**
