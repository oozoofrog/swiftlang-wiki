---
type: entity
category: compiler
tags: [generics, substitution-map, type-substitution]
aliases: [치환 맵, Substitution Map]
sources: [generics-book-readme.md]
---

# Substitution Maps

제네릭 선언에 대한 **참조**를 기술하는 시맨틱 객체. generic signature가 "계약"이라면, substitution map은 "이행". "Compiling Swift Generics" Chapter 6.

## 개념

Generic signature `<T, U>`에 대해 호출 `combine(Optional<Int>(), "Hello")`가 있으면:

```
Σ = { τ_0_0 ↦ Optional<Int>,
      τ_0_1 ↦ String }
```

## 타입 치환

원래 타입에서 제네릭 파라미터를 replacement type으로 교체:

```
원래: (T, Array<U>)
치환: (Optional<Int>, Array<String>)
```

## Input Generic Signature

substitution map의 "형태"를 결정. 요구사항이 있으면 replacement type은 해당 요구사항을 만족해야 한다.

## Conformance 포함

same-type이 아닌 conformance 요구사항에 대해서는, substitution map이 구체 타입의 **conformance** 정보도 함께 저장한다.

### 파일 위치

- `swift/lib/AST/SubstitutionMap.cpp`
- `swift/include/swift/AST/SubstitutionMap.h`

관련 페이지: [[compiling-swift-generics]], [[generic-signatures]], [[archetypes]], [[conformances]]
