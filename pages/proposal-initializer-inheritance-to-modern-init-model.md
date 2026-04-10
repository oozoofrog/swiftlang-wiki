---
type: reference
category: learning
tags: [swift, proposal, initializer-inheritance, init, class-design]
aliases: [Initializer Inheritance proposal 교차 읽기, initializer inheritance to modern init model]
sources: [swiftlang-swift/docs/proposals/InitializerInheritance.rst]
---

# Initializer Inheritance proposal → 현대 init 모델 교차 읽기

이 페이지는 `swift/docs/proposals/InitializerInheritance.rst`를
현재 Swift의 designated/convenience initializer 모델, inheritance 규칙, soundness 제약 관점으로 다시 읽는 교차 페이지다.

## 이 proposal이 던지는 핵심 질문

이 문서는 아주 직접적인 질문을 다룬다.

- initializer는 method처럼 상속되어야 하는가?
- `self.init`, `super.init`, dispatched initialization은 어떻게 구분해야 하는가?
- subclass가 superclass의 initializer를 물려받는 것이 언제 sound한가?

즉 이 proposal은
오늘날 Swift 초기화 모델의 가장 민감한 부분인
“상속 가능한 초기화와 soundness”를 설계 차원에서 설명하는 역사 문서다.

## proposal의 핵심 포인트

### 1. subobject initializer vs complete object initializer
문서는 initializer를 두 종류로 나눠서 본다.

- subobject initializer
- complete object initializer

핵심 아이디어는
초기화 책임이 “내 타입의 부분만 채우는가”와
“가장 파생된 객체 전체를 sound하게 만들어 내는가”를 분리해서 봐야 한다는 점이다.

이 구분은 지금의 구현 용어와 완전히 같지는 않지만,
현재의 designated / convenience 구분을 더 근본적으로 이해하게 해 준다.

### 2. delegation 종류를 셋으로 본다
문서는 delegation을
- super
- peer
- dispatched
세 종류로 나눈다.

특히 `dispatched` initialization을 별도 개념으로 세우는 점이 중요하다.
왜냐하면 soundness 문제는 결국
“가장 파생된 클래스가 어떤 initializer를 실제로 제공하는가”로 돌아가기 때문이다.

### 3. initializer inheritance는 무조건 편의 기능이 아니다
proposal은 initializer inheritance를 단순 보일러플레이트 제거 기능으로 보지 않는다.
오히려 잘못 허용하면 initialization soundness를 깨뜨릴 수 있다고 본다.
그래서 “언제 상속 가능한가”를 굉장히 엄격하게 다룬다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. designated / convenience initializer 모델
현재 위키에서 가장 직접적으로 이어지는 페이지:
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[proposal-initialization-and-accessors-to-property-model]]

### 2. initializer inheritance가 왜 제한적인가
오늘날 Swift는 Objective-C처럼 모든 initializer가 자연스럽게 상속되는 모델이 아니다.
proposal을 읽고 나면 이게 단순 불편이 아니라
객체 soundness와 API surface 문제라는 점이 보인다.

### 3. Objective-C interop와의 긴장
initializer inheritance proposal은
결국 ObjC initialization 습관과 Swift soundness 사이의 타협 문제이기도 하다.

관련 페이지:
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[objc-interop]]

## proposal을 읽을 때의 핵심 관찰

### soundness를 호출 시점에서 보려 한다
문서는 어떤 initializer 정의 자체보다도,
그 initializer가 어떤 동적 클래스에서 호출될 수 있는지를 중요하게 본다.
이건 method override와는 다른 initialization 특수성이다.

### virtual initializer 아이디어
proposal은 true virtual initializer 같은 개념도 논의한다.
오늘날 그대로 읽으면 안 되지만,
왜 metatype construction / inherited init / protocol init requirement가 어려운지 보여 준다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/InitializerInheritance.rst`
- `swift/docs/proposals/Initialization.rst`
- `swift/docs/SIL/SILInitializerConventions.md`

현재 위키 연결:
- [[proposal-initialization-and-accessors-to-property-model]]
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[objc-interop]]

## 추천 읽기 순서

1. [[proposal-initialization-and-accessors-to-property-model]]
2. [[proposal-initializer-inheritance-to-modern-init-model]]
3. [[sil-initializer-conventions]]
4. [[failable-initializers]]
5. [[proposal-constructors-and-class-construction-to-init-model]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-constructors-and-class-construction-to-init-model]]
- [[sil-initializer-conventions]]
- [[failable-initializers]]
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[keyword-network]]
