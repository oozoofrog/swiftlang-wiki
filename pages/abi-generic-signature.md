---
type: entity
category: compiler
tags: [abi, generics, generic-signature, canonicalization]
aliases: [제네릭 시그니처 ABI, ABI Generic Signature]
sources: [abi-generic-signature.md]
---

# ABI: 제네릭 시그니처

제네릭 시그니처의 ABI 표현 규격. 원본: `swift/docs/ABI/GenericSignature.md`

## ABI에서의 사용

- **맹글링**: 제네릭 엔티티의 심볼 이름에 generic signature 포함 ([[abi-mangling]])
- **타입 메타데이터 파라미터**: conformance 요구사항 → witness table 파라미터
- **Protocol Witness Table**: requirement signature가 엔트리 결정

## 최소화 (Minimization)

ABI에서 generic signature는 반드시 **minimal** (redundant 제약 없음):

```swift
// 원본: C1.Element: Equatable는 redundant (C2.Element: Equatable + same-type에서 추론)
<C1, C2 where C1: Collection, C2: Collection,
 C1.Element: Equatable, C1.Element == C2.Element, C2.Element: Equatable>

// 최소화 (두 가지 유효한 결과 중 canonical한 것 선택):
<C1, C2 where C1: Collection, C2: Collection,
 C1.Element: Equatable, C1.Element == C2.Element>
```

## 정규화 (Canonicalization)

정렬 순서:
1. Generic type parameters (type parameter ordering)
2. Constraints: superclass → layout → conformance → same-type

### Type Parameter Ordering

- depth 낮은 것이 먼저
- 같은 depth면 index 낮은 것이 먼저
- associated type은 base 비교 → protocol ordering → 이름 사전순

### Protocol Ordering

module name → protocol name 사전순.

### Canonical Constraints

- same-type: 작은 쪽이 왼쪽, 구체 타입은 항상 오른쪽
- conformance: canonical type parameter 사용

관련 페이지: [[generic-signatures]], [[compiling-swift-generics]], [[abi-mangling]], [[abi-stability]]
