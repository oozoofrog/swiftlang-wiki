---
type: reference
category: learning
tags: [swift, proposal, initialization, accessors, property-model, sil]
aliases: [Initialization/Accessors proposal 교차 읽기, initialization and accessors to property model]
sources: [swiftlang-swift/docs/proposals/Initialization.rst, swiftlang-swift/docs/proposals/Accessors.rst]
---

# Initialization / Accessors proposals → property model 교차 읽기

이 페이지는 `swift/docs/proposals/Initialization.rst`와
`swift/docs/proposals/Accessors.rst`를
현재 Swift의 initializer 규약, property model, writeback, memory access, SIL 관점으로 다시 읽는 교차 페이지다.

## 왜 이 두 proposal을 같이 봐야 하나

겉으로 보기엔
- 하나는 초기화(init)
- 하나는 accessor/getter/setter
문서처럼 보인다.

하지만 실제로 둘은 같은 큰 문제를 만진다.

- 객체와 값이 언제 “완전히 초기화된 것”인가?
- property / subscript 접근을 getter/setter로만 모델링하면 어떤 비용이 생기는가?
- writeback, `inout`, COW, subobject access, definite initialization은 어떻게 이어지는가?

즉 이 두 문서는 현재 Swift property model과 메모리 접근 모델의 역사적 배경이다.

## Initialization.rst의 핵심 포인트

### 1. two-phase initialization
문서는 Swift의 class initialization을
두 단계 초기화 모델로 본다.

핵심 포인트:
- subclass stored property를 먼저 초기화
- 그 다음 `super.init`
- peer delegation과 superclass delegation을 구분
- partially initialized object 정리를 명시적으로 다룸

이건 현재 다음 페이지와 직접 이어진다.

- [[failable-initializers]]
- [[sil-initializer-conventions]]
- [[type-checker]]

### 2. initializer inheritance / virtual initializer 문제
이 proposal은 initializer inheritance, peer delegation, protocol requirement initializer,
ObjC entrypoint와 dynamic dispatch 문제를 꽤 넓게 다룬다.

오늘날 세부 구현은 proposal 당시와 달라졌더라도,
“initializer는 단순 함수가 아니라 object construction rule”이라는 감각은 그대로 중요하다.

### 3. Objective-C interop와 초기화 모델 충돌
문서의 흥미로운 점은
Swift 초기화 soundness와 ObjC initialization entrypoint의 차이를 함께 본다는 점이다.
그래서 initialization proposal은 순수 init 문서가 아니라
interop 문서이기도 하다.

관련 페이지:
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[objc-interop]]

## Accessors.rst의 핵심 포인트

### 1. getter/setter만으로는 부족하다
이 문서는 abstract storage access를
full-value load/store만으로 처리하면 생기는 문제를 아주 길게 분석한다.

대표 문제:
- subobject clobbering
- writeback 비용
- abstraction barrier 때문에 optimizer가 보수적이 됨
- COW 값에서 구조적 복사가 강제됨

즉 accessors proposal은
현재 [[sil-memory-access]]와 [[proposal-value-semantics-and-cow-to-ownership]]로 이어지는 핵심 역사 문서다.

### 2. property model은 성능 문제이기도 하다
문서는 property / subscript / abstract storage를
단순 문법 설계가 아니라 optimization / aliasing / memory safety 문제로 다룬다.

특히 다음 축과 강하게 연결된다.
- [[sil-memory-access]]
- [[sil-ownership]]
- [[standard-library-runtime-and-compiler]]

### 3. resilient / abstract / overridable storage 문제
문서는 protocol member, non-final class member, resilient declaration처럼
구현을 정적으로 알 수 없는 storage를 보수적으로 접근해야 한다고 본다.
이 점은 ABI / resilience / accessor design을 같이 보게 만든다.

관련 페이지:
- [[library-evolution]]
- [[abi-stability]]

## 현재 구현과 어떻게 이어 읽으면 좋은가

### initialization 축
- [[failable-initializers]]
- [[sil-initializer-conventions]]
- [[type-checker]]

### storage / access 축
- [[sil-memory-access]]
- [[sil-ownership]]
- [[proposal-value-semantics-and-cow-to-ownership]]

### stdlib/runtime 축
- [[standard-library-runtime-and-compiler]]
- [[runtime]]

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/Initialization.rst`
- `swift/docs/proposals/Accessors.rst`
- `swift/docs/SIL/SILInitializerConventions.md`
- `swift/docs/SIL/SILMemoryAccess.md`

현재 위키 연결:
- [[failable-initializers]]
- [[sil-initializer-conventions]]
- [[sil-memory-access]]
- [[sil-ownership]]
- [[type-checker]]

## 이 문서를 읽을 때 주의할 점

- proposal의 세부 syntax/attribute 제안이 지금과 동일하다고 보면 안 된다.
- 하지만 “초기화와 storage access를 soundness + performance 문제로 본다”는 핵심은 지금도 그대로 중요하다.
- 그래서 현재 구현 페이지와 같이 읽을 때 가치가 크다.

## 추천 읽기 순서

1. [[proposal-initialization-and-accessors-to-property-model]]
2. [[failable-initializers]]
3. [[sil-initializer-conventions]]
4. [[sil-memory-access]]
5. [[proposal-value-semantics-and-cow-to-ownership]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[failable-initializers]]
- [[sil-initializer-conventions]]
- [[sil-memory-access]]
- [[sil-ownership]]
- [[keyword-network]]
