# Notion Knowledge Model

## 구조
최상위 페이지: `Optapex Manual`

이 아래에 다음 자산을 둔다.
- `CS Knowledge Hub` 페이지: 운영 개요와 사용 규칙
- `CS Knowledge Sources` 데이터베이스: 원문/근거/소스 메타데이터 저장
- `CS Answer Cards` 데이터베이스: 고객 답변용으로 정제된 카드 저장
- `CS Intake Queue` 데이터베이스: 아직 소화되지 않은 신규 material 임시 적재

## 데이터베이스 역할
### 1) CS Knowledge Sources
반복해서 참고할 내부 근거를 저장한다.
권장 속성:
- `Title` (title)
- `Status` (select): inbox / reviewing / distilled / blocked
- `Source Type` (select): MR / issue / doc / slack / notion / runbook / policy
- `Product Area` (multi_select)
- `Feature / Module` (multi_select)
- `Customer Impact` (multi_select)
- `Keywords` (multi_select)
- `Source URL` (url)
- `Confidence` (select): high / medium / low
- `Last Reviewed` (date)
- `Owner` (rich text)
- `Summary` (rich text)
- `CS Notes` (rich text)

### 2) CS Answer Cards
실제 응답에 바로 재사용할 카드 저장.
권장 속성:
- `Title` (title)
- `Status` (select): draft / ready / needs-review
- `Topic` (multi_select)
- `Audience` (select): customer / internal-cs / both
- `Keywords` (multi_select)
- `Source Links` (rich text)
- `Last Updated` (date)
- `Answer TL;DR` (rich text)
- `When to Use` (rich text)
- `Do Not Say` (rich text)
- `Escalate If` (rich text)

### 3) CS Intake Queue
아직 구조화되지 않은 material 임시함.
권장 속성:
- `Title` (title)
- `Status` (select): new / processing / blocked / done
- `Material URL` (url)
- `Material Type` (select)
- `Requested By` (rich text)
- `Notes` (rich text)
- `Created At` (date)

## 인덱스 원칙
인덱스는 제품 조직도보다 '질문이 들어오는 방식'에 맞춘다.
우선 축:
- 계정/권한
- 결제/구독
- 데이터 연동
- 리포트/집계
- 광고 운영/자동화
- 장애/지연/정합성
- 정책/제한사항

보조 축:
- 채널 (MOP UI / API / ETL / batch)
- 외부 연동처
- 고객 영향 수준

## 운영 규칙
- 신규 material은 먼저 `CS Intake Queue`에 넣는다.
- 검토 후 핵심 근거는 `CS Knowledge Sources`로 승격한다.
- 고객 답변에 재사용 가능한 수준이 되면 `CS Answer Cards`를 만든다.
- 하나의 Source에서 여러 Answer Card가 파생될 수 있다.
- Answer Card에는 고객에게 그대로 보내도 되는 문장 위주로 저장한다.
