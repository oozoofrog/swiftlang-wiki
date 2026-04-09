---
type: entity
category: compiler
tags: [generics, generic-signature, requirements, minimization]
aliases: [제네릭 시그니처, Generic Signature]
sources: [generics-book-readme.md]
---

# Generic Signatures

제네릭 선언의 타입 검사 동작을 기술하는 시맨틱 객체. "Compiling Swift Generics" Chapter 5.

## 구조

```
<T, U where T: Sequence, U: Equatable, T.Element == U>
 ^^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 파라미터        요구사항 (conformance, same-type 등)
```

- **Generic parameter types**: 외부 → 내부 순서로 수집 (중첩 선언의 "flat" 표현)
- **Requirements**: inheritance clause, where clause, opaque parameter, requirement inference에서 수집
- 항상 **최소화**(redundant 제거) + **정규화**(정렬) 상태

## 요구사항 종류

| 종류 | 구문 | 예시 |
|------|------|------|
| Conformance | `T: Protocol` | `T: Sequence` |
| Superclass | `T: Class` | `T: NSObject` |
| Same-type | `T == U` | `T.Element == Int` |
| Layout | `T: AnyObject` | 클래스 제약 |

## Requirement Minimization

redundant 요구사항 제거. 예: `T.Element: Equatable`와 `T.Element == U`이면 `U: Equatable`은 redundant.

## Canonical Generic Signature

- canonical type으로 모든 타입 정규화
- `τ_0_0`, `τ_0_1` 등 정규 타입 파라미터 사용
- 두 generic signature가 canonically equal이면 동일한 ABI ([[abi-generic-signature]])

## 디버깅

`-debug-generic-signatures` 플래그: 타입 검사 중 각 선언의 generic signature 출력.

관련 페이지: [[compiling-swift-generics]], [[substitution-maps]], [[archetypes]], [[conformances]], [[abi-generic-signature]], [[type-checker]]
