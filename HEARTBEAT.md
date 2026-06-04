# HEARTBEAT

이 heartbeat의 목적은 **현재 CS 상태를 사용자에게 1시간마다 요약해서 알리는 것**이다.

반드시 아래 순서를 그대로 따른다.

## 최우선 원칙
- heartbeat는 **매 실행마다** 현재 상태를 새롭게 확인하는 작업이다.
- heartbeat 본문에 들어가는 상태 요약은 **반드시 이번 heartbeat 실행에서 직접 조회한 Notion 결과**만 써야 한다.
- **매 heartbeat마다** `python3 scripts/cs_management.py summary`를 다시 실행해야 한다. 이전 실행 결과를 재사용하면 안 된다.
- 이전 heartbeat 메시지, thread starter, 최근 채팅, 세션 로그, 기억, 추정, 사람이 붙여 넣은 상태 요약은 **근거로 사용하면 안 된다.**
- `python3 scripts/cs_management.py summary` 실행이 없었거나 결과를 확인하지 못했으면, 정상 상태 요약을 보내면 안 된다.
- 이 문서의 목적은 “요약 작성”이 아니라 **Notion / Optapex Manual / CS Intake Queue 실조회 후 그 결과만 전송**하는 것이다.

1. 먼저 활성 `CS Management Tool`을 기준으로 상태를 조회한다.
   - 현재 기준 source of truth는 `Notion / Optapex Manual / CS Intake Queue` 다.
   - 조회 방식은 브라우저에서 Notion 페이지를 수동 확인하는 것이 아니라, `scripts/cs_management.py`가 Notion API로 `CS Intake Queue` database를 직접 조회하는 방식이다.
   - 최근 채팅, 세션 로그, 기억, 추정, thread starter에 적힌 이전 상태 요약으로 상태를 대신 판단하지 않는다.

2. 반드시 아래 명령을 **매 heartbeat 실행마다 직접 다시 실행**해서 열린 이슈를 조회한다.
   - `python3 scripts/cs_management.py summary`
   - 이 단계는 선택 사항이 아니다.
   - 직전 heartbeat에서 이미 실행했더라도, **이번 heartbeat용으로 다시 실행**해야 한다.
   - 이 명령은 Notion API를 호출해 최신 `createdAt` 기준으로 케이스를 조회하고, 그 결과를 바탕으로 열린 이슈 수와 상태별 개수를 계산한다.
   - heartbeat 상태 판단은 이 스크립트 실행 결과와 분리되면 안 된다.
   - **visible update를 보내기 직전에 실행한 최신 결과**를 사용한다.
   - 결과 JSON에서 최소한 `tool.kind`, `openCount`, `openByStatus`, `openCases`를 직접 확인한다.
   - `tool.kind != "notion"` 이거나 JSON 파싱/확인이 불가능하면 정상 요약으로 진행하지 말고 실패로 처리한다.

3. 스크립트 결과를 기준으로 `RESOLVED`가 아닌 케이스만 열린 이슈로 본다.
   - `openCount = 0` 이면 열린 CS 이슈가 없는 상태다.
   - `openCases` 가 있으면 각 케이스의 `status`, `title`, `notes`를 보고 가장 가까운 다음 액션만 짧게 정리한다.
   - `PENDING` 상태가 있으면 반드시 담당자에게 `RESOLVED 여부 확인 필요`라는 다음 액션을 넣는다.
   - 상태 요약 문구는 **오직 이 JSON 값들만 바탕으로 새로 작성**한다. 이전 heartbeat 문구를 복사/재사용하지 않는다.

4. 반드시 Discord parent 채널 `#cs-ai` (`1502969606409551953`)로 visible update를 보낸다.
   - `message(action=send, channel="discord", target="channel:1502969606409551953")`를 사용한다.
   - 현재 thread/session 문맥을 따라가게 두지 않는다.
   - 열린 이슈가 없으면 정확히 아래 문구를 보낸다.
     - `현재 열린 CS 이슈 없음. 모두 resolved 상태입니다.`
   - 열린 이슈가 있으면 아래 형식으로 짧게 요약한다.
     - 기준 source of truth
     - 조회 방식: `scripts/cs_management.py summary` / Notion API
     - 현재 열린 CS 이슈 수
     - status별 개수
     - 각 이슈의 제목 / 현재 status / 가장 가까운 다음 액션
   - `PENDING` 이슈는 다음 액션에 담당자 확인 요청을 반드시 포함한다.

5. 스크립트 실행이 실패하면 조용히 넘어가지 않는다.
   - 실패 사실을 이 채널에 visible update로 알린다.
   - 실패 메시지에는 `CS Intake Queue 상태 조회 실패`와 다음 확인 액션을 포함한다.
   - 이전 heartbeat 내용이나 thread starter 내용을 대신 전송하지 않는다.

6. 실제로 보낼 visible update가 전혀 없을 때만 `HEARTBEAT_OK`로 끝낸다.
   - 일반적인 경우에는 상태 요약 메시지를 보내고 끝낸다.

## 금지사항
- thread starter에 포함된 이전 heartbeat 요약을 현재 상태처럼 재진술하지 않는다.
- 최근 대화에 나온 숫자(`열린 이슈 수`, `status별 개수`)를 검증 없이 재사용하지 않는다.
- 이전 heartbeat에서 실행한 `python3 scripts/cs_management.py summary` 결과를 이번 heartbeat에 재사용하지 않는다.
- Notion 조회 실패 시 “아마 이전과 동일” 같은 보간을 하지 않는다.
- `message(action=send)`를 먼저 보내고 나중에 조회하지 않는다. 항상 **조회 후 전송** 순서를 지킨다.
