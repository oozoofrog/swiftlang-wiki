---
type: summary
category: learning
tags: [keywords, glossary, crosswalk, navigation]
aliases: [키워드 연결망, 키워드 네트워크, 개념 연결망]
sources: [glossary-compiler.md, official-docs/language-to-compiler-crosswalk.md]
---

# 위키 키워드 연결망

이 페이지는 Swift 컴파일러 위키의 키워드를 **허브처럼 묶어 주는 안내 페이지**다.
어떤 단어를 봤을 때 “이건 어느 페이지로 가야 하지?” 싶은 경우,
검색보다 먼저 여기서 키워드 덩어리를 따라가면 이동이 훨씬 빨라진다.

## 빠른 이동

- Swift 전체 최상위 허브: [[swift-ecosystem-map]]
- Swift 언어 입구: [[swift-language-overview]]
- 언어 ↔ 구현 브리지: [[swift-and-swift-compiler]]
- Swift 타입 시스템 허브: [[swift-type-system]]
- Swift 소유권·메모리 모델 허브: [[swift-ownership-memory-model]]
- Swift Concurrency 허브: [[swift-concurrency-architecture]]
- Swift actor isolation·Sendable 허브: [[swift-actor-isolation-and-sendable]]
- Swift Task·Executor·Runtime 허브: [[swift-task-executor-runtime]]
- Swift Evolution / proposal history 허브: [[swift-evolution-and-proposal-history]]
- Value Semantics / COW proposal 교차 읽기: [[proposal-value-semantics-and-cow-to-ownership]]
- Declaration Type Checker proposal 교차 읽기: [[proposal-declaration-type-checker-to-sema]]
- Compilation Model / WMO proposal 교차 읽기: [[proposal-compilation-model-and-wmo-to-driver]]
- ObjC interop proposal 교차 읽기: [[proposal-objc-interop-to-importer-and-dispatch]]
- Initialization/Accessors proposal 교차 읽기: [[proposal-initialization-and-accessors-to-property-model]]
- Remote Mirrors proposal 교차 읽기: [[proposal-remote-mirrors-to-runtime-reflection]]
- stdlib/runtime/compiler 허브: [[standard-library-runtime-and-compiler]]
- 툴체인 전체 지도: [[swift-toolchain-stack]]
- 매크로/도구 허브: [[swift-macro-tooling-stack]]
- 학습 로드맵: [[swift-compiler-learning-stack]]
- 언어 → 구현 전체 지도: [[official-docs/language-to-compiler-crosswalk]]
- 입문 루트: [[swift-compiler-7-day-course]]
- 용어 정의: [[glossary-compiler]]
- 큰 그림: [[overview]]

## 0. Swift 전체 / 학습 허브

핵심 키워드:
- [[swift-ecosystem-map|Swift 전체]]
- [[swift-language-overview|Swift 언어]]
- [[swift-and-swift-compiler|Swift ↔ Compiler]]
- [[swift-type-system|type system]]
- [[swift-ownership-memory-model|ownership/memory]]
- [[swift-concurrency-architecture|concurrency architecture]]
- [[swift-actor-isolation-and-sendable|actor/sendable]]
- [[swift-task-executor-runtime|task/executor/runtime]]
- [[swift-evolution-and-proposal-history|evolution/proposal history]]
- [[proposal-value-semantics-and-cow-to-ownership|value semantics/COW]]
- [[proposal-declaration-type-checker-to-sema|declaration type checker proposal]]
- [[proposal-compilation-model-and-wmo-to-driver|compilation model/WMO]]
- [[proposal-objc-interop-to-importer-and-dispatch|objc interop proposal]]
- [[proposal-initialization-and-accessors-to-property-model|initialization/accessors]]
- [[proposal-remote-mirrors-to-runtime-reflection|remote mirrors]]
- [[standard-library-runtime-and-compiler|stdlib/runtime/compiler]]
- [[swift-toolchain-stack|toolchain stack]]
- [[swift-macro-tooling-stack|macro/tooling]]
- [[swift-compiler-learning-stack|learning stack]]

추천 이동:
- Swift를 언어/도구/생태계 전체로 보고 싶다 → [[swift-ecosystem-map]]
- 언어 개념부터 컴파일러로 넘어가고 싶다 → [[swift-language-overview]] / [[swift-and-swift-compiler]]
- 타입 시스템을 generics/ABI/runtime까지 연결해서 보고 싶다 → [[swift-type-system]]
- ownership, borrow, lifetime, ARC를 한 장으로 먼저 잡고 싶다 → [[swift-ownership-memory-model]]
- task, actor, executor, Sendable까지 동시성 전체 그림을 먼저 잡고 싶다 → [[swift-concurrency-architecture]]
- actor 경계와 `Sendable` 오류를 집중해서 보고 싶다 → [[swift-actor-isolation-and-sendable]]
- task / executor / runtime 실행 모델을 보고 싶다 → [[swift-task-executor-runtime]]
- 왜 이런 기능들이 이런 방향으로 왔는지 설계 역사를 보고 싶다 → [[swift-evolution-and-proposal-history]]
- 기본 타입/표준 라이브러리/런타임이 어떻게 한 몸인지 보고 싶다 → [[standard-library-runtime-and-compiler]]
- SwiftSyntax / 매크로 / SourceKit 도구축을 보고 싶다 → [[swift-macro-tooling-stack]]
- 무엇을 어느 정도까지 배워야 할지 알고 싶다 → [[swift-compiler-learning-stack]]
- LLVM / driver / SwiftPM / LLDB 같은 주변 스택까지 보고 싶다 → [[swift-toolchain-stack]]

## 1. 구문 / 파싱 / 표면 문법

핵심 키워드:
- [[modules|module]]
- [[literals|literal]]
- [[access-control|access control]]
- [[swift-macro-tooling-stack|macro/tooling]]
- [[swift-syntax-package|SwiftSyntax]]
- [[sourcekit-lsp|LSP]]

추천 이동:
- 표면 문법과 도구층을 같이 보고 싶다 → [[swift-macro-tooling-stack]]
- 문법을 읽다가 AST/구문 트리 쪽으로 가고 싶다 → [[swift-syntax-package]]
- 파싱 이후 의미 부여 단계가 궁금하다 → [[type-checker]]
- 소스 편집기 기능과 연결해서 보고 싶다 → [[sourcekit-lsp]]

## 2. 타입 체커 / 진단 / 의미 분석

핵심 키워드:
- [[swift-type-system|type system]]
- [[type-checker|Sema]]
- [[type-checker|constraint system]]
- [[diagnostics]]
- [[request-evaluator]]
- [[concurrency-data-race-safety|actor isolation / Sendable]]

추천 이동:
- 타입 시스템 전체 지형부터 보고 싶다 → [[swift-type-system]]
- 오버로드/리터럴/클로저 추론이 궁금하다 → [[type-checker]]
- 오류 메시지가 어떻게 만들어지는지 궁금하다 → [[diagnostics]] / [[official-docs/diagnostics-authoring]]
- Swift 6 concurrency 안전성 검사가 궁금하다 → [[concurrency-data-race-safety]]

## 3. 제네릭 / 프로토콜 / 시그니처

핵심 키워드:
- [[swift-type-system|type system]]
- [[generic-signatures|generic signature]]
- [[archetypes|archetype]]
- [[substitution-maps|substitution map]]
- [[conformances|conformance]]
- [[official-docs/compiling-swift-generics-pdf|Compiling Swift Generics]]

추천 이동:
- 구현 중심으로 빠르게 들어가고 싶다 → [[compiling-swift-generics]]
- 상위 개념부터 정리하고 싶다 → [[swift-type-system]]
- 비전/설계까지 보고 싶다 → [[generics-manifesto]] / [[official-docs/swift-generics-manifesto]]
- ABI와 연결해 보고 싶다 → [[abi-generic-signature]]

## 4. SIL / Ownership / 메모리 모델 / 최적화

핵심 키워드:
- [[sil-reference|SIL]]
- [[sil-reference|raw SIL]]
- [[sil-reference|canonical SIL]]
- [[swift-ownership-memory-model|ownership/memory]]
- [[sil-ownership|OSSA]]
- [[sil-function-attributes|function attributes]]
- [[transparent-attr|@_transparent]]
- [[high-level-sil-optimizations|@_semantics]]
- [[sil-optimizer-pass-catalog|mandatory passes]]

추천 이동:
- SIL 전체 구조부터 보고 싶다 → [[sil-reference]]
- ownership/memory 큰 그림부터 잡고 싶다 → [[swift-ownership-memory-model]]
- ownership/borrow와 연결해서 보고 싶다 → [[sil-ownership]] / [[ownership-manifesto]]
- 최적화 패스 지형을 보고 싶다 → [[optimizer-design]] / [[sil-optimizer-pass-catalog]]
- 함수 속성과 인라이닝 정책이 궁금하다 → [[sil-function-attributes]] / [[transparent-attr]]

## 5. 동시성 / 격리 / 전송 가능성

핵심 키워드:
- [[swift-concurrency-architecture|concurrency architecture]]
- [[swift-actor-isolation-and-sendable|actor/sendable]]
- [[swift-task-executor-runtime|task/executor/runtime]]
- [[concurrency-data-race-safety|Strict Concurrency]]
- [[concurrency-data-race-safety|Sendable]]
- [[concurrency-data-race-safety|actor isolation]]
- [[sil-optimizer-pass-catalog|SendNonSendable]]
- [[sil-optimizer-pass-catalog|FlowIsolation]]

추천 이동:
- 전체 구조부터 보고 싶다 → [[swift-concurrency-architecture]]
- actor 경계와 sendability만 먼저 보고 싶다 → [[swift-actor-isolation-and-sendable]]
- 실행 모델과 executor hop을 보고 싶다 → [[swift-task-executor-runtime]]
- 설정/마이그레이션부터 보고 싶다 → [[concurrency-data-race-safety]]
- 공식 문서 입구에서 들어가고 싶다 → [[official-docs/concurrency-data-race-safety-to-compiler-checks]]
- ownership과 같이 보고 싶다 → [[swift-ownership-memory-model]] / [[sil-ownership]] / [[official-docs/value-reference-types-to-sil-ownership]]

## 6. ABI / 런타임 / 라이브러리 진화

핵심 키워드:
- [[standard-library-runtime-and-compiler|stdlib/runtime/compiler]]
- [[abi-stability|ABI stability]]
- [[abi-type-layout|type layout]]
- [[abi-type-metadata|metadata]]
- [[abi-calling-convention|reabstraction]]
- [[abi-mangling|mangling]]
- [[runtime]]
- [[library-evolution|fragile / resilient]]
- [[serialization|swiftmodule serialization]]

추천 이동:
- 표준 라이브러리, runtime, compiler 관계를 한 번에 보고 싶다 → [[standard-library-runtime-and-compiler]]
- concurrency runtime 축을 보고 싶다 → [[swift-task-executor-runtime]]
- 큰 그림 선언문부터 보고 싶다 → [[official-docs/abi-stability-manifesto]]
- 레이아웃/메타데이터로 바로 들어가고 싶다 → [[abi-type-layout]] / [[abi-type-metadata]]
- 공개 API 변화와 바이너리 호환성을 보고 싶다 → [[library-evolution]]

## 7. 드라이버 / 빌드 / 도구 / 패키지 생태계

핵심 키워드:
- [[compiler-driver|driver]]
- [[compiler-driver|WMO]]
- [[dependency-analysis]]
- [[swift-driver-package]]
- [[llbuild-package]]
- [[swift-package-manager]]
- [[swift-build-package]]
- [[sourcekit-lsp]]
- [[swift-compiler-build-test-debug-stack|build/test/debug]]
- [[cmake-and-ninja-build|CMake / Ninja]]
- [[lit-and-filecheck|lit / FileCheck]]
- [[lldb-and-swift-debugging|LLDB]]
- [[llvm-backend|LLVM backend]]

추천 이동:
- Swift가 왜 모듈 전체를 의식하며 컴파일되는지 보고 싶다 → [[compiler-driver]] / [[dependency-analysis]]
- 구현 패키지 구조를 보고 싶다 → [[swift-driver-package]] / [[llbuild-package]]
- 실제 기여 루프를 한 장으로 보고 싶다 → [[swift-compiler-build-test-debug-stack]]
- 빌드 인프라를 먼저 이해하고 싶다 → [[cmake-and-ninja-build]]
- 테스트 문화와 패턴 검증을 보고 싶다 → [[lit-and-filecheck]] / [[testing-guide]]
- 디버깅과 백엔드 추적까지 이어서 보고 싶다 → [[lldb-and-swift-debugging]] / [[llvm-backend]]
- 성능과 연결해서 보고 싶다 → [[compiler-performance]] / [[official-docs/compiler-performance-reference]]

## 8. Interop / Importer / C++

핵심 키워드:
- [[clang-importer|Clang Importer]]
- [[objc-interop]]
- [[c-to-swift-name-translation]]
- [[how-swift-imports-c-apis]]
- [[cpp-interop-overview]]
- [[cpp-using-from-swift]]
- [[cpp-calling-swift]]

추천 이동:
- C/ObjC/C++ 연결의 상위 구조를 먼저 보고 싶다 → [[clang-importer]]
- C/ObjC 선언이 Swift 이름으로 어떻게 들어오는지 보고 싶다 → [[c-to-swift-name-translation]] / [[how-swift-imports-c-apis]]
- C++를 Swift에서 쓰는 쪽이 궁금하다 → [[cpp-using-from-swift]]
- Swift를 C++에서 호출하는 쪽이 궁금하다 → [[cpp-calling-swift]]

## 9. 기여 / 테스트 / CI

핵심 키워드:
- [[getting-started]]
- [[development-tips]]
- [[compiler-faq]]
- [[testing-guide]]
- [[continuous-integration]]
- [[first-pull-request]]

추천 이동:
- 개발 환경을 처음 세팅한다 → [[getting-started]]
- 빠른 실무 팁이 먼저 필요하다 → [[development-tips]] / [[compiler-faq]]
- 테스트 작성/실행 체계를 익히고 싶다 → [[testing-guide]] / [[swift-testing-package]]
- PR를 실제로 열기 전 흐름을 보고 싶다 → [[first-pull-request]] / [[continuous-integration]]

## 10. 라이브러리 / 프레임워크 / 실사용 생태계

핵심 키워드:
- [[standard-library-runtime-and-compiler|stdlib/runtime/compiler]]
- [[swift-macro-tooling-stack|macro/tooling]]
- [[standard-library-to-compiler-crosswalk|standard library]]
- [[swift-foundation-package|Foundation]]
- [[swift-collections-package|Collections]]
- [[swift-nio-package|NIO]]
- [[swift-testing-package|Swift Testing]]
- [[core-libraries-to-compiler-crosswalk|Core Libraries]]

추천 이동:
- 언어 표면의 기본 타입이 어떻게 구현/진화되는지 보고 싶다 → [[standard-library-to-compiler-crosswalk]] / [[standard-library-runtime-and-compiler]]
- 크로스 플랫폼 라이브러리 경계를 보고 싶다 → [[core-libraries-to-compiler-crosswalk]]
- 매크로/IDE/formatter 도구축까지 함께 보고 싶다 → [[swift-macro-tooling-stack]]
- 테스트/툴링 생태계와 연결해서 보고 싶다 → [[swift-testing-package]] / [[sourcekit-lsp]]

## 11. 설계 비전 / proposal / 역사

핵심 키워드:
- [[swift-evolution-and-proposal-history|evolution/proposal history]]
- [[generics-manifesto|Generics Manifesto]]
- [[ownership-manifesto|Ownership Manifesto]]
- [[official-docs/abi-stability-manifesto|ABI Stability Manifesto]]
- [[library-evolution|library evolution]]
- [[official-docs/swift-generics-manifesto|swift-generics-manifesto]]

추천 이동:
- 설계 비전과 proposal history를 한 장으로 먼저 보고 싶다 → [[swift-evolution-and-proposal-history]]
- 제네릭 쪽 장기 비전부터 보고 싶다 → [[generics-manifesto]] / [[official-docs/swift-generics-manifesto]]
- ownership 방향을 보고 싶다 → [[ownership-manifesto]] / [[swift-ownership-memory-model]]
- ABI / resilience 방향을 보고 싶다 → [[official-docs/abi-stability-manifesto]] / [[library-evolution]]
- value semantics / COW proposal이 실제 ownership/runtime과 어떻게 이어졌는지 보고 싶다 → [[proposal-value-semantics-and-cow-to-ownership]]
- declaration type checker proposal이 현대 Sema와 어떻게 이어졌는지 보고 싶다 → [[proposal-declaration-type-checker-to-sema]]
- build model / WMO proposal이 driver와 어떻게 이어졌는지 보고 싶다 → [[proposal-compilation-model-and-wmo-to-driver]]
- ObjC interop proposal이 importer/dynamic dispatch와 어떻게 이어졌는지 보고 싶다 → [[proposal-objc-interop-to-importer-and-dispatch]]
- initialization/accessors proposal이 property model과 어떻게 이어졌는지 보고 싶다 → [[proposal-initialization-and-accessors-to-property-model]]
- remote mirrors proposal이 runtime/reflection과 어떻게 이어졌는지 보고 싶다 → [[proposal-remote-mirrors-to-runtime-reflection]]

## 자주 같이 움직이는 키워드 묶음

- literal → contextual type → constraint solving → diagnostics
  - [[literals]] → [[type-checker]] → [[diagnostics]]
- generic signature → archetype → substitution map → conformance
  - [[generic-signatures]] → [[archetypes]] → [[substitution-maps]] → [[conformances]]
- raw SIL → canonical SIL → ownership → optimization pass
  - [[sil-reference]] → [[sil-ownership]] → [[optimizer-design]] → [[sil-optimizer-pass-catalog]]
- value/reference → ownership/memory → OSSA → runtime
  - [[official-docs/value-reference-types-to-sil-ownership]] → [[swift-ownership-memory-model]] → [[official-docs/ownership-ssa]] → [[runtime]]
- async/await → task/actor → executor → safety checking
  - [[swift-concurrency-architecture]] → [[concurrency-data-race-safety]] → [[sil-optimizer-pass-catalog]] → [[runtime]]
- actor isolation → Sendable → FlowIsolation
  - [[swift-actor-isolation-and-sendable]] → [[concurrency-data-race-safety]] → [[sil-optimizer-pass-catalog]]
- Task → TaskGroup → executor → runtime
  - [[swift-task-executor-runtime]] → [[swift-concurrency-architecture]] → [[runtime]]
- manifesto → proposal history → implementation
  - [[generics-manifesto]] → [[swift-evolution-and-proposal-history]] → [[type-checker]]
- proposal → implementation (ownership/runtime)
  - [[proposal-value-semantics-and-cow-to-ownership]] → [[swift-ownership-memory-model]] → [[runtime]]
- proposal → implementation (Sema)
  - [[proposal-declaration-type-checker-to-sema]] → [[type-checker]] → [[request-evaluator]]
- proposal → implementation (driver/WMO)
  - [[proposal-compilation-model-and-wmo-to-driver]] → [[compiler-driver]] → [[dependency-analysis]]
- proposal → implementation (ObjC interop)
  - [[proposal-objc-interop-to-importer-and-dispatch]] → [[clang-importer]] → [[objc-interop]]
- proposal → implementation (property model)
  - [[proposal-initialization-and-accessors-to-property-model]] → [[sil-initializer-conventions]] → [[sil-memory-access]]
- proposal → implementation (reflection/runtime)
  - [[proposal-remote-mirrors-to-runtime-reflection]] → [[abi-type-metadata]] → [[runtime]]
- Sendable → actor isolation → FlowIsolation → ownership
  - [[concurrency-data-race-safety]] → [[sil-optimizer-pass-catalog]] → [[sil-ownership]]
- ABI stability → metadata → runtime → library evolution
  - [[abi-stability]] → [[abi-type-metadata]] → [[runtime]] → [[library-evolution]]
- driver → dependency analysis → llbuild → SwiftPM
  - [[compiler-driver]] → [[dependency-analysis]] → [[llbuild-package]] → [[swift-package-manager]]
- build-script/설정 → CMake/Ninja → lit/FileCheck → LLDB
  - [[getting-started]] → [[cmake-and-ninja-build]] → [[lit-and-filecheck]] → [[lldb-and-swift-debugging]]
- Clang Importer → C API 임포트 → 이름 변환 → C++ interop
  - [[clang-importer]] → [[how-swift-imports-c-apis]] → [[c-to-swift-name-translation]] → [[cpp-interop-overview]]
- 표면 문법 → macro/tooling → SwiftSyntax → SourceKit-LSP
  - [[swift-language-overview]] → [[swift-macro-tooling-stack]] → [[swift-syntax-package]] → [[sourcekit-lsp]]
- 표준 라이브러리 → runtime → ABI → compiler
  - [[standard-library-runtime-and-compiler]] → [[runtime]] → [[abi-stability]] → [[overview]]
- Swift 전체 지도 → 언어 개요 → Swift ↔ Compiler → 툴체인 스택 → 학습 스택
  - [[swift-ecosystem-map]] → [[swift-language-overview]] → [[swift-and-swift-compiler]] → [[swift-toolchain-stack]] → [[swift-compiler-learning-stack]]
