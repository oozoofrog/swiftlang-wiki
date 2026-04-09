---
type: concept
category: compiler
tags: [generics, archetype, generic-environment, contextual-type]
aliases: [아키타입, Archetype]
sources: [generics-book-readme.md]
---

# Archetypes

reduced type parameter + generic signature를 캡슐화한 자기 기술적(self-describing) 타입. "Compiling Swift Generics" Chapter 7.

## 핵심 개념

Archetype = 요구사항을 만족하는 "가장 일반적인 구체 타입". 프로토콜 conformance 등의 질의에 별도 컨텍스트 없이 답변 가능.

## Generic Environment

generic signature에서 archetype을 인스턴스화하는 매핑:

- **Map into environment**: type parameter → archetype (interface type → contextual type)
- **Map out of environment**: archetype → type parameter (역변환)

## Archetype의 역할 변화

| 컴파일러 단계 | Archetype 역할 |
|---------------|----------------|
| Sema | "가장 일반적인 구체 타입" — 타입 검사에 사용 |
| SILGen | SIL 값의 타입 (contextual type) |
| IRGen | 런타임 타입 메타데이터를 나타내는 **값** |

## Generic Environment 종류

1. **Primary**: generic signature당 정확히 1개. primary archetype 생성
2. **Opened existential**: existential 값의 동적 타입을 표현
3. **Opaque type**: opaque return type의 기반 타입을 표현

## 중첩 주의사항

중첩 제네릭 선언이 새로운 파라미터/요구사항을 도입하면 **새로운** primary generic environment를 생성. 외부 archetype을 재사용하지 않음.

관련 페이지: [[compiling-swift-generics]], [[generic-signatures]], [[substitution-maps]], [[glossary-compiler]], [[sil-reference]]
