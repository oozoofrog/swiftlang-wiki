---
type: summary
category: official-docs
tags: [official-docs, crosswalk, learning-path, compiler, language]
aliases: [언어-컴파일러 교차학습 지도, 문법에서 구현으로]
sources: [swift-docs-20260410-081300]
---

# 언어 → 컴파일러 교차학습 지도

이번에 다운로드한 공식 문서들은 서로 다른 층위에 있다.
어떤 문서는 언어 표면을 설명하고, 어떤 문서는 구현 세부를 설명하며,
어떤 문서는 빌드/툴링/ABI 같은 경계 영역을 설명한다.

이 페이지는 그 문서들을 “무엇을 배우다가 어디로 넘어가면 좋은가”라는 관점으로 다시 묶은 지도다.

## 한눈에 보는 연결 표

| 출발점 | 공식 문서 | 넘어갈 컴파일러 축 | 같이 읽을 위키 페이지 |
|---|---|---|---|
| 선언/문법/언어 규칙 | [[tspl-to-compiler-crosswalk]] | Parser, AST, TypeChecker | [[overview]], [[type-checker]], [[modules]], [[literals]] |
| 제네릭 문법 | [[compiling-swift-generics-pdf]], [[compiling-swift-generics-readme]], [[swift-generics-manifesto]] | generic signature, conformance, specialization | [[compiling-swift-generics]], [[generic-signatures]], [[substitution-maps]], [[conformances]] |
| 표현식 타입 추론 | [[type-checker-design-and-implementation]] | ConstraintSystem, diagnostics, solver performance | [[type-checker]], [[diagnostics]], [[compiler-performance]] |
| 값/참조 타입 의미론 | [[value-reference-types-to-sil-ownership]] | ownership, ARC, memory access, layout | [[sil-ownership]], [[sil-arc-optimization]], [[abi-type-layout]], [[runtime]] |
| 중간 표현과 최적화 | [[swift-intermediate-language]], [[ownership-ssa]], [[high-level-optimizations-in-sil]] | SILGen, OSSA, SILOptimizer | [[sil-reference]], [[sil-instructions]], [[optimizer-design]], [[sil-optimizer-pass-catalog]] |
| ABI와 라이브러리 진화 | [[abi-stability-manifesto]] | layout, metadata, mangling, calling convention, runtime | [[abi-stability]], [[library-evolution]], [[abi-type-metadata]], [[abi-mangling]], [[abi-calling-convention]] |
| 공개 API 설계 | [[api-design-guidelines-to-compiler-crosswalk]] | importer naming, diagnostics wording, API surface stability | [[c-to-swift-name-translation]], [[how-swift-imports-c-apis]], [[diagnostics]], [[library-evolution]] |
| 표준 라이브러리 | [[standard-library-to-compiler-crosswalk]] | stdlib/runtime/Builtin/SIL/ABI | [[stdlib-programmers-manual]], [[runtime]], [[library-evolution]], [[high-level-sil-optimizations]] |
| 코어 라이브러리와 생태계 | [[core-libraries-to-compiler-crosswalk]] | modules, overlays, ObjC interop, toolchain boundaries | [[swift-foundation-package]], [[swift-testing-package]], [[modules]], [[objc-interop]] |
| 빌드 시스템 / 패키지 | [[swiftpm-docs-to-build-pipeline]], [[driver-internals]], [[swift-compiler-architecture]] | driver, llbuild, dependency analysis | [[swift-package-manager]], [[compiler-driver]], [[dependency-analysis]], [[llbuild-package]] |
| 진단 UX / 컴파일러 도구 | [[diagnostics-authoring]], [[compiler-performance-reference]], [[swift-repl-and-debugger]] | diagnostics infra, verifier, profiling, debugger integration | [[diagnostics]], [[debugging-the-compiler]], [[compiler-performance]] |
| 동시성 안전성 | [[concurrency-data-race-safety-to-compiler-checks]] | isolation checking, Sendable, diagnostics, ownership | [[concurrency-data-race-safety]], [[type-checker]], [[diagnostics]], [[sil-optimizer-pass-catalog]], [[ownership-manifesto]] |

## 빠른 시작

- 전체 입문 루트를 순서대로 따라가고 싶다면 [[swift-compiler-7-day-course]]부터 시작하면 된다.

## 추천 학습 경로

### 1. 언어 입문에서 구현으로
1. [[tspl-to-compiler-crosswalk]]
2. [[swift-compiler-architecture]]
3. [[type-checker-design-and-implementation]]
4. [[swift-intermediate-language]]
5. [[abi-stability-manifesto]]

### 2. 제네릭 중심 경로
1. [[compiling-swift-generics-readme]]
2. [[compiling-swift-generics-pdf]]
3. [[swift-generics-manifesto]]
4. [[type-checker-design-and-implementation]]
5. [[generic-signatures]] → [[substitution-maps]] → [[conformances]]

### 3. 값 의미론과 메모리 모델 경로
1. [[value-reference-types-to-sil-ownership]]
2. [[ownership-ssa]]
3. [[high-level-optimizations-in-sil]]
4. [[abi-stability-manifesto]]
5. [[runtime]]

### 4. 라이브러리/ABI 경로
1. [[standard-library-to-compiler-crosswalk]]
2. [[core-libraries-to-compiler-crosswalk]]
3. [[api-design-guidelines-to-compiler-crosswalk]]
4. [[abi-stability-manifesto]]
5. [[library-evolution]]

### 5. 빌드/툴링 경로
1. [[swift-documentation-index]]
2. [[swift-compiler-architecture]]
3. [[driver-internals]]
4. [[swiftpm-docs-to-build-pipeline]]
5. [[compiler-performance-reference]] / [[swift-repl-and-debugger]]

## 어떻게 상호교차 지식을 습득할 수 있나

- 문법 문서를 읽다가 “왜 이런 규칙이 필요한가?”가 궁금해지면 `TypeChecker`, `Diagnostics`, `SIL` 계열로 이동한다.
- 표준 라이브러리 문서를 읽다가 “이 값 의미론/성능 특성은 어떻게 구현되나?”가 궁금해지면 `Ownership SSA`, `High-Level Optimizations in SIL`, `Runtime`, `ABI`로 이동한다.
- 패키지/빌드 문서를 읽다가 “Swift가 왜 파일 하나만 독립 컴파일하기 어려운가?”가 궁금해지면 `Driver Internals`, `Compiler Driver`, `Dependency Analysis`로 이동한다.
- concurrency / Sendable / actor 같은 표면 기능을 읽다가 “이 안전성은 누가 검사하나?”가 궁금해지면 먼저 [[concurrency-data-race-safety]]를 보고, 그 다음 `TypeChecker`, `Diagnostics`, 관련 SIL pass 문서로 이동한다.

## 메모

- `package-manager`와 `concurrency`는 이번 번들 안에서는 redirect-only 파일이었다. 따라서 새 위키 페이지에서는 “파일 자체의 내용”보다 canonical 주제와 현재 위키의 연결 구조를 정리했다.
- `TSPL`도 본문이 아니라 허브 페이지이므로, 이 역시 요약보다는 교차 읽기 인덱스로 다루는 편이 더 유용하다.
