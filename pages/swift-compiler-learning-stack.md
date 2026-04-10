---
type: summary
category: learning
tags: [swift, compiler, learning, roadmap, toolchain, stack]
aliases: [Swift Compiler 학습 스택, Swift Compiler 학습 로드맵, Swift 학습 스택]
sources: [swift.org/documentation/tspl/index.html, swift.org/documentation/swift-compiler/index.html, getting-started.md, testing.md, swiftlang-swift/docs/SIL/SIL.md]
---

# Swift Compiler 학습 스택

Swift Compiler를 배우기 위해 필요한 기술 스택은 생각보다 넓다.
이 페이지는 “무엇을 어느 정도까지 알아야 하는가?”를 학습 관점에서 정리한 로드맵이다.

## 핵심 원칙

Swift Compiler를 배우는 데 필요한 지식은 한 덩어리가 아니다.
대략 다음 다섯 층으로 쌓인다.

1. Swift 언어 이해
2. 컴파일러 일반 교양
3. Swift 특유의 구현 축
4. 빌드/테스트/디버그 도구
5. 생태계 패키지와 실전 도구

## 레벨별 학습 스택

### Level 0 — Swift 언어 사용자 시야
먼저 Swift를 실제로 쓰는 언어로 이해해야 한다.

필수 주제:
- declarations / expressions / modules
- protocol / generic / existential / opaque type
- ownership 감각과 값/참조 의미론
- concurrency와 `Sendable`
- SwiftPM 기반 프로젝트 구조

추천 페이지:
- [[swift-language-overview]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[standard-library-runtime-and-compiler]]
- [[official-docs/tspl-to-compiler-crosswalk]]
- [[official-docs/language-to-compiler-crosswalk]]
- [[swift-package-manager]]

### Level 1 — 컴파일러 일반 교양
Swift 고유 세부 구현으로 들어가기 전에,
컴파일러 전반에서 반복되는 개념을 알아두면 훨씬 덜 헤맨다.

필수 주제:
- parsing / AST
- semantic analysis
- type checking / constraint solving
- IR / SSA / optimization
- calling convention / ABI / runtime

추천 페이지:
- [[overview]]
- [[type-checker]]
- [[sil-reference]]
- [[abi-stability]]
- [[runtime]]

### Level 2 — Swift 특유의 핵심 구현
이 지점부터가 “Swift Compiler답다”는 느낌이 강해진다.

필수 주제:
- generic signature / archetype / substitution map
- protocol conformance model
- OSSA와 ownership
- resilience / library evolution
- strict concurrency checking

추천 페이지:
- [[compiling-swift-generics]]
- [[swift-ownership-memory-model]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[conformances]]
- [[sil-ownership]]
- [[library-evolution]]
- [[concurrency-data-race-safety]]

### Level 3 — 툴체인 실무 스택
여기서부터는 “읽기”뿐 아니라 “만지고 검증하는 능력”이 붙는다.

필수 주제:
- build-script / driver / SwiftPM / llbuild
- CMake / Ninja 기반 빌드 감각
- lit / FileCheck 테스트 문화
- LLDB 디버깅 루프
- CI와 validation 흐름

추천 페이지:
- [[swift-toolchain-stack]]
- [[swift-compiler-build-test-debug-stack]]
- [[cmake-and-ninja-build]]
- [[lit-and-filecheck]]
- [[lldb-and-swift-debugging]]
- [[llvm-backend]]
- [[getting-started]]
- [[testing-guide]]
- [[development-tips]]
- [[debugging-the-compiler]]
- [[continuous-integration]]

### Level 4 — 생태계와 도구 층
컴파일러만이 아니라 주변 도구와 패키지까지 연결되면 훨씬 입체적으로 보인다.

필수 주제:
- SwiftSyntax와 매크로/구문 도구
- SourceKit-LSP와 IDE 경험
- Foundation / Testing / Collections / NIO 같은 대표 패키지
- interop가 실제 라이브러리 경계에서 어떤 의미를 가지는지

추천 페이지:
- [[swift-macro-tooling-stack]]
- [[swift-syntax-package]]
- [[sourcekit-lsp]]
- [[swift-foundation-package]]
- [[swift-testing-package]]
- [[swift-collections-package]]
- [[swift-nio-package]]
- [[cpp-interop-overview]]

## 무엇을 얼마나 깊게 알아야 하나

| 목표 | 필요한 깊이 |
|---|---|
| Swift 언어를 잘 쓰는 개발자 | Level 0~1 |
| 컴파일러 위키를 읽고 길을 잃지 않는 수준 | Level 0~2 |
| 간단한 문서/테스트/진단 수정 기여 | Level 0~3 |
| Sema/SIL/ABI 쪽 구현 기여 | Level 0~4 |
| 툴체인/생태계 전체를 설계 관점으로 보기 | Level 0~4 + 지속적 확장 |

## 추천 학습 루트

### 빠른 전체 지도 루트
1. [[swift-ecosystem-map]]
2. [[swift-language-overview]]
3. [[swift-and-swift-compiler]]
4. [[swift-ownership-memory-model]]
5. [[swift-toolchain-stack]]
6. [[keyword-network]]

### 구현 중심 루트
1. [[overview]]
2. [[type-checker]]
3. [[sil-reference]]
4. [[optimizer-design]]
5. [[abi-stability]]

### 기여 중심 루트
1. [[getting-started]]
2. [[testing-guide]]
3. [[development-tips]]
4. [[debugging-the-compiler]]
5. [[first-pull-request]]

### 언어 ↔ 구현 연결 루트
1. [[official-docs/language-to-compiler-crosswalk]]
2. [[swift-and-swift-compiler]]
3. [[compiling-swift-generics]]
4. [[concurrency-data-race-safety]]
5. [[library-evolution]]

## 이 위키에서 다음에 더 보강할 축

- Swift concurrency 전체 구조 허브
- Swift Evolution / proposal history 허브

## 같이 보면 좋은 페이지

- [[swift-ecosystem-map]]
- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-ownership-memory-model]]
- [[swift-toolchain-stack]]
- [[swift-compiler-7-day-course]]
