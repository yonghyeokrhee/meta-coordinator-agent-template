# HEARTBEAT

- 매 1시간마다 `RESOLVED`가 아닌 상태의 CS 이슈가 있는지 확인한다.
- 상태 확인은 최근 채팅이나 세션 로그가 아니라 활성 `CS Management Tool` 기준으로 수행한다.
- 현재 활성 도구는 `Notion / Optapex Manual / CS Intake Queue` 다.
- 가능하면 먼저 `python3 scripts/cs_management.py summary`로 열린 이슈를 조회한다.
- 열린 이슈가 있으면 현재 상태와 가장 가까운 다음 액션만 짧게 정리한다.
- 이 Discord 채널에는 반드시 `message(action=send)`로 visible update를 보낸다.
- 열린 이슈가 없으면 `message(action=send)`로 `현재 열린 CS 이슈 없음. 모두 resolved 상태입니다.` 라고 보낸다.
- 실제로 알릴 내용이 없을 때만 `HEARTBEAT_OK`로 끝낸다.
