---
type: reference
category: learning
tags: [swift, proposal, value-semantics, cow, ownership, runtime]
aliases: [Value Semantics / COW proposals, value semantics와 COW proposal 교차 읽기]
sources: [swiftlang-swift/docs/proposals/ValueSemantics.rst, swiftlang-swift/docs/proposals/InoutCOWOptimization.rst]
---

# Value Semantics / COW proposals → ownership/runtime 교차 읽기

이 페이지는 `swift/docs/proposals/ValueSemantics.rst`와
`swift/docs/proposals/InoutCOWOptimization.rst`를
현재 Swift ownership / runtime / stdlib 구현 관점으로 다시 읽는 교차 페이지다.

## 이 proposal 묶음이 설명하는 핵심 문제

이 두 문서는 서로 다른 시기의 제안이지만,
사실상 같은 큰 질문을 다룬다.

- 값 의미론은 정확히 무엇인가?
- value semantics와 reference semantics는 generic code에서 왜 중요한가?
- copy-on-write는 어디서 성능 함정을 만나는가?
- `inout`, writeback, slice, uniqueness check는 어떤 구현 비용을 가지는가?

즉 이 proposal 묶음은
오늘날 [[swift-ownership-memory-model]]과 [[standard-library-runtime-and-compiler]]에서 보는 문제를
더 원형적인 언어/설계 문제로 보여 준다.

## ValueSemantics.rst의 핵심 포인트

### 1. 값 의미론의 가장 중요한 정의
이 문서는 value semantics를
“복사된 값이 원본과 독립적으로 수정 가능하고, 원본과 interchangeable 하다”는 관점으로 설명한다.

가장 중요한 문장은 사실 이것에 가깝다.

- value semantics는 mutable state로 가는 여러 경로를 만들지 않는다.

이 관점은 지금도 유효하다.
그래서 현재 위키의 [[official-docs/value-reference-types-to-sil-ownership]]와
[[swift-ownership-memory-model]]로 자연스럽게 이어진다.

### 2. `struct` vs `class`를 단순화하지 말라고 경고한다
이 proposal은 꽤 일찍부터 이미
“`struct` == value semantics, `class` == reference semantics”라고 기계적으로 보면 안 된다고 말한다.

- immutable class는 사실상 value semantics처럼 보일 수 있다.
- `struct`도 내부에 class storage를 두면 reference-semantics처럼 쓸 수 있다.
- `Array` 같은 타입은 이 긴장을 보여 주는 대표 사례다.

이건 현재 위키의 다음 축과 바로 이어진다.

- [[swift-ownership-memory-model]]
- [[official-docs/value-reference-types-to-sil-ownership]]
- [[runtime]]

### 3. generic algorithm은 semantics contract가 필요하다
이 문서는 generic programming에서
단순히 타입만 맞는다고 충분하지 않고,
복사/대입/인자 전달의 의미가 알고리즘 가정과 맞아야 한다고 강조한다.

즉 제네릭은 단순 타입 추상화가 아니라
semantic abstraction이기도 하다.

이 포인트는 현재 다음 페이지들과 맞닿는다.

- [[swift-type-system]]
- [[generics-manifesto]]
- [[type-checker]]

## InoutCOWOptimization.rst의 핵심 포인트

### 1. writeback model과 COW의 충돌
이 proposal은 `x[0].mutate()`나 slice 기반 알고리즘에서
getter/setter writeback 모델 때문에 불필요한 복사가 발생한다고 설명한다.

대표 문제의식:
- temporary를 만들면서 retain count가 2 이상이 되어
- buffer가 실제로는 고유해도 COW copy가 일어나고
- 결과적으로 O(1)이어야 할 수정이 O(N)이 될 수 있다

이 문제의식은 오늘날에도
copy-on-write를 “언어 의미 + API 설계 + lowering + runtime uniqueness check”로 같이 봐야 한다는 사실을 드러낸다.

### 2. slice와 divide-and-conquer 알고리즘
이 문서는 quicksort 예시로
slice 기반 재귀가 `inout`와 결합될 때 비용이 커지는 문제를 보여 준다.

특히 흥미로운 점은
나중의 structured concurrency / parallel algorithm 감각과도 닿는다는 점이다.
문서 안에는 non-overlapping slice와 async-style parallel mutation 가능성도 언급된다.

즉 이 proposal은
단순 stdlib 성능 문제가 아니라
ownership / aliasing / future concurrency 감각이 만나던 지점을 보여 준다.

### 3. 제안된 메커니즘은 역사적이지만 문제 자체는 아직 살아 있다
이 문서는 `@cow`, `inout_retain`, `inout_release`, `INOUT` bit 같은 구체 메커니즘을 제안한다.
오늘날 그대로 그 모양으로 읽는 건 위험하지만,
문제가 어디에 있었는지 이해하는 데는 매우 유용하다.

특히 다음 개념과 직접 이어서 읽으면 좋다.

- `Builtin.isUniquelyReferenced`
- SIL ownership / memory access
- copy_addr / writeback / exclusivity
- stdlib COW buffer model

관련 페이지:
- [[sil-ownership]]
- [[sil-memory-access]]
- [[sil-arc-optimization]]
- [[runtime]]

## 오늘의 구현과 어떻게 이어 읽으면 좋은가

### 1. 언어 표면
- 값/참조 의미론의 교육용 입구 → [[official-docs/value-reference-types-to-sil-ownership]]
- 큰 그림 허브 → [[swift-ownership-memory-model]]

### 2. SIL / ownership / access
- ownership model → [[sil-ownership]]
- 메모리 접근 → [[sil-memory-access]]
- ARC 최적화 → [[sil-arc-optimization]]

### 3. stdlib / runtime
- 표준 라이브러리와 runtime의 한 몸 관계 → [[standard-library-runtime-and-compiler]]
- 실행시 표현 → [[runtime]]

## 이 proposal 묶음을 읽을 때의 주의점

- proposal의 구체 메커니즘이 현재 구현과 1:1로 대응된다고 가정하면 안 된다.
- 하지만 문제가 어디서 발생했는지, 어떤 추상화가 필요했는지는 여전히 중요하다.
- 특히 “value semantics는 단순 저장 위치 이야기가 아니다”라는 핵심은 지금도 그대로 유효하다.

## 추천 읽기 순서

1. [[swift-ownership-memory-model]]
2. [[official-docs/value-reference-types-to-sil-ownership]]
3. [[proposal-value-semantics-and-cow-to-ownership]]
4. [[sil-ownership]]
5. [[standard-library-runtime-and-compiler]]
6. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-in-place-operations-to-writeback-and-cow]]
- [[proposal-optimizer-effects-and-attributes-to-sil-optimizer]]
- [[swift-ownership-memory-model]]
- [[official-docs/value-reference-types-to-sil-ownership]]
- [[sil-ownership]]
- [[sil-memory-access]]
- [[sil-arc-optimization]]
- [[standard-library-runtime-and-compiler]]
- [[runtime]]
- [[keyword-network]]
