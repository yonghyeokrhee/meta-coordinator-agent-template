# Optapex Source Routing

## 목적
Optapex 문의에서 **기본 Index 경로만으로 충분하지 않을 때** 어떤 canonical markdown source를 추가로 읽어야 하는지 빠르게 결정하기 위한 **예외 라우팅 메모**다.
`AGENTS.md`의 답변 원칙을 반복하지 않고, **문서 선택 규칙**만 제공한다.

## 기본 진입점
- 항상 먼저 `file:///Users/yong/.openclaw/workspace-cs-agent/knowledge/optapex_help_center_sections_kr/00_Index.md` 를 읽는다.
- 이 Index에서 질문과 가장 가까운 **읽어야 할 파일 목록**을 먼저 고른다.
- 기본값은 Index가 가리킨 실제 section markdown 을 바로 읽는 것이다.
- 이 문서는 **기본 흐름으로 충분하지 않을 때만** 추가로 참고한다.
- Index만으로 답변을 끝내지 않는다. 답변 근거는 반드시 실제 본문 파일에서 확인한다.

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

## 이 문서를 여는 예외 조건
아래 중 하나일 때만 이 문서를 추가로 본다.

1. 시스템 증상 / 운영 이슈 / 반영 지연 / 데이터 수집 멈춤처럼 `01_system_operations_manual.md` 판단이 필요한 경우
2. 기능 정의 / 용어 / 지표 / 내부 FAQ 보강을 위해 `02_optapex_manual_onboarding.md` 확인이 필요한 경우
3. 알려진 이슈 / ETA / 출시 예정 / 가능 여부처럼 `03_optapex_backlog.md` 확인이 필요한 경우
4. Help Center section과 internal manual/runbook 사이 우선순위 충돌을 정리해야 하는 경우
5. Index가 가리킨 파일만으로는 에스컬레이션 여부 판단이 어려운 경우

## 예외 시 우선순위 규칙
1. 고객에게 바로 전달 가능한 공개 가이드가 있으면 04 또는 Index가 가리킨 help center section 우선
2. 시스템 증상 / 운영 이슈면 01 우선
3. 기능 설명 보강이 필요하면 02 보강
4. 일정 / 알려진 이슈 / 가능 여부는 03 우선

## 주의
- `00_Index.md` 는 항상 먼저 읽는 기본 진입점이다.
- 이 문서는 상시 기본 라우팅 문서가 아니라 **예외 분기용 문서**다.
- `00_Index.md` 는 파일 선택용 라우팅 인덱스다. 본문 근거를 대체하지 않는다.
- 04의 공개 문구와 02의 내부 설명이 충돌하면 04를 우선한다.
- 03은 원인 분석 문서가 아니라 상태/일정 문서다.
- 01은 운영 판단용이므로 고객에게 내부 처리 흐름을 그대로 노출하지 않는다.
