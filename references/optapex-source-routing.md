# Optapex Source Routing

## 목적
Optapex 문의에서 어떤 canonical markdown source를 먼저 읽어야 하는지 빠르게 결정하기 위한 라우팅 메모다.
`AGENTS.md`의 답변 원칙을 반복하지 않고, **문서 선택 규칙**만 제공한다.

## Canonical knowledge folder
- `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge`

이 폴더의 4개 markdown이 현재 기준 1차 source다.

### 01. 시스템 운영 매뉴얼
- 경로: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/01_system_operations_manual.md`
- 성격: runbook
- 먼저 볼 질문:
  - 오류 / 반영 지연 / 데이터 수집 멈춤
  - 배치 / 동기화 / 자동 반영 / 운영 경로
  - 에스컬레이션 필요 여부 판단

### 02. 통합 매뉴얼
- 경로: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/02_optapex_manual_onboarding.md`
- 성격: feature doc + onboarding + FAQ
- 먼저 볼 질문:
  - 기능 정의 / 용어 / 지표 의미
  - Objective / budget / optimization option
  - 온보딩 중 자주 나오는 FAQ

### 03. backlog
- 경로: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/03_optapex_backlog.md`
- 성격: known issue / roadmap / release source
- 먼저 볼 질문:
  - 알려진 이슈인가요?
  - 언제 되나요?
  - 출시 예정인가요?
  - 가능한 기능인가요?

답변할 때는 항상 `진행현황`과 `완료 예정일/Release`를 같이 본다.

### 04. Help Center
- 경로: `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/04_optapex_help_center.md`
- 성격: public customer-facing guide
- 먼저 볼 질문:
  - 공개 사용법 / 정책 / 결제 / trial / 연결 조건
  - 고객에게 바로 전달 가능한 공식 문구가 필요한 경우

## 우선순위 규칙
1. 고객에게 바로 전달 가능한 공개 가이드가 있으면 04 우선
2. 시스템 증상 / 운영 이슈면 01 우선
3. 기능 설명 보강이 필요하면 02 보강
4. 일정 / 알려진 이슈 / 가능 여부는 03 우선

## 주의
- 04의 공개 문구와 02의 내부 설명이 충돌하면 04를 우선한다.
- 03은 원인 분석 문서가 아니라 상태/일정 문서다.
- 01은 운영 판단용이므로 고객에게 내부 처리 흐름을 그대로 노출하지 않는다.
