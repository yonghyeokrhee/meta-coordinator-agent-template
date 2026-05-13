# Optapex Help Center Seed

Source root: https://agricultural-hoverfly.super.site/krlg-optapex-help-center

## 목적
LG Optapex Help Center의 상위 구조를 CS 응답용 지식으로 재구성한 초안이다.
새 material이 들어오면 이 문서의 카테고리와 카드 패턴을 따라 Notion `CS Knowledge Sources`와 `CS Answer Cards`를 확장한다.

## 권장 인덱스
1. 온보딩 / 계정 연동
2. Trial / 데이터 수집 대기시간
3. 최적화 세트 / 예산 운영
4. 리포트 / 지표 이해
5. 실시간 대시보드 / 데이터 차이
6. 다운로드 / 원본 리포트
7. 브랜드 보호
8. 결제 / 구독 / 플랜 변경

## 핵심 사실 요약
### 1) 온보딩 / 계정 연동
- Amazon Ads Console과 Seller Central 또는 Vendor Central 둘 다 연결해야 한다.
- Ads Console 및 Seller/Vendor 계정 모두 최소 Editor 권한이 필요하다.
- 지역별로 연결 절차를 반복해야 한다.
- 신규 Ads account는 Ad profile 생성과 활성 ASIN 조건이 필요할 수 있다.

### 2) Trial / 데이터 수집
- 무료 체험은 30일이며 마켓플레이스 단위로 적용된다.
- Trial 활성화 후 데이터 수집이 시작되며 최대 72시간이 걸릴 수 있다.
- 72시간 이후에도 기능이 활성화되지 않으면 support ticket 등록 안내 가능.
- Brand Protection Dashboard는 최소 1주 이상 데이터가 필요하다.
- Budget Simulator는 14일 학습 + 최적화 상태 진입 후 사용 가능하다.
- 기본 과거 데이터 수집 범위는 최대 90일이다.
- Seller Central 2년치 과거 데이터는 별도 문의 및 추가 요금 가능성이 있다.

### 3) 최적화 세트 / 예산 운영
- Optimization Set은 만들고 끝나는 구조가 아니라 주기 점검이 필요한 살아 있는 포트폴리오다.
- 예산은 지나치게 타이트하게 두기보다 충분히 두는 것을 권장한다.
- 2주 단위 리뷰가 이상적이다.
- 모든 상품이 매출 극대화 대상은 아니므로 매출 목표와 이익 목표를 혼합해야 한다.

### 4) 리포트
- Product 리포트는 Seller Central 비즈니스 리포트 + Ads Console 데이터를 ASIN 기준으로 통합한다.
- Supported ad types: SP, SD (Product report), SB (Brand report).
- Product report에서는 Low Stock, Excess Stock 같은 알림으로 이상 징후를 볼 수 있다.
- Brand report는 NTB 등 브랜드 지표를 제공한다.

### 5) 실시간 대시보드
- 모든 Amazon 데이터가 완전 실시간은 아니다.
- 일반적으로 1시간 단위 업데이트이며 트래픽에 따라 더 빠르거나 느릴 수 있다.
- Real-Time Dashboard는 Glance View 기반이라 모든 클릭을 완벽 반영하지 않을 수 있다.
- 실시간 매출 수치는 반품/환불이 차감된 값이다.
- Reports와의 차이는 Amazon의 최대 72시간 데이터 보정 영향도 있다.
- 7일 이전 시간대별 성과는 Downloads로 내려받아 분석해야 한다.

### 6) Downloads
- Optapex generated consolidated reports와 Amazon 원본 리포트 다운로드를 모두 제공한다.
- Seller Central, Ads Console, Excel을 오가며 정리하지 않도록 설계된 메뉴다.

### 7) 브랜드 보호
- 브랜드 키워드 클릭 점유율, 보호 상태, 주간 퍼널을 본다.
- 광고 클릭 점유율과 유기 클릭 점유율을 같이 보며 브랜드 보호 기여도를 판단한다.

### 8) 결제 / 구독
- 월간/연간 결제를 모두 지원한다.
- 월간 업그레이드는 즉시 적용, 차액은 다음 청구서에 일할 계산된다.
- 월간 다운그레이드/해지는 다음 결제 주기부터 반영된다.
- 연간 업그레이드는 남은 기간 기준 추가 청구될 수 있다.
- 연간 다운그레이드/해지는 미사용 개월 환불 가능하나 할인분 제외 + 10% 조기 해지 수수료가 있다.
- 월간 플랜은 환불 불가다.
- 결제 실패가 지속되면 최적화 기능이 중단될 수 있다.

## 우선 생성할 답변 카드 후보
1. Amazon 계정 연동 조건 안내
2. Trial 활성화 후 데이터가 아직 안 보이는 경우
3. Reports와 Real-Time Dashboard 숫자가 다른 이유
4. Brand Protection Dashboard가 바로 안 보이는 이유
5. Budget Simulator를 아직 사용할 수 없는 이유
6. 여러 계정/여러 국가 연결 가능 여부
7. Downloads에서 어떤 데이터를 받을 수 있는지
8. 월간/연간 플랜 변경 규칙

## CS 답변 시 주의 문구
- `72시간 이내`인 경우 장애처럼 단정하지 말고 정상 초기 수집 구간일 수 있음을 먼저 안내한다.
- Reports와 Real-Time의 차이는 버그로 단정하지 말고 데이터 보정/갱신 주기/반품 반영 차이를 먼저 설명한다.
- Brand Protection, Budget Simulator는 추가 학습 기간이 필요할 수 있으므로 ‘기능 미노출=오류’로 바로 해석하지 않는다.
- 결제/환불 정책은 카드 문구를 그대로 재사용하되, 예외 케이스는 내부 확인으로 넘긴다.
