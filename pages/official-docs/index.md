---
type: summary
category: official-docs
tags: [official-docs, downloads, references, crosswalk]
aliases: [공식 문서 해설 허브, 다운로드 문서 해설]
sources: [swift-docs-20260410-081300]
---

# 공식/다운로드 문서 해설 허브

다운로드 번들에 포함된 21개 공식/준공식 문서를 위키 관점으로 다시 정리한 허브다.
이 섹션의 목적은 단순 파일 보관이 아니라, 각 문서를

1. 무엇을 위한 문서인지 파악하고
2. 관련 위키의 어느 심화 페이지와 이어지는지 확인하고
3. 언어 표면 지식에서 컴파일러 내부 지식으로 넘어가는 길을 만드는 것

에 있다.

## 먼저 읽으면 좋은 페이지

- [[language-to-compiler-crosswalk]] — 언어 개념 ↔ 컴파일러 구현의 전체 지도
- [[swift-documentation-index]] — Swift.org 공식 문서 지형도
- [[swift-compiler-architecture]] — 공개 컴파일러 개요
- [[downloads/index]] — 실제 다운로드 허브와 파일 링크

## 입문 허브
| 문서 | 요점 | 관련 위키 연결 |
|---|---|---|
| [Swift.org Documentation 허브 해설](swift-documentation-index.md) | TSPL, API Design Guidelines, Standard Library, Core Libraries, Package Manager, REPL/Debugger가 한 축으로 묶여 있다. | [[overview]], [[getting-started]], [[continuous-integration]] |
| [Swift Compiler 공개 개요 해설](swift-compiler-architecture.md) | main swift 저장소와 swift-driver 저장소를 함께 보여 준다. | [[overview]], [[compiler-driver]], [[diagnostics]] |
| [TSPL → 컴파일러 교차 읽기](tspl-to-compiler-crosswalk.md) | TSPL은 Swift의 권위 있는 언어 레퍼런스라는 위치를 가진다. | [[overview]], [[type-checker]], [[modules]] |

## 컴파일러 코어
| 문서 | 요점 | 관련 위키 연결 |
|---|---|---|
| [Compiling Swift Generics PDF 해설](compiling-swift-generics-pdf.md) | 제네릭 파라미터, requirement, conformance, substitution이 컴파일 과정에서 어떻게 표현되는지 따라갈 수 있다. | [[compiling-swift-generics]], [[generic-signatures]], [[substitution-maps]] |
| [Compiling Swift Generics README 해설](compiling-swift-generics-readme.md) | 책의 범위를 명시한다: Swift에서 parametric polymorphism을 컴파일러가 어떻게 구현하는지 다룬다. | [[compiling-swift-generics]], [[overview]], [[generic-signatures]] |
| [Generics Manifesto 해설](swift-generics-manifesto.md) | 제네릭 기능을 단편 기능 목록이 아니라 하나의 장기적 설계 공간으로 정리한다. | [[generics-manifesto]], [[compiling-swift-generics]], [[generic-signatures]] |
| [TypeChecker.md 해설](type-checker-design-and-implementation.md) | 타입 검사를 Constraint Generation → Solving → Solution Application의 세 단계로 정리한다. | [[type-checker]], [[diagnostics]], [[compiler-performance]] |
| [SIL.md 해설](swift-intermediate-language.md) | Swift 소스가 raw SIL, canonical SIL, optimized SIL을 거쳐 LLVM IR로 가는 위치를 명확히 보여 준다. | [[sil-reference]], [[sil-instructions]], [[sil-types]] |
| [Ownership SSA 해설](ownership-ssa.md) | 모든 SIL 값에 None / Owned / Guaranteed / Unowned 중 하나의 ownership kind를 부여한다. | [[sil-ownership]], [[ownership-manifesto]], [[sil-memory-access]] |
| [High-Level Optimizations in SIL 해설](high-level-optimizations-in-sil.md) | Array/String/Span 같은 표준 라이브러리 연산을 일반 함수 호출이 아니라 의미적 원자 연산처럼 이해하게 만든다. | [[high-level-sil-optimizations]], [[optimizer-design]], [[sil-reference]] |

## 툴링/운영
| 문서 | 요점 | 관련 위키 연결 |
|---|---|---|
| [Compiler Performance 문서 해설](compiler-performance-reference.md) | primary-file / batch / WMO 모드 차이가 성능 관찰에 직접적인 영향을 준다. | [[compiler-performance]], [[compiler-driver]], [[dependency-analysis]] |
| [Driver Internals 문서 해설](driver-internals.md) | 드라이버를 Parse → Pipeline → Build → Schedule → Batch → Execute 단계로 본다. | [[compiler-driver]], [[dependency-analysis]], [[swift-driver-package]] |
| [Diagnostics 작성 가이드 해설](diagnostics-authoring.md) | error / warning / note를 언제 어떻게 구분할지 명확한 기준을 준다. | [[diagnostics]], [[debugging-the-compiler]], [[error-handling]] |
| [REPL and Debugger 해설](swift-repl-and-debugger.md) | Swift REPL은 별도 인터프리터가 아니라 LLDB 기반 디버거 경험과 결합돼 있다. | [[debugging-the-compiler]], [[getting-started]], [[overview]] |
| [SwiftPM 문서 → 빌드 파이프라인 교차 읽기](swiftpm-docs-to-build-pipeline.md) | 번들 안의 실제 파일에는 본문이 없고 canonical SwiftPM DocC 문서로 리다이렉트만 걸려 있다. | [[swift-package-manager]], [[swift-driver-package]], [[compiler-driver]] |

## ABI/라이브러리/언어 의미
| 문서 | 요점 | 관련 위키 연결 |
|---|---|---|
| [ABI Stability Manifesto 해설](abi-stability-manifesto.md) | source compatibility, module stability, ABI stability를 구분한다. | [[abi-stability]], [[library-evolution]], [[abi-type-layout]] |
| [API Design Guidelines → 컴파일러 교차 읽기](api-design-guidelines-to-compiler-crosswalk.md) | 핵심 원칙은 “Clarity at the point of use”다. | [[library-evolution]], [[c-to-swift-name-translation]], [[how-swift-imports-c-apis]] |
| [Standard Library → 컴파일러 교차 읽기](standard-library-to-compiler-crosswalk.md) | 표준 라이브러리는 Swift 프로그램의 base layer이며, 소스와 테스트는 메인 swift 저장소에 있다. | [[stdlib-programmers-manual]], [[runtime]], [[abi-type-layout]] |
| [Core Libraries → 컴파일러 교차 읽기](core-libraries-to-compiler-crosswalk.md) | Foundation, libdispatch, Swift Testing, XCTest를 하나의 교차 플랫폼 라이브러리군으로 소개한다. | [[swift-foundation-package]], [[swift-testing-package]], [[how-swift-imports-c-apis]] |
| [Value/Reference Types → SIL 소유권 교차 읽기](value-reference-types-to-sil-ownership.md) | struct/enum/tuple는 value type, class/actor/closure는 reference type으로 소개한다. | [[sil-ownership]], [[sil-arc-optimization]], [[sil-memory-access]] |
| [Concurrency Data Race Safety → 컴파일러 검사 교차 읽기](concurrency-data-race-safety-to-compiler-checks.md) | 번들 안의 파일 자체에는 동시성 본문이 없고 redirect만 존재한다. | [[concurrency-data-race-safety]], [[type-checker]], [[diagnostics]] |
