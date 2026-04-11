---
type: reference
category: learning
tags: [swift, proposal, c-interop, bridging, importer, c-export]
aliases: [AttrC proposal 교차 읽기, c export and bridging to importer]
sources: [swiftlang-swift/docs/proposals/AttrC.rst]
---

# AttrC proposal → C export / bridging / importer 교차 읽기

이 페이지는 `swift/docs/proposals/AttrC.rst`를
현재 Swift의 C interop, C export, type bridging, header generation 문맥으로 다시 읽는 교차 페이지다.

## 이 proposal이 다루는 핵심 문제

이 문서는 Swift가 단지 C를 "가져오는" 데서 끝나지 않고,
반대로 Swift 선언을 pure C entry point로 노출하려면 어떤 제약이 필요한지를 다룬다.

핵심 질문:
- Swift top-level function / struct / enum을 C에 어떻게 내보낼 것인가?
- 어떤 타입만 C ABI에 안전하게 놓을 수 있는가?
- Darwin과 Linux에서 브리징 규칙은 어떻게 달라지는가?
- generated header / PrintAsClang 계열은 어떤 역할을 해야 하는가?

즉 이 proposal은 현재 [[how-swift-imports-c-apis]]와 [[clang-importer]]를
“가져오기(import)”뿐 아니라 “내보내기(export)” 축까지 확장해서 보게 해 준다.

## proposal의 핵심 포인트

### 1. `@c`는 `@objc`의 부분집합/사촌 같은 개념이다
문서는 `@c` attribute를 제안한다.
적용 대상:
- top-level functions
- non-generic class의 static method
- enum
- struct

핵심 의도는
ObjC runtime을 전제하지 않고도,
Swift 선언을 더 C다운 표면으로 노출하는 것이다.

### 2. C에 내보낼 수 있는 타입은 훨씬 더 좁다
proposal은 type bridging을
POD / non-POD 관점으로 다시 정리한다.

브리지 가능한 POD 예:
- integer
- floating point
- `@c` enum
- fixed-size array
- `@c` struct (모든 필드가 POD)
- pointers to C types
- `@convention(c)` function type

즉 이 문서는 C export를 단순 문법 속성이 아니라
ABI / layout / ownership 제약 문제로 본다.

### 3. Darwin vs Linux 차이를 매우 의식한다
proposal이 흥미로운 지점 중 하나는
Darwin에서는 일부 reference-counted pointer passing을 허용할 여지가 있지만,
Linux에서는 Objective-C 계열이 없으므로 훨씬 더 보수적으로 간다는 점이다.

즉 C interop 설계는 곧 플랫폼 모델 문제이기도 하다.

### 4. generated header와 importer는 같은 축의 양면이다
문서는 `PrintAsObjC` 재사용과 pure-C header generation을 언급한다.
이건 아주 중요하다.

- importer는 C 선언을 Swift 쪽으로 들여오고
- generated header / print-as-clang 계열은 Swift 선언을 C 쪽으로 내보낸다

즉 이 proposal은 Clang Importer를 단방향 번역기가 아니라
양방향 언어 경계 장치처럼 보게 만든다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. C API import / Clang Importer
가장 직접적인 연결:
- [[how-swift-imports-c-apis]]
- [[clang-importer]]
- [[c-to-swift-name-translation]]

### 2. calling convention / ABI 축
C export는 결국 calling convention, layout, symbol 이름과 만난다.
그래서 다음 페이지와도 이어진다.
- [[abi-calling-convention]]
- [[abi-mangling]]

### 3. ObjC interop와의 차이
`@c` proposal은 `@objc`와 닮았지만,
ObjC runtime / selector / category / dynamic replacement를 전제하지 않는다는 점에서 다르다.
그래서 다음 페이지와 비교해서 읽는 것이 좋다.
- [[objc-interop]]
- [[proposal-objc-interop-to-importer-and-dispatch]]

## proposal을 읽을 때 주의할 점

- proposal 속성 이름과 세부 규칙이 오늘날 그대로 남아 있다고 보면 안 된다.
- 하지만 Swift가 “C 친화적 ABI surface”를 어떻게 상상했는지는 매우 잘 보여 준다.
- 특히 Linux 포팅/시스템 프레임워크 이전 같은 현실적 동기가 드러난다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/AttrC.rst`
- `swift/lib/PrintAsClang/`
- `swift/lib/ClangImporter/`
- `swift/include/swift/SIL/` / calling convention 관련 축

현재 위키 연결:
- [[how-swift-imports-c-apis]]
- [[clang-importer]]
- [[c-to-swift-name-translation]]
- [[objc-interop]]
- [[abi-calling-convention]]
- [[abi-mangling]]

## 추천 읽기 순서

1. [[proposal-c-export-and-bridging-to-importer]]
2. [[how-swift-imports-c-apis]]
3. [[clang-importer]]
4. [[c-to-swift-name-translation]]
5. [[proposal-objc-interop-to-importer-and-dispatch]]
6. [[abi-calling-convention]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[how-swift-imports-c-apis]]
- [[clang-importer]]
- [[c-to-swift-name-translation]]
- [[objc-interop]]
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[abi-calling-convention]]
- [[keyword-network]]
