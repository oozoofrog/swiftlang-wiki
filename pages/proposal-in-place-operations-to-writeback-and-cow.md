---
type: reference
category: learning
tags: [swift, proposal, inplace, writeback, cow, mutating]
aliases: [In-Place Operations proposal 교차 읽기, inplace operations to writeback, in-place operations to COW]
sources: [swiftlang-swift/docs/proposals/Inplace.rst]
---

# In-Place Operations proposal → writeback / COW / optimizer-friendly API 교차 읽기

이 페이지는 `swift/docs/proposals/Inplace.rst`를
현재 Swift의 `mutating`, `inout`, writeback, COW, optimizer-friendly value API 문맥으로 다시 읽는 교차 페이지다.

## 이 proposal이 다루는 핵심 문제

문서의 큰 문제의식은 단순하다.

- non-mutating API와 mutating API를 왜 따로 이름 붙여야 하는가?
- 같은 연산의 두 버전 사이 semantic relation을 compiler가 알 수는 없는가?
- 사용자 표현력은 유지하면서, compiler가 중간 temporary를 줄일 수는 없는가?
- `self`가 암묵적 `inout`인 세계에서 API 표면은 어떻게 생겨야 하는가?

즉 이 proposal은
현재 Swift의 `mutating` 감각을 단순 문법이 아니라
value semantics + writeback + optimization 문제로 보게 해 준다.

## Inplace.rst의 핵심 포인트

### 1. mutating / non-mutating 쌍은 naming 문제이자 의미 문제다
문서는 `sort()` / `sorted()`, `union()` / `unionInPlace()` 같은 패턴을 보며
이름이 제각각이고 boilerplate가 많으며,
무엇보다 둘의 관계를 compiler가 이해하지 못한다고 본다.

핵심 질문은
"이 둘은 사실 같은 연산의 두 surface 아닌가?"
이다.

그래서 이 proposal은
mutating / non-mutating 연산을 한 쌍의 semantic relation으로 묶으려 한다.

### 2. `self`가 implicit `inout`라는 사실을 전면으로 끌어낸다
free function에서는
`union(x, y)`와 `union(&x, y)`처럼
address-of 여부로 mutating / non-mutating을 구분할 수 있다.

하지만 method는 `self`가 암묵적으로 `inout`이므로,
`x.union(y)`만 보고는 어떤 버전인지 모호해진다.

이 문제를 해결하려고 문서는
assignment method, `.=f(...)` 같은 역사적 문법을 제안한다.

오늘날 그 정확한 문법이 남아 있지는 않지만,
문제의 핵심은 여전히 유효하다.
- method call의 표면은 어떻게 mutation을 드러낼 것인가?
- `mutating`과 fluent API를 어떻게 공존시킬 것인가?
- non-mutating chain을 내부적으로 mutating lowering으로 바꿔도 되는가?

### 3. 자동 생성과 semantic requirement를 통해 optimizer 기회를 만들려 한다
문서는 value type에 대해
- non-mutating 버전에서 mutating 버전을 생성하거나
- mutating 버전에서 non-mutating 버전을 생성하고
- 둘 사이 semantic requirement를 둬서
compiler가 안전하게 substitution하도록 만들려 한다.

이건 아주 중요하다.
이 proposal의 본질은 편의 문법보다
"표면 API 쌍에 optimizer가 신뢰할 수 있는 의미를 부여하자"에 가깝기 때문이다.

### 4. chained expression을 temporary + in-place mutation으로 바꿀 수 있길 원한다
문서가 드는 대표 예시는
연속된 `intersect()` 호출 같은 non-mutating chain을
내부 temporary와 in-place mutation으로 재작성하는 것이다.

핵심 의도:
- 사용자는 선언적/표현적인 코드를 쓴다
- compiler는 필요하면 더 파괴적인 내부 형태로 lowering한다
- 단, 의미가 같다는 보장이 있을 때만

이건 이후 Swift가 계속 씨름한 문제와 직접 닿아 있다.
- value semantics 보존
- COW uniqueness
- accessor/writeback 비용
- `inout`와 exclusivity

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. COW / ownership 축
이 proposal을 읽으면 가장 먼저 떠오르는 연결은 여기다.
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[swift-ownership-memory-model]]
- [[official-docs/value-reference-types-to-sil-ownership]]

왜냐하면 non-mutating chain을 mutating lowering으로 바꾸는 문제는
결국 값 의미론과 COW 보장을 어디까지 compiler가 활용할 수 있는가의 문제이기 때문이다.

### 2. writeback / accessors / `inout` 축
실제 구현 비용은 getter/setter/writeback/accessor 모델에서 크게 드러난다.
- [[proposal-initialization-and-accessors-to-property-model]]
- [[sil-memory-access]]
- [[sil-initializer-conventions]]

즉 이 proposal은
property/subscript를 단순 getter/setter로 볼 때 왜 비용이 커지는지로도 이어진다.

### 3. optimizer-friendly stdlib surface 축
Array/String/Set 같은 값 타입 API가 왜 이런 표면을 가지는지 읽을 때도 도움이 된다.
- [[high-level-sil-optimizations]]
- [[optimizer-design]]
- [[standard-library-runtime-and-compiler]]

## 이 proposal을 읽을 때의 주의점

- `.=union` 같은 문법 자체가 현재 Swift 표면에 남아 있다고 보면 안 된다.
- proposal의 핵심은 문법 채택 여부보다, mutating/non-mutating 쌍을 compiler가 의미적으로 활용할 수 있느냐에 있다.
- 즉 이 문서는 현재 Swift API design, `mutating`, writeback, COW 최적화의 역사적 실험으로 읽는 편이 좋다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/Inplace.rst`
- `swift/docs/proposals/InoutCOWOptimization.rst`
- `swift/docs/proposals/Accessors.rst`
- `swift/docs/HighLevelSILOptimizations.rst`
- `swift/docs/SIL/SILMemoryAccess.md`

현재 위키 연결:
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[sil-memory-access]]
- [[high-level-sil-optimizations]]
- [[optimizer-design]]

## 추천 읽기 순서

1. [[proposal-in-place-operations-to-writeback-and-cow]]
2. [[proposal-value-semantics-and-cow-to-ownership]]
3. [[proposal-initialization-and-accessors-to-property-model]]
4. [[sil-memory-access]]
5. [[high-level-sil-optimizations]]
6. [[optimizer-design]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[swift-ownership-memory-model]]
- [[official-docs/value-reference-types-to-sil-ownership]]
- [[sil-memory-access]]
- [[high-level-sil-optimizations]]
- [[standard-library-runtime-and-compiler]]
- [[keyword-network]]
