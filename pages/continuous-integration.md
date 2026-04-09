---
type: entity
category: documentation
tags: [ci, testing, automation]
aliases: [지속적 통합, Continuous Integration]
sources: [continuous-integration.md]
---

# 지속적 통합 (CI)

Swift 프로젝트의 CI와 `@swift-ci` 봇 사용법.

## @swift-ci 명령어

| 유형 | 코멘트 |
|------|--------|
| Smoke (전체) | `@swift-ci Please smoke test` |
| Smoke (macOS) | `@swift-ci Please smoke test macOS platform` |
| Validation | `@swift-ci Please test` |
| Source compat | `@swift-ci Please test source compatibility` |

## Smoke vs Validation

- **Smoke**: macOS/Linux 빠른 빌드+테스트, 시뮬레이터 미포함
- **Validation**: 전체 플랫폼 대상, 더 포괄적

## 규칙

- 비자명 커밋은 최소 smoke test 수행
- 시뮬레이터 영향 시 validation test 필수
- 교차 레포 변경은 `Please test with following PR` 사용

관련 페이지: [[testing-guide]], [[overview]]
