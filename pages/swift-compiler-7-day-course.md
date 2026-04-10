---
type: summary
category: learning
tags: [course, beginner, learning-path, source-guided]
aliases: [Swift 컴파일러 7일 코스, 7일 입문 코스]
sources: [official-docs/language-to-compiler-crosswalk.md, concurrency-data-race-safety.md]
---

# Swift 컴파일러 입문 7일 코스

Swift 컴파일러 위키를 처음부터 끝까지 한 번에 읽는 건 꽤 버겁다.
이 코스는 “문법을 아는 Swift 개발자”가 7일 동안 위키와 실제 소스 트리를 오가며
컴파일러 내부 구조에 익숙해지도록 만든 입문용 루트다.

## 이 코스의 전제

- 하루 60~90분 정도를 가정한다.
- 로컬에 클론한 Swift 저장소 루트를 `<swift-source-root>`라고 두고 읽는다.
- 아래 경로 표기는 모두 `<swift-source-root>` 기준이다.
- 사용 중 toolchain 정보는 먼저 `swiftc --version`으로 확인한다.
- 입문 탐색에 자주 쓰는 플래그:
  - `-dump-parse`
  - `-dump-ast`
  - `-typecheck`
  - `-emit-silgen`
  - `-emit-sil`
  - `-emit-irgen`
  - `-emit-ir`
  - `-swift-version 6`
  - `-strict-concurrency=complete`

## Day 1 — 큰 그림과 Parser

목표:
- Swift 소스가 어떤 단계를 거쳐 기계 코드로 가는지 큰 그림을 잡는다.
- Parser가 “문법 구조를 만드는 단계”라는 감각을 익힌다.

읽을 페이지:
- [[overview]]
- [[official-docs/swift-documentation-index]]
- [[official-docs/swift-compiler-architecture]]

실제 경로:
- `<swift-source-root>/docs`
- `<swift-source-root>/lib/Parse/Parser.cpp`
- `<swift-source-root>/lib/Parse/PersistentParserState.cpp`

해볼 명령:
- `swiftc -dump-parse sample.swift`

끝나면 이해해야 할 것:
- Parser는 아직 타입을 “판단”하지 않고 구조를 만든다.
- 이후 Sema/TypeChecker가 의미를 붙인다.

## Day 2 — Type Checker와 Diagnostics

목표:
- Swift 타입 체커가 제약 기반 시스템이라는 점을 이해한다.
- 진단 메시지가 어디서, 어떤 원칙으로 나오는지 본다.

읽을 페이지:
- [[type-checker]]
- [[diagnostics]]
- [[official-docs/type-checker-design-and-implementation]]
- [[official-docs/diagnostics-authoring]]

실제 경로:
- `<swift-source-root>/docs/TypeChecker.md`
- `<swift-source-root>/lib/Sema/TypeChecker.cpp`
- `<swift-source-root>/lib/Sema/CSGen.cpp`
- `<swift-source-root>/lib/Sema/CSSolver.cpp`
- `<swift-source-root>/lib/Sema/CSApply.cpp`
- `<swift-source-root>/lib/Sema/CSDiagnostics.cpp`

해볼 명령:
- `swiftc -dump-ast sample.swift`
- `swiftc -typecheck sample.swift`

끝나면 이해해야 할 것:
- Swift 타입 추론은 bottom-up + top-down이 섞인 constraint solving 문제다.
- 좋은 diagnostics는 타입 체커 구조와 분리해서 생각하기 어렵다.

## Day 3 — Generics

목표:
- Swift 제네릭이 단순 문법 설탕이 아니라 컴파일러 핵심 구조라는 점을 이해한다.
- generic signature / substitution / conformance를 큰 축으로 잡는다.

읽을 페이지:
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[conformances]]
- [[official-docs/compiling-swift-generics-pdf]]
- [[official-docs/swift-generics-manifesto]]

실제 경로:
- `<swift-source-root>/docs/Generics/README.md`
- `<swift-source-root>/docs/Generics`
- `<swift-source-root>/lib/AST/GenericSignature.cpp`
- `<swift-source-root>/lib/AST/GenericEnvironment.cpp`
- `<swift-source-root>/lib/AST/RequirementMachine/GenericSignatureQueries.cpp`
- `<swift-source-root>/lib/AST/GenericParamList.cpp`

끝나면 이해해야 할 것:
- generic signature는 “문법 정보”가 아니라 의미적으로 정규화된 제약 집합이다.
- substitution / conformance는 이후 SIL/IRGen까지 계속 따라간다.

## Day 4 — SIL과 SILGen

목표:
- AST 이후 왜 SIL이라는 별도 IR가 필요한지 이해한다.
- raw SIL과 canonical SIL의 차이를 감으로 잡는다.

읽을 페이지:
- [[sil-reference]]
- [[sil-types]]
- [[sil-instructions]]
- [[official-docs/swift-intermediate-language]]

실제 경로:
- `<swift-source-root>/docs/SIL/SIL.md`
- `<swift-source-root>/lib/SIL`
- `<swift-source-root>/lib/SILGen/SILGen.cpp`
- `<swift-source-root>/lib/SILGen/SILGenExpr.cpp`
- `<swift-source-root>/lib/SILGen/SILGenApply.cpp`
- `<swift-source-root>/lib/SILGen/SILGenConcurrency.cpp`

해볼 명령:
- `swiftc -emit-silgen sample.swift`
- `swiftc -emit-sil sample.swift`

끝나면 이해해야 할 것:
- SIL은 Swift 의미를 보존한 채 최적화/검증이 가능하도록 설계된 IR다.
- SILGen은 단순 lowering이 아니라 Swift 언어 규칙을 IR로 번역하는 단계다.

## Day 5 — Ownership와 Concurrency Safety

목표:
- 값 이동, borrow, actor isolation, `Sendable`이 왜 한 묶음인지 이해한다.
- Swift 6 concurrency migration이 컴파일러에서 실제로 무엇을 강제하는지 본다.

읽을 페이지:
- [[concurrency-data-race-safety]]
- [[sil-ownership]]
- [[ownership-manifesto]]
- [[official-docs/value-reference-types-to-sil-ownership]]
- [[official-docs/concurrency-data-race-safety-to-compiler-checks]]

실제 경로:
- `<swift-source-root>/docs/SIL/Ownership.md`
- `<swift-source-root>/lib/Sema/TypeCheckConcurrency.cpp`
- `<swift-source-root>/lib/AST/ActorIsolation.cpp`
- `<swift-source-root>/lib/SIL/IR/ActorIsolation.cpp`
- `<swift-source-root>/lib/SILGen/SILGenConcurrency.cpp`
- `<swift-source-root>/lib/SILOptimizer/Mandatory/SendNonSendable.cpp`
- `<swift-source-root>/lib/SILOptimizer/Mandatory/FlowIsolation.cpp`
- `<swift-source-root>/lib/SILOptimizer/Utils/RegionIsolation.cpp`

해볼 명령:
- `swiftc -swift-version 6 -typecheck sample.swift`
- `swiftc -strict-concurrency=complete -typecheck sample.swift`

끝나면 이해해야 할 것:
- Swift 6의 concurrency safety는 “문법 기능”보다 “정적 안전성 검사 체계”에 가깝다.
- ownership / isolation / sendability는 서로 떨어진 주제가 아니다.

## Day 6 — Optimizer / Performance / Driver

목표:
- 컴파일러가 왜 느려지는지, 어떤 단계가 병목이 되는지 구분하는 눈을 익힌다.
- 드라이버가 왜 파일 하나만 독립 컴파일하기 어려운지 이해한다.

읽을 페이지:
- [[optimizer-design]]
- [[compiler-performance]]
- [[compiler-driver]]
- [[dependency-analysis]]
- [[sil-optimizer-pass-catalog]]
- [[official-docs/compiler-performance-reference]]
- [[official-docs/driver-internals]]

실제 경로:
- `<swift-source-root>/docs/CompilerPerformance.md`
- `<swift-source-root>/docs/DriverInternals.md`
- `<swift-source-root>/lib/SILOptimizer/PassManager/PassManager.cpp`
- `<swift-source-root>/lib/SILOptimizer/Mandatory`
- `<swift-source-root>/lib/Sema/CSOptimizer.cpp`

끝나면 이해해야 할 것:
- 성능 문제는 Parser/Sema/SIL/LLVM 중 어디가 느린지 분리해서 봐야 한다.
- Swift driver는 모듈 전체 의미를 유지해야 해서 빌드 시스템과 강하게 얽힌다.

## Day 7 — ABI / IRGen / Runtime

목표:
- 언어 규칙이 결국 바이너리 레이아웃/메타데이터/호출 규약으로 굳는다는 감각을 잡는다.
- IRGen과 runtime이 어디서 만나는지 본다.

읽을 페이지:
- [[abi-stability]]
- [[abi-type-layout]]
- [[abi-type-metadata]]
- [[abi-calling-convention]]
- [[runtime]]
- [[library-evolution]]
- [[official-docs/abi-stability-manifesto]]

실제 경로:
- `<swift-source-root>/docs/ABIStabilityManifesto.md`
- `<swift-source-root>/lib/IRGen/IRGenModule.cpp`
- `<swift-source-root>/lib/IRGen/MetadataLayout.cpp`
- `<swift-source-root>/lib/IRGen/MetadataRequest.cpp`
- `<swift-source-root>/lib/Demangling/ManglingUtils.cpp`
- `<swift-source-root>/stdlib/public/runtime/HeapObject.cpp`
- `<swift-source-root>/stdlib/public/runtime/MetadataLookup.cpp`
- `<swift-source-root>/stdlib/public/runtime/DynamicCast.cpp`
- `<swift-source-root>/lib/Frontend/ModuleInterfaceLoader.cpp`

해볼 명령:
- `swiftc -emit-irgen sample.swift`
- `swiftc -emit-ir sample.swift`

끝나면 이해해야 할 것:
- ABI는 “나중에 배우는 디테일”이 아니라 언어 설계의 장기적 제약 조건이다.
- IRGen과 runtime을 보면 Swift가 어디까지 정적이고 어디서부터 동적인지 감이 잡힌다.

## 7일이 끝난 뒤 추천 분기

- 제네릭으로 더 깊게: [[compiling-swift-generics]] → [[generic-signatures]] → [[substitution-maps]]
- 동시성/ownership으로 더 깊게: [[concurrency-data-race-safety]] → [[sil-ownership]] → [[ownership-manifesto]]
- 최적화로 더 깊게: [[sil-reference]] → [[optimizer-design]] → [[high-level-sil-optimizations]]
- ABI/runtime으로 더 깊게: [[abi-stability]] → [[abi-type-layout]] → [[runtime]]
