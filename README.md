## 사전 요구사항
- Python 3.8+
- pip
- Node.js (Appium 설치용)
- 모바일 디바이스 또는 에뮬레이터

## 빠른 시작

### 1. 가상 환경 설정
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
npm install -g appium  # Appium 글로벌 설치
```

### 3. 환경 설정
`config/appium_config.json`에 디바이스 및 앱 설정 확인

### 4. 테스트 실행
#### Robot Framework 테스트
```bash
robot tests.robot 
```

## 전체 테스트 및 Slack 알림 전송 
```bash
chmod +x run_robot_and_noti.sh
./run_robot_and_noti.sh
```
