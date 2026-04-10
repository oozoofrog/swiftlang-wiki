---
type: summary
category: learning
tags: [swift, concurrency, task, executor, runtime, scheduler]
aliases: [Swift Task·Executor·Runtime, Swift task executor runtime, task executor runtime]
sources: [swift-concurrency-architecture.md, runtime.md, swiftlang-swift/docs/proposals/Concurrency.rst, swiftlang-swift/docs/proposals/archive/MemoryAndConcurrencyModel.rst]
---

# Swift Task·Executor·Runtime

이 페이지는 Swift concurrency의 실행 모델,
즉 task, task group, cancellation, task local, executor, actor runtime, hop-to-executor를
하나의 허브로 묶는다.

[[swift-concurrency-architecture]]가 전체 지도를 제공한다면,
이 페이지는 그중에서도 “실제로 어떤 실행 단위가 어떻게 스케줄되고 이동하는가”를 중심으로 보는 입구다.

## 이 허브가 묶는 6개 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| task 모델 | async function과 task는 어떤 실행 단위인가 | [[swift-concurrency-architecture]], [[runtime]] |
| task group / cancellation | child task, task group, cancellation은 어떻게 묶이는가 | [[swift-concurrency-architecture]] |
| executor | 작업은 어떤 executor에서 실행되며 언제 hop 하는가 | [[swift-concurrency-architecture]], [[sil-optimizer-pass-catalog]] |
| actor runtime | actor와 executor는 실행시 어떻게 연결되는가 | [[swift-actor-isolation-and-sendable]], [[runtime]] |
| ABI / runtime | task/job/actor/executor는 ABI와 runtime에서 어떻게 표현되는가 | [[runtime]], [[standard-library-runtime-and-compiler]] |
| lowering / optimization | compiler는 async/actor 의미를 어떤 런타임 호출과 pass로 내리는가 | [[sil-reference]], [[sil-optimizer-pass-catalog]] |

## 왜 이 허브가 중요한가

Swift concurrency를 문법이나 진단 규칙만으로 이해하면,
정작 중요한 실행 모델이 비어 버린다.

- `async`는 곧바로 병렬 실행과 동의어가 아니다.
- `Task`는 곧 OS thread가 아니다.
- actor는 executor와 연결되지만 executor 그 자체와 동일하지 않다.
- `MainActor`는 isolation 규칙이면서 동시에 실행시 모델과 만난다.

즉 task / executor / runtime 축을 같이 봐야
Swift concurrency가 “타입 규칙 + 실행 모델”이라는 점이 보인다.

## 자주 헷갈리는 구분

### 1. async vs parallel
`async`는 suspension 가능성과 structured concurrency 모델을 뜻하지,
자동 병렬화 보장을 뜻하지는 않는다.

### 2. Task vs thread
Task는 Swift concurrency runtime의 작업 단위다.
실행은 executor를 통해 일어나며,
thread와 1:1 대응이라고 이해하면 자주 헷갈린다.

### 3. actor vs executor
actor는 isolation 경계이고,
executor는 실제 실행을 담당하는 메커니즘에 가깝다.
둘은 강하게 연결되지만 같은 개념은 아니다.

관련 페이지:
- [[swift-actor-isolation-and-sendable]]

### 4. runtime vs stdlib API
사용자는 `Task`, `TaskGroup`, `MainActor` 같은 표면 타입을 보지만,
그 뒤에는 ABI 구조와 runtime entrypoint가 있다.
그래서 stdlib public API와 runtime을 같이 보는 편이 맞다.

관련 페이지:
- [[standard-library-runtime-and-compiler]]
- [[runtime]]

## 컴파일러 안에서는 어디가 핵심인가

### 1. SILGen / IRGen
async function, actor hop, executor 관련 의미는 lowering 과정에서 더 명확해진다.

관련 페이지:
- [[sil-reference]]
- [[swift-concurrency-architecture]]

### 2. mandatory pass
실행시 hop과 actor 이동은 optimizer / mandatory transform과도 이어진다.

대표 예:
- `OptimizeHopToExecutor`
- `LowerHopToActor`

관련 페이지:
- [[sil-optimizer-pass-catalog]]
- [[optimizer-design]]

### 3. runtime / ABI 층
task, actor, executor는 결국 ABI 헤더와 runtime 구현을 통해 구체화된다.
그래서 이 축은 compiler 내부 문서만 읽어서는 절반만 보인다.

관련 페이지:
- [[runtime]]
- [[standard-library-runtime-and-compiler]]

## 로컬 Swift 소스에서 같이 볼 경로

### ABI / runtime 헤더
- `swift/include/swift/Runtime/Concurrency.h`
- `swift/include/swift/ABI/Task.h`
- `swift/include/swift/ABI/TaskStatus.h`
- `swift/include/swift/ABI/TaskGroup.h`
- `swift/include/swift/ABI/Actor.h`
- `swift/include/swift/ABI/Executor.h`

### stdlib public Concurrency 구현
- `swift/stdlib/public/Concurrency/Task.swift`
- `swift/stdlib/public/Concurrency/Task.cpp`
- `swift/stdlib/public/Concurrency/TaskGroup.swift`
- `swift/stdlib/public/Concurrency/TaskGroup.cpp`
- `swift/stdlib/public/Concurrency/TaskLocal.swift`
- `swift/stdlib/public/Concurrency/TaskLocal.cpp`
- `swift/stdlib/public/Concurrency/TaskCancellation.swift`
- `swift/stdlib/public/Concurrency/Actor.swift`
- `swift/stdlib/public/Concurrency/Actor.cpp`
- `swift/stdlib/public/Concurrency/MainActor.swift`
- `swift/stdlib/public/Concurrency/Executor.swift`
- `swift/stdlib/public/Concurrency/ExecutorBridge.swift`
- `swift/stdlib/public/Concurrency/ExecutorBridge.cpp`
- `swift/stdlib/public/Concurrency/GlobalExecutor.cpp`
- `swift/stdlib/public/Concurrency/DispatchExecutor.swift`
- `swift/stdlib/public/Concurrency/DispatchGlobalExecutor.cpp`
- `swift/stdlib/public/Concurrency/CooperativeExecutor.swift`
- `swift/stdlib/public/Concurrency/CooperativeGlobalExecutor.cpp`

### compiler lowering / transform
- `swift/lib/SILGen/SILGenConcurrency.cpp`
- `swift/lib/IRGen/GenConcurrency.cpp`
- `swift/lib/SILOptimizer/Mandatory/OptimizeHopToExecutor.cpp`
- `swift/lib/SILOptimizer/Mandatory/LowerHopToActor.cpp`

이 경로 묶음은 Swift concurrency의 실행 모델이
표면 라이브러리 타입만의 문제가 아니라,
ABI + runtime + stdlib + lowering이 함께 맞물리는 구조라는 점을 보여 준다.

## 추천 읽기 순서

### 실행 모델 관점
1. [[swift-concurrency-architecture]]
2. [[swift-task-executor-runtime]]
3. [[runtime]]
4. [[standard-library-runtime-and-compiler]]

### actor와 함께 보는 루트
1. [[swift-actor-isolation-and-sendable]]
2. [[swift-task-executor-runtime]]
3. [[concurrency-data-race-safety]]
4. [[runtime]]

### 구현 관점
1. [[sil-reference]]
2. [[sil-optimizer-pass-catalog]]
3. [[swift-task-executor-runtime]]
4. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[concurrency-data-race-safety]]
- [[runtime]]
- [[standard-library-runtime-and-compiler]]
- [[sil-reference]]
- [[sil-optimizer-pass-catalog]]
- [[keyword-network]]