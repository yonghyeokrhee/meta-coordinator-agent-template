# TOOLS

이 파일에는 환경별 메모를 적는다.

## 프로덕션 전에 채워둘 항목
- 트래커 이름과 팀 ID
- 제품 모듈 네이밍 규칙
- 에스컬레이션 연락처
- 선호 담당자/팀 라벨
- 저장소 또는 대시보드 링크

## 권장 매핑 블록
다음과 같은 단순 매핑 표를 유지한다:
- `billing-webhook` -> `payments-platform` (backup: `platform-triage`)
- `entitlement-sync` -> `identity-access` (backup: `platform-triage`)
- `invoice-email` -> `support-operations` (backup: `billing-ops`)

여기에는 비밀 정보나 시크릿을 저장하지 않는다.
