---
type: entity
category: compiler
tags: [dependency, incremental-build, provides-depends]
aliases: [의존성 분석, Dependency Analysis, 증분 빌드]
sources: [dependency-analysis.md]
---

# 의존성 분석 (증분 빌드)

Swift 모듈 내 파일 간 의존성 분석. 원본: `swift/docs/DependencyAnalysis.md`

## 기본 원리

"provides / depends" 시스템: 각 파일이 제공하는 것과 의존하는 것을 추적하여, 변경된 파일이 제공하는 것에 의존하는 파일만 재빌드.

> **황금률**: 보수적으로 판단. 불필요한 재빌드는 짜증나지만, 필요한 재빌드를 하지 않으면 **디버그 타임 미스컴파일**.

## 의존성 종류

| 종류 | 설명 |
|------|------|
| `top-level` | 모듈 스코프의 비한정 이름 사용/정의 |
| `nominal` | 특정 타입 사용 (맹글된 이름으로 식별) |
| `member` | 타입의 특정 멤버 제공/접근 |
| `dynamic-lookup` | `AnyObject`를 통한 `@objc` 멤버 접근 |

## 특수 케이스: 빈 멤버 이름

멤버 이름이 빈 `member` 항목 = 타입에 비-private 멤버가 추가될 때마다 재빌드 필요. 상속(superclass, protocol conformance)에 사용.

## 제공/의존 추적

- **provides**: 타입 검사 완료 후 계산
- **depends**: 컴파일러 조회(qualified/unqualified lookup, protocol conformance check)를 계측하여 추적

관련 페이지: [[request-evaluator]], [[compiler-driver]], [[overview]]
