---
name: optapex-cs-answer
description: Optapex CS 답변 전용 스킬. 이미 접수된 Optapex 문의에 대해 Skeleton을 확인하고, Knowledge Map을 따라 실제 markdown 근거를 확인한 뒤 바로 답변하거나 필요한 경우에만 backlog/owner 라우팅으로 넘긴다. 채팅에는 workflow 설명 없이 답변만 보낸다. MOP 서비스 문의에는 사용하지 않는다.
---

# Optapex CS Answer

이 스킬은 **Optapex CS 답변 전용**이다.
MOP 서비스 문의에는 사용하지 않는다.

## 기본 흐름
1. 접수된 문의의 Skeleton을 확인한다.
2. 한 메시지 안에 여러 이슈가 섞였는지 먼저 판단한다.
3. 즉답형 / backlog 확인형 / 에스컬레이션형이 섞여 있으면 질문 단위로 분리한다.
4. 분리된 질문 목록과 bucket 판단을 질문자인 AM에게 먼저 확인받는다.
5. 상태 추적/관리 맥락이면 먼저 `CS Management Tool`을 확인한다.
6. 에스컬레이션 필요 여부를 먼저 판단한다.
7. 에스컬레이션이 아니면 backlog 확인형 여부를 판단한다.
8. 둘 다 아니면 즉답형 여부를 판단한다.
9. `knowledge/optapex_help_center_sections_kr/00_Index.md` 를 먼저 읽고 질문과 연결된 파일 목록을 고른다.
10. Index가 가리킨 실제 markdown 문서를 직접 읽는다.
11. 위 문서만으로 부족하거나, 시스템/운영 이슈 / 공개 Help Center와 내부 문서 충돌 / 에스컬레이션 판단이 애매한 경우에만 `references/optapex-source-routing.md` 를 예외적으로 참고한다.
12. backlog는 **별도 필수 2차 조회가 아니라**, Index 또는 실제 section 문서를 읽은 뒤에도 질문이 `알려진 이슈 / ETA / 출시 예정 / 가능 여부`에 해당할 때만 `knowledge/03_optapex_backlog.md` 를 추가로 확인한다.
12. 답변 가능하면 채팅에 답변만 보낸다.
13. 답변이 나가면 `CS Intake Queue`에 답변 기록을 남긴다.
14. 담당자 확인 전이면 `PENDING`으로 두고 종결 여부 확인을 남긴다.
15. 답변이 불가하면 `PENDING` 또는 `ASSIGNED`로 유지하고 다음 액션을 남긴다.
16. `Q1 / Q2 / Q3` 모두 No 인 경우에는 `KB gap / 문서화 필요`로 기록하고 지식 보강 후보를 남긴다.

## 답변 원칙
- `00_Index.md` 는 항상 첫 진입점으로 쓰되, 파일 선택용으로만 쓴다.
- 인덱스만 보고 답하지 않는다.
- 답변 근거는 선택된 실제 markdown 문서에서만 잡는다.
- **답변 근거가 될 만한 실제 문서를 확보했고 그 문서만으로 결론이 났으면, 추가 탐색은 하지 않는다.**
- **추가 탐색은 현재 문서만으로 결론이 나지 않거나, 에스컬레이션/known issue/공개문구 우선순위 충돌 판단이 남아 있을 때만 한다.**
- backlog는 자동 추가 조회 대상이 아니라, index 기반 선택 이후에도 일정/known issue 확인이 남을 때만 여는 예외 source다.
- KB에 일반 설명이 있다는 이유만으로 즉답형으로 보내지 않는다.
- 계정별 확인, 운영 조치, 기술 확인이 필요하면 먼저 에스컬레이션형으로 본다.
- `Q1 / Q2 / Q3` 모두 No 인 경우는 지식 공백으로 보고 `KB gap / 문서화 필요`를 남긴다.
- KB markdown 근거로 바로 답하는 경우, 답변에 사용한 근거의 **실제 근거 문구 + 지식 문서명**을 반드시 포함한다.
- `Source: knowledge/...#L...` 같은 path/line-range 인용은 사용자 답변에 쓰지 않는다.
- 근거는 실제로 읽은 파일 기준으로만 달고, 사용자에게는 file path/line range 대신 실제 답변의 근거가 된 짧은 구문을 직접 적는다.
- 기본 포맷은 아래처럼 둔다.
  - `답변 근거`
  - `**{실제 근거 문구}** / **{지식 문서명}**`
- multi-issue 인 경우에는 agent가 먼저 분리안을 제시하고 질문자인 AM에게 확인받는다.
- 즉답형 항목과 에스컬레이션형 항목을 한 답변 카드로 억지 통합하지 않는다.
- 한 줄 결론부터 준다.
- 고객이 바로 알아야 할 조건과 예외만 짧게 덧붙인다.
- workflow 설명 요청이 아닌 이상, 채팅에는 내부 절차를 쓰지 않는다.

## backlog를 추가로 열 수 있는 질문
- 알려진 이슈인가요?
- 언제 되나요?
- 출시 예정인가요?
- 가능한 기능인가요?

위 질문이라도 먼저 `00_Index.md` 와 선택된 실제 markdown 문서를 확인한다.
그 뒤에도 일정 / known issue / 가능 여부 확인이 남아 있을 때만 backlog를 연다.

단, 위 질문처럼 보여도 실제 계정 상태 확인, 운영 조치, 기술 확인이 함께 필요하면 backlog 확인형보다 **에스컬레이션형을 우선**한다.
backlog 정보는 이 경우 보조 근거로만 사용한다.

## 상태 운용
- 시작: `NEW`
- 답변 탐색 시작 가능: `TRIAGED`
- 사람/엔지니어 후속 필요: `ASSIGNED`
- 답변 후 담당자 확인 대기: `PENDING`
- 담당자 확인 또는 종결 확인 완료: `RESOLVED`

bucket은 질문 단위에서 상호배타적으로 본다. 하나의 질문은 하나의 bucket만 가진다.
새 상태를 만들지 않는다.

## CS 관리 도구
- 현재 활성 CS 관리 도구는 `Notion / Optapex Manual / CS Intake Queue` 다.
- heartbeat, 열린 이슈 확인, 상태 요약은 이 도구를 먼저 본다.
- provider 설정과 migration 포인트는 `state/cs-management-tool.json`을 기준으로 관리한다.

## 참고 문서
- 답변 워크플로: `AGENTS.md`
- 운영 성향: `SOUL.md`
- 설계/수정 맥락 구분: `references/little-j-maintenance-mode.md`
- CS 관리 도구 계약: `references/cs-management-tool.md`
- source 선택 규칙: `references/optapex-source-routing.md`
- help-center 질문 축: `references/optapex-help-center-taxonomy.md`
- backlog 원문: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/03_optapex_backlog.md`
- canonical workspace skill: `skills/optapex-cs-answer/SKILL.md`
- canonical knowledge folder: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge`
