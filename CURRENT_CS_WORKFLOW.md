# Current Optapex CS Workflow

## 1. 목적
이 workflow는 **접수된 Optapex CS 문의를 어떻게 triage 하고, 답변하고, 상태 관리할지**를 정의한다.

현재 기준 source of truth는 아래다.
- **Notion / Optapex Manual / CS Intake Queue**

---

## 2. CS 등록 방법
새 문의가 들어오면 먼저 문의 원문을 확인하고, 아래 Skeleton을 맞춘다.

### Skeleton 필수 항목
- Reported Symptom
- Impact / Scope
- Page or Feature
- Time First Noticed
- Account / Marketplace
- Urgency
- Evidence

그 다음 `CS Intake Queue`에 등록하고 초기 상태를 `NEW`로 둔다.

---

## 3. 상태 체계
사용하는 canonical status는 아래 5개만 허용한다.
- `NEW`
- `TRIAGED`
- `ASSIGNED`
- `PENDING`
- `RESOLVED`

### 상태 해석
- `NEW`: 접수 직후
- `TRIAGED`: 이해했고 답변/판단 탐색을 시작할 수 있음
- `ASSIGNED`: 사람/엔지니어 후속 필요
- `PENDING`: 답변 후 확인 대기 또는 추가 확인 필요
- `RESOLVED`: 담당자 확인 또는 명시적 종결 확인 완료

무응답만으로 `RESOLVED` 처리하지 않는다.

---

## 4. Triage 분기 순서
분기 순서는 항상 아래 우선순위를 따른다.

### 4.1 에스컬레이션 필요 여부 먼저 확인
아래 중 하나라도 Yes 면 **에스컬레이션형**이다.
- 실제 계정 상태 확인이 필요한가?
- 운영 조치가 필요한가?
- 기술 확인 / 재현 / 로그 확인이 필요한가?
- 일반론 답변만으로 오진 위험이 있는가?

### 4.2 그 다음 backlog 확인형 여부 확인
아래 질문이면 **backlog 확인형**으로 본다.
- 알려진 이슈인가요?
- 언제 되나요?
- 출시 예정인가요?
- 가능한 기능인가요?

### 4.3 마지막으로 즉답형 여부 확인
위 두 조건이 아니고, **KB markdown 근거만으로 안전하게 답변하고 닫을 수 있을 때만** 즉답형으로 본다.

> 중요:
> KB에 일반 설명이 있다는 이유만으로 즉답형으로 보내지 않는다.

---

## 5. 근거 탐색 순서
답변은 반드시 검증된 문서 근거를 기반으로 한다.

### 탐색 순서
1. `knowledge/optapex_help_center_sections_kr/00_Index.md` 로 질문과 연결된 파일 목록 선택
2. 선택된 실제 markdown 문서 직접 읽기
3. 위 문서만으로 부족하거나, 시스템/운영 이슈 / 공개 Help Center와 내부 문서 충돌 / 에스컬레이션 판단이 애매한 경우에만 `references/optapex-source-routing.md` 참고
4. 일정 / known issue / 출시 예정 / 가능 여부 확인이 여전히 필요할 때만 backlog 확인
5. 그래도 부족하면 추가 확인 또는 owner 라우팅 판단

### 답변 시 근거 규칙
- **답변 근거가 될 만한 실제 문서를 확보했고 그 문서만으로 결론이 났으면, 추가 탐색은 하지 않는다.**
- **추가 탐색은 현재 문서만으로 결론이 나지 않거나, 에스컬레이션/known issue/공개문구 우선순위 충돌 판단이 남아 있을 때만 한다.**

즉답형(Q1)으로 답하는 경우, 답변에는 **반드시 실제 근거 문구 + 지식 문서명**을 포함한다.

`Source: knowledge/...#L...` 같은 path/line-range 인용은 사용자 답변에 쓰지 않는다.

예시:
- `답변 근거`
- `**현재 문서 기준으로 데이터는 child ASIN 기준으로 확인합니다.** / **Optapex Manual Onboarding**`

근거는 **실제로 읽은 markdown 파일 기준**으로만 붙이고, 사용자에게는 file path/line range 대신 **실제 답변의 근거가 된 짧은 문구**를 보여준다.

---

## 6. Bucket 규칙
사용하는 bucket은 아래 3개다.
- 즉답형
- backlog 확인형
- 에스컬레이션형

### 상호배타 규칙
- **질문 단위에서는 bucket이 상호배타적**이다.
- 하나의 질문은 하나의 bucket만 가진다.
- 다만 하나의 메시지에는 여러 질문이 섞일 수 있으므로, **메시지 단위에서는 여러 bucket이 동시에 존재 가능**하다.

### 충돌 우선순위
backlog처럼 보여도 아래가 함께 필요하면 **에스컬레이션형을 우선**한다.
- 실제 계정별 이상 확인
- 운영 조치
- 기술 확인

즉 우선순위는:
- **에스컬레이션형 > backlog 확인형 > 즉답형**

---

## 7. Multi-issue 처리
한 메시지 안에 서로 다른 질문이 2개 이상 섞여 있으면 먼저 분리한다.

### 분리 기준
- Reported Symptom 이 다르다
- 필요한 근거 source 가 다르다
- bucket 이 다르다
- 다음 액션 또는 owner 가 다르다

### 처리 절차
1. agent가 질문을 항목별로 분리
2. 각 항목에 bucket 표시
3. 질문자인 AM에게 **분리안이 맞는지 재확인**
4. 확인 후 항목별로 답변 또는 라우팅 진행

즉답형과 에스컬레이션형을 한 카드로 억지 통합하지 않는다.

---

## 8. 답변 처리 규칙
### 즉답형
- markdown 근거 확인 후 짧게 답변
- 답변에 `실제 근거 문구 / 지식 문서명` 포함
- 답변 기록 남김
- 담당자 확인 전이면 `PENDING`
- 확인 후 `RESOLVED`

### backlog 확인형
- backlog 상태와 release 범위 확인
- 확인된 범위만 보수적으로 안내
- 과도한 ETA 약속 금지
- 답변 기록 남김
- 필요 시 `PENDING`

### 에스컬레이션형
- 일반론으로 닫지 않음
- `PENDING` 또는 `ASSIGNED` 유지
- 다음 액션과 owner 포인트를 남김
- 조치/확인 후 `RESOLVED`

---

## 9. 답변 후 상태 처리
답변이 나가면 반드시 아래를 수행한다.
1. `CS Intake Queue`에 답변 기록 남김
2. 바로 `RESOLVED`로 닫지 않음
3. 담당자 확인 전이면 `PENDING`
4. 담당자 확인 또는 종결 확인이 끝나면 `RESOLVED`

---

## 10. KB gap 처리
아래가 모두 No 인 경우:
- Q1: KB markdown 근거로 바로 답할 수 있는가?
- Q2: backlog 확인형인가?
- Q3: 에스컬레이션형인가?

이 경우 단순 미답변으로 두지 않고 **`KB gap / 문서화 필요` 신호**로 기록한다.

### 남겨야 할 내용
`CS Intake Queue` 노트에 최소한 아래를 남긴다.
- 질문 요지
- 왜 기존 KB / backlog / 운영 확인 경로로 바로 처리되지 않았는지
- 어떤 문서 또는 Answer Card 가 추가로 필요해 보이는지

반복되면 아래 보강 후보로 올린다.
- `CS Knowledge Sources`
- `CS Answer Cards`

---

## 11. Heartbeat 운영
`cs-agent`는 1시간마다 heartbeat를 돌린다.

### heartbeat 규칙
- 반드시 `python3 scripts/cs_management.py summary` 결과를 기준으로 상태를 본다.
- 최근 채팅/추정으로 상태를 대신 판단하지 않는다.
- `RESOLVED`가 아닌 이슈를 열린 이슈로 본다.
- `PENDING` 이슈가 있으면 **`RESOLVED 여부 확인 필요`**를 다음 액션에 반드시 포함한다.
- 결과는 Discord parent 채널 `#cs-ai` (`1502969606409551953`)로 보낸다.

---

## 12. 운영 스크립트
### 상태/답변 기록
- `scripts/cs_management.py`
  - summary
  - update-status
  - add-answer-record

### Notion 지식 등록
- `scripts/notion_cs_knowledge.py`
  - source / answer card / intake row 생성

### workspace autosync
- `scripts/git_autosync.sh`
  - 변경사항이 있으면 `git add -A` → commit → push
- OpenClaw cron으로 **4시간마다 1회** 실행

---

## 13. 한 줄 요약
현재 workflow는 아래 구조다.

```text
문의 접수
→ Skeleton 정리
→ CS Intake Queue 등록 (NEW)
→ 에스컬레이션 여부 먼저 판단
→ 아니면 backlog 여부 판단
→ 아니면 즉답형 검토
→ 답변 또는 라우팅
→ 답변 기록
→ PENDING / ASSIGNED / RESOLVED 관리
→ 필요 시 KB gap 기록 및 문서화 후보 축적
```
