---
type: summary
category: learning
tags: [swift, concurrency, actor, sendable, executor, runtime]
aliases: [Swift Concurrency 전체 구조, Swift 동시성 전체 구조, Swift Concurrency 아키텍처]
sources: [concurrency-data-race-safety.md, official-docs/concurrency-data-race-safety-to-compiler-checks.md, swiftlang-swift/docs/proposals/Concurrency.rst, swiftlang-swift/docs/proposals/archive/MemoryAndConcurrencyModel.rst]
---

# Swift Concurrency 전체 구조

이 페이지는 Swift Concurrency를
단순한 `async`/`await` 문법 묶음이 아니라,
언어 표면, 타입/격리 규칙, SIL lowering, executor/runtime, migration까지 잇는 상위 허브로 정리한다.

strict checking, Task/actor API, executor/runtime, compiler lowering은 종종 따로 보이지만,
실제로는 하나의 실행/격리 모델을 다른 층에서 설명하는 요소들이다.
이 허브는 그 전체 지형을 한 장에 모은다.

## Swift Concurrency를 이루는 6개 층

| 층 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| 언어 표면 | `async`/`await`, `Task`, `TaskGroup`, `actor`, global actor는 무엇인가 | [[swift-language-overview]], [[official-docs/concurrency-data-race-safety-to-compiler-checks]] |
| 타입/안전성 | `Sendable`, actor isolation, cross-actor access는 어떻게 판정되는가 | [[swift-type-system]], [[swift-actor-isolation-and-sendable]], [[concurrency-data-race-safety]], [[type-checker]] |
| ownership / isolation | 값 이동, borrow, region isolation은 동시성과 어떻게 만나는가 | [[swift-ownership-memory-model]], [[ownership-manifesto]], [[sil-ownership]] |
| SIL / lowering | concurrency 의미가 SIL과 mandatory pass에서 어떻게 표현되는가 | [[sil-reference]], [[sil-optimizer-pass-catalog]], [[concurrency-data-race-safety]] |
| runtime / executor | task, job, executor, actor runtime은 실행시 어떻게 움직이는가 | [[swift-task-executor-runtime]], [[runtime]], [[standard-library-runtime-and-compiler]] |
| migration / diagnostics | Swift 5→6 전환에서 무엇이 warning/error가 되는가 | [[concurrency-data-race-safety]], [[diagnostics]], [[swift-compiler-learning-stack]] |

## 왜 별도 허브가 필요한가

Swift Concurrency는 자주 두 가지로 과소단순화된다.

1. “그냥 비동기 문법”
2. “Swift 6에서 Sendable 에러 내는 규칙”

하지만 실제 구조는 그보다 훨씬 넓다.

- 언어 표면에서는 `async` 함수, task, actor, global actor, async sequence 같은 모델이 보인다.
- 타입 시스템에서는 isolation, `Sendable`, function type sendability가 핵심이 된다.
- compiler 내부에서는 Sema 검사, SILGen, hop-to-executor lowering, FlowIsolation/SendNonSendable 같은 mandatory pass가 나온다.
- runtime 쪽에서는 task/job/executor/continuation/actor runtime이 움직인다.
- migration 관점에서는 Swift 5 mode warning과 Swift 6 mode error 승격 전략이 중요해진다.

즉 Swift Concurrency는 문법, 타입 시스템, ownership, runtime을 한 번에 묶는 주제다.

## 큰 그림에서 가장 중요한 축

### 1. async/await는 표면이고, 실제 핵심은 task 모델이다
사용자는 `async` 함수와 `await`를 보지만,
실제로는 suspension point, task creation, cancellation, task local, task group 같은 실행 모델이 뒤에 깔려 있다.

관련 페이지:
- [[swift-task-executor-runtime]]
- [[swift-language-overview]]
- [[runtime]]

### 2. actor는 단순한 클래스 변형이 아니라 isolation 경계다
actor의 핵심은 문법보다도
어떤 값/선언/클로저가 어느 실행 문맥에 속해 있는가를 정적으로 추적한다는 점이다.

관련 페이지:
- [[swift-actor-isolation-and-sendable]]
- [[concurrency-data-race-safety]]
- [[type-checker]]
- [[diagnostics]]

### 3. Sendable은 동시성의 타입 시스템 얼굴이다
Swift concurrency에서 타입 시스템이 가장 직접적으로 드러나는 지점은 `Sendable`이다.
그래서 이 주제는 단순 동시성 문서가 아니라 [[swift-type-system]]과도 깊게 이어진다.

### 4. concurrency safety는 ownership과 다시 만난다
무엇이 어느 실행 문맥으로 안전하게 이동할 수 있는가를 따지다 보면,
결국 borrow, consume, region isolation, lifetime 문제와 다시 합류한다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[ownership-manifesto]]
- [[sil-ownership]]

### 5. executor/runtime을 빼면 반쪽짜리 이해가 된다
Swift Concurrency는 compiler 검사만으로 끝나지 않는다.
task scheduling, executor hop, main actor 실행, cooperative/global executor 같은 실행시 모델이 반드시 따라온다.

관련 페이지:
- [[runtime]]
- [[standard-library-runtime-and-compiler]]

## 컴파일러 안에서는 어디가 핵심인가

### 1. Sema / type checker
동시성의 첫 관문은 대부분 여기다.

- actor isolation 판정
- cross-actor reference 검사
- `Sendable` conformance 및 sendability 판정
- closure / function type isolation 해석
- Swift 5 vs Swift 6 진단 강도 차이

관련 페이지:
- [[type-checker]]
- [[diagnostics]]
- [[concurrency-data-race-safety]]

### 2. SILGen / SIL lowering
표면 concurrency 의미는 SIL로 내려가면서 더 구체적인 실행 단위로 바뀐다.
이 단계에서 async function, actor hop, executor 관련 lowering이 드러난다.

관련 페이지:
- [[sil-reference]]
- [[sil-optimizer-pass-catalog]]

### 3. mandatory pass / isolation diagnostics
동시성은 단순 프론트엔드 검사에 멈추지 않는다.
SIL 단계에서도 isolation과 sendability를 추적하는 mandatory pass가 존재한다.

대표 예:
- `FlowIsolation`
- `SendNonSendable`
- `OptimizeHopToExecutor`
- `LowerHopToActor`

관련 페이지:
- [[sil-optimizer-pass-catalog]]
- [[optimizer-design]]

### 4. runtime / stdlib / ABI 층
compiler가 판정한 concurrency 의미는 결국 runtime과 stdlib public API가 실제로 받쳐야 한다.
Task, Actor, Executor, MainActor 같은 표면 타입 뒤에는 runtime entrypoint와 ABI 구조가 있다.

관련 페이지:
- [[swift-task-executor-runtime]]
- [[runtime]]
- [[standard-library-runtime-and-compiler]]

## 로컬 Swift 소스에서 같이 볼 경로

이 주제를 로컬 `swift/` 소스와 함께 읽고 싶다면,
아래 경로들이 좋은 진입점이다.

### 설계/문서
- `swift/docs/proposals/Concurrency.rst`
- `swift/docs/proposals/archive/MemoryAndConcurrencyModel.rst`
- `swift/docs/SIL/Ownership.md`

### 컴파일러 프론트엔드 / 의미 분석
- `swift/lib/Sema/TypeCheckConcurrency.cpp`
- `swift/include/swift/Sema/Concurrency.h`
- `swift/lib/AST/Concurrency.cpp`
- `swift/include/swift/AST/Concurrency.h`
- `swift/lib/AST/ActorIsolation.cpp`
- `swift/include/swift/AST/ActorIsolation.h`

### SILGen / IRGen / 최적화
- `swift/lib/SILGen/SILGenConcurrency.cpp`
- `swift/lib/IRGen/GenConcurrency.cpp`
- `swift/lib/SILOptimizer/Mandatory/FlowIsolation.cpp`
- `swift/lib/SILOptimizer/Mandatory/SendNonSendable.cpp`
- `swift/lib/SILOptimizer/Mandatory/OptimizeHopToExecutor.cpp`
- `swift/lib/SILOptimizer/Mandatory/LowerHopToActor.cpp`
- `swift/lib/SILOptimizer/Utils/RegionIsolation.cpp`

### runtime / ABI / public concurrency library
- `swift/include/swift/Runtime/Concurrency.h`
- `swift/include/swift/ABI/Task.h`
- `swift/include/swift/ABI/Actor.h`
- `swift/include/swift/ABI/Executor.h`
- `swift/stdlib/public/Concurrency/Task.swift`
- `swift/stdlib/public/Concurrency/Task.cpp`
- `swift/stdlib/public/Concurrency/TaskGroup.swift`
- `swift/stdlib/public/Concurrency/Actor.swift`
- `swift/stdlib/public/Concurrency/Actor.cpp`
- `swift/stdlib/public/Concurrency/GlobalActor.swift`
- `swift/stdlib/public/Concurrency/MainActor.swift`
- `swift/stdlib/public/Concurrency/Executor.swift`
- `swift/stdlib/public/Concurrency/GlobalExecutor.cpp`
- `swift/stdlib/public/Concurrency/ExecutorBridge.swift`
- `swift/stdlib/public/Concurrency/ExecutorBridge.cpp`
- `swift/stdlib/public/Concurrency/DispatchExecutor.swift`
- `swift/stdlib/public/Concurrency/CooperativeExecutor.swift`

이 파일 집합을 보면 Swift Concurrency가
문서 한 장이나 타입 하나의 문제가 아니라,
compiler + optimizer + runtime + stdlib public API를 가로지르는 구조라는 점이 드러난다.

## 추천 읽기 순서

### 언어/사용자 관점
1. [[swift-language-overview]]
2. [[swift-type-system]]
3. [[swift-concurrency-architecture]]
4. [[swift-actor-isolation-and-sendable]]
5. [[swift-task-executor-runtime]]
6. [[concurrency-data-race-safety]]

### 구현 관점
1. [[swift-and-swift-compiler]]
2. [[swift-actor-isolation-and-sendable]]
3. [[swift-task-executor-runtime]]
4. [[concurrency-data-race-safety]]
5. [[sil-reference]]
6. [[sil-optimizer-pass-catalog]]
7. [[runtime]]

### ownership과 같이 보는 루트
1. [[swift-ownership-memory-model]]
2. [[ownership-manifesto]]
3. [[sil-ownership]]
4. [[swift-concurrency-architecture]]
5. [[swift-actor-isolation-and-sendable]]
6. [[concurrency-data-race-safety]]

### migration / 실무 관점
1. [[official-docs/concurrency-data-race-safety-to-compiler-checks]]
2. [[concurrency-data-race-safety]]
3. [[diagnostics]]
4. [[swift-compiler-learning-stack]]

## 같이 보면 좋은 페이지

- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[concurrency-data-race-safety]]
- [[type-checker]]
- [[diagnostics]]
- [[sil-optimizer-pass-catalog]]
- [[runtime]]
- [[keyword-network]]