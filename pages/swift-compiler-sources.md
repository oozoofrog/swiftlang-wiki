---
type: entity
category: compiler
tags: [swift-in-swift, compiler-sources, optimizer, sil]
aliases: [SwiftCompilerSources, Swift-in-Swift 컴파일러]
sources: []
---

# SwiftCompilerSources (Swift-in-Swift)

Swift로 작성된 컴파일러 구성 요소. C++ 컴파일러를 점진적으로 Swift로 마이그레이션하는 방향.

## 모듈 구조

| 모듈 | 파일 수 | 역할 |
|------|---------|------|
| `Optimizer/` | **115** | SIL 최적화 패스 (Swift 구현) |
| `SIL/` | **39** | SIL IR 자료 구조의 Swift 래퍼 |
| `AST/` | **8** | AST 노드의 Swift 브릿징 |
| `Basic/` | **3** | 기본 유틸리티 |
| **합계** | **165** | |

## Optimizer 모듈 (핵심)

`Passes.def`에서 `PASS`/`MODULE_PASS`로 등록된 42+9=51개의 신규 패스가 모두 Swift로 구현되어 있다. 주요 패스:

- `AllocBoxToStack` — 박스 → 스택 승격
- `Simplification` — 인스트럭션 단순화
- `DestroyHoisting` — destroy 인스트럭션 호이스팅
- `RedundantLoadElimination` — 중복 로드 제거
- `StackPromotion` — 힙 → 스택 승격
- `ClosureSpecialization` — 클로저 특수화
- `ComputeEscapeEffects` / `ComputeSideEffects` — 효과 분석

## C++ Bridging

Swift 코드가 C++ 컴파일러와 상호 작용하는 방법:

1. **Bridging headers**: `SIL/` 모듈이 C++ SIL 자료 구조를 Swift로 래핑
2. **@_cdecl / @_silgen_name**: C++ 에서 Swift 패스를 호출하기 위한 엔트리 포인트
3. **registerSwiftPasses()**: Swift 패스를 C++ 패스 매니저에 등록

## 마이그레이션 현황

- **완료**: 42개 함수 패스 + 9개 모듈 패스 (Swift)
- **레거시**: 151개 패스 (C++, `LEGACY_PASS`)
- **방향**: 새로운 패스는 반드시 Swift로 작성. 기존 패스는 점진적 마이그레이션

## 파일 위치

- `swift/SwiftCompilerSources/Sources/` — Swift 소스
- `swift/SwiftCompilerSources/CMakeLists.txt` — 빌드 설정
- `swift/SwiftCompilerSources/Package.swift` — SPM 매니페스트

관련 페이지: [[sil-optimizer-pass-catalog]], [[optimizer-design]], [[sil-reference]], [[overview]]
