---
title: Optapex CS 고객 대응 매뉴얼 (시스템)
description: Optapex 운영 중 발생하는 시스템·기능·데이터·결제 이슈에 대한 표준 대응 매뉴얼. CS Agent가 1차 응답을 만들 때 가장 먼저 조회하는 문서.
source_type: SharePoint Excel
source_filename: Optapex_CS_고객 대응 매뉴얼(시스템)_2605.xlsx
source_url: https://lgcns.sharepoint.com/:x:/s/LGOptapexMOPCN/IQAXVZkWjnS-QIpy607U71KRAdCNrpXREPGMy0PJwpIf4IA
source_local: /Users/yong/cs-codi/assets/Optapex_CS_고객 대응 매뉴얼(시스템)_2605.xlsx
source_status: 본문 반영 완료 (시트 ①·②·③ 전체)
last_updated: 2026-05-12
maintainer: kanto@lgcns.com
scope_tags:
  - cs_taxonomy
  - response_playbook
  - escalation
  - batch_schedule
  - data_pipeline
---

# Optapex CS 고객 대응 매뉴얼 (시스템)

> 원본: SharePoint Excel — `Optapex_CS_고객 대응 매뉴얼(시스템)_2605.xlsx`
>
> 시트 ① CS 카테고리 / ② 고객 대응 매뉴얼 / ③ 시스템 주요 배치 스케쥴 의 내용을 그대로 미러링한 문서입니다. (Sheet1은 비어 있어 제외)
>
> 본문 내 "Y / N / 상황별" 컬럼은 **개발팀 에스컬레이션 필요 여부**를 의미합니다.

---

## §1. CS 분류 체계 (Lv1·Lv2·Lv3)

CS Agent가 들어온 문의를 **분류 → 라우팅 → 응답** 순서로 처리할 때 기준이 되는 분류 체계입니다.
빈도 표기: 🔴 15건+ / 🟠 5건+ / 🔵 1건+ / – 없음

### Lv1: 1. 기술적 문제

| Lv2 | Lv3 / 위치 | 빈도 | 예시 |
| --- | --- | --- | --- |
| 1.1 시스템 장애 | optapex 기능명(페이지) | – | 로그인 시 오류, 비밀번호 만료 |
| 1.2 기능 오류 |  | 🟠 5 | Optapex 생성/변경 → Amazon Ads Console 반영 지연 |
| 1.2 기능 오류 |  | – | Manual 캠페인 키워드 자동 추가 미작동 |
| 1.2 기능 오류 |  | – | 캠페인명 변경·직접 Pause 등 고객 임의 조작 후 문제 |
| 1.3 성능 저하 |  |  | 페이지 접속 무한 로드 등 |
| 1.4 연동/데이터 문제 |  | 🔵 2 | Ad Profile 미생성, ASIN 미등록으로 seller 데이터 연동 불가 |
| 1.4 연동/데이터 문제 |  | 🟠 8 | 연동 후 3일+ 100% 수집 화면에서 멈추는 경우 |
| 1.4 연동/데이터 문제 |  | 🔵 2 | 계정 해제 후 재연동 |
| 1.5 설정 관련 문제 |  | 🔵 2 | Opt Set 생성 후 기존 ASIN 자동 OFF 미작동 |
| 1.5 설정 관련 문제 |  | 🟠 5 | 학습기간 Out of budget 현상 발생 문의 |

### Lv1: 2. 결제 및 계정관리

| Lv2 | 빈도 | 예시 |
| --- | --- | --- |
| 2.1 결제/결제 수단 관련 문의 | – | Trial 종료 후 자동결제 여부 문의 |
| 2.1 결제/결제 수단 관련 문의 | 🔵 2 | 마켓플레이스 추가 구독 문의 |
| 2.2 환불 요청 |  | Ticket 시스템을 통해 문의 필요 |
| 2.3 구독 변경/해지 요청 |  | Ticket 시스템을 통해 문의 필요 |
| 2.4 계정 복구/비밀번호 재설정 |  | – |

### Lv1: 4. 일반문의 및 지원요청

| Lv2 | 빈도 | 예시 |
| --- | --- | --- |
| 4.1 사용법 문의 | 🔴 12 | 학습기간 Out of budget 현상 발생 문의 |
| 4.1 사용법 문의 | 🔴 23 | Ad Console 직접 수정 가능여부 |
| 4.1 사용법 문의 | 🟠 3 | Title/할인율 Optimization 조건 |
| 4.1 사용법 문의 | 🟠 5 | 리포트 타임존, 시차 문의 |
| 4.2 제품 데모 요청 |  | Ticket 시스템을 통해 문의 필요 |
| 4.3 정책 및 약관 관련 문의 | – | 대행사 혹은 추가 운영자 권한 부여 문의 |
| 4.4 프로모션 관련 문의 | – | Ticket 시스템을 통해 문의 필요 |
| 4.5 기타 일반 문의 | – | Help Center로 안내 |

### Lv1: 5. 기능요청 및 개선제안

| Lv2 | 처리 |
| --- | --- |
| 5.1 새로운 기능 요청 | Ticket 시스템을 통해 문의 필요 |
| 5.2 기존 기능 개선 요청 | Ticket 시스템을 통해 문의 필요 |
| 5.3 사용자 인터페이스(UI) 개선 제안 | Ticket 시스템을 통해 문의 필요 |
| 5.4 연동 확장 요청 | Ticket 시스템을 통해 문의 필요 |
| 5.5 상품 확장 요청 | Ticket 시스템을 통해 문의 필요 |

> 원본에 Lv1 "3." 항목은 비어 있어 본 문서에도 없음.

---

## §2. 표준 대응 매뉴얼 (시스템)

> 각 케이스는 (분류) · (위치) · (문의 사례) · (표준 대응 가이드) · (개발팀 에스컬레이션) 5개 축으로 정리.

### 2.1 기술적 문제 / 1.1 시스템 장애

#### Case 1 — 회원가입 / 로그인

- **위치**: 회원가입/로그인
- **문의 사례**: 패스워드 만료 혹은 회원가입 시 발생하는 오류
- **표준 대응**:
  1. **패스워드 만료** → 로그인 직후 유저가 직접 비밀번호를 변경하도록 안내
  2. **휴면 상태인 유저가 비밀번호 못 바꾸는 경우** → 로그인 시 비밀번호 찾기(forgot password)를 하라는 안내문이 나타남. 비밀번호 찾기를 이용해 비밀번호를 업데이트하도록 안내
  3. **회원 가입 시 실수로 code 입력창을 닫은 유저** (신규 가입도 안 되고 로그인·코드 입력이 안 되는 경우) → 해당 유저가 새로 가입할 수 있도록 고객 안내
  4. **이메일 수신을 못해 인증을 못 받는 문제** → 김태경C, 양도훈S 에게 swagger를 통해 처리 요청
  - +FAQ: Forgot password를 누르고 인증번호를 발송했는데 메일로 오지 않는 경우 → 김태경C, 양도훈S 에게 swagger를 통해 처리 요청 (강제인증 가능)
- **개발팀 에스컬레이션**: N

### 2.2 기술적 문제 / 1.2 기능 오류

#### Case 2 — Opt Set 저장 후 미표기 / ASIN 미포함

- **위치**: optimization > ads
- **문의 사례**: Opt Set 저장 후 optimization > 리스트에 미표기 / Opt Set이 ASIN 미포함 상태로 생성되는 경우
- **표준 대응**:
  - optimization 화면 내 리스트 미표기 이슈 → 개발팀 에스컬레이션
  - opt set 생성 버튼을 누르면 즉시 portfolio 생성됨. 따라서 딜레이가 발생하면 장애 상황으로, 개발팀 에스컬레이션 필요
  - optimization 삭제 후 재생성 시 캠페인이 중복 세팅될 수 있어 개발팀 즉시 에스컬레이션 필요
- **개발팀 에스컬레이션**: **Y**

#### Case 3 — Opt Set 이름 한글 입력 오류

- **위치**: optimization > ads
- **문의 사례**: Opt Set 이름 한글 입력 시 오류
- **표준 대응**: optimization name 한글 여부 확인 → 영문+숫자로 재생성
- **개발팀 에스컬레이션**: N

#### Case 4 — 생성된 캠페인이 ads console에 미표기 / Pause 상태

- **위치**: optimization > ads > Set Up
- **문의 사례**: 생성된 캠페인이 amazon ads console 에서 미표기 / Pause 상태
- **표준 대응**:
  1. 신규 opt set 생성 시 amazon ads console 내에서 5분 이내 반영
     - *Opt Set → Amazon 반영: 보통 5분, 한국시간 10~13시 최대 2시간 지연 가능 (특정 시간대 사용량이 많아질 경우 지연 가능)*
  2. optimization > ads 화면에서는 최적화 아이템 정상 세팅 확인 → 개발팀 에스컬레이션
- **개발팀 에스컬레이션**: **Y**

#### Case 5 — SP Manual 캠페인 키워드 자동 추가 미작동

- **위치**: optimization > ads > Set Up
- **문의 사례**: sponsored product - manual 캠페인 내 키워드 자동 추가 안 됨
- **표준 대응**:
  - 키워드 자동 추가는 매일 수행되나, opt set 생성 시점에 따라 최대 2일까지 소요될 수 있음
  - 2일+ 지속 시 → 개발팀 에스컬레이션
- **개발팀 에스컬레이션**: 상황별

#### Case 6 — 고객이 Ads Console에서 직접 Pause / 캠페인명 변경

- **위치**: optimization > ads > Set Up
- **문의 사례**:
  1. Optapex로 자동 생성된 캠페인을 ads console에서 직접 Pause 처리
  2. Optapex로 자동 생성된 캠페인을 ads console에서 캠페인명 임의 변경
- **표준 대응**:
  1. amazon ads에서 직접 캠페인 Pause 시 최적화 중단 → **고객이 직접 amazon ads 에서 재라이브 필요**
  2. Optapex 생성 캠페인 네이밍 변경 / 직접 조작 금지
     - 캠페인명 임의변경 시 데이터 수집 이슈 발생 가능
     - → 캠페인 명 원복 필요 시 어드민 페이지에서 AM이 직접 캠페인명 복원 진행
  - *추가 안내 사항: 캠페인명 수정 가능여부의 경우 HQ 내부 추가 검토 예정 (실제 개발 영향도 체크 필요)*
- **개발팀 에스컬레이션**: 상황별

### 2.3 기술적 문제 / 1.4 연동·데이터 문제

#### Case 7 — AD 연동 후 product data 단계로 안 넘어감

- **위치**: My profile > Accounts > Data Connect
- **문의 사례**: AD 연동 후 product data (Seller/Vendor Central Account 연동) 단계로 안 넘어감
- **표준 대응** — 필수 체크리스트:
  1. Amazon Ads Ad Profile 생성 완료 (Ad Console 최초 접속 + 마켓플레이스 선택)
  2. 판매 가능한 ASIN 1개 이상 Active (SKU 등록 후 최대 1일 대기)
  - → 미충족 시 조건 충족 후 연동 재시도
- **개발팀 에스컬레이션**: N

#### Case 8 — 연동 단계 버튼 비활성화 / 진행 안 됨

- **위치**: My profile > Accounts > Data Connect
- **문의 사례**:
  - Ads Console 연동 중 'Ad Account' 선택 비활성화
  - 연동 후 Manage Your Amazon Accounts 화면에서 계정이 안 보임
  - 'Activate & Pay' 버튼 클릭 후 진행 안 됨
- **표준 대응** — 예상 원인:
  1. Ad Profile 생성 완료 & 판매 가능한 ASIN 존재 여부 고객사 확인
  2. 이상 없을 경우, 연동 정보(수집 토큰 유효한지) 개발팀 확인 요청 → 이상 없으면 재시도
  3. 필요 시 연동 해제 후 재연동 필요 → 연동해제의 경우 개발팀이 아닌 **양도훈S, 김태경C** 에게 요청
  - **주의사항**: 광고주 본계정(Ad Account)이 아닌 대행사 / 매니저 계정은 연동 불가 → 광고주 본계정으로 재연동 안내
- **개발팀 에스컬레이션**: 상황별

#### Case 9 — Vendor Central 잘못 연동

- **위치**: My profile > Accounts > Data Connect
- **문의 사례**: product data (Seller/Vendor Central Account 연동) 단계에서 벤더(Vendor Central) 계정으로 잘못 연동
- **표준 대응**:
  - Vendor Central 잘못 연동 시: Seller 계정으로 Ad Console 접속 후 **Step 2(Ad Console 계정 연동)부터 재시도**
  - 이미 연동된 계정 있을 경우: 우측 기선택 계정 목록 제거 후 다시 선택
- **개발팀 에스컬레이션**: N

#### Case 10 — Trial 72시간 이후 데이터 수집 미완료

- **위치**: My profile > Accounts > Collecting data
- **문의 사례**:
  - Trial 활성화 후 72시간 이상 지나도 데이터 수집 완료 안 됨
  - 데이터 수집 화면에서 일부 항목이 PENDING 상태로 유지
- **표준 대응**:
  1. Trial 활성화 → Seller / Ads 계정 데이터 수집 시작 (최대 72시간 소요)
  2. 최대 72시간 이후에도 데이터 수집 완료 안 될 시 예상 사유
     - 데이터 수집 과정 중 재연동 시도한 경우
     - Ad Console / 셀러센트럴 > 권한관리에서 직접 해지한 경우
  3. 72시간 후에도 이슈 발생 가능한 기능 (추가 시간 소요):
     - **Brand Protection Dashboard**: 최소 1주일 이상 데이터 필요
     - **Budget Simulator**: 14일 학습 기간 후 캠페인이 학습 상태에 진입해야 이용 가능
- **개발팀 에스컬레이션**: **Y**

#### Case 11 — 다른 이메일로 잘못 연동 후 재연동 희망

- **위치**: My profile > Accounts > Data Connect
- **문의 사례**: 다른 이메일로 잘못 연동 후 타 계정으로 재연동 희망
- **표준 대응** — 잘못된 계정 연동 해제 후 올바른 계정으로 재연동 필요:
  1. 고객이 직접 amazon ads 및 amazon seller central 에서 연동 해지
  2. 직접 연동 해지 불가할 경우 → 개발팀이 아닌 **양도훈S, 김태경C** 에게 요청
  - **주의사항**: owner 계정은 이관 불가. 추가 계정 초대가 필요할 경우 operator, viewer 권한 부여 가능
- **개발팀 에스컬레이션**: **Y**

#### Case 12 — Region / 마켓플레이스 / 다국가 연동

- **위치**: My profile > Accounts > Data Connect
- **문의 사례**:
  - 적합한 Region 선택 문의
  - 한 플랜에서 복수 국가 연동 문의
  - 지원 마켓플레이스 범위 문의
- **표준 대응**:
  - **Region**: 호주는 'Far East' Region 선택 / 중동(UAE)은 EU Region 으로 연동
  - **국가별 별도 구독 필요**
  - **지원 마켓플레이스**:
    - North America: 미국, 캐나다, 멕시코, 브라질
    - Europe: 영국, 독일, 프랑스, 이탈리아, 스페인, 네덜란드, 스웨덴, 폴란드, 벨기에, 터키
    - Far East: 일본, 호주, 싱가포르, 인도, 아랍에미리트, 사우디아라비아
- **개발팀 에스컬레이션**: N

#### Case 13 — 신규 ASIN 반영 시점 / FBA SKU 변경

- **위치**: optimization > ads > Set Up
- **문의 사례**: seller central에서 신규 ASIN 등록 시 반영 시점 문의 / FBA SKU 변경 후 신규 SKU 조회 안 됨
- **표준 대응**:
  - **신규 ASIN**: Active 후 최소 4일 이상 소요
    - 신규 등록 ASIN은 아마존 인벤토리 리포트에 반영된 이후부터 Optapex에서 세팅 가능 (일반적 최소 4일 이상)
    - 상품은 신규(condition=NEW)이며, 판매 가능 상태(eligibility=ELIGIBLE)여야 함
    - 재고가 입고 되었더라도 아마존 인벤토리 시스템에 반영되기까지 리드타임 발생, 실제 판매 가능 상태가 된 이후에만 최적화 세팅 가능
  - **FBA SKU 변경**: 반영까지 최대 2-3일, SKU 변경 시 신규 캠페인 생성 + 학습 재시작
- **개발팀 에스컬레이션**: **Y**

#### Case 14 — Virtual Bundle ASIN

- **위치**: optimization > ads > Set Up
- **문의 사례**: Virtual Bundle ASIN 광고 연동 불가
- **표준 대응**: Virtual Bundle은 Optapex 미지원
- **개발팀 에스컬레이션**: N

#### Case 15 — Reports 데이터 시간 / 수치 불일치

- **위치**: Overviews
- **문의 사례**: Reports 데이터 시간 / 수치 불일치 / Optapex 수치 vs Ad Console 수치 차이
- **표준 대응**:
  - **시간 차이**: Real-Time 리포트는 마켓플레이스 타임존 기준 / UI Report: 미국 기준 2일 시차 (D-2 기준)
  - **Ad Console과 수치 차이**: 데이터 수집 시점 차이로 약간 다를 수 있음 (Optapex 실시간이 더 최신)
- **개발팀 에스컬레이션**: N

### 2.4 기술적 문제 / 1.5 설정 관련 문제

#### Case 16 — 멤버 권한 부여

- **위치**: My Profile > Account
- **문의 사례**: 멤버 별 권한 부여 (신규 회원가입 시, Optapex 특정 계정에 권한 부여)
- **표준 대응**: My Profile > Account 경로에서 유저가 직접 설정하도록 요청
  - 서포트센터 안내: https://agricultural-hoverfly.super.site/krlg-optapex-help-center/account
- **개발팀 에스컬레이션**: N

#### Case 17 — Opt Set 생성 후 기존 캠페인 자동 종료 안 됨

- **위치**: optimization > ads > Set Up
- **문의 사례**: Opt Set 생성 후 기존 캠페인 자동 종료 안 됨 (기존 광고 ON 상태로 이중 운영 우려)
- **표준 대응** — 정상 동작:
  1. Opt Set → Amazon 반영: 보통 5분
  2. 기존 캠페인에서 **동일 ASIN만 OFF** (캠페인 전체 OFF 아님)
  - → 시스템 오류로 자동 OFF 미작동 확인 시 고객에 수동 OFF 요청 하는 것이 가장 빠르며, 직접 처리 필요할 경우 개발팀에 에스컬레이션
- **개발팀 에스컬레이션**: 상황별

#### Case 18 — 학습기간 Out of Budget 빈번 발생

- **위치**: optimization > ads > Amazon auto
- **문의 사례**: 최적화 세팅 초기 캠페인 예산이 낮게 설정되어 out of budget 빈번 발생
- **표준 대응**:
  - **학습기간(14일)**: Amazon Suggested Budget 기준 → 일시적인 OOB 발생은 정상. 약 4-5일차 시점부터 자동으로 예산 복구됨
  - 첫 1~3일 일예산 크게 감소 (아마존 자체의 신규 캠페인 예열 과정)
  - 이후 Optapex 자동 최적화로 예산 안정화 (3주차 이후)
- **개발팀 에스컬레이션**: N

#### Case 19 — Ad Console 에서 직접 예산 / 입찰가 수정 가능 여부

- **위치**: optimization > ads > Amazon auto
- **문의 사례**: Ad Console에서 직접 캠페인 예산, 입찰가 수정 가능여부 문의
- **표준 대응**:
  - Optapex가 관리하는 캠페인의 예산이나 입찰가를 Ad Console에서 직접 수정 가능하나 (기술적으로는 가능)
  - → 학습기간에 일 1회씩 예산 및 bid 가 업데이트 되므로, 중복 조정을 고려해 **직접 수정 자제 권고**
  - → 입찰가 / 예산 관련 세팅을 유저가 직접 변경하고자 하는 경우, **현지시각으로 변경을 원하는 날짜의 전날 오후에 진행하는 것이 좋으며**, 그러면 보통 당일 새벽 5시부터 순차적으로 반영됨
- **개발팀 에스컬레이션**: N

#### Case 20 — Optapex / Ad Console 예산 수치 불일치

- **위치**: optimization > ads
- **문의 사례**: Optapex에서 예산 설정했는데 아마존 Ad Console과 예산 수치가 다르게 표시됨
- **표준 대응**: Optapex optimization 예산 수정 시, Ad Console > portfolio 예산으로 자동 반영되며, **캠페인 별 예산 재배분까지는 최대 2일 소요**
- **개발팀 에스컬레이션**: N

### 2.5 결제 및 계정관리 / 2.1 결제

#### Case 21 — Trial 종료 후 자동 결제 / 구독 취소

- **위치**: Billings
- **문의 사례**: Trial 종료 후 자동 결제 여부 문의 / 구독 취소 방법 문의
- **표준 대응**:
  - 무료 Trial 종료 후 유료 전환. Manage Billing & Payment 페이지 [평가판 종료 날짜] 확인. 구독 취소 미진행 시 자동 결제 진행됨
  - Billing > 구독 취소 + 결제 수단 해제 시 Trial은 정상 진행
- **개발팀 에스컬레이션**: N

### 2.6 일반문의 및 지원요청 / 4.1 사용법 문의

#### Case 22 — Smart CPC Guard 초과 입찰

- **위치**: optimization > ads
- **문의 사례**: Smart CPC Guard 적용 이후 설정 CPC 를 초과하여 입찰되는 경우
- **표준 대응**:
  1. 평시에는 Smart CPC **x 1.5** 만큼을 Max Bid로 제한, 이벤트 기간에는 **x 2.0** 까지 상승
  2. 다만 Dynamic Bid Up and Down 은 유지되기 때문에, 지정하신 smart CPC의 **최대 x 3 (Event: x 4) 까지 올라갈 수 있음**
  3. 학습기간(Amazon Auto)에도 Smart CPC Guard 는 동일하게 작동
- **개발팀 에스컬레이션**: N

#### Case 23 — Amazon Auto 기간이 2주보다 길어짐

- **위치**: optimization > ads > Amazon auto
- **문의 사례**: Amazon Auto 기간이 2주보다 길어지는 이유 / OPTIMIZER_BID으로 전환됐는데 일부 ASIN만 Amazon Auto 상태
- **표준 대응**:
  - Opt set 세팅 이후 약 D+14까지 학습기간 소요
  - 중간 이슈 발생 시 학습이 재시작되며 **2주 조건 충족 시** OPTIMIZER_BID로 전환
  - 따라서 중간에 광고가 off 되는 경우 2주 이상 소요 가능
  - asin 별 실적을 체크하기 때문에 **asin 별 OPTIMIZER_BID 전환 시점이 다를 수 있음**
  - → 상기 조건을 충족하는 경우에도 Amazon Auto 가 지속될 경우 개발팀 확인 요청
- **개발팀 에스컬레이션**: 상황별

#### Case 24 — Integrate Keywords 의 negative 키워드 포함 여부

- **위치**: optimization > ads > Set Up
- **문의 사례**: 기존에 운영하던 캠페인의 키워드를 가져오는 Integrate Keywords 옵션은 negative 키워드도 가져오는지
- **표준 대응**: Integrate 시 negative 는 가져오지 않음
- **개발팀 에스컬레이션**: N

#### Case 25 — Optapex 운영 중 고객 직접 개입 가능 영역

- **위치**: optimization > ads > Amazon auto
- **문의 사례**: Optapex 운영 관련 직접 개입 가능한 영역 구분
- **표준 대응**:

  **✅ 최적화 기간 중 고객이 할 수 있는 것**:
  - Opt Set 내 예산 조정 (Optapex UI 에서)
  - 광고 목표 변경 (Maximize Ad Sales ↔ Maximize Sales 등)
  - CPC Guard 설정 / 변경
  - Manual 캠페인에 키워드 직접 추가 (고효율 확인된 키워드)
  - Title Optimization 기능 활용
  - Boost Impression / Brand Defense / Competitor Conquesting ON/OFF (amazon auto 기간 미작동)

  **❌ Amazon Ad Console 변경**:
  - Optapex가 생성한 캠페인의 캠페인명 수정 시 수집 오류 발생 가능
  - 이외 예산, 입찰가 등 Ad Console에서 변경 사항은 즉시 Optapex와 동기화되지만, Optapex가 관리 중인 캠페인은 다음 배치 실행 시 **Optapex 설정값으로 덮어쓰임**
  - → 결국 Ad Console에서 수동 수정해도 Optapex가 다시 원래대로 조정함
- **개발팀 에스컬레이션**: N

#### Case 26 — Products 탭 / Title / 할인율 추천 데이터 없음

- **위치**: optimization > products
- **문의 사례**: Products 탭에서 전체 ASIN 조회 안 됨 / Title Optimization · 할인율 추천 데이터 없음
- **표준 대응**:
  - 페이지 상단 **Optimization Hints 필터 해제** → 전체 ASIN 확인

  **Title Optimization 조건**:
  1. 최근 30일 간 키워드 데이터(ad search term, sp search query)가 존재하는 ASIN
  2. 한달 이내에 타이틀이 변경되지 않은 ASIN
  3. 현재 타이틀 내 이미 모든 키워드가 포함된 ASIN 는 추천 대상에서 제외

  **할인율 추천 조건** (다음에 해당하는 ASIN 은 추천하지 않음):
  - Filter 1: log_discount_rate 의 계수가 0보다 작은 경우
  - Filter 2: 할인을 하여도 안 한 경우보다 추가적인 매출이 발생하지 않는 경우
  - Filter 3: 승리 확률 50%에 한 번도 도달하지 못한 경우
  - Filter 4: 기본 판매량이 1이 안 되는 경우
- **개발팀 에스컬레이션**: N

#### Case 27 — Title Optimization 키워드 선정 로직

- **위치**: optimization > products
- **문의 사례**: title optimization 키워드 선정 로직
- **표준 대응**:
  - 기본적으로 LLM의 답변 기반으로 수행
  - 키워드 리스트의 경우 Amazon 광고 내규를 준수할 수 있도록 추천이 구성 (계정의 서치쿼리 리포트 기반)
- **개발팀 에스컬레이션**: N

#### Case 28 — Budget Simulation 변동 없음

- **위치**: optimization > budget simulation
- **문의 사례**: 예산 증감에 따른 budget simulation의 변동이 없는 경우
- **표준 대응**: budget simulation은 **학습기간에는 표시되지 않으며 최적화 기간부터 확인 가능**. 데이터가 적은 경우 예산 변동에 따른 예측 데이터 변화가 없는 것으로 시뮬레이션에 표시될 수 있음
- **개발팀 에스컬레이션**: N

---

## §3. 시스템 주요 배치 스케쥴

> 출처: 시트 ③ "시스템 주요 배치 스케쥴". 시각 표기는 원본 그대로 보존.

| Status | UTC | 현지시간 (해당 marketplace timezone 기준) | KST | 내용 | 조건 |
| --- | --- | --- | --- | --- | --- |
| **Optimizing (OPTIMIZER_BID)** | 매시 30분 | – | 매시 30분 | 실시간 입찰가 변경 | Active Opt Set 존재 |
| Optimizing (OPTIMIZER_BID) | – | 일 4~5회 타임그룹별 조정 (5시 당일 첫 입찰 진행, 계산이 늦어지는 경우 10시 첫 입찰) | – | campaign 예산 변경 | OPTIMIZER_BID 상태로 예측 / 최적화 결과 존재 |
| Optimizing (OPTIMIZER_BID) | – | 일 4~5회 타임그룹별 조정 (5시 당일 첫 입찰, 계산 지연 시 10시 첫 입찰) | – | target bid 변경 | OPTIMIZER_BID 상태로 예측 / 최적화 결과 존재 |
| **Amazon Auto** | – | 매일 1시 30분 - 8시 55분 내 순차 실행 | – | campaign 예산 변경 | Amazon Auto 기간 Opt Set (누적 14회 성공 → Optimizing(OPTIMIZER_BID) 전환) |
| Amazon Auto | – | 매일 1시 30분 - 8시 55분 내 순차 실행 | – | target bid 변경 | Amazon Auto 기간 Opt Set (누적 14회 성공 → OPTIMIZER_BID 전환) |
| **공통** | – | 매일 10시 | – | manual 캠페인 target 추가 (keyword, asin) | manual target 발굴 및 Auto → Manual 이관 |
| 공통 | – | 매일 11시 | – | 저성과 target 의 negative 처리 | – |
| 공통 | 목요일 1시 | – | 목요일 10시 | asin 타이틀 변경 추천 | 1) 최근 30일 키워드 데이터(ad search term, sp search query) 존재 ASIN<br>2) 한달 이내 타이틀이 변경되지 않은 ASIN<br>3) 현재 타이틀에 이미 모든 키워드가 포함된 ASIN 은 추천 대상에서 제외 |

---

## §4. CS Agent 라우팅 힌트

- **이 문서를 우선 조회해야 하는 키워드**:
  - 시스템 장애 / 기능 오류: "로그인 안돼", "비밀번호", "Opt Set 안 보여", "캠페인 미표기", "Pause", "한글 입력 오류"
  - 연동 / 데이터: "연동", "Ad Profile", "Vendor Central", "재연동", "ASIN", "FBA SKU", "Virtual Bundle", "Region", "마켓플레이스"
  - 설정 / 운영: "Out of Budget", "예산", "입찰가", "캠페인명 변경", "Ad Console 직접 수정", "Smart CPC Guard"
  - 결제: "Trial", "자동 결제", "구독 취소", "환불"
  - 학습 / 최적화: "Amazon Auto", "OPTIMIZER_BID", "14일", "학습기간", "Title Optimization", "할인율 추천", "Budget Simulation"
  - 시간 / 시차: "시차", "타임존", "리포트 시간", "수치 차이"

- **이 문서로 답이 불충분할 경우**:
  - 제품 기능 / FAQ 가 필요한 경우 → [02_optapex_manual.md](./02_optapex_manual.md)
  - 미래 출시 / 알려진 이슈 / 로드맵 질문 → [03_optapex_backlog.md](./03_optapex_backlog.md)
  - 일반 사용 가이드 / 도움말 → [04_optapex_help_center.md](./04_optapex_help_center.md)

- **에스컬레이션 경로**:
  - 개발팀 에스컬레이션이 **Y / 상황별** 인 케이스는 케이스 ID 와 함께 개발팀 채널로 전달
  - 계정 연동 해제 / 인증 관련: 개발팀이 아닌 **양도훈S, 김태경C** 로 처리 요청
  - Ticket 시스템으로 라우팅: 환불 / 구독 변경 / 제품 데모 / 프로모션 / 5.X 기능 요청 계열

---

## 변경 이력

| 일자 | 변경 내용 |
| --- | --- |
| 2026-05-12 | 시트 ① · ② · ③ 본문 전체 반영 (28개 표준 응대 케이스, CS 분류 체계, 배치 스케쥴) |
| 2026-05-12 | 스켈레톤 최초 작성 |
