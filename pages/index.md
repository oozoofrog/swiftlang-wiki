---
title: Swift Compiler Wiki
type: summary
category: learning
tags: [swift, compiler, wiki, navigation, hub]
aliases: [Swift Compiler Wiki, Swift 컴파일러 위키, 홈]
sources: [overview.md, keyword-network.md, swift-ecosystem-map.md]
---

# Swift Compiler Wiki

Swift 언어, compiler 구현, 공식 문서, proposal history를
하나의 지식 그래프로 연결한 위키.

| 항목 | 값 |
|------|-----|
| 페이지 | 139 |
| 교차참조 | 2975 |
| 소스 | swift/docs/, 서브프로젝트 README, 코드 분석 |

## 어디서 시작할까

- **처음 시작한다** → [Swift 컴파일러 입문 7일 코스](swift-compiler-7-day-course.md) → [Swift 전체 지도](swift-ecosystem-map.md) → [Swift 언어 개요](swift-language-overview.md)
- **구현으로 바로 들어간다** → [파워유저 시작점](power-user-start.md) → [타입 체커](type-checker.md) / [SIL 레퍼런스](sil-reference.md) / [런타임](runtime.md)
- **자료/원문부터 본다** → [공식 참고 문서 다운로드](downloads/index.md) → [공식 문서 해설 허브](official-docs/index.md) → [언어 → 컴파일러 교차학습 지도](official-docs/language-to-compiler-crosswalk.md)
- **개념을 따라 탐색한다** → [위키 키워드 연결망](keyword-network.md) → [용어 사전](glossary-compiler.md)

!!! tip "반복 방문자 / 구현 위주 독자"
    긴 목록 대신 압축 인덱스로 바로 들어가고 싶다면 [파워유저 시작점](power-user-start.md)을 보세요.

## 대표 허브

- **[Swift 전체 지도](swift-ecosystem-map.md)** — Swift 언어, 컴파일러, 툴체인, 생태계를 한 장으로 보는 최상위 허브
- **[Swift 언어 개요](swift-language-overview.md)** — 언어 의미, 라이브러리, 런타임, 생태계를 함께 보는 입구
- **[Swift와 Swift Compiler의 관계](swift-and-swift-compiler.md)** — 언어 기능과 컴파일러 구현이 어떻게 맞물리는지 설명하는 브리지
- **[Swift 타입 시스템](swift-type-system.md)** — generics, existential, opaque, conformance, metadata까지 묶는 상위 허브
- **[Swift 소유권·메모리 모델](swift-ownership-memory-model.md)** — ownership, borrowing, ARC, lifetime, concurrency isolation을 함께 보는 허브
- **[Swift Concurrency 전체 구조](swift-concurrency-architecture.md)** — async/await, task, actor, executor, runtime, migration을 한 장으로 묶는 허브
- **[Swift Evolution / proposal history](swift-evolution-and-proposal-history.md)** — proposal, manifesto, archive, rejected 문서를 통해 설계 역사를 읽는 허브
- **[표준 라이브러리·런타임·컴파일러](standard-library-runtime-and-compiler.md)** — stdlib, runtime, compiler가 어떻게 한 몸처럼 움직이는지 정리한 허브
- **[Swift 툴체인 스택](swift-toolchain-stack.md)** — LLVM/Clang/driver/SwiftPM/CMake/Ninja/lit/LLDB까지 포함한 기술 스택 지도
- **[Swift Compiler 학습 스택](swift-compiler-learning-stack.md)** — 무엇을 어떤 순서로 공부해야 하는지 정리한 로드맵
- **[공식 문서 해설 허브](official-docs/index.md)** — 다운로드 문서별 위키 정리 페이지
- **[위키 키워드 연결망](keyword-network.md)** — 용어/개념/패키지 페이지를 키워드 허브로 묶은 지도

## 추천 읽기 경로

- **입문 루트**: [Swift 컴파일러 입문 7일 코스](swift-compiler-7-day-course.md) → [Swift 전체 지도](swift-ecosystem-map.md) → [Swift 언어 개요](swift-language-overview.md)
- **타입 시스템 루트**: [Swift 타입 시스템](swift-type-system.md) → [타입 체커](type-checker.md) → [Compiling Swift Generics](compiling-swift-generics.md) → [런타임](runtime.md)
- **소유권/메모리 루트**: [Swift 소유권·메모리 모델](swift-ownership-memory-model.md) → [Ownership SSA 해설](official-docs/ownership-ssa.md) → [런타임](runtime.md)
- **동시성 루트**: [Swift Concurrency 전체 구조](swift-concurrency-architecture.md) → [Swift actor isolation·Sendable](swift-actor-isolation-and-sendable.md) → [Swift Task·Executor·Runtime](swift-task-executor-runtime.md) → [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md)
- **proposal/history 루트**: [Swift Evolution / proposal history](swift-evolution-and-proposal-history.md) → [Value Semantics / COW proposals](proposal-value-semantics-and-cow-to-ownership.md) → [Declaration Type Checker proposal](proposal-declaration-type-checker-to-sema.md)
- **툴체인/기여 루트**: [Swift 툴체인 스택](swift-toolchain-stack.md) → [빌드·테스트·디버그 스택](swift-compiler-build-test-debug-stack.md) → [lit와 FileCheck](lit-and-filecheck.md) → [LLDB와 Swift 디버깅](lldb-and-swift-debugging.md)
- **공식 문서 기반 루트**: [공식 참고 문서 다운로드](downloads/index.md) → [공식 문서 해설 허브](official-docs/index.md) → [언어 → 컴파일러 교차학습 지도](official-docs/language-to-compiler-crosswalk.md)

## 주제별 탐색

| 카테고리 | 페이지 | 주요 내용 |
|----------|--------|-----------|
| [Swift 전체 지도](swift-ecosystem-map.md) | 13 | Swift 언어, 타입 시스템, ownership/memory, concurrency, actor/sendable, task/executor/runtime, evolution/proposal history, stdlib/runtime, 툴체인, 도구, 상호관계, 학습 로드맵 |
| [컴파일러 코어](type-checker.md) | 12 | Parser, Sema, IRGen, Request Evaluator, AST |
| [SIL](sil-reference.md) | 14 | IR 명세, 인스트럭션, 소유권, 옵티마이저, 패스 카탈로그 |
| [ABI](abi-mangling.md) | 7 | 맹글링, 타입 메타데이터/레이아웃, 호출 규약, Library Evolution |
| [Generics](generic-signatures.md) | 5 | 시그니처, 치환 맵, 아키타입, Conformance |
| [Interop](objc-interop.md) | 6 | ObjC, C API 임포트, C++ 양방향 |
| [언어 설계](ownership-manifesto.md) | 8 | 소유권, 동시성 안전성, 에러 처리, 캐스팅, 접근 제어 |
| [제안 → 구현 교차 읽기](swift-evolution-and-proposal-history.md) | 16 | evolution 허브, value semantics/COW, in-place operations, optimizer effects/attrs, declaration type checker, compilation model/WMO, enums/enum style, typestate, option sets, C export, C pointer interop, ObjC interop, initialization/accessors, initializer inheritance, constructors/class construction, remote mirrors |
| [기여 가이드](getting-started.md) | 7 | 시작하기, 테스트, CI, FAQ |
| [패키지](swift-syntax-package.md) | 11 | SwiftPM, SourceKit-LSP, SwiftNIO 등 |
| [툴체인/인프라](swift-toolchain-stack.md) | 7 | LLVM, Clang Importer, 빌드·테스트·디버그 스택, CMake/Ninja, lit/FileCheck, LLDB |

## 위키 사용 / 편집

- **[파워유저 시작점](power-user-start.md)** — 반복 방문자와 구현 중심 독자를 위한 압축 인덱스
- **[위키 원칙과 철학](wiki-knowledge-base-principles.md)** — 이 위키를 지식베이스로 유지하기 위한 작성 규칙과 발전 철학
- **[위키 편집 체크리스트](wiki-editor-checklist.md)** — 새 페이지 작성/수정/연결/검증 시 확인할 공개 체크리스트
- **[위키 생성 템플릿](wiki-page-templates.md)** — subject/hub/crosswalk/meta 페이지를 위한 공개 템플릿 모음
- **[위키 taxonomy / frontmatter 규칙](wiki-frontmatter-taxonomy.md)** — type/category/tags/aliases/sources를 어떤 기준으로 고르는지 정한 메타 문서
- **[위키 지식 연대기](wiki-knowledge-chronicle.md)** — 위키가 어떤 순서로 확장됐는지 기록한 메타 연대기
