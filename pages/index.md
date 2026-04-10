---
title: Swift Compiler Wiki
---

# Swift Compiler Wiki

Swift 컴파일러 내부 구조에 대한 LLM 생성 지식 베이스.

| 항목 | 값 |
|------|-----|
| 페이지 | 121 |
| 교차참조 | 2205 |
| 소스 | swift/docs/, 서브프로젝트 README, 코드 분석 |

## 빠른 탐색

- **[프로젝트 개요](overview.md)** — 컴파일러 파이프라인, 모노레포 구성
- **[SIL 레퍼런스](sil-reference.md)** — Swift Intermediate Language 명세
- **[205개 패스 카탈로그](sil-optimizer-pass-catalog.md)** — SIL 옵티마이저 전체 패스 목록
- **[심볼 맹글링](abi-mangling.md)** — ABI 맹글링/디맹글링 체계
- **[타입 체커](type-checker.md)** — 제약 기반 양방향 타입 추론
- **[Generics 책](compiling-swift-generics.md)** — "Compiling Swift Generics" 요약
- **[Swift 전체 지도](swift-ecosystem-map.md)** — Swift 언어, 컴파일러, 툴체인, 생태계를 한 장으로 보는 최상위 허브
- **[Swift 언어 개요](swift-language-overview.md)** — 언어 의미, 라이브러리, 런타임, 생태계를 함께 보는 입구
- **[Swift와 Swift Compiler의 관계](swift-and-swift-compiler.md)** — 언어 기능과 컴파일러 구현이 어떻게 맞물리는지 설명하는 브리지
- **[Swift 타입 시스템](swift-type-system.md)** — generics, existential, opaque, conformance, metadata까지 묶는 상위 허브
- **[Swift 소유권·메모리 모델](swift-ownership-memory-model.md)** — ownership, borrowing, ARC, lifetime, concurrency isolation을 함께 보는 허브
- **[Swift Concurrency 전체 구조](swift-concurrency-architecture.md)** — async/await, task, actor, executor, runtime, migration을 한 장으로 묶는 허브
- **[Swift actor isolation·Sendable](swift-actor-isolation-and-sendable.md)** — actor boundary, global actor, MainActor, Sendable을 집중해서 보는 허브
- **[Swift Task·Executor·Runtime](swift-task-executor-runtime.md)** — task, task group, executor, actor runtime의 실행 모델 허브
- **[Swift Evolution / proposal history](swift-evolution-and-proposal-history.md)** — proposal, manifesto, archive, rejected 문서를 통해 설계 역사를 읽는 허브
- **[Value Semantics / COW proposals → ownership/runtime](proposal-value-semantics-and-cow-to-ownership.md)** — 값 의미론·COW proposal을 현재 ownership/runtime 문맥으로 읽는 교차 페이지
- **[Declaration Type Checker proposal → 현대 Sema](proposal-declaration-type-checker-to-sema.md)** — 선언 타입 체커 proposal을 TypeChecker/Request Evaluator 맥락으로 읽는 교차 페이지
- **[Compilation Model / WMO proposals → driver](proposal-compilation-model-and-wmo-to-driver.md)** — 초기 build model/WMO proposal을 driver·dependency analysis 맥락으로 읽는 교차 페이지
- **[표준 라이브러리·런타임·컴파일러](standard-library-runtime-and-compiler.md)** — stdlib, runtime, compiler가 어떻게 한 몸처럼 움직이는지 정리한 허브
- **[Swift 툴체인 스택](swift-toolchain-stack.md)** — LLVM/Clang/driver/SwiftPM/CMake/Ninja/lit/LLDB까지 포함한 기술 스택 지도
- **[Swift 매크로·도구 스택](swift-macro-tooling-stack.md)** — SwiftSyntax, SourceKit-LSP, formatter, macro 생태계를 묶는 허브
- **[Swift Compiler 학습 스택](swift-compiler-learning-stack.md)** — 무엇을 어떤 순서로 공부해야 하는지 정리한 로드맵
- **[빌드·테스트·디버그 스택](swift-compiler-build-test-debug-stack.md)** — 실제 기여 루프를 build/test/debug 관점으로 묶은 허브
- **[LLVM 백엔드와 Swift](llvm-backend.md)** — IRGen 이후 LLVM 단계가 Swift와 어떻게 연결되는지 정리
- **[Clang Importer](clang-importer.md)** — C/ObjC/C++ 상호운용의 중심 구성 요소 정리
- **[lit와 FileCheck](lit-and-filecheck.md)** — Swift 컴파일러 테스트 문화의 핵심 도구 설명
- **[공식 참고 문서 다운로드](downloads/index.md)** — ZIP/개별 문서 다운로드 허브
- **[공식 문서 해설 허브](official-docs/index.md)** — 다운로드 문서별 위키 정리 페이지
- **[언어 → 컴파일러 교차학습 지도](official-docs/language-to-compiler-crosswalk.md)** — 문법/라이브러리/빌드 지식이 내부 구현과 만나는 지도
- **[위키 키워드 연결망](keyword-network.md)** — 용어/개념/패키지 페이지를 키워드 허브로 묶은 지도
- **[Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md)** — actor isolation / Sendable / strict concurrency를 컴파일러 관점에서 정리
- **[Swift 컴파일러 입문 7일 코스](swift-compiler-7-day-course.md)** — 공식 문서와 실제 소스 경로를 함께 따라가는 입문 루트
- **[용어 사전](glossary-compiler.md)** — 컴파일러 핵심 용어 ~60개

!!! tip "오프라인으로 읽기"
    로컬에 받아서 읽을 자료가 필요하면 [다운로드 허브](downloads/index.md)에서 전체 ZIP 번들이나 개별 참고 문서를 바로 받을 수 있습니다.

## 새로 추가된 읽기 경로

- **언어 입문 → 구현**: [TSPL → 컴파일러 교차 읽기](official-docs/tspl-to-compiler-crosswalk.md) → [타입 체커](type-checker.md) → [SIL 레퍼런스](sil-reference.md)
- **제네릭 중심**: [Compiling Swift Generics PDF 해설](official-docs/compiling-swift-generics-pdf.md) → [Generics Manifesto 해설](official-docs/swift-generics-manifesto.md)
- **값/참조 의미론 중심**: [Value/Reference Types → SIL 소유권 교차 읽기](official-docs/value-reference-types-to-sil-ownership.md) → [SIL 소유권](sil-ownership.md)
- **빌드/도구 중심**: [Swift Compiler 공개 개요 해설](official-docs/swift-compiler-architecture.md) → [Driver Internals 문서 해설](official-docs/driver-internals.md) → [SwiftPM 문서 → 빌드 파이프라인 교차 읽기](official-docs/swiftpm-docs-to-build-pipeline.md)
- **타입 시스템 중심**: [Swift 타입 시스템](swift-type-system.md) → [타입 체커](type-checker.md) → [Compiling Swift Generics](compiling-swift-generics.md) → [런타임](runtime.md)
- **소유권/메모리 모델 중심**: [Swift 소유권·메모리 모델](swift-ownership-memory-model.md) → [Value/Reference Types → SIL 소유권](official-docs/value-reference-types-to-sil-ownership.md) → [Ownership SSA 해설](official-docs/ownership-ssa.md) → [런타임](runtime.md) → [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md)
- **동시성 전체 구조 중심**: [Swift Concurrency 전체 구조](swift-concurrency-architecture.md) → [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md) → [타입 체커](type-checker.md) → [SIL 옵티마이저 패스 카탈로그](sil-optimizer-pass-catalog.md) → [런타임](runtime.md)
- **actor/sendable 중심**: [Swift actor isolation·Sendable](swift-actor-isolation-and-sendable.md) → [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md) → [타입 체커](type-checker.md) → [진단 시스템](diagnostics.md)
- **task/executor/runtime 중심**: [Swift Task·Executor·Runtime](swift-task-executor-runtime.md) → [Swift Concurrency 전체 구조](swift-concurrency-architecture.md) → [런타임](runtime.md) → [표준 라이브러리·런타임·컴파일러](standard-library-runtime-and-compiler.md)
- **설계 역사 중심**: [Swift Evolution / proposal history](swift-evolution-and-proposal-history.md) → [Generics Manifesto](generics-manifesto.md) → [Ownership Manifesto](ownership-manifesto.md) → [ABI Stability Manifesto 해설](official-docs/abi-stability-manifesto.md)
- **proposal → 구현 교차 읽기**: [Value Semantics / COW proposals](proposal-value-semantics-and-cow-to-ownership.md) → [Declaration Type Checker proposal](proposal-declaration-type-checker-to-sema.md) → [Compilation Model / WMO proposals](proposal-compilation-model-and-wmo-to-driver.md)
- **stdlib/runtime 중심**: [표준 라이브러리·런타임·컴파일러](standard-library-runtime-and-compiler.md) → [Standard Library 교차 읽기](official-docs/standard-library-to-compiler-crosswalk.md) → [ABI 안정성](abi-stability.md) → [런타임](runtime.md)
- **동시성 안전성 중심**: [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md) → [타입 체커](type-checker.md) → [SIL 옵티마이저 패스 카탈로그](sil-optimizer-pass-catalog.md)
- **Swift 전체 조감 루트**: [Swift 전체 지도](swift-ecosystem-map.md) → [Swift 언어 개요](swift-language-overview.md) → [Swift와 Swift Compiler의 관계](swift-and-swift-compiler.md) → [Swift 타입 시스템](swift-type-system.md) → [Swift 소유권·메모리 모델](swift-ownership-memory-model.md) → [Swift Concurrency 전체 구조](swift-concurrency-architecture.md) → [Swift actor isolation·Sendable](swift-actor-isolation-and-sendable.md) → [Swift Task·Executor·Runtime](swift-task-executor-runtime.md) → [Swift Evolution / proposal history](swift-evolution-and-proposal-history.md) → [표준 라이브러리·런타임·컴파일러](standard-library-runtime-and-compiler.md) → [Swift 툴체인 스택](swift-toolchain-stack.md)
- **학습 로드맵 루트**: [Swift Compiler 학습 스택](swift-compiler-learning-stack.md) → [Swift 컴파일러 입문 7일 코스](swift-compiler-7-day-course.md) → [키워드 연결망](keyword-network.md)
- **툴체인/실무 루트**: [Swift 툴체인 스택](swift-toolchain-stack.md) → [빌드·테스트·디버그 스택](swift-compiler-build-test-debug-stack.md) → [CMake와 Ninja](cmake-and-ninja-build.md) → [lit와 FileCheck](lit-and-filecheck.md) → [LLDB와 Swift 디버깅](lldb-and-swift-debugging.md)
- **매크로/도구 루트**: [Swift 매크로·도구 스택](swift-macro-tooling-stack.md) → [swift-syntax](swift-syntax-package.md) → [SourceKit-LSP](sourcekit-lsp.md) → [swift-format](swift-format-package.md)
- **입문자용 전체 루트**: [Swift 컴파일러 입문 7일 코스](swift-compiler-7-day-course.md)
- **키워드 탐색 루트**: [위키 키워드 연결망](keyword-network.md) → [용어 사전](glossary-compiler.md) → 세부 페이지

## 카테고리

| 카테고리 | 페이지 | 주요 내용 |
|----------|--------|-----------|
| [Swift 전체 지도](swift-ecosystem-map.md) | 13 | Swift 언어, 타입 시스템, ownership/memory, concurrency, actor/sendable, task/executor/runtime, evolution/proposal history, stdlib/runtime, 툴체인, 도구, 상호관계, 학습 로드맵 |
| [컴파일러 코어](type-checker.md) | 12 | Parser, Sema, IRGen, Request Evaluator, AST |
| [SIL](sil-reference.md) | 14 | IR 명세, 인스트럭션, 소유권, 옵티마이저, 패스 카탈로그 |
| [ABI](abi-mangling.md) | 7 | 맹글링, 타입 메타데이터/레이아웃, 호출 규약, Library Evolution |
| [Generics](generic-signatures.md) | 5 | 시그니처, 치환 맵, 아키타입, Conformance |
| [Interop](objc-interop.md) | 6 | ObjC, C API 임포트, C++ 양방향 |
| [언어 설계](ownership-manifesto.md) | 8 | 소유권, 동시성 안전성, 에러 처리, 캐스팅, 접근 제어 |
| [제안 → 구현 교차 읽기](swift-evolution-and-proposal-history.md) | 4 | evolution 허브, value semantics/COW, declaration type checker, compilation model/WMO |
| [기여 가이드](getting-started.md) | 7 | 시작하기, 테스트, CI, FAQ |
| [패키지](swift-syntax-package.md) | 11 | SwiftPM, SourceKit-LSP, SwiftNIO 등 |
| [툴체인/인프라](swift-toolchain-stack.md) | 7 | LLVM, Clang Importer, 빌드·테스트·디버그 스택, CMake/Ninja, lit/FileCheck, LLDB |
