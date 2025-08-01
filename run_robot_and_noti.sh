#!/bin/bash

# PYTHONPATH 설정 (현재 디렉토리를 모듈 경로로 추가)
export PYTHONPATH=$(pwd)

echo "[1] Robot 테스트 실행 중"
robot robot/test.robot

echo "[2] Slack으로 결과 전송 중"
python3 send_slack.py

# 실행은 이렇게
# chmod +x run_robot_and_noti.sh
# ./run_robot_and_noti.sh