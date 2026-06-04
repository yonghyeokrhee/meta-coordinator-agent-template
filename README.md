# meta-coordinator-agent-template

프로덕션 CS/내부 이슈 조정을 위한 GitHub 준비형 OpenClaw 에이전트 워크스페이스 템플릿입니다.

`meta-coordinator`는 거친 지원/운영 입력을 실행 가능한 트리아지 산출물로 바꾸고, 담당자 라우팅을 추천하며, 엄격한 케이스 상태 전환을 관리하고, 해결된 케이스 이력을 바탕으로 점진적으로 개선되는 가벼운 메타 에이전트입니다.

## 이 템플릿이 설계된 대상
- 결제 확인 지연
- 과금 및 웹훅 인시던트
- 권한/퍼미션 전파 실패
- 지원 요청 트리아지 및 개발자 핸드오프
- 활성 인시던트에 대한 무응답 팔로업
- 보수적인 해결 판정 및 상태 제어

## 핵심 운영 모델
1. **스켈레톤 우선 접수**: 라우팅 전에 이슈를 구조화한다.
2. **보수적 트리아지**: 사실, 추측, 누락 정보를 분리한다.
3. **실행 가능한 디스패치**: 항상 주 담당자와 백업 담당자를 함께 제안한다.
4. **엄격한 상태 관리**: `NEW / TRIAGED / ASSIGNED / PENDING / RESOLVED`만 사용한다.
5. **학습 루프**: 해결된 케이스의 학습을 이후 라우팅 품질 개선에 반영한다.

## 실제 워크플로 (다이어그램)
```mermaid
flowchart TD
    A["Incoming CS or Internal Issue"] --> B["Set NEW state and summarize issue"]
    B --> C["Create Issue Skeleton output"]
    C --> D["Quick triage with facts, guesses, and missing info"]
    D --> E["Infer likely modules with confidence note"]
    E --> F["Suggest primary owner and backup owner"]
    F --> G["Define next actions and move to TRIAGED / ASSIGNED / PENDING"]
    G --> H{"Is fix or outcome confirmed by a human?"}
    H -- No --> I["Keep nearest valid status and add nuance in notes"]
    I --> D
    H -- Yes --> J["Move to RESOLVED"]
    J --> K["Run learning loop and update routing signals"]
```

## OpenClaw 빠른 시작
```bash
cp -R meta-coordinator-agent-template ~/.openclaw/workspace-meta-coordinator

openclaw agents add meta-coordinator \
  --workspace ~/.openclaw/workspace-meta-coordinator \
  --model openai-codex/gpt-5.4 \
  --non-interactive
```

간단한 스모크 테스트:
```bash
openclaw agent --agent meta-coordinator --message "Customer reports payment confirmation delays and possible webhook failures since this morning."
```

## 신규 이슈의 필수 출력 계약
이 프롬프트 스택은 의도적으로 강한 규칙을 가진다. 새 이슈는 항상 아래 순서로 출력해야 한다:
- Issue Skeleton
- Quick Triage
- Facts / Guesses / Missing Info
- Likely Module
- Owner Suggestion
- Next Actions
- Status Move

## 포함 파일
- `AGENTS.md` — 필수 워크플로와 가드레일
- `SOUL.md` — 운영 정체성과 원칙
- `IDENTITY.md` — 역할 및 톤 메타데이터
- `USER.md` — 운영자 및 환경 커스터마이징
- `TOOLS.md` — 모듈/팀/에스컬레이션 매핑 메모
- `SKILL.md` — 스킬 메타데이터와 행동 계약
- `INSTALL.md` — 설정 및 배포 메모
- `references/optapex-source-routing.md` — canonical source 선택 기준
- `references/optapex-help-center-taxonomy.md` — Help Center 질문 축과 카드 후보
- `references/cs-management-tool.md` — CS 상태 추적용 공통 도구 계약
- `skills/optapex-cs-answer/SKILL.md` — Optapex 답변 전용 스킬
- `skills/knowledge-distill/SKILL.md` — Notion 지식화 스킬

## HEARTBEAT.md: 선택 사항
`HEARTBEAT.md`는 OpenClaw에서 **선택 사항**이다.
- `HEARTBEAT.md`가 없어도 heartbeat는 동작하며, 모델이 무엇을 할지 스스로 판단한다.
- `HEARTBEAT.md`가 있지만 사실상 비어 있으면, OpenClaw는 호출 절약을 위해 heartbeat 실행을 건너뛸 수 있다.

이 템플릿에서는 기본적으로 생략해도 괜찮다. 명시적인 주기 체크리스트 동작이 필요할 때만 작은 `HEARTBEAT.md`를 추가한다.

## 배포 체크리스트
- `USER.md`에 운영자 이름, 타임존, 에스컬레이션 기대치를 반영한다.
- `TOOLS.md`에 실제 모듈 이름과 담당자/백업 매핑을 반영한다.
- 트래커 상태를 `NEW/TRIAGED/ASSIGNED/PENDING/RESOLVED`에 매핑한다.
- 무응답 타이밍 기준(예: 30분, 1시간, 3시간)을 정한다.
- `RESOLVED` 판정을 위한 명시적 인간 확인 기준을 정한다.

## 권장 테스트 프롬프트
- `Customer reports payment captured but receipt confirmation is delayed by 20+ minutes.`
- `A paid teammate still cannot access the workspace after invitation acceptance.`
- `Customer asks how to change the billing email for invoices.`

## 라이선스
MIT
