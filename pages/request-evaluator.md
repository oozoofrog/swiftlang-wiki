---
type: entity
category: compiler
tags: [request-evaluator, architecture, lazy-evaluation, caching]
aliases: [요청 평가기, Request Evaluator]
sources: [request-evaluator.md]
---

# Request Evaluator

Swift 컴파일러의 요청 기반 평가 아키텍처. 원본: `swift/docs/RequestEvaluator.md`

## 해결하는 문제

1. **Mutable AST state**: 어떤 상태가 결과에 기여했는지 추적 불가
2. **Lazy type checking**: 다중 파일 타겟에서만 발현되는 버그
3. **Ad hoc recursion**: `LazyResolver` 콜백의 순환 의존성
4. **Coarse-grained queries**: 필요 이상으로 많은 작업 수행

## 핵심 개념

### Request
정보 계산을 기술하는 값 타입. hash/compare 가능. 예:
- `SuperclassTypeRequest(class Foo)` → Type
- `InterfaceTypeRequest(func bar)` → Type
- `FormalAccessRequest(decl x)` → AccessLevel

### 의존성 및 순환 탐지
- evaluator가 요청 스택을 유지하여 의존성 자동 추적
- 순환 감지 시 진단 및 복구
- `-debug-cycles` 플래그로 순환 디버깅

### 캐싱
- evaluator 내부 캐시 또는 "separate caching" (기존 AST 상태 활용)
- 장기적으로 AST mutable state를 evaluator 캐시로 대체 목표

## 증분 의존성 추적

- **Dependency Source**: 의존성 등록 범위 (예: `TypeCheckSourceFileRequest(File.swift)`)
- **Dependency Sink**: 이름 조회 등 의존성 기록 (예: `DirectLookupRequest(Foo, "bar")`)
- evaluator가 자동으로 source/sink 매칭 → 증분 컴파일 정보 생성

## Prior Art

Rust의 [demand-driven compilation](https://rustc-dev-guide.rust-lang.org/query.html)에서 영감.

### 파일 위치

- `swift/include/swift/AST/Evaluator.h` — 핵심 Evaluator 클래스
- `swift/include/swift/AST/SimpleRequest.h` — Request 기본 템플릿

관련 페이지: [[type-checker]], [[dependency-analysis]], [[overview]]
