---
type: reference
category: learning
tags: [swift, proposal, optimizer, effects, function-attributes, specialization]
aliases: [Optimizer Effects proposal 교차 읽기, optimization attributes 교차 읽기, optimizer effects to sil optimizer]
sources: [swiftlang-swift/docs/proposals/OptimizerEffects.rst, swiftlang-swift/docs/proposals/UnsupportedOptimizationAttributes.rst]
---

# Optimizer Effects / Unsupported Optimization Attributes proposals → SIL optimizer / function attributes 교차 읽기

이 페이지는 `swift/docs/proposals/OptimizerEffects.rst`와
`swift/docs/proposals/UnsupportedOptimizationAttributes.rst`를
현재 Swift의 SIL optimizer, 함수 속성, specialization, COW 최적화 문맥으로 다시 읽는 교차 페이지다.

## 이 proposal 묶음이 다루는 핵심 문제

이 두 문서는 공통적으로 이런 질문을 다룬다.

- 함수가 프로그램 상태에 무엇을 할 수 있다고 compiler가 "알고 있어야" 하는가?
- 그 정보는 분석으로만 충분한가, 아니면 source-level 힌트가 필요한가?
- 인라이닝, specialization, COW 최적화는 어떤 semantic contract 위에서 안전해지는가?
- 언더스코어 optimizer 속성은 언어 기능인가, 내부 구현 계약인가?

즉 이 proposal 묶음은
현재 [[high-level-sil-optimizations]], [[sil-function-attributes]], [[optimizer-design]]에서 보이는
optimizer 표면을 더 원형적인 설계 문제로 보여 준다.

## OptimizerEffects.rst의 핵심 포인트

### 1. optimizer는 "함수 효과 모델"이 필요하다
문서는 optimizer가 함수 호출을 공격적으로 재배치/제거/합치려면
그 함수가 어떤 상태를 읽고, 쓰고, 붙잡고, 해제하는지 알아야 한다고 본다.

핵심 primitive:
- `allocs`
- `traps`
- `read`
- `write`
- `capture`
- `release`

중요한 점은 이 효과들이
"반드시 한다"가 아니라
"할 수 있다(may)"의 보수적 모델로 해석된다는 것이다.

이 관점은 지금의 side-effect analysis와
`@_effects` 계열을 이해하는 출발점이다.

### 2. 상태를 argument-reachable state와 unspecified state로 나눈다
문서는 프로그램 상태를
- 인자를 통해 도달 가능한 상태
- 그 외의 unspecified state
로 나눠서 설명한다.

예를 들어 `@_effects(argonly)`는
unspecified state에는 효과가 없고,
효과가 있더라도 인자 쪽 reachable state 안에만 있다는 뜻으로 읽힌다.

이 구분은 단순 attribute 문법 문제가 아니라,
optimizer가 aliasing / hoisting / call reordering을 어디까지 해도 되는지에 관한 규칙이다.

### 3. COW 최적화는 일반 효과 모델 위에 특수 보장을 더 얹는다
문서가 특히 흥미로운 지점은
Array 같은 COW 타입 최적화를 위해
일반적인 `read/write/capture/release`만으로는 부족하다고 본다는 점이다.

그래서 다음 같은 self-state 중심 보장을 제안한다.
- `@make_unique`
- `@preserve_unique`
- `@get_subobject`
- `@get_subobject_non_bridged`

핵심 의도:
- `self`를 unique 상태로 만들 수 있는가?
- unique 상태를 깨지 않는가?
- subobject를 projection하되 optimizer가 aliasing/capture를 더 좁게 볼 수 있는가?
- bridged / non-bridged 상태를 구분해야 하는가?

즉 이 문서는 COW 최적화를
단순 stdlib 요령이 아니라
effect system + ownership/capture 모델 + bridged storage 문제로 본다.

관련 페이지:
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[high-level-sil-optimizations]]
- [[swift-ownership-memory-model]]

## UnsupportedOptimizationAttributes.rst의 핵심 포인트

### 1. 언더스코어 optimizer 속성은 안정된 언어 기능이 아니다
문서는 `@inline(__always)`와 `@_specialize`를
실험적 optimizer directive로 설명한다.

중요한 메시지:
- 밑줄 속성은 내부 compiler 계약에 가깝다
- 정식 Swift Evolution을 거친 안정 surface라고 보면 안 된다
- compiler 버전 변화에 따라 source maintainer가 수동 개입해야 할 수 있다

즉 이 문서는
오늘날에도 언더스코어 속성을 "성능용 private escape hatch"로 봐야 한다는 감각을 준다.

### 2. `@inline(__always)`는 `_transparent`와 닮았지만 같은 것은 아니다
`@inline(__always)`는 강한 인라이닝 힌트지만,
`@_transparent`처럼
진단 이전 mandatory inlining과 language-like transparency를 뜻하는 것은 아니다.

그래서 이 proposal은
현재 다음 두 페이지를 같이 읽을 때 더 잘 보인다.
- [[sil-function-attributes]]
- [[transparent-attr]]

즉 "인라인된다"는 한 단어 안에도
- 언제 인라인되는가
- semantic visibility를 어떻게 약속하는가
- debug / diagnostics / resilience와 어떤 관계인가
같은 층위 차이가 있다.

### 3. `@_specialize`는 generic specialization의 역사적 창문이다
문서는 cross-module 상황에서
compiler가 자동 specialization을 항상 해주지 못하므로,
programmer가 `@_specialize`로 힌트를 줄 수 있다고 설명한다.

이건 지금도 중요한 질문과 이어진다.
- specialization은 어디서 자동으로 일어나는가?
- module boundary는 왜 최적화 장벽이 되는가?
- performance-sensitive generic API는 어떤 속성에 기대는가?

관련 페이지:
- [[optimizer-design]]
- [[compiler-performance]]
- [[compiling-swift-generics]]
- [[generic-signatures]]

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. optimizer의 고수준 의미 모델
이 proposal 묶음을 읽고 바로 이어 가기 좋은 페이지:
- [[high-level-sil-optimizations]]
- [[official-docs/high-level-optimizations-in-sil]]

여기서 `@_semantics`, `@_effects`, stdlib intrinsic-like API 모델이
어떻게 실제 최적화 전략으로 이어지는지 볼 수 있다.

### 2. 함수 속성과 인라이닝 정책
source-level optimizer 속성의 표면은 다음 페이지에 모여 있다.
- [[sil-function-attributes]]
- [[transparent-attr]]

### 3. 실제 optimizer 파이프라인과 패스
효과 정보가 실제로 쓰이는 자리는 결국 optimizer다.
- [[optimizer-design]]
- [[sil-optimizer-pass-catalog]]
- [[sil-arc-optimization]]

특히 generic specialization, COW 패스, ARC 최적화를 같이 보면
왜 effect/capture 모델이 필요한지 감이 온다.

## 이 proposal 묶음을 읽을 때의 주의점

- proposal의 attribute 이름과 현재 compiler surface가 1:1 대응된다고 보면 안 된다.
- 특히 언더스코어 속성은 여전히 구현 디테일/내부 계약 성격이 강하다.
- 하지만 optimizer가 어떤 semantic guarantee를 원했는지는 지금도 매우 중요하다.
- 즉 이 문서들은 "현대 optimizer 표면의 역사적 설계 메모"로 읽는 편이 맞다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/OptimizerEffects.rst`
- `swift/docs/proposals/UnsupportedOptimizationAttributes.rst`
- `swift/docs/HighLevelSILOptimizations.rst`
- `swift/docs/SIL/FunctionAttributes.md`
- `swift/lib/SILOptimizer/Transforms/GenericSpecializer.cpp`
- `swift/lib/SILOptimizer/Transforms/COWOpts.cpp`
- `swift/lib/SILOptimizer/LoopTransforms/COWArrayOpt.cpp`
- `swift/lib/SILOptimizer/Analysis/`

현재 위키 연결:
- [[high-level-sil-optimizations]]
- [[sil-function-attributes]]
- [[transparent-attr]]
- [[optimizer-design]]
- [[sil-optimizer-pass-catalog]]
- [[proposal-value-semantics-and-cow-to-ownership]]

## 추천 읽기 순서

1. [[proposal-optimizer-effects-and-attributes-to-sil-optimizer]]
2. [[high-level-sil-optimizations]]
3. [[sil-function-attributes]]
4. [[transparent-attr]]
5. [[optimizer-design]]
6. [[sil-optimizer-pass-catalog]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[high-level-sil-optimizations]]
- [[official-docs/high-level-optimizations-in-sil]]
- [[sil-function-attributes]]
- [[transparent-attr]]
- [[optimizer-design]]
- [[compiler-performance]]
- [[compiling-swift-generics]]
- [[keyword-network]]
