# meta-coordinator Korean demo script

## Scenario A — billing/webhook incident
- CS intake: 고객이 오늘 아침부터 결제 확인이 늦고 webhook 처리도 깨진 것 같다고 합니다.
- Ops evidence: 오전 9시 5분 이후 Stripe 카드 결제 전체에서 같은 증상이 보입니다.
- No response: 1시간 동안 엔지니어링 업데이트가 없습니다.
- Recovery: backlog가 모두 비워졌고 최근 테스트 결제가 정상 확인됩니다.

## Scenario B — permission/access issue
- CS intake: 결제는 됐는데 초대한 팀원이 아직 팀 워크스페이스에 접근을 못 합니다.
- Evidence: payment verified as captured, entitlement record exists, workspace membership sync failed.
- No response: 3시간 무응답.
- Resolution: membership sync replay completed and Support verified access.
