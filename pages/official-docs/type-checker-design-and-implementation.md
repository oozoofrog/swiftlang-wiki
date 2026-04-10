---
type: reference
category: official-docs
tags: [official-docs, type-checker, sema, constraints]
aliases: [TypeChecker.md, Type Checker Design and Implementation]
sources: [swiftlang-swift/docs/TypeChecker.md]
---

# TypeChecker.md 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/TypeChecker.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/TypeChecker.md

## 이 문서는 무엇을 설명하나

Swift 타입 체커의 제약식 모델, 풀이 절차, 오버로드 선택, 성능 최적화 포인트를 설명하는 핵심 구현 문서다.

## 핵심 포인트

- 타입 검사를 Constraint Generation → Solving → Solution Application의 세 단계로 정리한다.
- 양방향 타입 추론과 오버로드 해결을 하나의 constraint 시스템으로 설명한다.
- disjunction, locator, score 같은 실제 solver 어휘를 배울 수 있다.
- connected components, worklist simplification, online scoring 같은 실전 성능 기법도 함께 담고 있다.

## 컴파일러와 어떻게 연결되나

- lib/Sema / ConstraintSystem
- CSGen.cpp / CSSolver.cpp / CSApply.cpp
- ConstraintLocator와 진단 생성
- 표현식 타입 추론의 병목 분석

## 언어 표면에서 어떻게 들어오면 좋은가

- 오버로드 함수와 메서드
- 리터럴 추론
- 클로저와 멤버 조회
- `as` 캐스트 / `inout` / 삼항 연산자

## 같이 보면 좋은 위키 페이지

- [[type-checker]]
- [[diagnostics]]
- [[compiler-performance]]
- [[request-evaluator]]
- [[generics-manifesto]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

기존 `[[type-checker]]`가 개념 요약이라면 이 페이지는 공식 문서의 용어와 단계 구조를 그대로 따라가며 읽는 데 초점을 둔다.
