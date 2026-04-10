---
type: reference
category: learning
tags: [swift, proposal, constructors, class-construction, objc, initialization]
aliases: [Constructors/ClassConstruction proposal 교차 읽기, constructors and class construction to init model]
sources: [swiftlang-swift/docs/proposals/rejected/Constructors.rst, swiftlang-swift/docs/proposals/rejected/ClassConstruction.rst]
---

# Constructors / ClassConstruction proposals → 현대 init 모델 교차 읽기

이 페이지는 rejected proposal인
`swift/docs/proposals/rejected/Constructors.rst`와
`swift/docs/proposals/rejected/ClassConstruction.rst`를
현재 Swift의 initialization soundness, designated/convenience 모델, Objective-C interop 제약 관점으로 다시 읽는 교차 페이지다.

## 이 rejected proposal 묶음이 중요한 이유

두 문서는 rejected 되었지만,
오늘날 Swift 초기화 모델이 왜 지금 형태가 되었는지를 이해하는 데 매우 중요하다.

핵심 질문:
- Objective-C식 `alloc` + `init` 세계를 Swift가 그대로 받아들일 수 있는가?
- constructor delegation은 얼마나 허용해야 sound한가?
- superclass initializer를 subclass에 자동 노출하면 어떤 문제가 생기는가?

즉 이 문서들은
현재 init 모델의 “부정형 역사”를 보여 준다.
무엇이 채택되지 않았는지를 봐야 현재 규칙의 의도가 더 선명해진다.

## Constructors.rst의 핵심 포인트

### 1. allocation과 initialization을 한 함수로 본다
문서는 Swift constructor를
Objective-C처럼 `alloc`와 `init`를 나누지 않고,
한 번에 allocation + initialization을 수행하는 모델로 본다.

이건 오늘날 Swift 사용자가 매우 당연하게 느끼는 부분이지만,
당시에는 Objective-C 초기화 모델과 대비되는 큰 선택이었다.

### 2. Objective-C two-phase initialization의 위험을 직접 다룬다
문서는 superclass `init` 중에 subclass method가 호출될 수 있는 문제,
즉 partially initialized object에 대한 dynamic dispatch 위험을 예시로 보여 준다.
이 문제의식은 지금 봐도 여전히 핵심이다.

### 3. designated initializer pattern은 편의가 아니라 soundness 대응이다
rejected proposal이지만,
문서는 designated/secondary initializer 패턴이 왜 등장했는지 매우 잘 설명한다.
즉 이 문서는 final design은 아니어도
문제 자체를 가장 교육적으로 보여 주는 자료다.

## ClassConstruction.rst의 핵심 포인트

### 1. superclass `init`를 기본 공개 인터페이스로 두지 말자는 문제의식
이 proposal은 Objective-C의 가장 큰 문제로
superclass `init`가 자동으로 subclass 생성 API가 되어 버리는 점을 지적한다.

그 결과:
- subclass invariant가 깨질 수 있다
- 모든 superclass initializer를 override해야 한다
- base class에 init를 추가하면 subclass가 사실상 깨질 수 있다

이건 오늘날 Swift가 왜 초기화 surface를 더 엄격하게 다루는지를 이해하는 데 매우 중요하다.

### 2. `self.init`의 virtual dispatch를 경계한다
proposal은 constructor delegation에서 virtual dispatch를 허용하면
soundness가 크게 흔들린다고 본다.
이 점은 initializer inheritance proposal과도 맞닿는다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. 현재 init 규약
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[proposal-initialization-and-accessors-to-property-model]]

### 2. inheritance와 soundness
- [[proposal-initializer-inheritance-to-modern-init-model]]

### 3. Objective-C interop
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[objc-interop]]

## 이 rejected proposal들을 오늘 어떻게 읽어야 하나

- “이 아이디어가 rejected 되었으니 무가치하다”가 아니라
- “어떤 위험 때문에 지금 규칙이 더 보수적으로 굳어졌는가”를 보는 편이 좋다.

즉 이 두 문서는
현재 init 모델의 rationale 문서처럼 읽을 수 있다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/rejected/Constructors.rst`
- `swift/docs/proposals/rejected/ClassConstruction.rst`
- `swift/docs/proposals/Initialization.rst`
- `swift/docs/proposals/InitializerInheritance.rst`

현재 위키 연결:
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-initializer-inheritance-to-modern-init-model]]
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[proposal-objc-interop-to-importer-and-dispatch]]

## 추천 읽기 순서

1. [[proposal-constructors-and-class-construction-to-init-model]]
2. [[proposal-initialization-and-accessors-to-property-model]]
3. [[proposal-initializer-inheritance-to-modern-init-model]]
4. [[sil-initializer-conventions]]
5. [[failable-initializers]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-initializer-inheritance-to-modern-init-model]]
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[objc-interop]]
- [[keyword-network]]
