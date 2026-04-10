---
type: reference
category: learning
tags: [swift, proposal, type-checker, sema, request-evaluator, diagnostics]
aliases: [Declaration Type Checker proposal, declaration type checker 교차 읽기]
sources: [swiftlang-swift/docs/proposals/DeclarationTypeChecker.rst]
---

# Declaration Type Checker proposal → 현대 Sema 교차 읽기

이 페이지는 `swift/docs/proposals/DeclarationTypeChecker.rst`를
현재 Swift의 Sema / Request Evaluator / diagnostics 구조와 연결해서 읽는 교차 페이지다.

## 이 proposal이 설명하는 핵심 문제

이 문서는 “선언 타입 체커가 왜 그렇게 자주 깨지는가?”를 정면으로 다룬다.
핵심 문제의식은 다음과 같다.

- phase가 뒤엉켜 있다
- recursion이 제어되지 않는다
- circular dependency를 ad hoc하게 끊고 있다
- declaration validation이 너무 많은 일을 한 번에 한다
- 그래서 crash, order dependence, broken AST가 생긴다

즉 이 proposal은
현재 [[type-checker]] 페이지의 “어떻게 타입을 푸는가”보다 한 단계 위에서,
“왜 Sema 아키텍처 자체를 다시 생각해야 했는가”를 설명하는 문서다.

## proposal의 핵심 포인트

### 1. phase-aware architecture
이 문서는 parsing, import resolution, extension binding, type hierarchies,
primary name binding, generic signature resolution, declaration type validation,
override checking, attribute checking, semantics checking 같은 phase를 분리해서 본다.

핵심은
- AST node가 자신이 어느 phase까지 올라갔는지 알고
- 필요한 만큼만 다음 phase로 이동하며
- 다른 declaration에 대한 dependency를 명시적으로 관리해야 한다
는 점이다.

### 2. ad hoc recursion 대신 dependency graph
문서는 직접 재귀로 다른 선언을 type-check하는 현재 방식이 문제라고 본다.
대신
- dependency graph
- priority queue
- cycle detection
을 통한 반복적 해결을 제안한다.

이 포인트는 오늘날 [[request-evaluator]]를 같이 읽을 때 가장 의미가 크다.
완전히 동일한 구현이 됐다는 뜻은 아니지만,
“dependency를 명시적 단위로 쪼개고 순환을 다루는 방식”이라는 문제의식은 매우 가깝다.

### 3. semantic side table 아이디어
이 문서는 semantic information을 AST에 직접 다 쌓기보다
side table로 분리하는 방향도 제안한다.
이건 incremental compilation과 lazy evaluation 감각까지 염두에 둔 제안이다.

즉 이 proposal은 단순 리팩터링이 아니라
Swift front-end를 더 lazy하고 order-independent하게 만들려는 설계 문서다.

## 현재 구현과 어떻게 이어 읽을 수 있나

### 1. TypeChecker 자체
현재 위키의 [[type-checker]]는
constraint generation / solving / application 중심 설명이다.
여기에 이 proposal을 붙여 읽으면,
표현식 타입 추론 이전에 declaration/Sema architecture 자체가 얼마나 어려운지 보인다.

### 2. Request Evaluator
이 proposal을 가장 자연스럽게 이어서 읽을 페이지는 [[request-evaluator]]다.
왜냐하면 둘 다
- 의존성을 잘게 나누고
- 필요한 정보만 demand-driven으로 계산하고
- cycle을 체계적으로 다루려는 방향
을 공유하기 때문이다.

### 3. Diagnostics / compiler performance
순환 의존, 순서 의존, 과도한 eager validation 문제는
결국 오류 품질과 성능 문제로 이어진다.
그래서 이 proposal은 다음 페이지와도 강하게 연결된다.

- [[diagnostics]]
- [[compiler-performance]]
- [[official-docs/type-checker-design-and-implementation]]

## proposal을 읽을 때 특히 볼 부분

### Phase 분리
- extension binding
- generic signature resolution
- declaration validation
- attribute/semantics checking
이 구분은 지금 봐도 매우 중요하다.

### Order independence
문서는 declaration order에 따라 결과가 달라지는 문제를 매우 심각하게 본다.
이건 Swift 사용자 입장에서는 이상한 버그로 보이지만,
구현 관점에서는 dependency 관리 실패의 징후다.

### Minimal work
proposal은 “필요한 만큼만 검사하자”를 반복해서 강조한다.
이건 이후 Swift front-end 전반의 lazy evaluation 감각과 닿아 있다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/DeclarationTypeChecker.rst`
- `swift/lib/Sema/`
- `swift/lib/Sema/TypeChecker*.cpp`
- `swift/lib/Sema/CSGen.cpp`
- `swift/lib/Sema/CSSolver.cpp`
- `swift/lib/Sema/CSApply.cpp`

현재 위키 연결:
- [[type-checker]]
- [[request-evaluator]]
- [[diagnostics]]
- [[compiler-performance]]

## 이 문서를 오늘 기준으로 어떻게 읽어야 하나

- “이 proposal이 그대로 구현되었는가?”보다
- “Swift front-end가 어떤 고통을 겪고 있었고 어떤 방향으로 진화했는가?”를 보는 편이 좋다.

즉 이 문서는 현재 구현 설명서가 아니라,
현대 Swift Sema가 왜 dependency-driven / laziness / phase separation을 중시하게 되었는지를 보여 주는 역사 문서다.

## 추천 읽기 순서

1. [[proposal-declaration-type-checker-to-sema]]
2. [[type-checker]]
3. [[request-evaluator]]
4. [[diagnostics]]
5. [[compiler-performance]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[swift-type-system]]
- [[type-checker]]
- [[request-evaluator]]
- [[diagnostics]]
- [[compiler-performance]]
- [[official-docs/type-checker-design-and-implementation]]
- [[keyword-network]]
