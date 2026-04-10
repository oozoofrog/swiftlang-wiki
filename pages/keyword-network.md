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

- 언어 → 구현 전체 지도: [[official-docs/language-to-compiler-crosswalk]]
- 입문 루트: [[swift-compiler-7-day-course]]
- 용어 정의: [[glossary-compiler]]
- 큰 그림: [[overview]]

## 1. 구문 / 파싱 / 표면 문법

핵심 키워드:
- [[modules|module]]
- [[literals|literal]]
- [[access-control|access control]]
- [[swift-syntax-package|SwiftSyntax]]
- [[sourcekit-lsp|LSP]]

추천 이동:
- 문법을 읽다가 AST/구문 트리 쪽으로 가고 싶다 → [[swift-syntax-package]]
- 파싱 이후 의미 부여 단계가 궁금하다 → [[type-checker]]
- 소스 편집기 기능과 연결해서 보고 싶다 → [[sourcekit-lsp]]

## 2. 타입 체커 / 진단 / 의미 분석

핵심 키워드:
- [[type-checker|Sema]]
- [[type-checker|constraint system]]
- [[diagnostics]]
- [[request-evaluator]]
- [[concurrency-data-race-safety|actor isolation / Sendable]]

추천 이동:
- 오버로드/리터럴/클로저 추론이 궁금하다 → [[type-checker]]
- 오류 메시지가 어떻게 만들어지는지 궁금하다 → [[diagnostics]] / [[official-docs/diagnostics-authoring]]
- Swift 6 concurrency 안전성 검사가 궁금하다 → [[concurrency-data-race-safety]]

## 3. 제네릭 / 프로토콜 / 시그니처

핵심 키워드:
- [[generic-signatures|generic signature]]
- [[archetypes|archetype]]
- [[substitution-maps|substitution map]]
- [[conformances|conformance]]
- [[official-docs/compiling-swift-generics-pdf|Compiling Swift Generics]]

추천 이동:
- 구현 중심으로 빠르게 들어가고 싶다 → [[compiling-swift-generics]]
- 비전/설계까지 보고 싶다 → [[generics-manifesto]] / [[official-docs/swift-generics-manifesto]]
- ABI와 연결해 보고 싶다 → [[abi-generic-signature]]

## 4. SIL / Ownership / 최적화

핵심 키워드:
- [[sil-reference|SIL]]
- [[sil-reference|raw SIL]]
- [[sil-reference|canonical SIL]]
- [[sil-ownership|OSSA]]
- [[sil-function-attributes|function attributes]]
- [[transparent-attr|@_transparent]]
- [[high-level-sil-optimizations|@_semantics]]
- [[sil-optimizer-pass-catalog|mandatory passes]]

추천 이동:
- SIL 전체 구조부터 보고 싶다 → [[sil-reference]]
- ownership/borrow와 연결해서 보고 싶다 → [[sil-ownership]] / [[ownership-manifesto]]
- 최적화 패스 지형을 보고 싶다 → [[optimizer-design]] / [[sil-optimizer-pass-catalog]]
- 함수 속성과 인라이닝 정책이 궁금하다 → [[sil-function-attributes]] / [[transparent-attr]]

## 5. 동시성 / 격리 / 전송 가능성

핵심 키워드:
- [[concurrency-data-race-safety|Strict Concurrency]]
- [[concurrency-data-race-safety|Sendable]]
- [[concurrency-data-race-safety|actor isolation]]
- [[sil-optimizer-pass-catalog|SendNonSendable]]
- [[sil-optimizer-pass-catalog|FlowIsolation]]

추천 이동:
- 설정/마이그레이션부터 보고 싶다 → [[concurrency-data-race-safety]]
- 공식 문서 입구에서 들어가고 싶다 → [[official-docs/concurrency-data-race-safety-to-compiler-checks]]
- ownership과 같이 보고 싶다 → [[sil-ownership]] / [[official-docs/value-reference-types-to-sil-ownership]]

## 6. ABI / 런타임 / 라이브러리 진화

핵심 키워드:
- [[abi-stability|ABI stability]]
- [[abi-type-layout|type layout]]
- [[abi-type-metadata|metadata]]
- [[abi-calling-convention|reabstraction]]
- [[abi-mangling|mangling]]
- [[runtime]]
- [[library-evolution|fragile / resilient]]
- [[serialization|swiftmodule serialization]]

추천 이동:
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

추천 이동:
- Swift가 왜 모듈 전체를 의식하며 컴파일되는지 보고 싶다 → [[compiler-driver]] / [[dependency-analysis]]
- 구현 패키지 구조를 보고 싶다 → [[swift-driver-package]] / [[llbuild-package]]
- 성능과 연결해서 보고 싶다 → [[compiler-performance]] / [[official-docs/compiler-performance-reference]]

## 8. 라이브러리 / 프레임워크 / 실사용 생태계

핵심 키워드:
- [[standard-library-to-compiler-crosswalk|standard library]]
- [[swift-foundation-package|Foundation]]
- [[swift-collections-package|Collections]]
- [[swift-nio-package|NIO]]
- [[swift-testing-package|Swift Testing]]
- [[core-libraries-to-compiler-crosswalk|Core Libraries]]

추천 이동:
- 언어 표면의 기본 타입이 어떻게 구현/진화되는지 보고 싶다 → [[standard-library-to-compiler-crosswalk]]
- 크로스 플랫폼 라이브러리 경계를 보고 싶다 → [[core-libraries-to-compiler-crosswalk]]
- 테스트/툴링 생태계와 연결해서 보고 싶다 → [[swift-testing-package]] / [[sourcekit-lsp]]

## 자주 같이 움직이는 키워드 묶음

- literal → contextual type → constraint solving → diagnostics
  - [[literals]] → [[type-checker]] → [[diagnostics]]
- generic signature → archetype → substitution map → conformance
  - [[generic-signatures]] → [[archetypes]] → [[substitution-maps]] → [[conformances]]
- raw SIL → canonical SIL → ownership → optimization pass
  - [[sil-reference]] → [[sil-ownership]] → [[optimizer-design]] → [[sil-optimizer-pass-catalog]]
- Sendable → actor isolation → FlowIsolation → ownership
  - [[concurrency-data-race-safety]] → [[sil-optimizer-pass-catalog]] → [[sil-ownership]]
- ABI stability → metadata → runtime → library evolution
  - [[abi-stability]] → [[abi-type-metadata]] → [[runtime]] → [[library-evolution]]
- driver → dependency analysis → llbuild → SwiftPM
  - [[compiler-driver]] → [[dependency-analysis]] → [[llbuild-package]] → [[swift-package-manager]]
