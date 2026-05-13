# INSTALL

## 옵션 1 — OpenClaw 에이전트 워크스페이스로 사용

1. 이 폴더를 OpenClaw 워크스페이스 위치로 복사한다.

예시:
```bash
cp -R meta-coordinator-agent-template ~/.openclaw/workspace-meta-coordinator
```

2. OpenClaw에 에이전트를 추가한다.

예시:
```bash
openclaw agents add meta-coordinator \
  --workspace ~/.openclaw/workspace-meta-coordinator \
  --model openai-codex/gpt-5.4 \
  --non-interactive
```

3. 워크스페이스 파일을 열어 다음 항목을 커스터마이즈한다:
- `USER.md`
- `TOOLS.md`
- `references/` 안의 트래커 또는 로깅 매핑
- `state/cs-management-tool.json` 의 활성 CS 관리 도구 설정
- 담당 팀 이름
- 제품별 모듈 이름

4. 에이전트를 테스트한다.

예시:
```bash
openclaw agent --agent meta-coordinator --message "고객이 오늘 아침부터 결제 확인이 지연되고 웹훅 처리도 깨진 것 같다고 합니다."
```

## 옵션 2 — 템플릿 저장소로 사용

1. 새 GitHub 저장소를 만든다.
2. 이 파일들을 저장소 루트에 복사한다.
3. 커밋하고 푸시한다.
4. 대상 머신에 클론한 뒤 트리아지 에이전트의 워크스페이스로 사용한다.

## 선택적 트래커 연동

Linear 같은 이슈 트래커에 지속적으로 이슈를 남기고 싶다면:
- `TRIAGED` / `ASSIGNED` / `RESOLVED`를 내부 워크플로 상태에 매핑한다
- 트래커 라벨과 우선순위 매핑을 업데이트한다
- 초기 트리아지에는 이슈 설명을 사용한다
- 담당 지정, 무응답 팔로업, 해결 업데이트에는 코멘트를 사용한다

이슈 트래커를 사용하지 않는다면:
- 별도 tracker reference를 두기보다 현재 workspace 운영 규칙에 맞는 최소 로그 구조를 직접 정의한다
- CS 상태 추적의 단일 기준은 `state/cs-management-tool.json`으로 선언한다
- 필요하면 `AGENTS.md`와 skill 기준에 맞춰 `cases.jsonl` 또는 일별 마크다운 로그를 추가한다

주기적인 품질 개선은:
- 반복 문의를 `CS Answer Cards`로 승격하는 방식으로 우선 정리한다
- source 선택 규칙은 `references/optapex-source-routing.md`를 기준으로 유지한다

## 권장 첫 테스트 프롬프트
- `고객이 오늘 아침부터 결제 확인이 지연되고 웹훅 처리도 깨진 것 같다고 합니다.`
- `결제와 초대가 끝났는데도 유료 팀원이 아직 팀 워크스페이스에 접근하지 못합니다.`
- `고객이 청구서의 과금 이메일을 어떻게 바꾸는지 물어봅니다.`
