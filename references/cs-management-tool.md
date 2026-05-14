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

## intake material 필드 규칙
`CS Intake Queue`의 material 관련 필드는 아래처럼 해석한다.

- `Material URL`: 실제 원문 또는 근거가 있는 위치
- `Material Type`: 그 URL이 가리키는 **자료의 종류**

중요:
- `Material Type`은 유입 채널명이나 서비스명 자체를 적는 칸이 아니다.
- 즉 `Discord`, `Slack`, `Notion`처럼 채널/도구 이름을 그대로 넣지 않는다.
- 먼저 자료의 성격을 분류하고, 채널 정보가 필요하면 `Material URL` 또는 `Notes`에 남긴다.

현재 기본 분류는 아래 select 값만 사용한다.
- `MR`: merge request / PR 성격의 변경물
- `issue`: 이슈 트래커 카드 / 버그 리포트 / 티켓
- `doc`: 가이드 / 매뉴얼 / 헬프센터 / 문서
- `message`: Discord / Slack / 이메일 / 채팅 문의 원문
- `policy`: 운영 정책 / 과금 정책 / 내부 규정
- `other`: 위 분류로 명확히 떨어지지 않는 자료

예시:
- Discord 문의 링크 → `Material Type = message`
- Notion help center 문서 → `Material Type = doc`
- 환불 정책 문서 → `Material Type = policy`
- Jira / Linear / GitHub Issue 링크 → `Material Type = issue`

규칙 충돌 시 우선순위:
1. 채널명이 아니라 자료 성격으로 분류한다.
2. 고객 문의 원문이면 우선 `message`로 둔다.
3. 같은 도구 안에 있어도 문서면 `doc`, 정책이면 `policy`, 티켓이면 `issue`로 둔다.

## heartbeat 규칙
- heartbeat는 항상 먼저 활성 CS Management Tool을 조회한다.
- `RESOLVED`가 아닌 케이스를 열린 이슈로 본다.
- 채널 요약에는 현재 열린 이슈 수, 각 이슈의 status, 가장 가까운 다음 액션만 짧게 담는다.
- `PENDING` 상태가 있으면 담당자 확인이 아직 남아 있는 것으로 보고, 요약에 반드시 `RESOLVED 여부 확인 필요`를 포함한다.

## intake 식별자 / 시간 필드 규칙
- 모든 intake row에는 별도 컬럼 `CS No`를 둔다.
- `CS No`는 `cs-001`, `cs-002` 형식의 순번형 식별자를 사용한다.
- 새 intake 작성 시 title에 번호를 붙이지 않고, `CS No` 컬럼에만 번호를 기록한다.
- `Title`은 순수 문의 제목만 유지한다.
- `Created At`은 가능하면 날짜만이 아니라 **시간까지 포함한 timestamp**로 기록한다.
- 기존 row도 원본 page 생성 시각을 기준으로 `Created At`을 보정할 수 있다.
- `Resolved At`은 status가 `RESOLVED`로 바뀐 시각을 기록하는 필드다.
- status가 `RESOLVED`가 아니면 `Resolved At`은 비워 둔다.
- 스크립트로 status를 변경할 때는 즉시 반영한다.
- Notion UI에서 status를 직접 바꾼 경우에도, `scripts/cs_management.py summary` 또는 `sync-resolved-at` 실행 시 `Resolved At`이 자동 보정된다.

## 답변 기록 규칙
- 답변이 나가면 `CS Intake Queue`에 답변 기록을 남긴다.
- 답변 기록에는 최소한 답변이 나갔다는 사실, 시점, 종결 확인 필요 여부가 포함되어야 한다.
- 담당자 확인 전에는 `RESOLVED`로 닫지 않고 `PENDING`으로 둔다.
- 담당자 확인이 끝난 경우에만 `RESOLVED`로 변경한다.
- `RESOLVED`로 변경할 때는 가능하면 같은 시점에 `Resolved At`도 함께 기록한다.

## migration 규칙
- Notion → 다른 도구로 바뀌어도 `AGENTS.md`, `SOUL.md`, `SKILL.md`, `HEARTBEAT.md`의 운영 원칙은 유지한다.
- migration 시에는 `state/cs-management-tool.json`의 활성 도구와 mapping만 바꾼다.
- 스크립트는 provider adapter를 추가하는 방식으로 확장한다.
