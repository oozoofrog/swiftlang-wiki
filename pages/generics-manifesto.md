---
type: concept
category: compiler
tags: [generics, type-system, manifesto, protocols]
aliases: [제네릭 매니페스토, Generics Manifesto, Complete Generics]
sources: [generics-manifesto.md]
---

# 제네릭 매니페스토

Swift 제네릭 시스템의 장기 비전. 원본: `swift/docs/GenericsManifesto.md` (Douglas Gregor, 2016)

## 불필요한 제한 제거 (구현됨)

| 기능 | 상태 | 릴리스 |
|------|------|--------|
| 재귀 프로토콜 제약 | SE-0157 | Swift 4.1 |
| 중첩 제네릭 | 구현됨 | Swift 3.1 |
| 구체 same-type 요구사항 | 구현됨 | Swift 3.1 |

## 조건부 conformance

`extension Array: Equatable where Element: Equatable` — 요소가 특정 프로토콜을 준수할 때만 컨테이너도 준수. **SE-0143, Swift 4.1**

## 주요 미래 방향

- **Variadic generics**: 가변 개수 제네릭 파라미터 (`each T`)
- **Opaque return types**: `some Protocol` — **SE-0244, Swift 5.1**
- **Existential types**: `any Protocol` — **SE-0335, Swift 5.6**
- **Parameter packs**: `<each T>` — **SE-0393, Swift 5.9**
- **Generic associated types**: 연관 타입에 제네릭 파라미터

## 컴파일러 내부

- `swift/docs/Generics/` — "Compiling Swift Generics" 책
- Generic signature, requirement machine, substitution map 등

관련 페이지: [[compiling-swift-generics]], [[generic-signatures]], [[type-checker]], [[glossary-compiler]], [[overview]]
