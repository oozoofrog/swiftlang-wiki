---
page_count: 73
source_count: 72
last_updated: "2026-04-10"
---

# Wiki Index

## 개요 (Summary)

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [overview](pages/overview.md) | Swift 컴파일러 모노레포 전체 개요 및 파이프라인 | overview, architecture, pipeline |
| [compiling-swift-generics](pages/compiling-swift-generics.md) | "Compiling Swift Generics" 책 요약 — 4가지 핵심 시맨틱 객체 | generics, compilation, book |
| [downloads](pages/downloads/index.md) | Swift 공식/준공식 참고 문서 다운로드 허브 | downloads, references, offline |

## 엔티티 (Entity)

### 컴파일러 코어

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [type-checker](pages/type-checker.md) | 제약 기반 양방향 타입 추론 시스템 | type-checker, sema, constraints |
| [request-evaluator](pages/request-evaluator.md) | 요청 기반 평가 아키텍처 (lazy eval, 순환 탐지) | request-evaluator, caching |
| [diagnostics](pages/diagnostics.md) | 진단 메시지 시스템 (error, warning, fix-it) | diagnostics, errors |
| [serialization](pages/serialization.md) | 바이너리 직렬화 (swiftmodule, LLVM bitstream) | serialization, swiftmodule |
| [dependency-analysis](pages/dependency-analysis.md) | 증분 빌드 의존성 (provides/depends) | dependency, incremental-build |
| [compiler-driver](pages/compiler-driver.md) | Swift 컴파일 모델과 드라이버 동작 | driver, compilation-model |
| [compiler-performance](pages/compiler-performance.md) | 컴파일러 성능 측정 기법 | performance, profiling |
| [debugging-the-compiler](pages/debugging-the-compiler.md) | 컴파일러 디버깅 기법 (IR 덤프, LLDB, bisect) | debugging, lldb, sil-dump |
| [runtime](pages/runtime.md) | Swift 런타임 ABI (메모리 관리, 타입 시스템, 디맹글링) | runtime, abi |
| [ast-node-hierarchy](pages/ast-node-hierarchy.md) | AST 노드 계층 구조 (Decl/Expr/Stmt/Type) — 코드 분석 | ast, nodes, declarations |
| [swift-compiler-sources](pages/swift-compiler-sources.md) | SwiftCompilerSources — Swift-in-Swift 컴파일러 (165 파일) | swift-in-swift, optimizer |
| [modules](pages/modules.md) | Swift 모듈 시스템 (6가지 의미, import, 직렬화) | modules, import |

### SIL

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [sil-reference](pages/sil-reference.md) | SIL 중간 표현 명세 (3가지 표현, 스테이지, OSSA) | sil, ir |
| [sil-types](pages/sil-types.md) | SIL 타입 시스템 (object/address type) | sil, types |
| [sil-instructions](pages/sil-instructions.md) | SIL 인스트럭션 카테고리별 목록 | sil, instructions |
| [sil-function-attributes](pages/sil-function-attributes.md) | SIL 함수 속성 (inline, semantics) | sil, function |
| [sil-function-conventions](pages/sil-function-conventions.md) | SIL 파라미터/결과 전달 규약 | sil, conventions |
| [sil-initializer-conventions](pages/sil-initializer-conventions.md) | SIL 이니셜라이저 표현 규약 | sil, initializer |
| [sil-memory-access](pages/sil-memory-access.md) | SIL 메모리 접근 배타성 모델 | sil, memory |
| [sil-arc-optimization](pages/sil-arc-optimization.md) | ARC 최적화 패스 (retain/release 제거) | sil, arc |
| [sil-utilities](pages/sil-utilities.md) | SIL 분석 및 변환 유틸리티 인프라 | sil, utilities |
| [optimizer-design](pages/optimizer-design.md) | SIL 옵티마이저 파이프라인 설계 | optimizer, pipeline |
| [sil-optimizer-pass-catalog](pages/sil-optimizer-pass-catalog.md) | 205개 SIL 패스 전체 카탈로그 — 코드 분석 | sil, passes, catalog |

### ABI

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [abi-mangling](pages/abi-mangling.md) | 심볼 맹글링/디맹글링 체계 ($s 접두사, symbolic ref) | abi, mangling, demangling |
| [abi-type-metadata](pages/abi-type-metadata.md) | 타입 메타데이터 레코드 레이아웃 | abi, type-metadata |
| [abi-type-layout](pages/abi-type-layout.md) | 타입 메모리 레이아웃 알고리즘 (struct/class/enum) | abi, type-layout |
| [abi-calling-convention](pages/abi-calling-convention.md) | Swift 호출 규약 (소유권 전달, 에러 레지스터) | abi, calling-convention |
| [abi-generic-signature](pages/abi-generic-signature.md) | 제네릭 시그니처 ABI (최소화, 정규화) | abi, generics |

### Generics

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [generic-signatures](pages/generic-signatures.md) | 제네릭 파라미터 + 요구사항 시맨틱 객체 | generics, signatures |
| [substitution-maps](pages/substitution-maps.md) | 제네릭 파라미터 → 구체 타입 매핑 | generics, substitution |
| [conformances](pages/conformances.md) | 프로토콜 준수 표현 (normal, conditional, specialized) | generics, conformance |

### Interop (ObjC / C / C++)

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [objc-interop](pages/objc-interop.md) | Swift ↔ ObjC 상호운용 (bridging, @objc, selector) | objc, interop, bridging |
| [c-to-swift-name-translation](pages/c-to-swift-name-translation.md) | C/ObjC → Swift 이름 변환 (Clang Importer) | clang-importer, name-translation |
| [how-swift-imports-c-apis](pages/how-swift-imports-c-apis.md) | C/ObjC API 임포트 매핑 상세 | clang-importer, c-apis |
| [cpp-interop-overview](pages/cpp-interop-overview.md) | Swift-C++ 양방향 상호운용 개요 | cpp-interop, overview |
| [cpp-using-from-swift](pages/cpp-using-from-swift.md) | Swift에서 C++ 사용하기 | cpp-interop, importing-cpp |
| [cpp-calling-swift](pages/cpp-calling-swift.md) | C++에서 Swift 호출하기 | cpp-interop, exposing-swift |

### 패키지 및 도구

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [swift-syntax-package](pages/swift-syntax-package.md) | SwiftSyntax — 구문 트리/매크로 인프라 | swift-syntax, parser, macro |
| [swift-driver-package](pages/swift-driver-package.md) | 컴파일러 드라이버 Swift 재구현 | swift-driver, build-system |
| [swift-package-manager](pages/swift-package-manager.md) | Swift Package Manager | swiftpm, dependencies |
| [sourcekit-lsp](pages/sourcekit-lsp.md) | SourceKit-LSP — 지능형 편집 기능 | lsp, ide, code-completion |
| [swift-testing-package](pages/swift-testing-package.md) | Swift Testing — 매크로 기반 테스트 프레임워크 | swift-testing, macros |
| [swift-foundation-package](pages/swift-foundation-package.md) | Foundation 순수 Swift 재구현 | foundation, cross-platform |
| [swift-build-package](pages/swift-build-package.md) | Swift Build 시스템 (llbuild 기반) | swift-build, xcode |
| [swift-format-package](pages/swift-format-package.md) | swift-format 포매팅/린팅 도구 | swift-format, code-style |
| [llbuild-package](pages/llbuild-package.md) | llbuild 저수준 빌드 시스템 | llbuild, build-system |
| [swift-collections-package](pages/swift-collections-package.md) | Swift Collections 데이터 구조 | data-structures, deque |
| [swift-nio-package](pages/swift-nio-package.md) | SwiftNIO 비동기 네트워크 프레임워크 | networking, async-io |

### 기여 가이드

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [getting-started](pages/getting-started.md) | 개발 환경 설정 (Linux/macOS) | getting-started, build, setup |
| [first-pull-request](pages/first-pull-request.md) | 첫 PR 제출 가이드 | contributing, pull-request |
| [compiler-faq](pages/compiler-faq.md) | 컴파일러 개발 FAQ | faq, how-to |
| [testing-guide](pages/testing-guide.md) | 테스트 스위트 실행/개발 (lit, FileCheck) | testing, lit, filecheck |
| [continuous-integration](pages/continuous-integration.md) | CI 설정 및 @swift_ci 봇 | ci, automation |
| [development-tips](pages/development-tips.md) | 컴파일러 개발 팁 | tips, development |

## 개념 (Concept)

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [archetypes](pages/archetypes.md) | 제네릭 환경의 "가장 일반적인 구체 타입" | generics, archetype |
| [sil-ownership](pages/sil-ownership.md) | OSSA 소유권 모델 (owned/guaranteed/unowned/none) | sil, ownership, ossa |
| [abi-stability](pages/abi-stability.md) | ABI 안정성과 Library Evolution | abi, binary-compatibility |
| [ownership-manifesto](pages/ownership-manifesto.md) | 소유권 시스템 비전 (move, borrow, ~Copyable) | ownership, borrowing |
| [generics-manifesto](pages/generics-manifesto.md) | 제네릭 시스템 장기 비전 (variadic, opaque, packs) | generics, type-system |
| [error-handling](pages/error-handling.md) | 에러 처리 모델 (throws/try/catch) | error-handling, throws |
| [dynamic-casting](pages/dynamic-casting.md) | 동적 캐스팅 규칙 (is, as?, as!) | casting, runtime |
| [access-control](pages/access-control.md) | 접근 제어 수준 (open~private) | access-control, visibility |
| [literals](pages/literals.md) | 리터럴 타입 검사 및 추론 | literals, type-inference |
| [failable-initializers](pages/failable-initializers.md) | 실패 가능 이니셜라이저 (init?) | initializers, failable |
| [library-evolution](pages/library-evolution.md) | 바이너리 호환성 유지 규칙 (@frozen, @inlinable) | library-evolution, resilience |
| [high-level-sil-optimizations](pages/high-level-sil-optimizations.md) | @_semantics 기반 고수준 SIL 최적화 | sil, semantics, currency-types |
| [transparent-attr](pages/transparent-attr.md) | @_transparent 속성 시맨틱 | transparent, inlining |

## 용어 (Glossary)

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [glossary-compiler](pages/glossary-compiler.md) | Swift 컴파일러 핵심 용어 사전 (~60개) | glossary, terminology |

## 엔티티 (stdlib)

| 페이지 | 설명 | 태그 |
|--------|------|------|
| [stdlib-programmers-manual](pages/stdlib-programmers-manual.md) | stdlib 기여자 가이드 (규약, 성능, 테스트) | stdlib, guide |

## 분석 (Analysis)

| 페이지 | 설명 | 태그 |
|--------|------|------|
