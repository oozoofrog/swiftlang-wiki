---
type: entity
category: compiler
tags: [type-checker, sema, type-inference, constraints]
aliases: [타입 체커, TypeChecker, Sema]
sources: [type-checker.md]
---

# 타입 체커 설계 및 구현

Swift 타입 체커의 설계 문서. 원본: `swift/docs/TypeChecker.md`

## 핵심 특징

Swift는 **양방향 타입 추론** (bi-directional type inference)을 사용한다:
- **Bottom-up**: 표현식 리프에서 루트로 타입 전파 (일반적)
- **Top-down**: 컨텍스트 타입에서 리프로 타입 전파 (ML-like)

예: `var eFloat: Float = -identity(2.71828)` — `Float` 컨텍스트가 리터럴 타입 결정

## 세 단계 파이프라인

### 1. Constraint Generation
입력 표현식에서 타입 제약조건 집합 생성. 미지 타입은 **type variable**로 표현.

### 2. Constraint Solving
제약 시스템을 풀어 각 type variable에 구체 타입 할당. 여러 대안 중 가장 구체적인 해 선택.

### 3. Solution Application
제약 해를 적용하여 모든 암시적 변환과 오버로드를 해결한 well-typed 표현식 생성. 이 단계는 실패할 수 없다.

## 설계 원칙

- **제약 기반 접근**: Hindley-Milner 유사하지만, 제약 다형성 + 오버로딩 지원
- **범위 제한**: 추론은 단일 표현식/문 범위 — 성능과 진단 개선
- **분리된 관심사**: 제약 기술(안정)과 풀이(발전 가능)를 분리

## 파일 위치

- `swift/lib/Sema/` — 의미 분석 전체
  - `TypeChecker*.cpp` — 타입 검사 코어
  - `CSGen.cpp` — Constraint Generation
  - `CSSolver.cpp` — Constraint Solving
  - `CSApply.cpp` — Solution Application

관련 페이지: [[overview]], [[request-evaluator]], [[diagnostics]], [[compiler-performance]], [[generics-manifesto]], [[glossary-compiler]]
