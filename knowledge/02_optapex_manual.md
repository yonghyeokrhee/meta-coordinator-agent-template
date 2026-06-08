---
title: Optapex 통합 매뉴얼 (제품 기능 · 지표 · FAQ · 온보딩)
description: Optapex 제품 기능 정의·주요 지표·FAQ·온보딩 미팅 가이드·리포트 메타데이터를 통합한 매뉴얼. CS Agent가 사용법·기능·정의·FAQ 관련 문의에 답할 때 참조.
source_type: SharePoint Excel
source_filename: Optapex_매뉴얼작성용_통합_260120.xlsx
source_url: https://lgcns.sharepoint.com/:x:/s/LGOptapexMOPCN-Resource-KR/IQAXVZkWjnS-QIpy607U71KRAdCNrpXREPGMy0PJwpIf4IA
source_local: /Users/yong/cs-codi/assets/Optapex_매뉴얼작성용_통합_260120.xlsx
source_status: 본문 반영 완료 — 5개 시트 (opt set 구조 · Optapex 기능 · 미팅 가이드 · FAQ · Optapex 주요 지표 · 리포트 관련). 2개 시트(DBeaver연동가이드·DBeaver Query)는 내부 운영자용 자격증명·SQL 이라 의도적으로 제외.
last_updated: 2026-05-12
maintainer: kanto@lgcns.com
scope_tags:
  - product_reference
  - feature_definition
  - faq
  - onboarding
  - metrics_glossary
  - opt_set_structure
  - report_metadata
---

# Optapex 통합 매뉴얼

> 원본: SharePoint Excel — `Optapex_매뉴얼작성용_통합_260120.xlsx`
>
> 본 문서는 다음 5개 시트의 내용을 미러링합니다.
> - **opt set 구조** → §1 Opt Set & 캠페인 구조
> - **Optapex 기능** → §2 기능 정의 + Amazon Fee 용어
> - **Optapex 주요 지표** → §3 주요 지표 글로사리
> - **FAQ** → §4 FAQ
> - **미팅 가이드** → §5 AM 미팅 가이드 (내부용)
> - **리포트 관련** → §6 리포트 메타데이터
>
> **의도적으로 제외된 시트** (사내 운영자 전용, 고객 응대 범위 외):
> - `DBeaver연동가이드` — DB 자격증명, Hiware 접속 정보, Studio 계정
> - `DBeaver Query` — AM 내부 SQL 분석 쿼리
>
> CS Agent 는 위 두 시트의 내용을 **절대로 외부로 노출해서는 안 됩니다**.

---

## §1. Opt Set & 캠페인 구조

### 1.1 광고 기간 (Ads period)

- Period 는 종료일자에서 **하루 전까지만 러닝** (예: 12/19 23:59 OFF)
- 수정 시 **시작일자는 유지하고 종료일만 연장**으로 수정 필요 (오류 발생)

### 1.2 광고 구조 위계

| 레벨 | 매핑 |
| --- | --- |
| ad group 내 소재 / 키워드 | 동일 레벨 |
| optimization set | **포트폴리오 레벨** |

- *Naming 규칙은 수정 X* → 수정 시 API에서 인식 불가
- Portfolios / Budget / Period 만 amazon ad ↔ optapex 간 동일
- 나머지 항목(Objective 등)은 optapex 내에서의 기능으로, 실제 Amazon Console에 반영되는 내용이 아님
- Amazon은 제품 단위 광고 X, **캠페인 단위로 운영**

### 1.3 Optapex 캠페인 자동 생성 (4개 고정)

| # | 캠페인 타입 | 형식 | 비고 |
| --- | --- | --- | --- |
| 1 | SP | Auto | 검색광고 형식 |
| 2 | SP | Manual (키워드) | 검색광고 형식 — ex. brand, general |
| 3 | SP | Manual (제품) | 검색광고 형식 — ex. 대체재(경쟁사), 보안재 |
| 4 | SD | Auto + Manual | SD 안 하는 경우 자동 OFF |

### 1.4 캠페인 형식: Auto

키워드 타입 4개로 형성 (Loose, Close / Substitute, Complement)
- keyword 타겟은 제품명과 product 상세 (about this item)에서 amazon이 자동으로 끌어옴 ← Amazon 제품 페이지가 중요
- **Optapex는 아래 4개 타겟의 bid 조정을 수행**

| 분류 | 타겟 | 설명 |
| --- | --- | --- |
| 특정 키워드 타겟 | Loose | Broad match 개념 (+ 동일 의미 키워드도 타겟팅 적용) |
| 특정 키워드 타겟 | Close | Exact match와 유사 |
| 제품 타겟 | Substitute | 경쟁사 / 자사 브랜드 제품 (PDP 하단 related item 노출) |
| 제품 타겟 | Complement | — |

### 1.5 캠페인 형식: Manual

**1) Keyword** — 키워드 + match type + bid 설정 가능

**2) Product** — 경쟁사 or 자사 브랜드 제품까지 타겟
- keyword보다 CPC 낮음, SOV 먹기용
- amazon ad에서 카테고리 / 개별 제품 / suggest bid까지 제안함
- suggest bid는 벤치마크로 활용

### 1.6 기존 광고 운영 셀러 → Optapex 신규 사용 시

- 기존 운영 방식에서 Optapex로 넘어갈 때 **Optapex에서 운영하려는 ASIN만 OFF**, 캠페인 전체 OFF 가 아님
- Optapex 가 ASIN을 자동으로 찾아서 OFF + 담당자가 이전 캠페인 예산 조정 필요

**셋팅 구조 차이**

| 기존 셀러 | Optapex |
| --- | --- |
| Portfolio | Portfolio |
| n Campaign | n Campaign |
| 1 ad group | 1 ad group |
| **n ASIN** | **1 ASIN** |
| n keywords | n keywords |

### 1.7 분석 흐름

Overview (Total/월별 등) → Campaign match type별 데이터 확인 → 월별로 구성이 어떻게 바뀌었는지 확인 (manual 쪽 예산 비중이 늘었다 ~ 뭐 어떤게 바뀌었다 등) → 캠페인 구조 (구성의 공통 속성: 셀러의 머릿속 예측하기) → 이상했던 부분(데이터가 튀거나) 체크

---

## §2. Optapex 기능 정의

### 2.1 기능별 설명

| 기능 | 세부 기능 | 설명 |
| --- | --- | --- |
| Overview | — | 광고 실적을 원하는 기간만큼 시계열로 확인할 수 있는 전체 대시보드 |
| Download | Optapex report | Seller central + Ad console 리포트가 하나로 합쳐진 리포트를 다운받아 확인 |
| Machine Learning | — | 첫 14일 'Amazon Auto' → 이후 'Processing/Optimized'로 변함 |
| Opt set product 선정 | — | ASIN 선택 시 주의: 전환율이 비슷한 제품을 하나의 Set로 묶는게 효율적<br>전환율 기여 요소: 객단가, 인지도, 인기 |

### 2.2 Objective (광고 목표)

| Objective | 설명 |
| --- | --- |
| **Maximize Sales** | Organic + Ad 데이터 모두 활용하여 전체 매출 극대화. 이미 오가닉과 광고 매출 볼륨이 어느정도 확보된 상태에 적합한 모델.<br>- *Minimize inventory*: 재고 소진 속도에 초점 → 조금 더 공격적으로 비딩 (CPC 상승 가능)<br>- ex) Hero ASIN 월매출 최소 $1000 이상 & Organic 판매 비중 50% 이상일 때 |
| **Maximize Profit** | Organic + Ad 데이터 모두 참고. Margin 극대화 (referral, FBA, coupon 등 Fee 제외한 profit 극대화) |
| **Maximize Ad sales** | Only 광고 데이터 기반으로 매출 최적화 (Organic 데이터는 보지 않음) |
| **Maximize ROAS** | Only 광고 데이터 기반으로 ROAS 최적화 |

### 2.3 Advanced Options

| 옵션 | 설명 |
| --- | --- |
| None | — |
| **Brand Defense** | 자사 브랜드 키워드의 클릭 점유율을 강화 → 기존 수요 방어 (내 고객 지키기) |
| **Competitor Conquesting** | 경쟁사 키워드의 클릭 share를 가져오는 전략 → 신규 수요 공략 (경쟁사를 찾는 고객까지 우리 고객으로 가져오기) |
| **Target Same SKU only** | 광고하고 있는 제품의 **직접 매출**을 더 Drive하고 싶은 경우 (파생매출이 아닌). Opt Set 내 교차 sales를 유도하려면 사용하지 않는 것을 추천 |

### 2.4 Advertising Type

| 옵션 | 설명 |
| --- | --- |
| **Auto 생성** | Opt set 생성 시 ASIN별로 자동 4개 캠페인 생성: SP Auto, SP Manual 2개(product, keyword), SD<br>→ 동일 ASIN 중복 운영 및 비딩 경쟁 방지 위해 기존 캠페인 내 해당 ASIN 자동 오프 처리<br>→ **캠페인명 수정 X**<br>→ Keyword도 알고리즘을 통해서 최적화 진행 |
| Sponsored Product | 신규 셀러의 경우, 초반에는 SP만 활용 추천 |
| SP + Sponsored Display | SD: audience, contextual<br>제품 출시 초기에는 SP에 집중하여 매출 볼륨 확보. SP로 충분한 매출 볼륨을 확보하고 성장 곡선이 둔화될 시점에 SD 추가 고려.<br>(통상 오가닉 매출이 월 2~3천불 이상일 때 SD 고려 가이드) |

### 2.5 Scheduling

| 옵션 | 설명 |
| --- | --- |
| **Monthly recurring** | 매달 1일자, 한 달 단위로 광고 예산이나 규칙을 자동으로 갱신·반복 실행해주는 설정 |
| **Total Budget** | 이전 한 달 간 지출된 광고비의 90% 이상으로 세팅을 추천. 초기 운영 시에는 목표매출의 30%를 초기 예산으로 세팅 |
| **Smart CPC Guard** | CPC 상한 limit 설정. '소프트 가드' — 전환 가능성이 높다면 약간 상회할 수 있으나 가드 근처에서 KPI를 극대화하는 차선 전략 선택 |

### 2.6 Keyword

| 옵션 | 설명 |
| --- | --- |
| **Integrated Keyword** | 리드타임을 줄이고자 이전 성과의 키워드를 참고할지 여부.<br>*Integrate 을 하지 않더라도 target은 5개씩 세팅되나, 해당 작업 배치가 밤 9~10시에 수행되어 셀러에게 안내할 때는 **옵트셋 세팅 다음날부터** manual 캠페인에 target 세팅되는 것으로 안내 필요* |
| Negative Keyword | 제외하고 싶은 키워드 |

### 2.7 Products

| 옵션 | 설명 |
| --- | --- |
| Growth | 효율을 유지하면서 매출이 더 커질 것으로 기대하는 ASIN |
| Efficiency | 효율이 더 높아질 잠재력이 있는 ASIN |
| Excess / Low stock | 최근 판매량 대비 재고가 적거나 많다 |
| Pricing Optimization | ASIN의 가격을 제안해주는 시뮬레이션 기능, 할인율이 높다고만 해서 효율이 좋은 게 아님 |
| **Title Optimization** | ASIN 광고 노출 시 광고 효율을 더욱 높여줄 수 있는 Title을 추천하고 스코어링을 제공하는 기능<br>**타이틀 추천 조건**:<br>1. 키워드 데이터(ad search term, sp search query)가 존재하는 ASIN(기본적으로 한 달치 데이터를 확인하지만 데이터가 존재하기만 해도 수행)<br>2. 한 달 이내에 타이틀이 변경되지 않은 ASIN<br>3. 현재 타이틀에 모든 키워드 데이터의 (브랜드 키워드 제외한) 키워드가 포함된 ASIN 제외 |

### 2.8 Amazon Fee 용어집

| 구분 | Fee 종류 | 발생 조건 | 비용 기준 | 운영 시 포인트 |
| --- | --- | --- | --- | --- |
| 판매 수수료 | Referral Fee | 상품 판매 시 | 판매가의 % (약 8~15%) | 판매되면 무조건 발생 |
| 판매 수수료 | Refund Admin Fee | 고객 환불 시 | Referral fee 일부 차감 | 완전 환불 아님 |
| 계정 수수료 | Professional Fee | 프로 셀러 계정 | 월 $39.99 | 광고 운영 전 필수 |
| 물류(FBA) | Fulfillment Fee | FBA 주문 발생 시 | 사이즈·무게별 고정 | 개당 원가에 포함 |
| 물류(FBA) | Storage Fee | 재고 보관 | 월·부피 기준 | Q4 비용 급증 |
| 물류(FBA) | Long-Term Storage Fee | 장기 재고 | 181/365일 초과 | 방치 시 손실 확대 |
| 물류(FBA) | Aged Inventory Surcharge | 노후 재고 | 재고 연령별 추가 | 최근 중요도 상승 |
| 광고비 | Sponsored Ads Cost | 광고 클릭 시 | CPC | ACoS·TACoS 핵심 |
| 프로모션 | Coupon Discount | 쿠폰 사용 시 | 할인 금액 | 전환율 ↑ |
| 프로모션 | Coupon Fee | 쿠폰 사용 시 | 사용 1회당 약 $0.60 | 누적 비용 주의 |
| 프로모션 | Deal Fee | Deal 진행 시 | 고정 Fee | 볼륨용 |
| 재고 정리 | Liquidation Fee | 재고 청산 | 판매가 일부 정산 | 손절 목적 |
| 재고 정리 | Removal Fee | 재고 회수 / 폐기 | 개당 비용 | LTSF 회피용 |
| 기타 | Prep Service Fee | 아마존 포장 대행 | 작업 단가 | 대량 운영 시 유용 |
| 기타 | High Return Rate Fee | 반품률 높을 때 | 카테고리별 | 일부 카테고리만 |

---

## §3. 주요 지표 (Metrics Glossary)

> 출처: LG Optapex Help Center.

### 3.1 Total Performance

| Metric | Definition |
| --- | --- |
| Estimated Fee | Estimated amount of fee charged by Amazon.<br>`Estimated Fee = Total Sales - Ad Spend - Referral Fee - FBA Handling Fee - Inventory Fee - Storage Fee - Penalties - Return/Refund Fee - Coupon Fee - Deal Fee - Various Promotion Costs` |
| Units Sold | Total number of units purchased (organic + ad-driven). |
| Units Returned | Number of units purchased but later returned. |
| Sales Returned | Total value of refunded sales due to returns. |
| Sessions | Unique visits to product detail pages. |
| Buy Box % | Percentage of time your product won the Buy Box. |
| TACOS | Ad spend ÷ Total Sales (organic + ad). |
| Profit | `Estimated profit = Total Sales – Estimated Fee – Ad Spend` |

### 3.2 Sponsored Products (SP)

| Metric | Definition |
| --- | --- |
| SP Spend | Total ad spend on SP campaigns. |
| SP Sales | Sales attributed to SP ads (Same SKU + Other SKU). |
| SP ROAS | SP Sales ÷ SP Spend. |
| SP Units Sold | Units sold attributed to SP ads. |
| SP Sales (Same SKU) | Ad-attributed sales for the advertised product only. |
| SP Units Sold (Same SKU) | Units sold for the advertised product via SP. |
| SP ACOS | SP Spend ÷ SP Sales. |
| SP Impressions | Number of times SP ads were shown. |
| SP Clicks | Number of clicks on SP ads. |
| SP CTR | SP Clicks ÷ SP Impressions. |
| SP Avg. CPC | SP Spend ÷ SP Clicks. |
| SP CVR | SP Units Sold ÷ SP Clicks. |

### 3.3 Sponsored Display (SD)

| Metric | Definition |
| --- | --- |
| SD Spend | Total ad spend on SD campaigns. |
| SD Sales | Sales attributed to SD ads. |
| SD Promoted Click Sales | The amount of sales generated when advertised ASIN gets purchased due to ad. |
| SD Units Sold | Units sold attributed to SD ads. |
| SD Clicks | Number of clicks from SD ads. |
| SD Impressions | Total times SD ads were served. |
| SD Impressions Views | Number of SD impressions served in a viewable placement. |
| SD Cumulative Reach | Unique shoppers reached by SD ads. |
| SD Detail Page Views | Views of product detail pages after SD ad clicks. |
| SD New to Brand Detail Page Views | Detail page views from new-to-brand customers (no purchases in 12 months). |
| SD New to Brand Sales | Sales attributed to new-to-brand customers. |
| SD ROAS | SD Sales ÷ SD Spend. |
| SD ACOS | SD Spend ÷ SD Sales. |
| SD CVR | SD Units Sold ÷ SD Clicks. |
| SD View CTR | Rate at which viewed impressions turned into clicks. |
| SD New to Brand Sales Rate | % of SD sales from new-to-brand customers. |
| SD Impression Frequency Avg. | Average number of times a shopper saw your SD ad. |
| SD Viewability Rate | % of SD ads served in placements considered "viewable." |
| SD New to Brand Detail Page View Rate | % of detail page views from new-to-brand customers. |

---

## §4. FAQ

> 원본 시트 `FAQ` 의 Q/A 페어를 그대로 보존. **CS Agent 가 가장 자주 참조해야 하는 섹션.**

### 4.1 일반 FAQ

**Q1. 왜 신규에는 'Maximize Ad Sales'를 권장하나요?**
- 오가닉 데이터가 부족한 초기엔 광고매출 중심으로 볼륨을 먼저 확보해야 알고리즘의 학습 모수가 풍부해집니다.
- 이후 오가닉이 붙으면 'Maximize Sales'로 전환합니다.

**Q2. 캠페인은 어떻게 생성되고 기존 캠페인과의 관계는?**
- ASIN별로 SP 오토 / 매뉴얼(제품·키워드) / SD 캠페인이 자동 생성됩니다.
- 중복 운영 방지 위해 기존 캠페인 '내' 동일 ASIN만 오프되며, 캠페인 자체는 유지됩니다.

**Q3. 학습 기간 동안 대시보드 상태와 운영 원칙은?**
- 최초 14일은 'Amazon Auto'로 표기되며 공격적 테스트가 포함됩니다. 이후 'Processing/Optimized'로 전환되고 예산·입찰이 안정화됩니다.

**Q4. Optimal Budget 시뮬레이션은 어떤 로직인가요?**
- 연동된 과거·현재 성과 데이터를 학습하여 예산 변화에 따른 노출 / 클릭 / 매출을 예측합니다.
- 목표(매출 / 이익 / ROAS)에 따라 권장 예산이 다릅니다.

**Q5. 네이밍을 바꾸면 안 되는 이유는?**
- 시스템이 생성 네이밍을 기준으로 캠페인을 판독하므로 변경 시 데이터 동기화·오류가 발생할 수 있습니다.

**Q6. 재고 관련**
- 재고 추이에 따라 연동된 데이터 기반 알럿 시스템이 있음. 한달 이상 광고시 그런 ASIN도 같이 운영해도 이슈 없음.

**Q7. Smart CPC Guard는 무엇이고 하드캡인가요?**
- CPC 상한선 성격의 '소프트 가드'입니다. 전환 가능성이 높다면 약간 상회할 수 있으나 가드 근처에서 KPI를 극대화하는 차선 전략을 선택합니다.

**Q8. 초기 진입 브랜드에서의 예산 설정 문의**
- 설정하신 매출목표의 TACOS 30% 수준 제안, 단 **ASIN 당 1일 예산은 최소 $5 이상** 될 수 있도록 검토가 필요.

**Q9. Opt set 목표 설정 변경 시점 / 다음 스텝 문의**
- 이번 아마존 프로모션을 통해 Trial을 신청하신 고객 대상으로는 온보딩 세션과 2~3월 중 한번 더 세션을 진행 예정.
- 추후에 Opt set를 통한 실적 데이터를 기반으로 한번 더 논의하는 것으로 마무리.

**Q10. 벤치마크 데이터**
- 전달 불가.

**Q11. Optapex 키워드 타겟팅 방식**
- Auto 캠페인 키워드 성과 확인 → 매뉴얼로 이동하여 운영 + 이외 캠페인에서 negative 처리.

**Q12. Low stock 있는 제품의 예산이 빠지는게 자연스러운 현상인지?**
- 재고가 크게 영향을 끼치지는 않으나, 해당 제품이 노출을 얼마나 가져올 수 있냐에 따라 budget이 정해짐.
- 다만 재고가 없어 노출 확대 가능성이 적다고 알고리즘이 판단하는 경우 budget이 적게 잡히는 데 영향을 끼칠 수는 있음.

**Q13. 조기 소진 문의 (opt 이후 오후 시간대 캠페인 pause)**
- 초반 3~5일 동안은 세팅 초반이라 budget이 낮게 형성, 그 이후 캠페인별 적정 예산이 늘어나며 다시 배분됨.

**Q14. Integrated 키워드의 뜻은?**
- 기존에 운영하던 캠페인이 있을 경우 해당 캠페인에서 실적이 좋았던 키워드 타겟을 끌어와서 함께 운영하도록 함.

**Q15. Title Optimization 활용 가능 시기?**
- 최소 한 달 정도로 보고, 충분한 데이터가 쌓이고 나서 확인 가능.

### 4.2 FLOUREN GUT 질문지 답변 (송부본과 동일)

**Q16. 아마존 셀러센트럴 자동 광고 대비 Optapex 가 어떤 부분이 우수한지?**
- Optapex 는 실시간으로 수집된 데이터를 기반으로 운영하시는 ASIN에 대한 예상 실적을 계산하고, 이를 기반으로 성장 가능성을 판단하여 장기적인 성장을 만들어낼 수 있는 방향으로 최적화를 진행할 수 있는 점이 가장 큰 강점.
  1. **최적의 예산 분배**: 설정한 Objective를 달성하기 위해 제품별·캠페인별 최적의 예산을 찾아 자동으로 조정하고 키워드별 상시 입찰을 조정합니다.
  2. **키워드 자동 추출**: Auto 캠페인에서 발굴한 고효율 키워드를 자동으로 추출하여 manual keyword 캠페인으로 옮겨 디테일하게 관리함으로써 지속적으로 고효율 키워드를 발굴하여 전체 성과를 개선시킬 수 있는 선순환 구조를 구축할 수 있습니다.

**Q17. 시장 점유율 높은 경쟁사를 타겟팅하여 주요 키워드 분석이 가능한지?**
- Optapex는 학습을 통해 성과가 좋은 키워드를 자동으로 수집하고 비딩 단가를 조정하여 효율 좋은 키워드 위주로 운영합니다.
- 시장 진입 초기인 ASIN의 경우, 시장 점유율이 높은 경쟁사 키워드에서 좋은 성과를 기대하기 어렵기 때문에, 해당 키워드에 비딩가를 높이며 비효율을 발생시킬 가능성이 낮습니다. 경쟁사 키워드의 성과가 낮다면 자동으로 비딩 단가를 낮춰 광고 비효율이 발생하지 않도록 작동합니다.
- 추가로 Optapex의 고급설정 기능 중 **Competitor Conquesting** 옵션을 활성화하시면, Optapex 알고리즘이 경쟁사 키워드에 대한 Click Share를 보다 확보하는 방향으로 운영될 수 있도록 설정할 수 있어, 함께 고려해보시면 좋습니다.

**Q18. 현재 키워드 광고 예산은 $100/day, $3,000/month인데, 어떻게 설정하는 것이 좋을지?**
- 통상적으로 매출 목표 기준 TACOS 30%를 광고 예산으로 설정합니다. 광고 초기에는 예산을 넉넉하게 설정하는 것이 적정 예산을 찾아가는 데에 안전합니다.
- 일단은 현재 예산으로 1개월 이상 운영을 해보시고 optimal한 예산을 찾아가시는 게 좋을 듯합니다.
- Optapex 학습 기간이 끝나고 최적화 운영이 시작되면 Optapex의 Ads 메뉴에서 Optimization set 별로 예산의 적정 여부를 체크하실 수 있습니다. 예산이 과다하거나 부족할 경우 Budget Usage 메뉴에서 Alert를 확인하실 수 있습니다. (예: "Budget must be decreased" 알림)

**Q19. 목표 중 "Maximize Sales"가 신규 제품 / 초기 단계에도 적합한지?**
- "Maximize Sales" 목표는 광고 데이터와 오가닉 데이터를 모두 참조하여 학습합니다. 이미 오가닉과 광고 매출 볼륨이 어느정도 확보된 상태일 때 Total sales 극대화 목표로 원활히 작동되는 모델입니다. (오가닉 데이터가 부족할 경우에는 적합하지 않습니다.)
- 제품 출시 초기에는 **"Ad Sales" 목표**를 선택하셔서, 광고 효율보다는 공격적인 투자를 통해 노출 기회를 얻고 매출 볼륨을 확보하시는 걸 추천 드립니다.
- 추후에 오가닉 데이터가 충분히 쌓이면 Maximize Sales 목표로 전환하시는 걸 고려해보시면 좋습니다.

**Q20. SP로 시작한 뒤, SB / SD로 확장하는 타이밍은 언제인지?**
- 제품 출시 초기 단계에서는 일단 매출 볼륨 확보에 유리한 SP에 집중하여 운영하시는 걸 추천 드립니다.
- SP로 충분한 매출 볼륨을 확보하고, 성장 곡선이 둔화될 시점에 추가적인 노출 확보로 SD를 고려해보시는 게 좋습니다. (통상 오가닉 매출이 **월 2~3천불 이상**일 때 SD를 고려해보는 걸로 가이드)
- SB는 광고형태 상 **제품 캐로셀이 3개 이상 필요**하기 때문에, 제품이 3개 이상 출시되고 스토어로 유입을 확대하여 브랜드 인지도를 갖추고 싶으실 때 고려.

**Q21. 적정 CPC 가드를 정하는 기준은?**
- 일단 운영 초기부터 제한을 두는 건 매출 상승을 저해할 수 있는 요인이기 때문에 CPC 가드는 고려하지 않으시는 게 좋습니다.
- 추후 어느정도 매출 성장 확인 후, 광고 효율 관리가 필요한 시점에 비효율을 가져올 정도의 CPC 수준을 판단하시는 걸로 권장.

**Q22. 예산 초과 방지 및 예산 소진 속도 조절 가능한지?**
- Optapex는 광고가 조기종료 되지 않도록 예산 속도를 모니터링하고, 트래픽과 전환이 몰리는 시점(황금시간대 등)에 예산이 집중되도록 자동 관리합니다.
- 다만, 초반 학습 기간이거나, 설정된 예산이 지나치게 낮은 경우에는 광고 조기 종료 방지를 개런티하기 어렵습니다.

**Q23. Vine 리뷰 무료 배포 수량이 데이터에 포함되는지?**
- Vine의 무료 배포 수량이 데이터에 포함되나, **Ad Sales 목표로 운영할 경우는 총 매출이나 전환율 데이터를 학습에 참조하지 않기 때문에 바이어스로 작용하지 않습니다**.
- 추후 Maximize Sales 목표로 전환할 시점에는 Vine 데이터들이 희석될 걸로 보여 문제되지 않을 듯합니다.

**Q24. 아마존 셀러 센트럴 데이터를 Optapex가 모든 데이터를 끌어다 쓰는지? 실시간?**
- Optapex 시스템 상에서는 **실시간으로 데이터를 반영하여 최적화를 진행**하나, UI 상에는 batch 시간에 따라 데이터가 반영됩니다. Report 메뉴에서 확인하실 수 있는 데이터는 **미국 기준 2일 정도의 시차**가 있습니다. (14일 기준, 12일까지의 데이터 확인 가능)

**Q25. Optapex 가 찾아낸 '고효율 키워드'를 리스팅(SEO)에 어떻게 반영할 수 있는지?**
- Optapex가 자동으로 운영한 키워드 실적은 **리포트 다운로드**를 통해 확인하실 수 있습니다.
- SEO로 활용하실 목적이라면 Optapex의 "Product" 메뉴에서 **"Title Optimization"** 기능 활용을 추천 드립니다. 현재의 Product Title을 어떻게 수정해야 score를 높일 수 있을 지 AI Recommendation을 제공합니다.

**Q26. 성과가 나쁜 키워드를 AI가 자동으로 '제외 키워드'로 등록해주는지?**
- 설정한 목표에 따라 AI가 키워드 별 성과의 좋고 나쁨을 판단하고, 자동으로 비딩가를 조정하여 노출을 강화하거나 약화합니다. (score 개념으로 키워드 별 성과를 제공 드리진 않습니다.)
- 성과가 나쁜 키워드는 **비딩가를 극단적으로 낮춰 노출에서 제외시키는 방식**이고, 자동으로 Negative로 등록하진 않습니다.

**Q27. Dietary supplements 카테고리에서 Optapex 사용 시 ACoS 개선 폭은? 레퍼런스가 있다면?**
- 통상적으로 **총 매출 20~30% 증가**하는 걸로 확인됩니다. 광고 효율 측면에서 **ROAS가 많게는 100%까지 증가**하나, 현재 단계에서는 광고 효율보다는 매출 볼륨 확보에 집중하시는 게 좋습니다.

---

## §5. 미팅 가이드 (AM 내부용)

> ⚠️ **이 섹션은 내부 AM 미팅 진행용 체크리스트입니다. 고객에게 그대로 전달하지 마세요.** CS Agent 는 이 섹션을 응답 작성 시 컨텍스트로만 활용.

### 5.1 초기 미팅 가이드

| 주제 | 상세 질문 / 설명 |
| --- | --- |
| 오프닝 & 미팅 목적 | 오늘은 Optapex 솔루션 소개, 목표(KPI) 설정, 운영 전략을 논의합니다. 질문은 언제든지 주세요. |
| 현황 진단 (데이터·캠페인·목표) | 운영 중 캠페인 수·타겟, 히어로 ASIN 선정 기준, 최근 3개월 ROAS / TACoS / 광고매출 비중은? |
| Optapex 핵심 기능 설명 | 선택한 ASIN 기준으로 SP 오토 / 매뉴얼(프로덕트·키워드) / SD 캠페인을 자동 생성. 동일 ASIN 중복 운영 방지 위해 기존 캠페인 내 해당 ASIN은 자동 오프 처리. (+ 대시보드 기능 설명) |
| 최적화 목표(Optimization Target) 선정 | 신규 셀러 / 신제품은 'Maximize Ad Sales' 권장. 오가닉 데이터가 충분해지면 'Maximize Sales'로 전환. |
| Opt Set 생성 & 예산 / 기간 설정 | 예: 3개 제품, SP 중심, 4주 기간, 총 예산 X. Smart CPC Guard는 상한선 성격의 '소프트 가드'로 필요 시 설정. |
| 학습 기간 운영 (첫 14일) | 최초 14일은 학습 기간(대시보드 상태 'Amazon Auto' 표기). 이후 3주차부터 'Processing / Optimized' 상태로 전환. |
| 시뮬레이션 / Optimal Budget 활용 | 학습된 데이터 기반으로 예산을 증·감할 때 노출·클릭·매출의 예상 변동을 그래프로 제시. |
| KPI 설계 & 모니터링 | 오가닉 비중 높으면 총매출 기준, 광고 비중 높으면 'Maximize Ad Sales'로 관리. |
| 브랜드 / 키워드 전략 | 고객 상황에 따라 Brand Defense·경쟁사 타게팅 등 고급 옵션은 데이터 축적 후(1~2개월) 적용. |
| 거버넌스 (중복 / 네이밍 / 오프라인 캠페인) | 중복 운영 방지 로직 동작 여부 점검(필요 시 수동 오프), 아마존 콘솔에서 동일 리스트 확인. |
| 지원 채널 & 에스컬레이션 | 예산 과·소진, 캠페인 상태 이슈 등 발견 시 즉시 티켓 등록. |
| 클로징 & 다음 단계 | 오늘 논의한 타깃과 예산으로 즉시 셋업 후 2주 뒤 리뷰. |

### 5.2 학습 기간 운영 노트

- Opt set 14일 학습 기간 (Amazon Auto로 표기 — Optapex 기능이 하나도 들어가지 않음)
- 중간에 이슈가 있으면 14일보다 길어질 수 있음 — 데일리로 추천 입찰가가 오는데, **14번이 count 되어야하는 로직**
- Amazon Auto 는 amazon의 daily 추천 예산과 입찰가 반영 → **예산은 그대로 반영, 입찰가는 x 0.6 ~ 0.7 수준으로 반영** (클릭 발생 전까지는 단계별로 $0.5씩 올려가면서 운영, 클릭발생 이후 고정)
- *초기에는 추천 예산이 작음* (4일차 이후부터 실제 제품의 반응에 따라 예산 제안)
- 너무 작다면 실제 Ad console 들어가서 셀프 조정해도 된다 노티하기
- 학습 기간 동안은 smart CPC도 X, optapex 내 할 수 있는 것과 자동으로 되는 것이 없음
- ASIN 당 하루에 예산 **$5는 쓸 수 있도록, 넉넉하게는 $10 수준**

### 5.3 Opt set 세팅 방법 설명

- **Overview**
- **Optimizations > Ads**
  - 캠페인 운영 목표가 동일하고, 객단가가 비슷한 수준의 제품을 그룹핑하여 운영하는 것을 추천 / 하나의 ASIN만 운영도 가능
  - **Objective 설정**:
    - Maximize Sales와 Maximize Profit은 전체 세일즈 데이터과 광고 데이터를 기반으로 최적화
    - Maximize Ad Sales와 ROAS는 광고 데이터 기반의 최적화
- **기본적인 GOAL 설정 가이드**:
  1. 전체 매출을 견인하고 있는 Hero ASIN 중 **Organic 비중이 50% 이상**이면 안정적인 판매가 진행되고 있는 것으로 예상되기 때문에 **Maximize Sales** 설정 권장
  2. 새로 진입했을 경우 공격적인 비딩을 통해 노출 볼륨을 확보하기 위해서는 **Maximize Ad Sales** 설정 권장 — 새로 진입해서 데이터가 충분하지 않을 경우, 빠르게 매출을 올려야 할 경우
  3. 안정적인 매출이 나오면서 이익을 극대화가 필요한 경우에 **Maximize Profit** 권장
  4. 광고 효율 극대화 및 목표가 있을 경우에 **Maximize ROAS** 권장 (마케팅 예산이 한정된 브랜드의 니즈가 있을 경우만 제안)
  - *보통의 셀러의 경우 매출목표를 최대화하여 볼륨을 높이는 것이 우선 → 매출 볼륨이 높아지면 랭킹이 상승, 랭킹 상승하면 Conversion 상승, Conversion 상승하면 광고효율은 자동으로 따라옴*
- **Advertising type 설정**:
  - 초기 진입의 경우 매출 볼륨을 높이기 위해 **SP 위주 운영** 추천
  - 브랜드 노출 볼륨을 높여야 하는 단계에서는 **SP + SD 운영**으로 변경 추천
- **Schedule & Budget 설정**:
  - 기간은 보통 한 달 기준으로 그 이상 설정 권장
  - 초기 진입 고객은 목표 매출의 **TACOS 30% 수준** 의 예산 설정 추천. 초기 진입 제품의 경우 월 $1,000 이상의 매출이 나와줘야 랭킹에 안정적으로 진입할 가능성이 높기 때문에 매출목표를 가져가는 것이 좋음
- **Next 일정에 대한 노티**
- **문의사항은 티켓을 통해 접수 요청**

### 5.4 초반 광고주 브랜드 현황 확인

1. **총 매출 현황 확인 + 주요 제품**
   - 자사 브랜드 top sales product가 어떤건지 확인
   - 상위 3개 product의 sales 비중은 몇 % 정도인지
   - 상위 rank에 있는 ASIN이 있다면, 같은 Parent ASIN 내 Child ASIN이 모두 상위 rank인지도 확인
2. **광고 소진액 어느 수준인지**
   - 혹시 광고 push가 필요한데 소진되지 않고 있는 제품이 있을지도 확인
3. **BSR 확인**
   - 최근 7일 기준으로 같은 카테고리 내 제품 rank 확인
4. **브랜드 경쟁력 없는 제품은 broad keyword 검색 내 순위를 확인할 필요가 있음**

### 5.5 기존 셀러 분석

1. 매출이 갑자기 떨어지는 애들이 있는지 (seasonality or 재고문제)
2. Why? 왜 떨어지는지?
3. 타겟팅(이행관점)에서 어떤 걸 해야 하는지
   - Product 타겟팅 ROAS와 ACOS를 보고 키워드 CPC가 높고 매출에 도움이 안될 수도 → product를 좀 더 메인으로 운영하기 (너네는 경쟁사 타겟을 열심히 하더라)
   - Broad로 운영한 애들 실제 search term을 보고, 동일하게 (exact)로 검색된 애의 실적이 어떨지 확인 → 동일할 때 ROAS가 높은 애들은 Exact로 끌어와서 집중적으로 운영
   - 캠페인 별로 파서 키워드 / 제품을 확인
   - auto search term 모두 확인하고 우리의 운영 키워드와 겹치는 거 찾기 → 이중비딩이라 한곳에서 죽이기
   - manual과 Auto에서 CPC가 비슷하지 않은 거면 유지해도 괜찮음

### 5.6 Amazon Auto 기간에 확인해야 할 내용

1. 일자별 소진금액이 이전과 차이가 많이 나는지
2. process가 amazon auto로 잘 들어가 있는지 (done이나 이상한 거 있는지 더블체크)
3. 3일차 부터 budget이 변동이 너무 없거나, bid amount rate이 너무 낮은데 CPC도 예산 대비 너무 낮은지 체크 (노출량 확인 — CPC가 너무 낮아 노출이 없을 수도)
4. 보통 5일차부터 셀러들이 물어봄 → DBeaver 통해서 target 리스트 뽑아서 Bid 확인

---

## §6. 리포트 메타데이터

### 6.1 기본 리포트 (테이블 이름)

- `ad_reports_advertised_product`
- `ad_reports_purchased`
- `ad_reports_search term`
- `ad_reports_targeting`
- `sp_reports_sales and traffic by asin`
- `sp_reports_search query performance report`
- `sp_sales ranks`
- `proc_products`
- `amazon_account`

**확인 기준**:
- `amazon_account` raw 내 확인 기준 → ad console, seller central 모두 연동 완료되어야 노출
- `in collect` 로 표기된 계정은 데이터 연동 전으로, 최대 48시간 내 연동 될 예정
  - optapex 내 대시보드 또한 open 되어 있지 않은 상태로 보임
- **DB 상에 표시되는 시간은 UTC 기준** (출처: 이지영S)

### 6.2 SQP (Search Query Performance)

| # | 항목 | 의미 |
| --- | --- | --- |
| 1 | Search Query Score | 해당 키워드가 실제 conversion에 영향을 미치는 정도를 rank화 |
| 2 | Query impression — total | amazon 내 해당 키워드 노출양 전체 |
| 2 | Query impression — asin | 해당 ASIN 노출양 |
| 3 | median_click | 해당 키워드를 통해 클릭된 제품들의 중위 값 → **promotion price 결정 시 활용** |
| 4 | purchase count | unit 개수가 아닌 **구매 횟수** |

- 특정 키워드 market share를 올리고 싶을 때 → CTR 역산해서 광고주에게 역제안하는 방식으로 해당 데이터 활용 가능
- *어떤 제품에 어떤 키워드의 효율이 이렇다 ~*

### 6.3 sp_reports_sales and traffic by asin (Business Report)

- 실적 + traffic
- Marketplace id: `ATV~` 는 미국
- *데이터는 child asin 기준으로 확인*
- conversion 구할 때 page view 기준으로 봄
- **buy box percentage**: 가격(최저가여야 하고 가중치 80%) / brand power / seller rating / zip code

### 6.4 ad_reports_advertised_product

- 일자 / ASIN 기준으로 리포팅
- 창고나 바코드 부착 여부에 따라 같은 제품이어도 SKU가 다름
- ⚠️ **`campaign budget amount`**: 리포트 추출 날짜 기준으로 모두 동일하게 나오는 **버그**. 해당 데이터 보지 않기

### 6.5 search term 리포트

- 클릭값만 집계
- `match type`: `targeting expression_predefined` 은 auto 광고
- *Excel 데이터 깨질 때는 Excel → Data → 데이터 가져오기로 import*

---

## §7. CS Agent 라우팅 힌트

- **이 문서를 우선 조회해야 하는 키워드**:
  - 기능 정의 / 사용법: "Maximize Sales", "Maximize Ad Sales", "Maximize Profit", "Maximize ROAS", "Objective", "Smart CPC Guard", "Brand Defense", "Competitor Conquesting", "Title Optimization", "Integrated Keyword"
  - 구조 / 캠페인: "Opt Set", "캠페인 4개", "SP Auto", "SP Manual", "SD", "Portfolio", "Ad Group"
  - 지표 / 정의: "TACOS", "ACOS", "ROAS", "Buy Box", "Estimated Fee", "Referral Fee", "FBA Fee", "Storage Fee", "Coupon Fee"
  - 시간 / 시차: "UTC", "D-2", "미국 기준 2일", "타임존"
  - 자주 묻는 일반 Q: "왜", "권장", "타이밍", "언제", "어떻게", "기준"

---

## 변경 이력

| 일자 | 변경 내용 |
| --- | --- |
| 2026-05-12 | 5개 시트 본문 전체 반영 (opt set 구조, 기능, 지표, FAQ, 미팅 가이드, 리포트). DBeaver 2개 시트는 내부 자격증명·SQL 이라 의도적으로 제외 |
| 2026-05-12 | 문서 스코프를 "온보딩 중심" → "통합 매뉴얼"로 확장. 파일명은 INDEX 호환을 위해 유지 |
| 2026-05-12 | 스켈레톤 최초 작성 |
