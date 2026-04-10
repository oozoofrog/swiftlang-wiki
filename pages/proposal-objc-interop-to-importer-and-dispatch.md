---
type: reference
category: learning
tags: [swift, proposal, objc, interop, clang-importer, dispatch]
aliases: [ObjC interop proposal 교차 읽기, ObjC interop to importer/disptach]
sources: [swiftlang-swift/docs/proposals/ObjCInteroperation.rst]
---

# ObjC interop proposal → importer / dispatch 교차 읽기

이 페이지는 `swift/docs/proposals/ObjCInteroperation.rst`를
현재 Swift의 Objective-C interop, Clang Importer, dynamic dispatch 제약 관점으로 다시 읽는 교차 페이지다.

## 이 proposal이 던지는 핵심 질문

이 문서는 단순히 “Swift가 ObjC를 호출할 수 있다”는 수준이 아니라,
Objective-C의 동적 구현 모델을 어디까지 받아들이고 어디서 제약할 것인가를 다룬다.

핵심 질문은 대략 이렇다.

- ObjC의 메시지 디스패치와 동적 메서드 교체를 Swift가 얼마나 허용할 것인가?
- devirtualization이 중요한 Swift에서 ObjC interop는 어떤 비용을 강제하는가?
- property / initializer / method model이 ObjC 세계와 만날 때 어떤 제약이 필요한가?

즉 이 proposal은 현재 [[objc-interop]]와 [[clang-importer]]를
설계 역사 관점으로 거꾸로 비춰 주는 문서다.

## proposal의 핵심 포인트

### 1. Objective-C는 구현 모델 중심 언어다
문서는 ObjC semantics가
- ivar access
- message send
- dynamic method resolution
- forwarding
- category / runtime replacement
같은 구현 메커니즘에 깊게 묶여 있다고 설명한다.

이 말은 곧 Swift가 ObjC 세계와 상호운용할 때
정적 reasoning과 devirtualization을 그냥 얻을 수 없다는 뜻이다.

### 2. Swift는 devirtualization을 더 강하게 원한다
문서는 Swift property model과 abstraction model에서
method/property devirtualization이 매우 중요하다고 본다.
특히 ObjC식 unrestricted dynamism을 그대로 허용하면
- property getter/setter 최적화
- class member devirtualization
- 분석 정확도
가 크게 손해 본다고 본다.

즉 ObjC interop는 단순 FFI 문제가 아니라
Swift optimization 철학과 직접 충돌하는 설계 주제다.

### 3. `@dynamic` / `@objc` / dynamic replacement 감각의 역사적 배경
이 proposal의 흥미로운 부분은
Swift가 왜 모든 것을 ObjC처럼 열어 두지 않고,
동적 교체 가능성을 더 제한적이고 명시적인 속성으로 다루려 했는가를 보여 준다는 점이다.

오늘날의 구현은 proposal 문구 그대로는 아니더라도,
“동적 디스패치를 쓰려면 더 명시적이어야 한다”는 방향성과 잘 맞는다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. Objective-C 상호운용 자체
현재 상태를 요약해서 보려면 먼저
- [[objc-interop]]
- [[clang-importer]]
를 보는 것이 좋다.

### 2. importer / naming / overlay 축
proposal의 “언어가 다른 구현 모델과 만날 때 생기는 문제”는
오늘날 importer 축에서 더 구체적으로 드러난다.

관련 페이지:
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]
- [[clang-importer]]

### 3. dynamic dispatch와 최적화 축
proposal의 진짜 긴장은
동적 교체 가능성과 devirtualization 사이 충돌이다.
이건 다음 페이지들과 같이 보면 더 잘 보인다.

- [[compiler-driver]]
- [[optimizer-design]]
- [[high-level-sil-optimizations]]

### 4. initializer/property 모델과의 접점
ObjC interop proposal은
initializer / property / accessor 모델과도 직접 얽혀 있다.
특히 initialization proposal과 accessors proposal을 같이 보면 더 선명해진다.

관련 페이지:
- [[proposal-initialization-and-accessors-to-property-model]]
- [[failable-initializers]]
- [[sil-memory-access]]

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/ObjCInteroperation.rst`
- `swift/lib/ClangImporter/`
- `swift/lib/PrintAsClang/`
- `swift/include/swift/Runtime/` 일부 ObjC interop 관련 축

현재 위키 연결:
- [[objc-interop]]
- [[clang-importer]]
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]
- [[cpp-interop-overview]]

## 이 문서를 읽을 때 주의할 점

- 이 proposal은 지금의 interop 구현 설명서가 아니다.
- 대신 “Swift가 ObjC의 dynamism을 얼마나 제약해야 optimization이 가능한가”라는 설계 고민을 보여 준다.
- 따라서 importer 문서와 optimizer 문서를 같이 봐야 가치가 커진다.

## 추천 읽기 순서

1. [[proposal-objc-interop-to-importer-and-dispatch]]
2. [[objc-interop]]
3. [[clang-importer]]
4. [[how-swift-imports-c-apis]]
5. [[c-to-swift-name-translation]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[objc-interop]]
- [[clang-importer]]
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[keyword-network]]
