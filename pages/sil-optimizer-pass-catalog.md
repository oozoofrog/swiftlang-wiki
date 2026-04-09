---
type: entity
category: sil
tags: [sil, optimizer, passes, catalog, pipeline]
aliases: [SIL 패스 카탈로그, SIL Optimizer Passes]
sources: []
---

# SIL 옵티마이저 패스 카탈로그

`Passes.def`와 소스 디렉토리 분석에서 추출한 SIL 최적화 패스 전체 목록.

## 패스 통계

| 종류 | 수 | 설명 |
|------|-----|------|
| PASS | 42 | Swift로 구현된 함수 패스 (신규 패스는 여기) |
| MODULE_PASS | 9 | Swift로 구현된 모듈 패스 |
| LEGACY_PASS | 151 | C++로 구현된 레거시 패스 |
| IRGEN_PASS | 3 | IRGen 단계에서 실행되는 패스 |
| **합계** | **205** | |

> 신규 패스는 Swift로 구현 (`PASS`/`MODULE_PASS`). 기존 C++ 패스(`LEGACY_PASS`)는 점진적으로 마이그레이션 중.

## 디렉토리 구조

| 디렉토리 | 파일 수 | 역할 |
|----------|---------|------|
| `Mandatory/` | 55 | 필수 패스 (raw → canonical SIL) |
| `Transforms/` | 32 | 성능 최적화 변환 |
| `Utils/` | 36 | 공유 유틸리티 |
| `UtilityPasses/` | 31 | 디버깅/분석 유틸리티 패스 |
| `Analysis/` | 28 | 분석 (alias, callgraph, dominance, escape 등) |
| `ARC/` | 11 | ARC 최적화 ([[sil-arc-optimization]]) |
| `Differentiation/` | 10 | 자동 미분 |
| `SemanticARC/` | 8 | OSSA 기반 ARC 최적화 |
| `FunctionSignatureTransforms/` | 6 | 함수 시그니처 변환 |
| `IPO/` | 6 | 프로시저 간 최적화 |
| `LoopTransforms/` | 6 | 루프 최적화 |
| `SILCombiner/` | 5 | 인스트럭션 결합 |
| `PassManager/` | 5 | 패스 관리자 + 파이프라인 정의 |

## 주요 패스 분류

### Mandatory (진단 + 정규화)
- `DefiniteInitialization` — DI: 모든 변수 초기화 검증
- `DiagnoseStaticExclusivity` — 메모리 배타성 정적 검사
- `DiagnoseUnreachable` — 도달 불가 코드 진단
- `MandatoryInlining` — `@_transparent` 함수 인라이닝
- `RawSILInstLowering` — raw SIL 인스트럭션 정규화
- `SendNonSendable` — Sendable 검사
- `MoveOnlyChecker` — ~Copyable 타입 검사
- `FlowIsolation` — actor isolation 진단

### Performance Optimization
- `GenericSpecializer` — 제네릭 함수를 구체 타입으로 특수화
- `Devirtualizer` — 가상 호출 → 직접 호출
- `PerfInliner` / `EarlyPerfInliner` — 성능 인라이닝
- `CSE` / `HighLevelCSE` — 공통 하위 표현 제거
- `DCE` — 죽은 코드 제거
- `SimplifyCFG` — CFG 단순화
- `SROA` — 집합체 분해 (Scalar Replacement of Aggregates)
- `Mem2Reg` — 메모리 → 레지스터 승격
- `LoopRotate` / `LoopUnroll` — 루프 변환
- `ClosureSpecialization` — 클로저 특수화
- `StringOptimization` — String 타입 최적화
- `COWArrayOpts` — Copy-on-Write 배열 최적화

### ARC 최적화
- `ARCSequenceOpts` — retain/release 시퀀스 최적화
- `SemanticARCOpts` — OSSA 기반 ARC 최적화
- `RetainSinking` / `ReleaseHoisting` — retain/release 이동
- `CopyPropagation` — 복사 전파

### Move/Ownership
- `MoveOnlyObjectChecker` / `MoveOnlyAddressChecker`
- `ConsumeOperatorCopyableValuesChecker`
- `OwnershipModelEliminator` — OSSA → plain SSA lowering

## 파이프라인 정의

`PassPipeline.cpp`에서 정의. 주요 파이프라인:
- **Diagnostic Pipeline**: SILGen 직후 실행 (mandatory passes)
- **Performance Pipeline**: `-O` 최적화 시 실행
- **Lowering Pipeline**: OSSA lowering, IRGen 준비

디버깅 플래그:
- `-sil-print-all`: 모든 패스 후 SIL 출력
- `-sil-opt-pass-count=N`: N번째 패스까지만 실행

관련 페이지: [[optimizer-design]], [[sil-reference]], [[sil-arc-optimization]], [[debugging-the-compiler]], [[swift-compiler-sources]]
