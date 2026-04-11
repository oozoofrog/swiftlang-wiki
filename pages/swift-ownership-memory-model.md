---
type: summary
category: learning
tags: [swift, ownership, memory-model, ossa, arc, concurrency]
aliases: [Swift 소유권·메모리 모델, Swift ownership memory model, ownership/memory model]
sources: [ownership-manifesto.md, sil-ownership.md, official-docs/ownership-ssa.md, official-docs/value-reference-types-to-sil-ownership.md, concurrency-data-race-safety.md]
---

# Swift 소유권·메모리 모델

이 페이지는 Swift의 ownership, borrowing, ARC, copy-on-write, lifetime, concurrency isolation을
하나의 이야기로 묶는 상위 허브다.
값/참조 의미론, borrow, consume, exclusivity, ARC, actor isolation은 보통 따로 배우기 쉽지만,
실제로는 모두 Swift의 메모리/수명/이동 규칙이라는 하나의 문제로 다시 만난다.

## 이 허브가 묶는 5개 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| 언어 의미 | 값/참조 의미론, copy-on-write, `inout`, move-only는 어떤 약속을 가지는가 | [[swift-language-overview]], [[swift-type-system]], [[official-docs/value-reference-types-to-sil-ownership]] |
| SIL 소유권 | borrow scope, consume, lifetime-ending use, OSSA는 어떻게 표현되는가 | [[ownership-manifesto]], [[sil-ownership]], [[official-docs/ownership-ssa]] |
| 메모리 접근과 수명 | 주소 기반 접근, exclusivity, lexical lifetime은 어디서 보이는가 | [[sil-memory-access]], [[sil-reference]], [[runtime]] |
| ABI / runtime 연결 | 타입 레이아웃, metadata, ARC, reference counting은 어떻게 맞물리는가 | [[standard-library-runtime-and-compiler]], [[abi-type-layout]], [[abi-type-metadata]], [[runtime]] |
| 동시성 / 격리 | `Sendable`, actor isolation, region isolation은 ownership과 어떻게 연결되는가 | [[swift-concurrency-architecture]], [[swift-actor-isolation-and-sendable]], [[concurrency-data-race-safety]], [[official-docs/concurrency-data-race-safety-to-compiler-checks]], [[sil-optimizer-pass-catalog]] |

## 왜 이 허브가 중요한가

Swift에서 ownership과 memory는 단순히 “힙이냐 스택이냐”의 문제가 아니다.

- value semantics는 저장 위치를 직접 약속하지 않는다.
- reference semantics는 “로컬 변수 자체가 힙에 있다”는 뜻이 아니다.
- ARC는 ownership 모델의 일부이지만 ownership 전체와 같지 않다.
- concurrency safety는 결국 무엇이 어느 실행 문맥으로 안전하게 이동할 수 있는가의 문제이므로 ownership과 다시 만난다.

즉 Swift의 메모리 모델을 이해하려면
값/참조 의미론, lifetime, borrow, consume, copy-on-write, ARC, isolation을 분리해서 보되,
마지막에는 다시 한 장으로 합쳐서 볼 필요가 있다.

## 자주 헷갈리는 구분

### 1. value semantics vs storage location
`struct`가 value type이라는 말은 “항상 stack”이라는 뜻이 아니다.
반대로 `class`가 reference type이라는 말도 “지역 변수 슬롯까지 heap”이라는 뜻이 아니다.
이 차이를 먼저 잡아야 [[official-docs/value-reference-types-to-sil-ownership]], [[runtime]], [[sil-ownership]]가 자연스럽게 이어진다.

### 2. ownership vs ARC
ARC는 retain/release 기반의 메모리 관리 전략이다.
하지만 ownership은 값의 생성, borrow, consume, lifetime ending use까지 포함하는 더 넓은 계약이다.
그래서 ownership을 보려면 [[ownership-manifesto]]와 [[official-docs/ownership-ssa]]를 같이 보는 편이 좋다.

### 3. borrow vs `inout` vs consume
Swift 표면에서는 이 셋이 비슷하게 “복사 없이 다루는 방식”처럼 보일 수 있다.
하지만 컴파일러 관점에서는 address-only 접근, borrow scope, lifetime, mutation 규칙이 서로 다르다.
이 차이는 [[sil-memory-access]], [[sil-function-conventions]], [[sil-ownership]]에서 구체화된다.

### 4. ownership vs concurrency isolation
동시성 검사 표면에서는 `Sendable`, actor isolation, global actor 규칙이 보인다.
그러나 구현 층으로 내려가면 region isolation, sendability, lifetime 추적이 ownership 문제와 다시 만난다.
그래서 [[concurrency-data-race-safety]]를 읽을 때도 ownership 배경이 있으면 훨씬 덜 헷갈린다.

## 컴파일러 안에서는 어디가 핵심인가

### 1. Sema / 타입 시스템 층
언어 표면의 값/참조 의미론, `inout`, sendability, isolation 규칙은
먼저 의미 분석과 타입 검사 층에서 판정된다.

관련 페이지:
- [[swift-type-system]]
- [[type-checker]]
- [[diagnostics]]
- [[concurrency-data-race-safety]]

### 2. SILGen / OSSA 층
표면 언어 의미는 SIL로 내려오면서 ownership kind, borrow scope, copy/destroy 규칙으로 드러난다.
이 지점이 Swift ownership 모델의 핵심 구현 입구다.

관련 페이지:
- [[sil-reference]]
- [[sil-ownership]]
- [[official-docs/ownership-ssa]]

### 3. 검증기와 mandatory transform 층
OSSA는 설명용 개념으로 끝나지 않는다.
borrow scope 축소, move-only 검사, lifetime issue 진단 같은 검증/변환이 뒤따른다.
그래서 ownership은 최적화 이전의 안정성 규칙이면서,
동시에 이후 변환이 의존하는 계약이기도 하다.

관련 페이지:
- [[sil-optimizer-pass-catalog]]
- [[optimizer-design]]
- [[sil-arc-optimization]]

### 4. runtime / ABI 층
메모리 모델은 결국 실행시 표현과 만나야 한다.
metadata, layout, reference counting, value witness, copy-on-write 구현은
ownership 이야기의 런타임 쪽 얼굴이다.

관련 페이지:
- [[standard-library-runtime-and-compiler]]
- [[runtime]]
- [[abi-type-layout]]
- [[abi-type-metadata]]

## 로컬 Swift 소스에서 같이 볼 경로

이 주제를 로컬 `swift/` 소스 트리와 같이 읽고 싶다면,
아래 경로들이 좋은 진입점이다.

- `swift/docs/OwnershipManifesto.md`
- `swift/docs/SIL/Ownership.md`
- `swift/lib/Sema/TypeCheckConcurrency.cpp`
- `swift/lib/AST/ActorIsolation.cpp`
- `swift/lib/SIL/IR/ActorIsolation.cpp`
- `swift/lib/SIL/Utils/OSSACompleteLifetime.cpp`
- `swift/lib/SIL/Verifier/MemoryLifetimeVerifier.cpp`
- `swift/lib/SILOptimizer/Utils/ShrinkBorrowScope.cpp`
- `swift/lib/SILOptimizer/Mandatory/MoveOnlyChecker.cpp`
- `swift/lib/SILOptimizer/Mandatory/DiagnoseLifetimeIssues.cpp`
- `swift/lib/SILOptimizer/Utils/RegionIsolation.cpp`
- `swift/lib/SILOptimizer/Mandatory/FlowIsolation.cpp`
- `swift/lib/SILOptimizer/Mandatory/SendNonSendable.cpp`

이 목록만 봐도 ownership이 단순 문서 주제가 아니라
Sema, SIL, verifier, optimizer, concurrency 검증을 가로지르는 축이라는 점이 드러난다.

## 추천 읽기 순서

### 언어 의미에서 들어가는 루트
1. [[swift-language-overview]]
2. [[official-docs/value-reference-types-to-sil-ownership]]
3. [[standard-library-runtime-and-compiler]]
4. [[ownership-manifesto]]
5. [[runtime]]

### 구현 중심 루트
1. [[ownership-manifesto]]
2. [[sil-reference]]
3. [[sil-ownership]]
4. [[official-docs/ownership-ssa]]
5. [[sil-arc-optimization]]
6. [[sil-optimizer-pass-catalog]]

### 동시성과 연결해서 보는 루트
1. [[swift-concurrency-architecture]]
2. [[concurrency-data-race-safety]]
3. [[official-docs/concurrency-data-race-safety-to-compiler-checks]]
4. [[sil-ownership]]
5. [[official-docs/ownership-ssa]]
6. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-type-system]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[standard-library-runtime-and-compiler]]
- [[ownership-manifesto]]
- [[sil-ownership]]
- [[official-docs/value-reference-types-to-sil-ownership]]
- [[official-docs/ownership-ssa]]
- [[concurrency-data-race-safety]]
- [[keyword-network]]