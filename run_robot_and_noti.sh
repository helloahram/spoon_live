#!/bin/bash

echo "[1] Robot 테스트 실행 중"
robot robot/web_access.robot

echo "[2] Slack으로 결과 전송 중"
python3 send_slack.py

# 실행은 이렇게
# chmod +x run_robot_and_noti.sh
# ./run_robot_and_noti.sh