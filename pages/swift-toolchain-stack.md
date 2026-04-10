---
type: summary
category: tooling
tags: [swift, compiler, toolchain, llvm, clang, lldb, cmake, ninja, lit, filecheck]
aliases: [Swift 툴체인 스택, Swift Compiler 기술 스택, Swift Toolchain Stack]
sources: [swift.org/documentation/swift-compiler/index.html, getting-started.md, testing.md, swiftlang-swift/docs/DriverInternals.md]
---

# Swift 툴체인 스택

Swift Compiler를 이해하거나 기여하려면 Swift 언어 자체만이 아니라,
그 언어를 둘러싼 툴체인과 인프라를 함께 알아야 한다.
이 페이지는 그 기술 스택을 위에서 아래로 정리한 지도다.

## 한눈에 보는 스택

| 층 | 구성 요소 | 관련 페이지 |
|---|---|---|
| 언어/문서 층 | TSPL, 공식 문서 허브, manifesto류 | [[official-docs/index]], [[swift-language-overview]] |
| 프론트엔드 층 | Parser, AST, Sema, diagnostics, request evaluator | [[overview]], [[type-checker]], [[diagnostics]], [[request-evaluator]] |
| IR 층 | SILGen, SIL, mandatory passes, optimizer, IRGen, LLVM IR | [[sil-reference]], [[optimizer-design]], [[compiler-performance]] |
| 백엔드/interop 층 | LLVM, Clang Importer, C/ObjC/C++ interop | [[objc-interop]], [[cpp-interop-overview]], [[how-swift-imports-c-apis]] |
| 드라이버/빌드 층 | swift-driver, SwiftPM, llbuild, Swift Build, dependency analysis | [[compiler-driver]], [[swift-driver-package]], [[swift-package-manager]], [[llbuild-package]], [[swift-build-package]] |
| 편집/툴링 층 | SwiftSyntax, SourceKit-LSP, swift-format | [[swift-syntax-package]], [[sourcekit-lsp]], [[swift-format-package]] |
| 디버그/테스트/인프라 층 | LLDB, CMake, Ninja, lit, FileCheck, CI | [[debugging-the-compiler]], [[getting-started]], [[testing-guide]], [[continuous-integration]] |

## 왜 이 스택이 중요한가

Swift Compiler는 단일 바이너리만 가리키지 않는다.
실제로는 여러 저장소, 여러 빌드 도구, 여러 테스트 시스템, 여러 편집/분석 도구가 함께 움직이는 생태계다.

즉 “Swift Compiler를 배운다”는 말은 보통 다음을 함께 배운다는 뜻이다.

- 언어 의미가 어디서 판정되는가
- 어떤 중간표현을 거쳐 최적화되는가
- 어떤 빌드 도구가 전체 파이프라인을 조율하는가
- 어떤 디버깅/테스트 인프라로 검증하는가
- 어떤 패키지와 도구가 개발자 경험을 만든다

## 핵심 구성 요소별 역할

### 1. LLVM / Clang
- LLVM은 Swift가 최종적으로 내려가는 백엔드 최적화/코드 생성 기반이다.
- Clang은 C/ObjC 세계와의 상호운용에서 중요한 축이며, Swift는 Clang Importer를 통해 선언을 가져온다.
- C++ interop도 이 축의 확장선에 있다.

연결 페이지:
- [[overview]]
- [[llvm-backend]]
- [[clang-importer]]
- [[objc-interop]]
- [[cpp-interop-overview]]
- [[compiler-performance]]

### 2. swift-driver / SwiftPM / llbuild
- `swift-driver`는 컴파일 파이프라인을 구성하고 작업을 스케줄한다.
- SwiftPM은 패키지 그래프와 빌드 설정의 중심이고, 실제 컴파일 호출과도 이어진다.
- llbuild는 저수준 작업 그래프 실행 엔진이다.

연결 페이지:
- [[compiler-driver]]
- [[swift-driver-package]]
- [[swift-package-manager]]
- [[llbuild-package]]
- [[dependency-analysis]]

### 3. SwiftSyntax / SourceKit-LSP / swift-format
- SwiftSyntax는 파싱된 구조를 도구 친화적으로 다루게 해 준다.
- SourceKit-LSP는 IDE와 에디터 경험의 핵심 축이다.
- swift-format은 문법 구조와 규칙 기반 포매팅의 예시다.

연결 페이지:
- [[swift-macro-tooling-stack]]
- [[swift-syntax-package]]
- [[sourcekit-lsp]]
- [[swift-format-package]]

### 4. CMake / Ninja / lit / FileCheck / LLDB
- CMake는 대규모 빌드 구성을 정의한다.
- Ninja는 빠른 증분 빌드 실행기다.
- lit와 FileCheck는 Swift 컴파일러 테스트 문화의 핵심이다.
- LLDB는 컴파일러 자신이나 결과 프로그램을 디버깅할 때 중요하다.

관련 기존 페이지:
- [[swift-compiler-build-test-debug-stack]]
- [[cmake-and-ninja-build]]
- [[lit-and-filecheck]]
- [[lldb-and-swift-debugging]]
- [[getting-started]]
- [[development-tips]]
- [[testing-guide]]
- [[debugging-the-compiler]]
- [[compiler-faq]]

## 배울 때 어떤 순서가 좋은가

1. `swift` 저장소의 프론트엔드/SIL/IRGen 큰 흐름 이해
2. `swift-driver`, SwiftPM, llbuild의 빌드 흐름 이해
3. lit/FileCheck/LLDB/CMake/Ninja 기반의 실무 루프 익히기
4. SwiftSyntax / SourceKit-LSP / formatter 같은 도구 계층까지 확장하기

## 최소 필수 스택 vs 확장 스택

### 최소 필수
- [[overview]]
- [[type-checker]]
- [[sil-reference]]
- [[compiler-driver]]
- [[getting-started]]
- [[testing-guide]]

### 강하게 추천
- [[swift-driver-package]]
- [[swift-package-manager]]
- [[llbuild-package]]
- [[debugging-the-compiler]]
- [[compiler-performance]]

### 확장 심화
- [[swift-syntax-package]]
- [[sourcekit-lsp]]
- [[cpp-interop-overview]]
- [[swift-foundation-package]]
- [[swift-testing-package]]

## 같이 보면 좋은 페이지

- [[swift-ecosystem-map]]
- [[swift-and-swift-compiler]]
- [[swift-compiler-learning-stack]]
- [[keyword-network]]
