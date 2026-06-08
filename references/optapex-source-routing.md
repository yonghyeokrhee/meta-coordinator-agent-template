# Optapex Source Routing

## 목적
`knowledge/00_Index.md`의 1단계(01→02→03)와 2단계(04_help_center)로도 부족할 때,
어떤 source를 추가로 참고할지 결정하기 위한 **예외 라우팅 메모**다.
`AGENTS.md`의 답변 원칙을 반복하지 않고, **문서 선택 규칙**만 제공한다.

## Canonical knowledge folder
- `knowledge/`

## 파일별 성격

### 01. 시스템 운영 매뉴얼
- 경로: `knowledge/01_system_operations_manual.md`
- 성격: runbook
- 해당 질문:
  - 오류 / 반영 지연 / 데이터 수집 멈춤
  - 배치 / 동기화 / 자동 반영 / 운영 경로
  - 에스컬레이션 필요 여부 판단
- 주의: 운영 판단용이므로 고객에게 내부 처리 흐름을 그대로 노출하지 않는다.

### 02. 통합 매뉴얼
- 경로: `knowledge/02_optapex_manual.md`
- 성격: feature doc + onboarding + FAQ
- 해당 질문:
  - 기능 정의 / 용어 / 지표 의미
  - Objective / budget / optimization option
  - 온보딩 중 자주 나오는 FAQ

### 03. backlog
- 경로: `knowledge/03_optapex_backlog.md`
- 성격: known issue / roadmap / release source
- 해당 질문:
  - 알려진 이슈인가요?
  - 언제 되나요?
  - 출시 예정인가요?
  - 가능한 기능인가요?
- 답변 시 `진행현황`과 `완료 예정일/Release`를 함께 본다.
- 원인 분석 문서가 아니라 상태/일정 문서다.

### 04. Help Center (섹션별 가이드)
- 진입점: `knowledge/04_help_center/00_Index.md`
- 성격: 공개 사용자 가이드 (단계별 사용법)
- 해당 질문:
  - 공개 사용법 / 정책 / 결제 / trial / 연결 조건
  - 고객에게 바로 전달 가능한 공식 문구가 필요한 경우
- 주의: 04의 공개 문구와 02의 내부 설명이 충돌하면 04를 우선한다.

### 05. FAQ (중국어·한국어)
- 경로: `knowledge/05_optapex_faq_zh_kr.md`
- 성격: 언어별 FAQ 보충
- 해당 질문: 중국어 또는 한국어 FAQ가 필요한 경우

## 예외 조건
아래 중 하나일 때만 이 문서를 추가로 참고한다.

1. 시스템 증상 / 운영 이슈 / 반영 지연 등 `01` 판단이 추가로 필요한 경우
2. 기능 정의 / 용어 / 지표 보강을 위해 `02` 확인이 필요한 경우
3. 알려진 이슈 / ETA 확인을 위해 `03` 추가 확인이 필요한 경우
4. Help Center 섹션과 내부 매뉴얼 사이 우선순위 충돌을 정리해야 하는 경우
5. 에스컬레이션 여부 판단이 어려운 경우

## 예외 시 우선순위
1. 고객에게 바로 전달 가능한 공개 가이드가 있으면 `04` 우선
2. 시스템 증상 / 운영 이슈면 `01` 우선
3. 기능 설명 보강이 필요하면 `02`
4. 일정 / 알려진 이슈 / 가능 여부는 `03`
