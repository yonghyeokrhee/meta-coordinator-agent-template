# CS Management Tool Contract

## 목적
CS 상태 추적, heartbeat 요약, 후속 관리가 **하나의 동일한 CS 관리 도구**를 바라보도록 강제하기 위한 공통 계약이다.

## 현재 활성 도구
- tool kind: `notion`
- tool name: `Optapex Manual`
- source of truth database: `CS Intake Queue`

즉, 현재 Little J가 보는 CS 상태의 단일 기준은:
**Notion의 `Optapex Manual / CS Intake Queue`** 다.

## 추상화 원칙
1. heartbeat는 임의 세션 기록이나 최근 채팅을 기준으로 상태를 추정하지 않는다.
2. CS 상태 추적/관리도 동일하게 `CS Intake Queue`를 먼저 본다.
3. 다른 도구로 migration 하더라도, workflow는 개별 도구명이 아니라 **CS Management Tool** 추상화를 기준으로 유지한다.
4. 도구별 세부 정보는 `state/cs-management-tool.json`에 둔다.
5. 상태 요약/열린 이슈 조회는 가능하면 `scripts/cs_management.py`를 통해 수행한다.

## canonical status
도구가 무엇이든 내부 workflow는 아래 canonical status만 사용한다.
- `NEW`
- `TRIAGED`
- `ASSIGNED`
- `PENDING`
- `RESOLVED`

외부 도구의 raw status 값은 필요하면 canonical status로 매핑해서 사용한다.

## heartbeat 규칙
- heartbeat는 항상 먼저 활성 CS Management Tool을 조회한다.
- `RESOLVED`가 아닌 케이스를 열린 이슈로 본다.
- 채널 요약에는 현재 열린 이슈 수, 각 이슈의 status, 가장 가까운 다음 액션만 짧게 담는다.
- `PENDING` 상태가 있으면 담당자 확인이 아직 남아 있는 것으로 보고, 요약에 반드시 `RESOLVED 여부 확인 필요`를 포함한다.

## 답변 기록 규칙
- 답변이 나가면 `CS Intake Queue`에 답변 기록을 남긴다.
- 답변 기록에는 최소한 답변이 나갔다는 사실, 시점, 종결 확인 필요 여부가 포함되어야 한다.
- 담당자 확인 전에는 `RESOLVED`로 닫지 않고 `PENDING`으로 둔다.
- 담당자 확인이 끝난 경우에만 `RESOLVED`로 변경한다.

## migration 규칙
- Notion → 다른 도구로 바뀌어도 `AGENTS.md`, `SOUL.md`, `SKILL.md`, `HEARTBEAT.md`의 운영 원칙은 유지한다.
- migration 시에는 `state/cs-management-tool.json`의 활성 도구와 mapping만 바꾼다.
- 스크립트는 provider adapter를 추가하는 방식으로 확장한다.
