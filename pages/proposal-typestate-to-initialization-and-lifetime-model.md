---
type: reference
category: learning
tags: [swift, proposal, typestate, lifetime, initialization, ownership]
aliases: [TypeState proposal 교차 읽기, typestate to initialization and lifetime model, typestate proposal]
sources: [swiftlang-swift/docs/proposals/TypeState.rst]
---

# TypeState proposal → 초기화 / lifetime / ownership 경계 교차 읽기

이 페이지는 `swift/docs/proposals/TypeState.rst`를
현재 Swift의 initialization soundness, lifetime, invalidation, ownership 경계 문맥으로 다시 읽는 교차 페이지다.

## 이 proposal이 다루는 핵심 문제

문서는 전형적인 typestate 질문을 다룬다.

- 어떤 객체가 open/closed, valid/invalid 같은 상태를 타입 차원에서 가질 수 있는가?
- 메서드는 `self`나 by-ref 인자의 상태 전이를 계약으로 표현할 수 있는가?
- invalid object 접근 같은 실수를 language/runtime가 더 잘 막을 수 있는가?
- 상태 전이가 aliasing, ownership, ARC/GC와 만나면 어떤 비용이 생기는가?

즉 이 proposal은
Swift가 first-class typestate 문법을 채택하지 않았더라도,
상태 전이와 수명 경계 문제를 어디서 계속 마주쳤는지를 보여 주는 역사 문서다.

## TypeState.rst의 핵심 포인트

### 1. typestate는 곧 "유효한 상태 공간" 문제다
문서는 파일의 open/closed 상태,
객체 invalidation,
immutable 전이 같은 예시를 통해
값/객체가 언제 어떤 연산을 허용하는지를 상태로 기술하려 한다.

핵심 감각:
- 단순 타입만으로는 표현되지 않는 protocol of use가 있다
- 어떤 API는 호출 순서와 상태 전이에 강하게 의존한다
- 그 제약을 런타임 assert가 아니라 더 정적인 모델로 표현하고 싶다

### 2. invalidation과 ownership 모델이 매우 가깝다
문서의 DVTInvalidation 사례는 특히 중요하다.

핵심 문제:
- 객체는 메모리상 살아 있어도 "이미 끝난(done)" 상태일 수 있다
- useful lifetime과 physical lifetime이 어긋날 수 있다
- single-owner가 useful lifetime을 통제해야 하는데, alias가 남아 있으면 상태 규칙이 흐려진다

이건 typestate가 단순 학술 개념이 아니라
ownership discipline과 직접 맞닿는다는 뜻이다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[sil-ownership]]
- [[runtime]]

### 3. 상태 전이는 precondition/postcondition 계약을 요구한다
문서는
`open() [ClosedFile>>OpenFile]` 같은 표기를 상상하며,
메서드가 호출 전후에 `self` 상태를 어떻게 바꾸는지 계약으로 적고 싶어 한다.

이 문제의식은 지금도 여전히 중요하다.
- 초기화 전/후 상태
- partially initialized object
- consumed / borrowed / invalidated value
- actor isolation이나 sendability 같은 사용 가능성 경계

즉 typestate 문서는
상태 전이 계약을 언어가 어디까지 표면화해야 하는가를 묻는다.

### 4. typestate는 ADT / discriminated union과도 닿아 있다
문서는 Plaid의 예를 들며
상태 전이가 representation 자체를 바꿀 수 있고,
공통 데이터 + 상태별 데이터가 섞인 모델은 discriminated union과도 닮아 있다고 본다.

그래서 typestate는
초기화/lifetime 문제이면서,
다른 한편으로는 "상태를 가진 ADT" 문제이기도 하다.

관련 페이지:
- [[proposal-enums-and-enum-style-to-type-system-and-layout]]
- [[abi-type-layout]]

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. initialization soundness 축
Swift에서 typestate에 가장 가까운 강한 compiler 규칙 중 하나는 초기화 모델이다.
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-initializer-inheritance-to-modern-init-model]]
- [[proposal-constructors-and-class-construction-to-init-model]]
- [[failable-initializers]]

여기서는
"완전히 초기화되었는가"
"부분 초기화 상태에서 무엇이 가능한가"
같은 질문이 사실상 state transition 문제로 다뤄진다.

### 2. memory access / ownership 축
typestate는 결국 aliasing과 ownership을 피할 수 없다.
- [[swift-ownership-memory-model]]
- [[sil-memory-access]]
- [[sil-ownership]]

특히 exclusivity와 borrow scope는
"지금 이 값/주소를 어떤 방식으로 써도 되는가"를 제한한다는 점에서
약한 형태의 state discipline처럼 읽을 수 있다.

### 3. concurrency / isolation 축
직접적인 typestate 문법은 아니지만,
사용 가능성과 이동 가능성 경계를 정적으로 제한한다는 점에서
동시성 규칙과도 닿는다.
- [[swift-actor-isolation-and-sendable]]
- [[concurrency-data-race-safety]]

다만 이것을 typestate의 직접 후계로 단정하면 과장이다.
더 정확히는 같은 계열의 "사용 가능성 제약" 문제를 다룬다고 보는 편이 맞다.

## 이 proposal을 읽을 때 주의할 점

- Swift가 이 문서의 typestate surface syntax를 실제 언어 기능으로 채택했다고 보면 안 된다.
- Plaid-style state transition model이 Swift에 그대로 들어온 것도 아니다.
- 하지만 initialization, invalidation, ownership, useful lifetime 같은 문제를 어떤 언어 층에서 다뤄야 하는지는 지금도 매우 중요한 질문이다.

즉 이 문서는
현재 Swift의 기능 설명서라기보다,
Swift가 상태 전이와 수명 경계를 어떤 언어 문제로 인식했는지 보여 주는 설계 메모에 가깝다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/TypeState.rst`
- `swift/docs/proposals/Initialization.rst`
- `swift/docs/OwnershipManifesto.md`
- `swift/docs/SIL/SILMemoryAccess.md`
- `swift/docs/SIL/SILInitializerConventions.md`

현재 위키 연결:
- [[swift-ownership-memory-model]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[failable-initializers]]
- [[sil-memory-access]]
- [[sil-ownership]]

## 추천 읽기 순서

1. [[proposal-typestate-to-initialization-and-lifetime-model]]
2. [[proposal-initialization-and-accessors-to-property-model]]
3. [[failable-initializers]]
4. [[swift-ownership-memory-model]]
5. [[sil-memory-access]]
6. [[sil-ownership]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-initializer-inheritance-to-modern-init-model]]
- [[proposal-constructors-and-class-construction-to-init-model]]
- [[failable-initializers]]
- [[swift-ownership-memory-model]]
- [[sil-memory-access]]
- [[sil-ownership]]
- [[swift-actor-isolation-and-sendable]]
- [[concurrency-data-race-safety]]
- [[keyword-network]]
