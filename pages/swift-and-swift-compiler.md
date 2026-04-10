---
type: concept
category: learning
tags: [swift, compiler, relationship, architecture, crosswalk]
aliases: [Swift와 Swift Compiler, 언어와 컴파일러의 관계, Swift ↔ Compiler]
sources: [swift-readme.md, docs-index.md, swift.org/documentation/swift-compiler/index.html]
---

# Swift와 Swift Compiler의 관계

이 페이지는 “Swift라는 언어”와 “Swift Compiler라는 구현체”가 어떻게 연결되는지를 정리한다.
Swift를 배우다 보면 둘이 같은 것처럼 보일 때가 많지만,
실제로는 구분해야 할 층과 서로 강하게 영향을 주는 층이 함께 존재한다.

## 가장 짧은 요약

- Swift는 언어다.
- Swift Compiler는 그 언어의 주된 구현체다.
- 하지만 Swift의 핵심 특성들 중 상당수는 컴파일러 구현을 함께 보지 않으면 제대로 이해되지 않는다.

## 층별로 보면 어떻게 다른가

| 층 | Swift 쪽 질문 | Compiler 쪽 질문 | 연결 페이지 |
|---|---|---|---|
| 문법 | 어떤 선언과 표현식을 쓸 수 있는가 | 파서는 그것을 어떻게 AST로 읽는가 | [[modules]], [[literals]], [[overview]] |
| 의미 분석 | 타입, 프로토콜, 제네릭, 오류는 어떤 규칙을 가지는가 | Sema와 constraint solver는 그 규칙을 어떻게 판정하는가 | [[type-checker]], [[diagnostics]], [[generic-signatures]] |
| 중간 표현 | 언어 의미가 어떤 실행/최적화 단위로 바뀌는가 | SILGen, SIL, optimizer가 어떻게 lowering하는가 | [[sil-reference]], [[sil-ownership]], [[optimizer-design]] |
| ABI/런타임 | 프로그램이 바이너리와 메모리에서 어떤 약속을 지는가 | IRGen과 runtime은 그 약속을 어떻게 구현하는가 | [[abi-stability]], [[abi-type-layout]], [[runtime]] |
| 도구/생태계 | 패키지, 에디터, 테스트, 포맷터는 어떻게 쓰는가 | driver, SwiftPM, SourceKit-LSP, SwiftSyntax는 어떻게 컴파일러와 연결되는가 | [[swift-toolchain-stack]], [[sourcekit-lsp]], [[swift-syntax-package]] |

## 언어 기능이 곧바로 컴파일러 일이 되는 지점

### 1. 제네릭
사용자는 `func f<T: P>(_ x: T)` 같은 선언을 본다.
하지만 컴파일러는 이를
- generic signature
- substitution map
- archetype
- conformance lookup
의 문제로 풀어낸다.

관련 페이지:
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[conformances]]

### 2. 동시성
사용자는 `actor`, `async`, `await`, `Sendable`을 본다.
하지만 컴파일러는 이를
- actor isolation 검사
- sendability 판정
- flow isolation
- ownership / region 추적
의 문제로 다룬다.

관련 페이지:
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[swift-ownership-memory-model]]
- [[concurrency-data-race-safety]]
- [[type-checker]]
- [[sil-optimizer-pass-catalog]]
- [[sil-ownership]]

### 3. ABI와 라이브러리 진화
사용자는 public API의 변화와 배포 호환성을 본다.
컴파일러는 이를
- metadata layout
- calling convention
- resilience boundary
- serialization / module interface
의 문제로 본다.

관련 페이지:
- [[abi-stability]]
- [[library-evolution]]
- [[serialization]]
- [[abi-calling-convention]]

## 반대로, 컴파일러 구현이 언어 이해를 바꾸는 지점

- 진단 시스템을 보면 Swift의 문법보다 “어떤 의미를 중요하게 여기는가”가 드러난다.
- SIL을 보면 고수준 언어 의미가 실제로 어떤 추상기계로 내려가는지 보인다.
- ABI 문서를 보면 왜 어떤 언어 기능은 쉽게 추가되지 않는지 이해하게 된다.
- interop 페이지를 보면 Swift가 독립 언어이면서도 C/ObjC/C++ 세계와 어떻게 타협하는지 보인다.

## 왜 둘을 함께 배워야 하나

Swift를 실전에서 깊게 이해하려면 다음 질문들이 결국 컴파일러 질문으로 바뀐다.

- 왜 이 표현식은 타입 추론이 안 되지?
- 왜 이 API 변경은 source-compatible인데 ABI-safe하지 않지?
- 왜 이 concurrency 코드는 warning에서 error로 승격되지?
- 왜 이 generic abstraction은 specialization되는데 저건 안 되지?
- 왜 이 interop API는 Swift 이름이 이렇게 바뀌지?

즉 Swift와 Swift Compiler는 “서로 다른 주제”이면서 동시에
서로를 설명하는 가장 강력한 문맥이기도 하다.

## 추천 읽기 순서

1. [[swift-language-overview]]
2. [[official-docs/language-to-compiler-crosswalk]]
3. [[overview]]
4. [[type-checker]]
5. [[sil-reference]]
6. [[abi-stability]]
7. [[swift-toolchain-stack]]

## 같이 보면 좋은 페이지

- [[swift-ecosystem-map]]
- [[swift-language-overview]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[swift-ownership-memory-model]]
- [[overview]]
- [[official-docs/language-to-compiler-crosswalk]]
- [[swift-compiler-learning-stack]]
