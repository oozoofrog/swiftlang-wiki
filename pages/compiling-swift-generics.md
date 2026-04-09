---
type: summary
category: compiler
tags: [generics, compilation, book, type-system, signatures]
aliases: [Compiling Swift Generics, 제네릭 컴파일]
sources: [generics-book-readme.md]
---

# Compiling Swift Generics

Swift 컴파일러의 제네릭(parametric polymorphism) 구현에 관한 책. TeX 형식, PDF 제공.
원본: `swift/docs/Generics/` (24개 챕터)

> PDF: https://download.swift.org/docs/assets/generics.pdf

## 설계 제약

1. 제네릭 함수는 모든 가능한 인자를 알지 않고도 독립적으로 타입 검사 가능해야 함
2. 공유 라이브러리가 resilient하게 진화 가능해야 함
3. 제네릭 struct/enum은 박싱 없이 필드를 인라인 저장해야 함
4. 런타임 오버헤드는 절대적으로 필요한 경우에만 (모듈 경계, 타입 정보 부재 시)

## 핵심 시맨틱 객체

| 객체 | 역할 | 상세 |
|------|------|------|
| **Generic Signature** | 제네릭 파라미터 + 요구사항 목록 | [[generic-signatures]] |
| **Substitution Map** | 제네릭 파라미터 → 구체 타입 매핑 | [[substitution-maps]] |
| **Conformance** | 타입이 프로토콜을 준수하는 방법 | [[conformances]] |
| **Archetype** | 제네릭 컨텍스트 내 "가장 일반적인 구체 타입" | [[archetypes]] |

## 컴파일 파이프라인 (Generics 관점)

```
Parse → Sema(타입 검사 + Generic Signature 구성)
→ SILGen(Archetype으로 lowering)
→ SILOptimizer(Generic Specialization)
→ IRGen(타입 메타데이터 전달)
```

- **타입 검사**: generic signature에서 derived requirements 추론, requirement minimization
- **SILGen**: interface type → contextual type 변환 (archetype 사용)
- **최적화**: 정의가 보이면 **specialization**으로 제네릭 오버헤드 제거
- **IRGen**: 런타임 타입 메타데이터를 caller가 전달

## 챕터 구성

### Part I: 개요
- Introduction — 설계 제약, 핵심 객체 소개
- Compilation Model — 드라이버, 프론트엔드, 파이프라인 ([[compiler-driver]])

### Part II: 시맨틱 객체
- Declarations — 제네릭 선언 구문과 의미
- Types — 타입 표현, 타입 해석 ([[glossary-compiler]])
- Generic Signatures — 파라미터 + 요구사항, 최소화, 정규화 ([[generic-signatures]])
- Substitution Maps — 타입 치환 ([[substitution-maps]])
- Archetypes — 제네릭 환경, contextual type ([[archetypes]])
- Conformances — 프로토콜 준수 표현 ([[conformances]])

### Part III: 타입 해석
- Type Resolution — 구문 → 시맨틱 타입 변환
- Extensions — 확장에서의 제네릭
- Opaque Result Types — `some Protocol`
- Existential Types — `any Protocol`

### Part IV: Generic Signature 구축
- Building Generic Signatures — 요구사항 수집 → 최소화
- Symbols, Terms, and Rules — 형식 체계
- The Property Map / Completion / Minimization

## 파일 위치

- `swift/docs/Generics/` — TeX 소스 + Makefile
- `swift/lib/AST/GenericSignature*.cpp` — 구현
- `swift/lib/AST/SubstitutionMap.cpp` — 치환 맵
- `swift/include/swift/AST/GenericSignature.h` — 헤더

관련 페이지: [[generics-manifesto]], [[type-checker]], [[overview]], [[abi-generic-signature]], [[glossary-compiler]]
