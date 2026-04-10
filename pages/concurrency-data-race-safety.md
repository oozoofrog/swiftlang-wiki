---
type: concept
category: compiler
tags: [concurrency, sendable, actor-isolation, migration, diagnostics]
aliases: [Swift 6 데이터 경쟁 안전성, 데이터 경쟁 안전성 검사, Strict Concurrency]
sources: [swift.org/documentation/concurrency/index.html, official-docs/concurrency-data-race-safety-to-compiler-checks.md]
---

# Swift 6 데이터 경쟁 안전성 검사

Swift 6의 concurrency migration 문서가 설명하는 핵심은 단순히 `async`/`await`를 배우는 것이 아니다.
정말 중요한 변화는 **actor isolation**과 **`Sendable` 규칙**을 컴파일러가 훨씬 더 강하게 검사하기 시작한다는 점이다.

원문 진입점은 `https://www.swift.org/documentation/concurrency/` 이지만, 다운로드 번들 안의 파일은 redirect-only다.
실제 canonical 주제는 Swift 6 migration guide의 **Enable data-race safety checking** 페이지다.

## 핵심 요약

- Swift 6 language mode는 기본적으로 **완전한 데이터 경쟁 안전성 검사**를 켠다.
- 아직 Swift 5 모드에 머무는 프로젝트는 `-strict-concurrency=complete`로 **warning 기반 사전 점검**을 할 수 있다.
- 이 검사의 표면 주제는 `actor`, global actor, `Sendable`, 캡처된 값의 전송 가능성, cross-actor 접근이다.
- 내부적으로는 타입 체커의 isolation/`Sendable` 검사와 SIL의 concurrency 관련 mandatory pass가 함께 얽혀 있다.

## 무엇을 켜는가

### 1. Swift 6 language mode

가장 직접적인 방법이다.
Swift 6 모드에 들어가면 full data-race safety checking이 기본 동작이 된다.

대표 설정 축:

- SwiftPM: `swift-tools-version: 6.0`
- CLI: `-swift-version 6`
- Xcode: `Swift Language Version = 6`
- xcconfig: `SWIFT_VERSION = 6`

### 2. Swift 5 모드에서 warning으로 미리 점검

기존 모듈을 한 번에 Swift 6로 올리기 어렵다면,
먼저 warning으로 현재 위반 지점을 측정할 수 있다.

대표 설정 축:

- CLI: `-strict-concurrency=complete`
- SwiftPM 5.9/5.10: `.enableExperimentalFeature("StrictConcurrency")`
- SwiftPM 6+: `.enableUpcomingFeature("StrictConcurrency")`
- Xcode: `Strict Concurrency Checking = Complete`
- xcconfig: `SWIFT_STRICT_CONCURRENCY = complete`

즉 migration 전략은 보통 다음 순서를 따른다.

1. Swift 5 모드에서 warning을 먼저 켠다.
2. `Sendable` / isolation warning을 모듈 단위로 정리한다.
3. 준비된 타깃만 Swift 6 language mode로 올린다.
4. 마지막에 패키지/앱 전체를 Swift 6 모드로 정리한다.

## SwiftPM / CLI / Xcode에서의 차이

### SwiftPM

Swift 6 tools에서는 패키지 전체를 6으로 올리거나,
타깃별로 `swiftLanguageMode`를 조절할 수 있다.

핵심 포인트:

- `swift-tools-version: 6.0`이면 기본 언어 모드는 6이다.
- 아직 준비 안 된 타깃은 `.swiftLanguageMode(.v5)`로 남길 수 있다.
- pre-6 툴체인을 계속 지원해야 하면 version-specific manifest가 필요할 수 있다.
- 완전 전환 전에는 StrictConcurrency feature flag로 warning 기반 점검이 가능하다.

### CLI

직접 `swift` / `swiftc`를 돌릴 때는 설정이 가장 단순하다.

- Swift 6 모드: `-swift-version 6`
- warning 기반 점검: `-strict-concurrency=complete`
- SwiftPM 명령에서 넘길 때는 `-Xswiftc`를 사용한다.

### Xcode

빌드 설정 레벨에서 제어한다.

- 언어 모드: `Swift Language Version`
- warning 기반 점검: `Strict Concurrency Checking`
- 설정 파일 기반 관리가 필요하면 `SWIFT_VERSION`, `SWIFT_STRICT_CONCURRENCY`를 xcconfig에 둔다.

## 컴파일러 내부에서는 어디가 핵심인가

### 1. Type Checker / Sema

사용자가 실제로 가장 먼저 체감하는 검사는 대부분 여기서 나온다.

핵심 역할:

- cross-actor 접근 검증
- actor-isolated 선언 접근 규칙 확인
- `Sendable` conformance 및 전송 가능성 검사
- 클로저/함수 타입의 isolation 및 sendability 판단
- Swift 5 모드에서는 warning, Swift 6 모드에서는 더 강한 진단으로 승격

관련 기존 페이지:

- [[type-checker]]
- [[diagnostics]]
- [[official-docs/type-checker-design-and-implementation]]

### 2. SIL mandatory pass

위키의 패스 카탈로그를 보면 concurrency 관련 mandatory pass가 이미 드러난다.

- `SendNonSendable` — `Sendable` 위반 검사
- `FlowIsolation` — actor isolation 진단

이 말은 concurrency safety가 단순 프론트엔드 문법 체크에 그치지 않고,
SIL 단계의 흐름/격리 정보와도 연결된다는 뜻이다.

관련 페이지:

- [[sil-optimizer-pass-catalog]]
- [[sil-reference]]
- [[sil-ownership]]

### 3. Ownership / region / noncopyable와의 접점

동시성 안전성은 결국 “무엇이 어느 실행 문맥에 안전하게 이동할 수 있는가”의 문제다.
그래서 ownership 모델과 자연스럽게 맞물린다.

특히 같이 보면 좋은 축:

- 값 이동과 borrow의 의미: [[ownership-manifesto]]
- SIL ownership 규칙: [[sil-ownership]]
- non-Sendable 값이 SIL에서 어떻게 추적되는가: [[sil-instructions]]

즉 표면적으로는 `actor`와 `Sendable` 이야기지만,
더 깊게 들어가면 ownership / isolation / region 추적 이야기로 바뀐다.


## 이 머신 기준 실제 경로

이 페이지를 로컬 소스와 같이 읽고 싶다면, 실제 Swift 소스 트리는 다음 경로에 있다.

- 소스 루트: `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift`

동시성 안전성과 직접적으로 이어지는 파일:

- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/Sema/TypeCheckConcurrency.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/AST/ActorIsolation.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/SIL/IR/ActorIsolation.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/SILGen/SILGenConcurrency.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/SILOptimizer/Mandatory/SendNonSendable.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/SILOptimizer/Mandatory/FlowIsolation.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/lib/SILOptimizer/Utils/RegionIsolation.cpp`
- `/Volumes/eyedisk/develop/oozoofrog/swiftlang/swift/docs/SIL/Ownership.md`

## 이 머신에서 확인한 명령

이 머신에서 다음 명령은 실제 실행 확인했다.

- `swiftc -swift-version 6 -typecheck sample.swift`
- `swiftc -strict-concurrency=complete -typecheck sample.swift`

즉 학습용으로는 먼저 warning 기반(`-strict-concurrency=complete`)으로 현재 위반 지점을 보고,
그 다음 Swift 6 language mode로 올리는 흐름을 실제로 시험해볼 수 있다.

## 왜 이 주제가 중요한가

Swift 6의 concurrency migration은 단순한 스타일 권장이 아니라,
기존 코드에서 “원래는 돌았지만 사실상 안전하지 않았던 패턴”을
컴파일러가 더 이상 묵인하지 않는 방향의 변화다.

그래서 이 주제를 공부할 때는 세 층을 같이 봐야 한다.

1. 사용자 설정 층
   - SwiftPM / CLI / Xcode에서 무엇을 켜는가
2. 언어 의미 층
   - actor isolation, `Sendable`, global actor, cross-actor access
3. 구현 층
   - type checker 진단 + SIL isolation/sendability pass

이 세 층이 연결되어 보여야 migration 문서가 단순 설정 가이드가 아니라
컴파일러 동작 설명서로 읽힌다.

## 추천 읽기 순서

1. [[official-docs/concurrency-data-race-safety-to-compiler-checks]]
2. [[type-checker]]
3. [[diagnostics]]
4. [[sil-optimizer-pass-catalog]]
5. [[sil-ownership]]
6. [[ownership-manifesto]]

## 같이 보면 좋은 페이지

- [[official-docs/language-to-compiler-crosswalk]]
- [[official-docs/swift-documentation-index]]
- [[type-checker]]
- [[diagnostics]]
- [[sil-optimizer-pass-catalog]]
- [[sil-ownership]]
- [[ownership-manifesto]]
