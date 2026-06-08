---
title: "Product 리포트 이해하기"
category: report
tags: [Product리포트, 어트리뷰션, ProductOverview, ProfitTrend, 이상감지, LowStock, Growth]
summary: "날짜·필터 활용법, 어트리뷰션 윈도우(1/7/14/30일), ASIN 이상감지 배지(Low Stock·Excess Stock·Growth·Efficiency), Profit Trend 마진 공식."
related: ['18_실시간_대시보드.md', '19_다운로드.md', '22_Brand_리포트_이해하기.md', '23_지표_이해하기.md']
---

# 21. Product 리포트 이해하기

시간 흐름에 따른 성과를 분석해 Amazon 비즈니스의 패턴을 파악하세요.

> ⚠️ **중요 참고사항**
> Reports 페이지의 데이터는 Amazon API 정책에 따라 **최대 2일 지연**될 수 있습니다.

## 날짜 / 필터 살펴보기

1. **트렌드 차트에서 원하는 날짜 범위를 선택합니다.**
2. **Optimization Set 기준 필터링**
3. **재고 부족 상품 필터링**
4. **과잉 재고 상품 필터링**
5. **성장 / 효율 개선 가능 ASIN 필터링**

## 데이터 비교하기

1. Reports 페이지 상단의 **[Compare With]** 버튼을 클릭합니다.
2. 비교 기간의 데이터는 **점선(dotted line)**으로 표시됩니다.

## 어트리뷰션 이해하기

어트리뷰션 윈도우를 **1일, 7일, 14일, 30일** 중에서 설정할 수 있습니다.

**기본 어트리뷰션 기간 (광고 유형별):**
- Sponsored Products (Seller): 7 days
- Sponsored Display (Seller): 14 days
- Sponsored Products (Vendor): 14 days
- Sponsored Display (Vendor): 14 days

## Product Overview 이해하기

### ASIN 상태 확인하기

**이상감지 배지:**

| 배지 | 설명 |
|------|------|
| **Low Stock** | 재고 소진까지 30일 미만 |
| **Excess Stock** | 180일 이상 재고 보유로 자금 회전 및 마진 악화 가능 |
| **Growth** | LG Optapex가 높은 매출 성장 가능성이 있다고 판단한 ASIN |
| **Efficiency** | 최적화 시 광고 효율 개선 가능성이 높은 ASIN |

## Understanding the Profit Trend

### 📌 Estimated Margin Formula

```
Estimated Margin = [총매출 - 광고비 - 추천수수료 - FBA처리수수료 - 재고수수료 - 보관수수료 - 패널티 - 반품/환불수수료 - 쿠폰수수료 - 딜수수료 - 기타프로모션비용] ÷ 총 매출
```

---

---

## 관련 문서

- [18_실시간_대시보드.md](18_실시간_대시보드.md)
- [19_다운로드.md](19_다운로드.md)
- [22_Brand_리포트_이해하기.md](22_Brand_리포트_이해하기.md)
- [23_지표_이해하기.md](23_지표_이해하기.md)