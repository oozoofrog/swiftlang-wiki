---
type: entity
category: sil
tags: [sil, arc, optimization, reference-counting]
aliases: [ARC 최적화, ARC Optimization]
sources: [sil-arc-optimization.md]
---

# SIL ARC 최적화

ARC(Automatic Reference Counting) 최적화 패스에 대한 레퍼런스. 원본: `swift/docs/SIL/ARCOptimization.md`

## 목적

불필요한 retain/release 쌍을 제거하여 런타임 오버헤드를 줄인다. SIL 수준에서 소유권과 참조 관계를 분석하여 안전하게 최적화한다.

## 주요 최적화

- **Redundant retain/release elimination**: 불필요한 참조 카운팅 연산 제거
- **Retain sinking / Release hoisting**: retain을 사용 지점 가까이, release를 더 빨리 수행
- **Copy-on-write optimization**: CoW 컨테이너의 불필요한 복사 제거

## 파일 위치

- `swift/lib/SILOptimizer/ARC/` — ARC 최적화 패스 구현

관련 페이지: [[sil-reference]], [[keyword-network]], [[sil-ownership]], [[optimizer-design]], [[high-level-sil-optimizations]], [[compiler-performance]], [[runtime]]
