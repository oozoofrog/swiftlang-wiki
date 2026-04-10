---
type: summary
category: learning
tags: [swift, compiler, ecosystem, map, learning]
aliases: [Swift 전체 지도, Swift 생태계 지도, Swift/Compiler 전체 지도]
sources: [swift-readme.md, docs-index.md, swift.org/documentation/index.html, swift.org/documentation/swift-compiler/index.html]
---

# Swift 전체 지도

이 페이지는 “Swift와 Swift Compiler 전체를 어디서부터 어떻게 읽을까?”를 위한 최상위 허브다.
이 위키의 다른 페이지들이 개별 주제의 설명서라면,
이 페이지는 그 설명서들을 하나의 지도처럼 묶어 주는 입구다.

## Swift 전체를 이루는 5개 층

| 층 | 질문 | 먼저 갈 페이지 |
|---|---|---|
| 언어 | Swift는 어떤 언어인가? | [[swift-language-overview]] |
| 구현 | Swift는 컴파일러 안에서 어떻게 구현되는가? | [[overview]], [[swift-and-swift-compiler]] |
| 툴체인 | 컴파일러를 둘러싼 도구와 저장소는 무엇인가? | [[swift-toolchain-stack]] |
| 학습 경로 | 무엇을 어떤 순서로 공부해야 하는가? | [[swift-compiler-learning-stack]], [[swift-compiler-7-day-course]] |
| 생태계 | 패키지, 라이브러리, IDE 도구는 어떻게 연결되는가? | [[keyword-network]], [[official-docs/index]] |

## 이 위키에서 말하는 “Swift 전체”란 무엇인가

이 위키의 목표는 Swift를 단순히 “문법이 있는 프로그래밍 언어”로 다루는 데서 멈추지 않는 것이다.
Swift를 이해하려면 최소한 다음을 함께 봐야 한다.

1. 언어 표면
   - 문법, 타입 시스템, 제네릭, 동시성, 모듈, 상호운용성
2. 표준 라이브러리와 런타임
   - 값/참조 의미론, ABI, metadata, library evolution
   - ownership, borrowing, ARC, lifetime
3. 컴파일러 구현
   - Parser, Sema, Request Evaluator, SIL, IRGen, LLVM backend
4. 툴체인과 빌드 인프라
   - swift-driver, SwiftPM, llbuild, Swift Build, CMake, Ninja, lit, LLDB
5. 실사용 생태계
   - SwiftSyntax, SourceKit-LSP, Foundation, Testing, Collections, NIO, formatters

## 어떤 사람에게 어떤 출발점이 좋은가

### 1. Swift 언어부터 이해하고 싶은 경우
- [[swift-language-overview]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[official-docs/tspl-to-compiler-crosswalk]]
- [[official-docs/language-to-compiler-crosswalk]]

### 2. Swift Compiler 구조부터 이해하고 싶은 경우
- [[overview]]
- [[swift-and-swift-compiler]]
- [[swift-compiler-7-day-course]]

### 3. 툴체인/저장소 전체 구성이 궁금한 경우
- [[swift-toolchain-stack]]
- [[compiler-driver]]
- [[swift-driver-package]]
- [[swift-package-manager]]

### 4. 실제 기여와 빌드/테스트 루프가 궁금한 경우
- [[swift-compiler-learning-stack]]
- [[getting-started]]
- [[testing-guide]]
- [[development-tips]]
- [[debugging-the-compiler]]

## 큰 그림에서 가장 중요한 상호관계

- Swift 언어 기능은 결국 Parser / Sema / SIL / ABI 규칙으로 내려간다.
- 표준 라이브러리와 Foundation 같은 실사용 계층은 언어와 ABI의 제약을 그대로 받는다.
- SwiftPM, SourceKit-LSP, SwiftSyntax 같은 도구 계층은 컴파일러 프론트엔드와 강하게 얽혀 있다.
- C/ObjC/C++ interop는 Clang Importer와 모듈 시스템을 통해 언어/컴파일러/생태계를 한 번에 이어 준다.

## 추천 읽기 순서

1. [[swift-language-overview]]
2. [[swift-and-swift-compiler]]
3. [[swift-ownership-memory-model]]
4. [[swift-concurrency-architecture]]
5. [[swift-actor-isolation-and-sendable]]
6. [[swift-task-executor-runtime]]
7. [[swift-toolchain-stack]]
8. [[swift-compiler-learning-stack]]
9. [[keyword-network]]
10. [[official-docs/index]]

## 같이 보면 좋은 페이지

- [[overview]]
- [[official-docs/index]]
- [[official-docs/language-to-compiler-crosswalk]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[keyword-network]]
- [[glossary-compiler]]
- [[swift-compiler-7-day-course]]

이 페이지를 기준으로 보면,
이 위키는 더 이상 “Swift compiler 내부 문서 모음”이 아니라
“Swift 언어, 구현, 도구, 생태계 전체를 연결해서 읽는 지식 베이스”가 된다.
