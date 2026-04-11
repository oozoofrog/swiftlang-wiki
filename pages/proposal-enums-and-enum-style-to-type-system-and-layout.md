---
type: reference
category: learning
tags: [swift, proposal, enums, adt, rawrepresentable, layout]
aliases: [Enums proposal 교차 읽기, EnumStyle proposal 교차 읽기, enums and enum style to type system and layout]
sources: [swiftlang-swift/docs/proposals/Enums.rst, swiftlang-swift/docs/proposals/EnumStyle.rst]
---

# Enums / EnumStyle proposals → 타입 시스템 / API 표면 / 레이아웃 교차 읽기

이 페이지는 `swift/docs/proposals/Enums.rst`와
`swift/docs/proposals/EnumStyle.rst`를
현재 Swift의 enum 모델, `RawRepresentable`, pattern matching, API 표면, ABI 레이아웃 문맥으로 다시 읽는 교차 페이지다.

## 왜 이 proposal 묶음을 같이 봐야 하나

이 두 문서는 모두 enum을
단순한 "정수 상수 묶음"이 아니라
Swift 타입 시스템의 핵심 값 모델로 다룬다.

핵심 질문:
- Swift enum은 C enum의 연장인가, algebraic data type(ADT)인가?
- payload case와 no-payload case는 어떤 사용자 모델을 가져야 하는가?
- case 이름, case 생성, pattern matching은 다른 Swift API 표면과 얼마나 비슷해야 하는가?
- enum 표면 모델은 layout / raw value / importer와 어떻게 이어지는가?

즉 이 proposal 묶음은
오늘날 Swift enum이
ADT, API surface, ABI layout, importer 감각이 만나는 지점이라는 사실을 잘 보여 준다.

## Enums.rst의 핵심 포인트

### 1. Swift enum을 ADT로 전면화한다
문서는 Swift enum을
C식 symbolic enum에 payload를 얹은 정도가 아니라,
열거형과 union을 안전하게 결합한 ADT로 설명한다.

핵심 의도:
- enum은 닫힌 variant set을 나타낸다
- payload를 통해 각 case가 다른 값을 품을 수 있다
- `switch`는 그 variant를 안전하게 해체하는 기본 도구다

이건 현재 Swift가 `Optional`, `Result`, 사용자 정의 sum type을 어떻게 설명하는지의 뿌리에 가깝다.

### 2. `enum`이라는 이름 자체를 ADT 소개 전략으로 쓴다
문서는 왜 `union`이 아니라 `enum`이라는 이름을 썼는지 길게 설명한다.

중요한 감각은 이것이다.
- C 사용자에게 가장 익숙한 진입점은 `enum` + `switch`다
- Swift는 그 익숙한 표면에서 시작해 payload case와 pattern matching으로 확장한다
- 즉 새 개념을 완전히 새 이름으로 들이밀기보다, 익숙한 문맥에서 확장한다

이건 언어 설계와 교육 전략이 한 몸이라는 걸 보여 준다.

### 3. `RawRepresentable` 축이 이미 같이 등장한다
문서는 전통적인 C enum과 raw type의 관계를
library-side `RawRepresentable`로 설명한다.

즉 Swift enum은 처음부터 두 층을 같이 가진다.
- ADT로서의 풍부한 enum
- raw value를 가진 imported/bridged enum

이 구분은 현재 다음 페이지와 직접 이어진다.
- [[how-swift-imports-c-apis]]
- [[proposal-option-sets-to-importer-and-layout]]
- [[abi-type-layout]]

## EnumStyle.rst의 핵심 포인트

### 1. case naming은 단순 취향 문제가 아니다
문서는 enum case가
다른 Swift API 표면과 너무 다르게 느껴진다는 점을 문제로 본다.

대표적으로:
- no-payload case는 property-like하게 lowerCamelCase가 더 자연스럽지 않은가?
- associated-value case는 initializer-like하게 보여야 하지 않는가?
- enum을 쓰기 위해 helper initializer/property boilerplate를 계속 추가해야 하는 건 언어 설계 신호가 아닌가?

즉 이 proposal은 enum style을 naming bikeshed가 아니라
API ergonomics 문제로 본다.

### 2. payload case를 initializer-like surface로 끌어오려 한다
문서는 `case init(success: Wrapped)` 같은 표면을 제안한다.

핵심 의도:
- payload case는 생성자처럼 느껴진다
- 그러면 선언도 사용도 pattern matching도 initializer-like해야 하지 않는가?
- enum case 생성과 match를 다른 function-like declaration과 더 통일할 수 있지 않은가?

오늘날 정확히 이 문법이 채택된 것은 아니지만,
이 문제의식은 여전히 살아 있다.
- `Result.success(...)` / `.success(...)` 같은 감각
- case label ergonomics
- payload access boilerplate

### 3. enum case property화/boilerplate 제거를 요구한다
문서는 associated-value case label에서
암시적 accessor property를 뽑아내는 아이디어까지 논의한다.

이건 결국 다음 질문과 이어진다.
- enum 값을 switch 없이 더 조합적으로 다룰 수는 없는가?
- 패턴 매칭만이 유일한 user model이어야 하는가?
- ADT를 library surface에서 더 다루기 쉽게 만들 수는 없는가?

즉 EnumStyle.rst는 enum의 "표현력"보다
enum의 "일상적 사용성"을 개선하려는 문서다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. 타입 시스템 / ADT 축
가장 직접적인 연결:
- [[swift-type-system]]
- [[dynamic-casting]]
- [[sil-instructions]]

특히 `switch_enum` 같은 SIL 인스트럭션을 떠올리면,
enum이 표면 문법이면서 동시에 control-flow shape를 강하게 규정하는 타입이라는 점이 보인다.

### 2. ABI / layout 축
Swift enum은 예쁜 문법이 아니라 레이아웃 문제이기도 하다.
- [[abi-type-layout]]
- [[abi-type-metadata]]
- [[runtime]]

특히 single-payload / multi-payload enum 구분은
ADT 표면이 실제 메모리 표현까지 이어지는 대표 사례다.

### 3. importer / raw-value 축
raw enum, imported enum, bitmask-like imported surface를 같이 보면 더 잘 보인다.
- [[how-swift-imports-c-apis]]
- [[proposal-option-sets-to-importer-and-layout]]
- [[c-to-swift-name-translation]]

즉 Swift enum은
"순수 ADT"와 "C 계열 imported symbolic type" 두 감각이 계속 교차하는 위치에 있다.

## 이 proposal 묶음을 읽을 때 주의할 점

- `case init(...)` 같은 문법 제안이 현재 Swift 표면과 그대로 일치한다고 보면 안 된다.
- 또한 no-payload case naming 논의도 역사적 맥락을 포함한다.
- 하지만 Swift enum을 ADT로 밀어 올리는 방향,
  그리고 enum case를 더 Swift다운 API surface로 다듬으려는 방향은 아주 중요한 설계 흔적이다.

즉 이 문서들은
현재 enum 모델의 세부 명세서라기보다,
Swift가 enum을 어떤 언어 핵심 구성요소로 만들고 싶어 했는지 보여 주는 역사 문서다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/Enums.rst`
- `swift/docs/proposals/EnumStyle.rst`
- `swift/docs/DynamicCasting.md`
- `swift/docs/SIL/SILInstructions.md`
- `swift/docs/ABI/TypeLayout.rst`

현재 위키 연결:
- [[swift-type-system]]
- [[abi-type-layout]]
- [[how-swift-imports-c-apis]]
- [[proposal-option-sets-to-importer-and-layout]]
- [[sil-instructions]]

## 추천 읽기 순서

1. [[proposal-enums-and-enum-style-to-type-system-and-layout]]
2. [[swift-type-system]]
3. [[abi-type-layout]]
4. [[sil-instructions]]
5. [[how-swift-imports-c-apis]]
6. [[proposal-option-sets-to-importer-and-layout]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[swift-type-system]]
- [[abi-type-layout]]
- [[abi-type-metadata]]
- [[runtime]]
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]
- [[proposal-option-sets-to-importer-and-layout]]
- [[dynamic-casting]]
- [[sil-instructions]]
- [[keyword-network]]
