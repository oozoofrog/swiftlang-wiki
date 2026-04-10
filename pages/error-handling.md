---
type: concept
category: compiler
tags: [error-handling, throws, try, catch]
aliases: [에러 처리, Error Handling]
sources: [error-handling.md]
---

# 에러 처리 설계

Swift 에러 처리 모델의 설계 문서. 원본: `swift/docs/ErrorHandling.md`

## 에러의 네 가지 분류

| 분류 | 설명 | Swift 처리 |
|------|------|-----------|
| **Simple domain error** | 명확한 실패, 즉각 처리 | `Optional` 반환 |
| **Recoverable error** | 복잡하지만 예상 가능한 실패 | `throws`/`try`/`catch` |
| **Universal error** | 회복 가능하지만 예측 불가 | 범위 밖 |
| **Logic failure** | 프로그래머 실수 | `fatalError`, `precondition` |

## Swift 에러 처리의 핵심

- **의도적으로 "exception handling"이라 부르지 않음**: 다른 언어와 중요한 차이 존재
- `throws` 함수는 호출 시 반드시 `try` 표시 → 에러 전파 경로가 코드에 명시적
- `catch`는 exhaustive 또는 `do` 블록에서 처리
- Cocoa `NSError` 패턴과 자연스럽게 통합

## 설계 원칙

1. **명시적 전파**: 에러가 어디서 발생할 수 있는지 코드에서 보여야 함
2. **강제 처리**: 에러를 무시하기 어렵게 (나쁜 습관 방지)
3. **표현력**: 일반적인 에러 처리 패턴을 간결하게

관련 페이지: [[overview]], [[keyword-network]], [[diagnostics]], [[type-checker]], [[failable-initializers]], [[dynamic-casting]], [[abi-calling-convention]]
