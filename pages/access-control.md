---
type: concept
category: compiler
tags: [access-control, visibility]
aliases: [접근 제어, Access Control, 가시성]
sources: [access-control.md]
---

# Swift 접근 제어

Swift의 접근 제어는 5단계로 구성되며, "더 낮은 접근 수준의 엔티티로 정의될 수 없다"는 원칙을 따른다. 기본 접근 수준은 `internal`로, 단일 타겟 앱에 최적화되어 있다.

## 접근 수준

| 수준 | 범위 |
|------|------|
| `open` | 모듈 외부에서 서브클래싱/오버라이드 허용 |
| `public` | 모듈 외부에서 접근 가능 |
| `internal` | 같은 모듈 내 접근 (기본값) |
| `fileprivate` | 같은 소스 파일 내 접근 |
| `private` | 선언된 렉시컬 스코프 내 접근 |

## 주요 규칙

- 접근 불가 엔티티는 name lookup에 나타나지 않음 (C++과 다름)
- 프로토콜 요구사항의 접근 수준은 프로토콜 자체의 접근 수준과 같음
- `private(set)`, `internal(set)`으로 setter만 별도 제한 가능
- `protected`와 class-only 접근은 의도적으로 제외됨

관련 페이지: [[modules]], [[overview]]
