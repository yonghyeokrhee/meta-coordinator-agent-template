# TOOLS

이 파일에는 환경별 메모를 적는다.

## 프로덕션 전에 채워둘 항목
- Knowledge base는 Notion을 사용한다
- CS 상태 추적과 관리의 단일 source of truth는 현재 `Notion / Optapex Manual / CS Intake Queue` 다.
- CS 관리 도구의 활성 설정은 `state/cs-management-tool.json` 에 둔다.
- 상태 조회, heartbeat 요약, 열린 이슈 확인은 가능하면 `scripts/cs_management.py` 를 통해 공통으로 수행한다.
- 다른 도구로 migration 하더라도 workflow는 `CS Management Tool` 추상화를 유지하고 provider 설정만 교체한다.
- Linear 등 다른 도구로 라우팅하더라도, 기준 상태 추적 도구를 바꾸기 전까지는 `CS Intake Queue`를 우선한다.

## 권장 매핑 블록

여기에는 비밀 정보나 시크릿을 저장하지 않는다.
