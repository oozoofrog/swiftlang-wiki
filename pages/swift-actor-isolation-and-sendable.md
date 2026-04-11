---
type: summary
category: learning
tags: [swift, concurrency, actor-isolation, sendable, mainactor, diagnostics]
aliases: [Swift actor isolation·Sendable, Swift actor isolation과 Sendable, actor isolation and Sendable]
sources: [concurrency-data-race-safety.md, official-docs/concurrency-data-race-safety-to-compiler-checks.md, swiftlang-swift/docs/proposals/Concurrency.rst]
---

# Swift actor isolation·Sendable

이 페이지는 Swift 동시성에서 가장 자주 부딪히는 정적 안전성 축,
즉 actor isolation, global actor, `MainActor`, `Sendable`, cross-actor access를
하나의 허브로 묶는다.

[[concurrency-data-race-safety]]가 Swift 5→6 migration과 strict checking에 초점을 맞췄다면,
이 페이지는 그보다 한 단계 더 구조적으로
“무엇이 어떤 격리 경계에 속하고, 무엇이 안전하게 전송될 수 있는가”를 설명하는 입구다.

## 이 허브가 묶는 5개 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| actor isolation | 어떤 선언/값/클로저가 어느 actor 문맥에 속하는가 | [[swift-concurrency-architecture]], [[concurrency-data-race-safety]], [[type-checker]] |
| global actor | `MainActor`와 global actor는 어떤 격리 경계를 제공하는가 | [[swift-concurrency-architecture]], [[diagnostics]] |
| `Sendable` | 어떤 타입과 캡처가 안전하게 전송 가능한가 | [[swift-type-system]], [[concurrency-data-race-safety]] |
| SIL isolation | isolation 규칙이 SIL과 pass에서 어떻게 검증되는가 | [[sil-optimizer-pass-catalog]], [[sil-ownership]] |
| ownership 접점 | region isolation, borrow, noncopyable는 동시성과 어떻게 만나는가 | [[swift-ownership-memory-model]], [[ownership-manifesto]] |

## 왜 이 축이 중요한가

Swift concurrency를 쓰다 보면 결국 가장 많이 마주치는 질문은 이것들이다.

- 왜 이 actor-isolated 프로퍼티에 여기서 접근하면 안 되지?
- 왜 이 closure capture는 `Sendable`이 아니라고 하지?
- 왜 Swift 5에서는 warning인데 Swift 6에서는 error가 되지?
- 왜 `MainActor`는 단순한 annotation 이상으로 동작하지?

즉 동시성의 실전 체감은 task 생성 자체보다도
isolation boundary와 sendability 규칙에서 먼저 온다.

## 자주 헷갈리는 구분

### 1. actor isolation vs thread
actor isolation은 “이 값이 어떤 실행 문맥에 논리적으로 속하는가”의 규칙이지,
곧바로 특정 OS thread 하나에 고정된다는 뜻은 아니다.
그래서 actor 이야기를 볼 때는 executor/runtime 모델도 같이 봐야 한다.

관련 페이지:
- [[swift-task-executor-runtime]]
- [[runtime]]

### 2. `Sendable` vs value type
value type이라고 자동으로 모든 것이 안전 전송 가능한 것은 아니다.
반대로 reference type이라고 항상 불가능한 것도 아니다.
`Sendable`은 동시성 맥락에서의 안전 전송 계약이고,
이는 타입 시스템과 API 설계 문제로 이어진다.

관련 페이지:
- [[swift-type-system]]
- [[swift-language-overview]]

### 3. `MainActor` vs “메인 스레드 감각”
앱 개발자 감각에서는 둘이 거의 같이 느껴지지만,
컴파일러 관점에서는 `MainActor` 역시 global actor isolation 규칙의 한 사례다.
그래서 단순 UI 관습보다 넓은 언어/타입 규칙으로 읽는 편이 맞다.

### 4. isolation diagnostics vs ownership diagnostics
둘은 다른 오류처럼 보이지만,
깊게 들어가면 region isolation, borrow scope, non-Sendable 값 추적처럼
ownership 계열 문제와 맞물린다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[sil-ownership]]

## 컴파일러 안에서는 어디가 핵심인가

### 1. Sema / type checker
가장 직접적인 actor isolation / `Sendable` 판정은 여기서 나온다.

- cross-actor reference 확인
- actor-isolated 선언 접근 규칙 판정
- global actor 전파와 함수 타입 isolation 해석
- `Sendable` conformance / capture sendability 확인

관련 페이지:
- [[type-checker]]
- [[diagnostics]]
- [[concurrency-data-race-safety]]

### 2. AST / SIL isolation representation
isolation 정보는 프론트엔드 내부 표현과 SIL 레벨에서도 계속 이어진다.
그래서 actor isolation은 단순 parser annotation이 아니라,
후속 lowering과 검사에 계속 살아 있는 의미 정보다.

관련 페이지:
- [[sil-reference]]
- [[sil-optimizer-pass-catalog]]

### 3. mandatory pass
동시성 검사는 프론트엔드에서 끝나지 않는다.
대표적으로 `FlowIsolation`, `SendNonSendable`는
SIL 단계에서 isolation / sendability를 다시 다룬다.

관련 페이지:
- [[sil-optimizer-pass-catalog]]
- [[optimizer-design]]

## 로컬 Swift 소스에서 같이 볼 경로

### 의미 분석 / isolation 규칙
- `swift/lib/Sema/TypeCheckConcurrency.cpp`
- `swift/include/swift/Sema/Concurrency.h`
- `swift/lib/AST/ActorIsolation.cpp`
- `swift/include/swift/AST/ActorIsolation.h`
- `swift/lib/AST/Concurrency.cpp`
- `swift/include/swift/AST/Concurrency.h`

### SIL / 하위 검사
- `swift/lib/SIL/IR/ActorIsolation.cpp`
- `swift/lib/SILOptimizer/Mandatory/FlowIsolation.cpp`
- `swift/lib/SILOptimizer/Mandatory/SendNonSendable.cpp`
- `swift/lib/SILOptimizer/Utils/RegionIsolation.cpp`

### 표면 라이브러리 선언
- `swift/stdlib/public/Concurrency/Actor.swift`
- `swift/stdlib/public/Concurrency/GlobalActor.swift`
- `swift/stdlib/public/Concurrency/MainActor.swift`
- `swift/stdlib/public/Distributed/DistributedActor.swift`

이 경로 묶음을 보면 actor isolation / `Sendable`가
문법 attribute 하나의 문제가 아니라,
Sema, AST, SIL, stdlib public API를 가로지르는 축이라는 점이 드러난다.

## 추천 읽기 순서

### 실전 오류 해결 관점
1. [[swift-concurrency-architecture]]
2. [[swift-actor-isolation-and-sendable]]
3. [[concurrency-data-race-safety]]
4. [[diagnostics]]

### 타입 시스템 관점
1. [[swift-type-system]]
2. [[swift-actor-isolation-and-sendable]]
3. [[concurrency-data-race-safety]]
4. [[type-checker]]

### ownership과 연결해서 보는 루트
1. [[swift-ownership-memory-model]]
2. [[sil-ownership]]
3. [[swift-actor-isolation-and-sendable]]
4. [[concurrency-data-race-safety]]

## 같이 보면 좋은 페이지

- [[swift-concurrency-architecture]]
- [[swift-task-executor-runtime]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[concurrency-data-race-safety]]
- [[type-checker]]
- [[diagnostics]]
- [[sil-optimizer-pass-catalog]]
- [[keyword-network]]