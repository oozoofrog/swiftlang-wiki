---
type: entity
category: compiler
tags: [generics, conformance, protocol, witness-table]
aliases: [Conformance, 프로토콜 준수]
sources: [generics-book-readme.md]
---

# Conformances

타입이 프로토콜을 준수하는 방법의 컴파일러 내부 표현. "Compiling Swift Generics" Chapter 8.

## 개요

`ProtocolConformanceRef`가 conformance를 표현. 런타임에는 [[glossary-compiler|witness table]]로 구체화.

## Conformance 종류

| 종류 | 설명 |
|------|------|
| **Normal** | 명시적 conformance 선언 (`struct Foo: Protocol`) |
| **Inherited** | 슈퍼클래스에서 상속 |
| **Conditional** | 조건부 (`extension Array: Equatable where Element: Equatable`) |
| **Specialized** | 제네릭 특수화 후의 conformance |

## Requirement Signature

프로토콜 자체의 generic signature 변형. 프로토콜의 associated type과 요구사항을 기술. Protocol witness table 엔트리와 대응.

## Conformance Lookup

1. 타입의 선언과 확장에서 conformance 탐색
2. 조건부 conformance의 조건 검증
3. [[substitution-maps]]에 conformance 정보 저장

### 파일 위치

- `swift/lib/AST/ProtocolConformance.cpp`
- `swift/lib/AST/ConformanceLookupTable.cpp`

관련 페이지: [[compiling-swift-generics]], [[generic-signatures]], [[substitution-maps]], [[glossary-compiler]]
