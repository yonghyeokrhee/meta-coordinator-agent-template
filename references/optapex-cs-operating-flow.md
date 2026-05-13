# Optapex CS Operating Flow

## 목적
Optapex 고객 문의가 들어왔을 때 같은 순서와 같은 기준으로 접수, 답변, 트리아지를 반복하기 위한 전용 운영 플로우다.

## 범위
- Optapex CS 전용
- MOP 서비스 문의에는 적용하지 않음

## 1. 접수
새 문의가 들어오면 먼저 Skeleton부터 만든다.

최소 필요 정보:
- Reported Symptom
- Impact / Scope
- Page or Feature
- Time First Noticed
- Account / Marketplace
- Urgency
- Evidence (screenshot, repro steps, raw message)

알려진 이슈/출시/가능 여부 문의라면 backlog 기준도 함께 본다.
- 기준 문서: `file:///Users/yong/.openclaw/media/inbound/03_optapex_backlog---c5977569-a77f-4065-8f20-5d2d982c25a6.md`
- 특히 `진행현황`과 `완료 예정일/Release`를 같이 확인한다.

## 2. Intake 기록
새 Optapex CS는 우선 Notion `Optapex Manual > CS Intake Queue`에 기록한다.

기록 원칙:
- 상태는 intake DB 안에서는 `new`로 시작
- 운영 상태는 별도로 `NEW`로 간주
- 원문 링크/메시지/메모를 최대한 보존

스크립트:
- `scripts/notion_cs_knowledge.py add-intake`

## 3. 초기 트리아지
`AGENTS.md` 구조를 그대로 사용한다.

필수 산출물:
- Issue Skeleton
- Quick Triage
- Facts / Guesses / Missing Info
- Likely Module
- Owner Suggestion
- Next Actions
- Status Move

상태 규칙:
- 접수 직후 `NEW`
- Skeleton 정리 + 초기 판단 완료 시 `TRIAGED`
- 사람/엔지니어 후속이 필요하면 `ASSIGNED`
- 명시적 해결 확인이 있을 때만 `RESOLVED`

답변이 불가하더라도 새 상태를 만들지 않는다.

## 4. Answer 탐색 경로
답변 가능한 케이스는 아래 순서로 찾는다.

1. `Optapex Manual`의 Knowledge Map에서 질문 축 확인
2. 관련 실제 markdown 문서 직접 확인
3. 필요 시 backlog와 대조
4. 근거가 충분하면 답변

중요:
- 인덱스만 보고 답하지 않는다.
- 실제 markdown 근거를 직접 읽은 뒤 답한다.
- 추측은 사실처럼 말하지 않는다.

## 5. 답변 후 처리
### 답변 가능
- 사용자에게 바로 응답
- 재사용 가능한 내용이면 추후 Knowledge Source / Answer Card로 승격 검토
- 상태는 상황에 따라 `TRIAGED` 유지 또는 명시적 해결 시 `RESOLVED`

### 답변 불가
- `TRIAGED` 또는 `ASSIGNED` 유지
- 아래를 반드시 남긴다.
  - 확인된 사실
  - 아직 불명확한 점
  - 필요한 확인 주체
  - 다음 액션

## 6. backlog 문의 응답 원칙
질문이 아래 유형이면 backlog를 먼저 본다.
- 이거 알려진 이슈인가요?
- 언제 되나요?
- 출시 예정인가요?
- 가능한 기능인가요?

응답 원칙:
- `기획/논의중`: 일정 약속 금지
- `개발예정`: 배정된 release 범위만 안내
- `개발중`: 진행 중이라고만 말하고 과도한 ETA 약속 금지
- `개발완료` / `배포완료`: 실제 반영 여부 확인 후 안내

## 7. 참고 문서
- Skill entry: `/Users/yong/.openclaw/workspace-cs-agent/SKILL.md`
- Notion schema: `/Users/yong/.openclaw/workspace-cs-agent/references/notion-knowledge-model.md`
- Answer rules: `/Users/yong/.openclaw/workspace-cs-agent/references/cs-answering-workflow.md`
- Optapex knowledge seed: `/Users/yong/.openclaw/workspace-cs-agent/references/optapex-help-center-seed.md`
- Backlog source: `/Users/yong/.openclaw/media/inbound/03_optapex_backlog---c5977569-a77f-4065-8f20-5d2d982c25a6.md`
