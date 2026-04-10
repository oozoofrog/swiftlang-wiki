---
type: summary
category: learning
tags: [swift, standard-library, runtime, compiler, abi, overlays]
aliases: [표준 라이브러리·런타임·컴파일러, stdlib-runtime-compiler, 표준 라이브러리와 런타임]
sources: [runtime.md, swift.org/documentation/standard-library/index.html, swift-foundation-readme.md, abi-stability-manifesto.md]
---

# 표준 라이브러리·런타임·컴파일러의 관계

Swift를 배우는 많은 사람은
- 표준 라이브러리
- 런타임
- 컴파일러
를 서로 다른 영역처럼 느낀다.
하지만 실제로는 이 셋이 거의 한 몸처럼 움직인다.
이 페이지는 그 관계를 상위 레벨에서 묶는 허브다.

## 세 층을 가장 짧게 설명하면

| 층 | 하는 일 | 연결 페이지 |
|---|---|---|
| 표준 라이브러리 | Swift 프로그램이 직접 쓰는 기본 타입/프로토콜/API를 제공 | [[official-docs/standard-library-to-compiler-crosswalk]], [[stdlib-programmers-manual]] |
| 런타임 | 메모리 관리, metadata, casting, conformance lookup 같은 실행시 서비스를 제공 | [[runtime]], [[abi-type-metadata]], [[dynamic-casting]] |
| 컴파일러 | 언어 의미를 검사하고 stdlib/runtime 계약에 맞는 코드로 lowering | [[overview]], [[type-checker]], [[sil-reference]], [[abi-stability]] |

## 왜 셋이 분리되지 않는가

### 1. 기본 타입은 언어이면서 라이브러리다
`Int`, `String`, `Array`, `Optional` 같은 타입은 사용자 입장에서는 “언어의 일부”처럼 느껴진다.
하지만 구현 관점에서는 표준 라이브러리 타입이면서,
동시에 ABI와 런타임, 최적화 규칙에 강하게 묶여 있다.

### 2. 컴파일러는 stdlib/runtime 계약을 알고 있어야 한다
Swift 컴파일러는 단순히 구문만 번역하지 않는다.
특정 타입 표현, builtins, ownership, witness, metadata 접근 같은 부분에서
stdlib/runtime과 맞물린 계약을 전제로 움직인다.

### 3. ABI와 library evolution이 셋을 묶는다
공개 API와 기본 타입을 안정적으로 배포하려면
- 타입 레이아웃
- metadata 표현
- calling convention
- resilience boundary
가 함께 맞아야 한다.

관련 페이지:
- [[abi-stability]]
- [[abi-type-layout]]
- [[library-evolution]]

## 구체적으로 어디서 만나나

### 표준 라이브러리 ↔ 런타임
- reference counting
- dynamic casting
- generic metadata instantiation
- builtins와 low-level runtime entrypoint

### 컴파일러 ↔ 표준 라이브러리
- literal defaulting과 기본 타입
- generic/protocol 기반 알고리즘 모델
- copy-on-write 최적화와 의미 보존
- stdlib 특화 SIL 최적화

### 컴파일러 ↔ 런타임
- metadata access
- value witness / type lowering
- existential container handling
- calling convention과 reabstraction

### ownership / memory model은 어디에 놓이나
ownership과 memory model은 사실 이 세 층을 가로지르는 공통 축에 가깝다.
값 의미론, ARC, borrow, copy-on-write, lifetime 문제는
stdlib API 감각에서 시작해 SIL ownership과 runtime 계약까지 이어진다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[ownership-manifesto]]
- [[sil-ownership]]

## Foundation 같은 상위 라이브러리는 어디에 놓이나

Foundation은 stdlib 바로 위의 실사용 계층처럼 볼 수 있다.
특히 overlay, module boundary, interop, cross-platform runtime 계약을 생각할 때 중요한 예시다.

관련 페이지:
- [[swift-foundation-package]]
- [[official-docs/core-libraries-to-compiler-crosswalk]]
- [[modules]]
- [[clang-importer]]

## 왜 이 허브가 필요한가

기존 위키에는
- stdlib 관련 문서
- runtime 문서
- ABI 문서
- compiler core 문서
가 각각 있다.
하지만 독자는 자주 이런 질문을 한다.

- 왜 기본 타입이 언어처럼 느껴지는데 사실 라이브러리 구현인가?
- 왜 ABI 문서가 stdlib 설계와 연결되는가?
- 왜 런타임 문제를 보다가 compiler/IRGen 문서로 넘어가야 하는가?

이 페이지는 바로 그 연결 고리를 보여 주는 용도다.

## 추천 읽기 순서

1. [[official-docs/standard-library-to-compiler-crosswalk]]
2. [[runtime]]
3. [[abi-stability]]
4. [[abi-type-metadata]]
5. [[library-evolution]]
6. [[swift-foundation-package]]

## 같이 보면 좋은 페이지

- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-ownership-memory-model]]
- [[official-docs/standard-library-to-compiler-crosswalk]]
- [[runtime]]
- [[abi-stability]]
- [[library-evolution]]
- [[swift-foundation-package]]
- [[keyword-network]]
