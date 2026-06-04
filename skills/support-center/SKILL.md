---
name: support-center
description: Answer MOP CS/support issues by checking the official support site first, then checking prior issue tracker history for similar cases, and only then starting repository/owner triage. Use when a user reports a product issue, asks a support question, or when triaging inbound CS requests that may be answerable immediately from support content or prior issue history.
---

# Support Center

Use this workflow for inbound CS or product-support issues.

## Core order of operations

1. Check whether the issue can be answered directly from the official support page first.
2. Check prior issue tracker logs for a similar issue and a previously used answer or resolution.
3. If the issue is still unresolved, begin owner-selection and engineering triage.

Do not jump straight to owner assignment if a support answer is already available.

## Support page check

Start with the official support center before triage.
Use `web_fetch` for the most relevant page on `support.mop.co.kr`.
Use the existing support-agent skill as source material for likely page locations and answer style:
- 시작하기: `https://support.mop.co.kr/introduce`
- 원플로우: `https://support.mop.co.kr/one-flow`
- 데이터 연동: `https://support.mop.co.kr/data-connect`
- 애드써클: `https://support.mop.co.kr/adcircle`
- 유닛 설정: `https://support.mop.co.kr/unit`
- 구독/결제: `https://support.mop.co.kr/구독-및-결제`
- 목표입찰: `https://support.mop.co.kr/target-bidding`
- Spend Pacing: `https://support.mop.co.kr/spend-pacing`
- 서비스 FAQ: `https://support.mop.co.kr/faq-service`
- 운영 FAQ: `https://support.mop.co.kr/faq-manage`
- 에러 가이드: `https://support.mop.co.kr/error-guide`

If the support page gives a sufficient answer:
- answer the user directly and clearly
- mention any limits or next checks if needed
- avoid unnecessary escalation

If the support page partially answers the issue:
- answer what is known
- clearly separate confirmed support guidance from engineering guesses

## Prior issue tracker check

Before owner triage, inspect issue tracker history for similar incidents.
Look for:
- same feature area
- same symptom pattern
- same external provider/integration
- same customer-visible wording

If a similar prior issue exists:
- reuse the established answer shape when still applicable
- cite that this appears similar to a previous issue
- keep confidence calibrated; do not assume root cause is identical

## Owner triage only when needed

If support content and issue history do not resolve the issue, start engineering triage.

Build the normal issue skeleton first.
Then infer likely module/repository.
Before assigning an owner, briefly inspect the candidate repository contents under `~/` when possible.
This repository inspection may be delegated to `dev-lead`.

Current repository → owner map:
- `mop-fe` → 박철종
- `mop-be` → 박철종
- `mop-crawling` → 이용혁
- `mop-etl` → 이용혁
- `api-etl` → 이용혁
- `mop-batch` → 이용혁
- `mop-opt-job` → 손새아
- `mop-solver-ec2` → 강성호

If repository confidence is weak:
- say so explicitly
- prefer a conservative owner suggestion plus backup owner
- use `platform triage` if no better owner is known

## Response style

- Be short, operational, and calm.
- Separate facts from guesses.
- Prefer immediate answer over escalation when support docs already cover it.
- Do not invent root cause.
- Do not mark resolved without explicit confirmation.
