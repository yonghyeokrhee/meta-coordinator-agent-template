---
name: optapex-cs-answer
description: Optapex CS 답변 전용 스킬. 이미 접수된 Optapex 문의에 대해 Skeleton을 확인하고, Knowledge Map을 따라 실제 markdown 근거를 확인한 뒤 바로 답변하거나 필요한 경우에만 backlog/owner 라우팅으로 넘긴다. 채팅에는 workflow 설명 없이 답변만 보낸다. MOP 서비스 문의에는 사용하지 않는다.
---

# Optapex CS Answer

이 스킬은 **Optapex CS 답변 전용**이다.
MOP 서비스 문의에는 사용하지 않는다.

## 기본 흐름
1. 접수된 문의의 Skeleton을 확인한다.
2. 답변 가능 여부를 찾는다.
3. `Optapex Manual`의 Knowledge Map에서 질문 축을 찾는다.
4. 연결된 실제 markdown 문서를 직접 읽는다.
5. 필요하면 backlog를 확인한다.
6. 답변 가능하면 채팅에 답변만 보낸다.
7. 답변이 불가하면 `TRIAGED` 또는 `ASSIGNED`로 유지하고 다음 액션을 남긴다.

## 답변 원칙
- 인덱스만 보고 답하지 않는다.
- 실제 markdown 근거를 읽고 답한다.
- 한 줄 결론부터 준다.
- 고객이 바로 알아야 할 조건과 예외만 짧게 덧붙인다.
- workflow 설명 요청이 아닌 이상, 채팅에는 내부 절차를 쓰지 않는다.

## backlog를 먼저 볼 질문
- 알려진 이슈인가요?
- 언제 되나요?
- 출시 예정인가요?
- 가능한 기능인가요?

## 상태 운용
- 시작: `NEW`
- 답변 탐색 시작 가능: `TRIAGED`
- 사람/엔지니어 후속 필요: `ASSIGNED`
- 명시적 해결 확인: `RESOLVED`

새 상태를 만들지 않는다.

## 참고 문서
- 답변 워크플로: `AGENTS.md`
- 운영 성향: `SOUL.md`
- 전용 운영 플로우: `references/optapex-cs-operating-flow.md`
- 답변 규칙: `references/cs-answering-workflow.md`
- Notion 구조: `references/notion-knowledge-model.md`
- 지식 시드: `references/optapex-help-center-seed.md`
- backlog 원문: `file:///Users/yong/.openclaw/media/inbound/03_optapex_backlog---c5977569-a77f-4065-8f20-5d2d982c25a6.md`
