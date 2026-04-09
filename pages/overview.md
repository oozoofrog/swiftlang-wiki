---
type: summary
category: compiler
tags: [overview, architecture, pipeline]
aliases: [프로젝트 개요, swiftlang]
sources: [swift-readme.md, docs-index.md]
---

# Swift 컴파일러 모노레포 개요

Swift는 고성능 시스템 프로그래밍 언어로, 현대적 구문과 메모리 안전성을 제공한다. 이 모노레포(swiftlang)는 Swift 컴파일러와 관련 도구 전체를 포함한다.

## 컴파일러 파이프라인

```
Swift Source → Parser → Sema(TypeChecker) → SILGen → Mandatory Passes
→ Canonical SIL → Optimization Passes → IRGen → LLVM IR → Machine Code
```

1. **Parser**: Swift 소스에서 AST(Abstract Syntax Tree) 구성
2. **Sema/TypeChecker**: AST 타입 검사 및 주석 — 제약 기반 양방향 타입 추론 사용 ([[type-checker]])
3. **SILGen**: AST에서 raw [[sil-reference|SIL]] 생성
4. **Mandatory Passes**: 필수 최적화 및 진단 → canonical SIL 생성
5. **Optimization Passes**: 성능 최적화 (ARC, devirtualization, 제네릭 특수화 등) ([[optimizer-design]])
6. **IRGen**: SIL → LLVM IR 하위 변환
7. **LLVM Backend**: LLVM 최적화 및 기계 코드 생성

## 모노레포 구성

### 컴파일러 코어 (`swift/`)
- `lib/AST/` — AST 정의 및 조작
- `lib/Parse/` — 파서
- `lib/Sema/` — 의미 분석 (타입 검사)
- `lib/SILGen/` — SIL 생성
- `lib/SIL/` — SIL IR 자료 구조
- `lib/SILOptimizer/` — SIL 최적화 패스
- `lib/IRGen/` — LLVM IR 생성
- `lib/SwiftDemangle/` — 심볼 디맹글링

### LLVM/Clang (`llvm-project/`)
LLVM IR 최적화 및 코드 생성 백엔드. Clang Importer가 C/Objective-C 선언을 Swift에 노출한다.

### 표준 라이브러리 (`swift/stdlib/`, `swift-foundation/`)
Swift 표준 라이브러리(swiftCore)와 Foundation 구현.

### 패키지 및 도구
- `swift-syntax/` — Swift 구문 분석 라이브러리 (매크로 기반)
- `swift-driver/` — 컴파일러 드라이버
- `swiftpm/` / `swift-build/` — Swift Package Manager
- `sourcekit-lsp/` — SourceKit LSP 서버
- `swift-format/` — 코드 포매터
- `swift-testing/` — Swift Testing 프레임워크

## 주요 문서

### 컴파일러 코어
- [[glossary-compiler]] — 컴파일러 용어 사전
- [[sil-reference]] — SIL 중간 표현 명세
- [[optimizer-design]] — 옵티마이저 파이프라인 설계
- [[type-checker]] — 타입 체커 설계 및 구현
- [[request-evaluator]] — 요청 기반 평가 아키텍처
- [[diagnostics]] — 진단 시스템
- [[serialization]] — 바이너리 직렬화 (swiftmodule)
- [[dependency-analysis]] — 증분 빌드 의존성
- [[compiler-driver]] — 컴파일 모델과 드라이버
- [[debugging-the-compiler]] — 컴파일러 디버깅 가이드
- [[compiler-performance]] — 성능 측정
- [[compiling-swift-generics]] — 제네릭 컴파일 (책)
- [[generic-signatures]] — 제네릭 시그니처
- [[substitution-maps]] — 치환 맵
- [[archetypes]] — 아키타입
- [[conformances]] — 프로토콜 준수

### ABI
- [[abi-mangling]] — 심볼 맹글링/디맹글링
- [[abi-type-metadata]] — 타입 메타데이터 레이아웃
- [[abi-type-layout]] — 타입 메모리 레이아웃
- [[abi-calling-convention]] — 호출 규약
- [[abi-stability]] — ABI 안정성과 Library Evolution
- [[abi-generic-signature]] — 제네릭 시그니처 ABI
- [[runtime]] — Swift 런타임 ABI

### 코드 구조 분석
- [[sil-optimizer-pass-catalog]] — 205개 SIL 패스 전체 카탈로그
- [[ast-node-hierarchy]] — AST 노드 계층 (Decl/Expr/Stmt/Type)
- [[swift-compiler-sources]] — Swift-in-Swift 컴파일러 (165 파일)

### Interop (ObjC / C / C++)
- [[objc-interop]] — Swift ↔ ObjC 상호운용
- [[c-to-swift-name-translation]] — C/ObjC 이름 변환
- [[how-swift-imports-c-apis]] — C API 임포트 매핑
- [[cpp-interop-overview]] — C++ Interop 개요
- [[cpp-using-from-swift]] — Swift에서 C++ 사용
- [[cpp-calling-swift]] — C++에서 Swift 호출

### 언어 설계
- [[ownership-manifesto]] — 소유권 시스템
- [[generics-manifesto]] — 제네릭 시스템 비전
- [[error-handling]] — 에러 처리 모델
- [[dynamic-casting]] — 동적 캐스팅 규칙
- [[modules]] — 모듈 시스템
- [[access-control]] — 접근 제어
- [[literals]] — 리터럴 타입 추론
- [[failable-initializers]] — 실패 가능 이니셜라이저
- [[library-evolution]] — Library Evolution
- [[high-level-sil-optimizations]] — 고수준 SIL 최적화
- [[transparent-attr]] — @_transparent

### 기여 가이드
- [[getting-started]] — 개발 환경 설정
- [[first-pull-request]] — 첫 PR 가이드
- [[compiler-faq]] — FAQ
- [[testing-guide]] — 테스트 스위트
- [[continuous-integration]] — CI
- [[development-tips]] — 개발 팁
- [[stdlib-programmers-manual]] — stdlib 기여 가이드

### 패키지 및 도구
- [[swift-syntax-package]] — SwiftSyntax (구문 분석/매크로)
- [[swift-driver-package]] — 컴파일러 드라이버 패키지
- [[swift-package-manager]] — Swift Package Manager
- [[sourcekit-lsp]] — SourceKit LSP
- [[swift-testing-package]] — Swift Testing
- [[swift-foundation-package]] — Foundation
- [[swift-collections-package]] — Collections
- [[swift-nio-package]] — SwiftNIO
- [[llbuild-package]] — llbuild (저수준 빌드 엔진)
- [[swift-build-package]] — Swift Build
- [[swift-format-package]] — swift-format
