---
type: reference
category: learning
tags: [swift, proposal, c-interop, pointers, unsafe-pointer, importer]
aliases: [C pointer interop proposal 교차 읽기, c pointer interop to unsafe pointer model]
sources: [swiftlang-swift/docs/proposals/CPointerInteropLanguageModel.rst, swiftlang-swift/docs/proposals/CPointerArgumentInterop.rst]
---

# C pointer interop proposals → UnsafePointer 모델 교차 읽기

이 페이지는
`swift/docs/proposals/CPointerInteropLanguageModel.rst`와
`swift/docs/proposals/CPointerArgumentInterop.rst`를
현재 Swift의 `UnsafePointer` 계열, `inout`, array-to-pointer, C argument bridging 문맥으로 다시 읽는 교차 페이지다.

## 왜 이 proposal 묶음이 중요한가

Swift의 C interop에서 가장 자주 체감되는 부분 중 하나가 pointer 규칙이다.
이 문서들은 바로 그 사용자 모델을 어떻게 언어에 굳힐지 다룬다.

핵심 질문:
- pointer user model을 implicit conversion 위에 둘 것인가, 언어 규칙으로 승격할 것인가?
- `UnsafePointer`, `UnsafeMutablePointer`, autoreleasing pointer는 어떤 의미를 가져야 하는가?
- `inout`, array, string, nil이 pointer argument로 어떻게 변환되어야 하는가?
- lifetime extension, writeback, COW uniqueness는 어디서 책임져야 하는가?

즉 이 proposal 묶음은
오늘날 Swift의 C pointer interop 감각의 설계 근거다.

## CPointerInteropLanguageModel.rst의 핵심 포인트

### 1. bridging pointer type 난립을 정리하려 한다
문서는 기존 bridging pointer type과 user-facing pointer type이 섞여 있는 상황을 문제로 본다.
그 해결 방향은
- 한 세트의 plain pointer types를 두고
- function argument context가 특별한 변환 규칙을 가지게 하는 것
이다.

이 점은 지금의 `UnsafePointer` 계열 모델을 이해하는 데 핵심이다.

### 2. pointer argument conversion은 호출 문맥의 능력이다
이 문서는 pointer conversion을 단순 타입 변환이 아니라
function application이 가진 특별한 능력으로 설명한다.
그래서
- `&x`
- `&array`
- `nil`
- `String`
같은 것이 어떤 pointer parameter에서 허용되는지가 매우 문맥적이다.

### 3. ownership / writeback / autoreleasing 문제를 다룬다
특히 ObjC object pointer의 `**` 계열과
`AutoreleasingUnsafeMutablePointer` 모델은
단순 C pointer가 아니라 ARC/writeback 문제와 이어진다.

이건 현재 다음 페이지와 같이 보면 더 잘 보인다.
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[proposal-initialization-and-accessors-to-property-model]]

## CPointerArgumentInterop.rst의 핵심 포인트

### 1. const pointer vs non-const pointer를 다르게 취급한다
문서는
- const pointer는 in array / inout scalar / pointer value
- non-const C pointer는 inout array / inout scalar / mutable pointer
- ObjC object pointer는 scalar inout 또는 nil
같은 식으로 사용 모델을 세분화한다.

즉 pointer interop는 “모두 UnsafePointer로 통일”이 아니라,
mutability / ownership / lifetime을 반영한 호출 규칙의 집합으로 설계된다.

### 2. array-to-pointer와 COW uniqueness
문서는 mutable pointer argument에 배열을 넘길 때
copy-on-write buffer를 미리 unique하게 만들어야 한다고 본다.
이건 pointer interop가 곧 ownership / COW 문제라는 점을 보여 준다.

관련 페이지:
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[swift-ownership-memory-model]]

### 3. inout address conversion / writeback conversion / interior pointer conversion
이 문서는 pointer passing을 위해
언어/stdlib 차원의 특수 conversion 메커니즘을 제안한다.
즉 C interop는 단순 importer 규칙이 아니라
언어 evaluation / lifetime model과 직접 엮여 있다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. C API import 기본 축
- [[how-swift-imports-c-apis]]
- [[clang-importer]]

### 2. memory access / ownership 축
pointer interop는 메모리 안전성과 분리해서 볼 수 없다.
- [[sil-memory-access]]
- [[sil-ownership]]
- [[swift-ownership-memory-model]]

### 3. property model / writeback 축
`inout` writeback과 pointer conversion은 매우 가깝다.
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-value-semantics-and-cow-to-ownership]]

## proposal을 읽을 때 주의할 점

- proposal 속 bridging pointer type 이름이 오늘날 표면 모델과 정확히 같지는 않을 수 있다.
- 하지만 왜 지금의 `UnsafePointer` user model이 문맥적 규칙을 많이 가지는지는 아주 잘 설명한다.
- 즉 이 문서들은 현재 unsafe pointer ergonomics의 역사 문서다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/CPointerInteropLanguageModel.rst`
- `swift/docs/proposals/CPointerArgumentInterop.rst`
- `swift/stdlib/public/core/` pointer 관련 표면 타입 축

현재 위키 연결:
- [[how-swift-imports-c-apis]]
- [[clang-importer]]
- [[sil-memory-access]]
- [[sil-ownership]]
- [[swift-ownership-memory-model]]
- [[proposal-value-semantics-and-cow-to-ownership]]

## 추천 읽기 순서

1. [[proposal-c-pointer-interop-to-unsafe-pointer-model]]
2. [[how-swift-imports-c-apis]]
3. [[clang-importer]]
4. [[proposal-value-semantics-and-cow-to-ownership]]
5. [[sil-memory-access]]
6. [[swift-ownership-memory-model]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[proposal-c-export-and-bridging-to-importer]]
- [[how-swift-imports-c-apis]]
- [[clang-importer]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[sil-memory-access]]
- [[sil-ownership]]
- [[keyword-network]]
