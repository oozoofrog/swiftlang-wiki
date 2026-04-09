---
type: entity
category: documentation
tags: [contributing, pull-request, guide]
aliases: [첫 PR 제출, First Pull Request]
sources: [first-pull-request.md]
---

# 첫 번째 Pull Request 제출

Swift 프로젝트에 첫 기여를 위한 PR 제출 과정.

## 작업 선택

- good first issues 라벨에서 시작
- 이슈에 다른 작업자가 없는지 확인 후 댓글로 의사 표시

## PR 절차

1. 포크 후 기능별 브랜치 생성
2. 변경 의도를 명확히 기술한 커밋
3. 관련 테스트 추가/수정 후 통과 확인
4. `@swift-ci Please smoke test`로 CI 트리거
5. 리뷰어 피드백 반영

## 도움 받기

- Swift 포럼 Development 카테고리에서 질문
- `git log`로 관련 코드 변경 이력 참고

관련 페이지: [[getting-started]], [[testing-guide]], [[overview]]
