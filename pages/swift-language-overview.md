---
title: swift-language-overview
type: summary
category: learning
tags: [swift, language, overview, semantics, ecosystem]
aliases: [Swift 언어 개요, Swift 개요, Swift Language Overview]
sources: [swift-readme.md, swift.org/documentation/index.html, swift.org/documentation/tspl/index.html]
---

# swift-language-overview

이 페이지의 목적은 Swift를 “문법 목록”이 아니라
언어 의미, 라이브러리, 런타임, 도구 생태계까지 포함한 하나의 시스템으로 보는 데 있다.

## Swift를 이해할 때 같이 봐야 하는 층

| 층 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| 표면 문법 | 사용자가 어떤 문법과 선언 모델을 쓰는가 | [[official-docs/tspl-to-compiler-crosswalk]], [[modules]], [[access-control]], [[literals]] |
| 타입 시스템 | 값, 참조, 프로토콜, 제네릭, 오류, 동시성을 어떻게 모델링하는가 | [[type-checker]], [[generic-signatures]], [[error-handling]], [[swift-concurrency-architecture]], [[concurrency-data-race-safety]] |
| 실행 의미 | 값/참조 의미론, 소유권, 메모리, 런타임은 어떻게 작동하는가 | [[ownership-manifesto]], [[sil-ownership]], [[runtime]], [[abi-type-metadata]] |
| ABI/배포 | 모듈 안정성, ABI 안정성, 라이브러리 진화는 어떻게 다뤄지는가 | [[abi-stability]], [[library-evolution]], [[serialization]] |
| 생태계 | SwiftPM, Foundation, SwiftSyntax, SourceKit-LSP 같은 도구/패키지는 어디에 위치하는가 | [[swift-package-manager]], [[swift-foundation-package]], [[swift-syntax-package]], [[sourcekit-lsp]] |

## Swift를 구성하는 핵심 주제들

### 1. 표현식과 선언
Swift는 사용성이 높은 표면 문법을 제공하지만,
실제로는 파서가 AST를 만들고 타입 체커가 의미를 채워 넣으면서 언어가 완성된다.

바로 이어지는 구현 축:
- [[overview]]
- [[type-checker]]
- [[request-evaluator]]

### 2. 프로토콜과 제네릭
Swift의 핵심 정체성 중 하나는 제네릭과 프로토콜 중심 설계다.
이 축을 이해하지 못하면 표준 라이브러리, 최적화, ABI까지 모두 끊겨 보인다.

관련 페이지:
- [[swift-type-system]]
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[conformances]]
- [[generics-manifesto]]

### 3. 값 의미론과 소유권
Swift는 value semantics를 강하게 강조하지만,
실제 구현에서는 ARC, borrow, OSSA, copy-on-write 같은 메커니즘이 함께 작동한다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[standard-library-runtime-and-compiler]]
- [[ownership-manifesto]]
- [[sil-ownership]]
- [[sil-arc-optimization]]
- [[official-docs/value-reference-types-to-sil-ownership]]

### 4. 동시성과 안전성
Swift 6 이후에는 동시성이 단지 async/await 문법이 아니라
정적 안전성 검사 체계라는 점이 훨씬 중요해졌다.

관련 페이지:
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[concurrency-data-race-safety]]
- [[diagnostics]]
- [[sil-optimizer-pass-catalog]]

### 5. 상호운용성과 모듈 경계
Swift는 독립 언어이면서도 C, Objective-C, C++와의 상호운용을 전략적으로 중시한다.
그래서 module, importer, naming, overlay 구조를 함께 보는 것이 중요하다.

관련 페이지:
- [[swift-macro-tooling-stack]]
- [[objc-interop]]
- [[c-to-swift-name-translation]]
- [[how-swift-imports-c-apis]]
- [[cpp-interop-overview]]

## Swift는 컴파일러 없이 설명될 수 있는가

부분적으로는 가능하지만, 완전하게는 어렵다.
Swift의 제네릭, ownership, concurrency, resilience 같은 중요한 특성은
언어 사양의 문장만으로는 충분히 이해되지 않고,
컴파일러의 제약과 구현 구조를 같이 봐야 제대로 보인다.

그래서 이 위키에서는 Swift를 배울 때 자연스럽게
- [[swift-and-swift-compiler]]
- [[official-docs/language-to-compiler-crosswalk]]
- [[swift-compiler-learning-stack]]
으로 넘어가게 설계한다.

## Swift를 배우는 세 가지 관점

1. 사용자 관점
   - 문법, 라이브러리, 패키지, 앱/서버 코드 작성
2. 구현 관점
   - Parser, Sema, SIL, IRGen, ABI, runtime
3. 도구 관점
   - SwiftPM, driver, SourceKit-LSP, SwiftSyntax, LLDB

이 세 관점이 같이 연결될 때 Swift 전체가 보이기 시작한다.

## 추천 읽기 순서

1. [[official-docs/tspl-to-compiler-crosswalk]]
2. [[official-docs/language-to-compiler-crosswalk]]
3. [[swift-and-swift-compiler]]
4. [[swift-toolchain-stack]]
5. [[keyword-network]]

## 같이 보면 좋은 페이지

- [[swift-ecosystem-map]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[swift-evolution-and-proposal-history]]
- [[standard-library-runtime-and-compiler]]
- [[swift-macro-tooling-stack]]
- [[overview]]
- [[swift-and-swift-compiler]]
- [[swift-compiler-learning-stack]]
- [[official-docs/index]]
