---
name: meta-coordinator
description: 스켈레톤 우선 접수, 보수적인 심각도/카테고리 라우팅, 담당자 추천, 무응답 팔로업 처리, 엄격한 상태 관리(NEW/TRIAGED/ASSIGNED/RESOLVED), 그리고 이슈 트래커 또는 일반 로그를 통한 해결 케이스 기반의 지속 학습을 지원하는 가벼운 CS/엔지니어링 이슈 트리아지 스킬.
---

# Meta Coordinator

거친 CS 또는 운영 입력을 지속 가능하고 운영적으로 유용한 이슈 기록으로 바꾼다.

## 핵심 워크플로
1. 먼저 이슈 스켈레톤을 만든다.
2. 이슈를 요약하고 분류한다.
3. 심각도를 보수적으로 추정한다.
4. 가능성 높은 모듈을 최대 2개까지 추론한다.
5. 주 담당자 1명과 백업 담당자 1명을 추천한다.
6. 이슈를 `NEW -> TRIAGED -> ASSIGNED -> RESOLVED` 흐름으로 이동시킨다.
7. 이슈가 조용해지면 무응답 팔로업 가이드를 명시적으로 만든다.
8. 이슈 트래커 또는 일반 로그에 지속 가능한 처리 기록을 남긴다.
9. 해결이 확인된 뒤에는 이후 라우팅 품질 개선을 위한 간단한 학습 메모를 남긴다.

## 필수 출력 구조
- Issue Skeleton
- Quick Triage
- Facts / Guesses / Missing Info
- Likely Module
- Owner Suggestion
- Next Actions
- Status Move

## 해결 게이트
`RESOLVED`는 사람 또는 명시적 메시지로 복구가 확인된 경우에만 사용한다.
무응답은 절대 해결과 같지 않다.

## 지속 기록 옵션
- 트래커 기반 워크플로: `references/tracker-workflow.md` 참고
- 로그 전용 워크플로: `references/log-only-workflow.md` 참고
- 학습 루프 워크플로: `references/learning-loop.md` 참고

## 예시 프롬프트
- Customer says payment confirmation is delayed and webhook processing seems broken since this morning.
- Paid teammate still cannot access the team workspace after payment and invitation.
- Customer asks how to change the billing email on the invoice.
