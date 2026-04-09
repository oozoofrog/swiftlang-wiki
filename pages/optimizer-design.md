---
type: entity
category: sil
tags: [optimizer, pipeline, passes, performance]
aliases: [옵티마이저 설계, SIL Optimizer]
sources: [optimizer-design.md]
---

# Swift 옵티마이저 설계

SIL 수준 최적화 파이프라인의 설계 문서. 원본: `swift/docs/OptimizerDesign.md`

## 파이프라인 개요

```
Swift Source → SILGen → Mandatory Passes → Optimization Passes → IRGen → LLVM
```

SIL 수준에서 최적화하는 이유: IRGen으로 LLVM IR에 내리면 고수준 시맨틱 정보가 소실되어, LLVM 옵티마이저가 클로저 인라이닝, 가상 메서드 CSE 등을 수행할 수 없다.

## 패스 매니저

- 함수를 **bottom-up** 순서로 처리 (callee → caller)
- 최적화 순서는 `Passes.cpp`에 정적 정의
- 분석(Analysis) 등록 및 무효화 관리

## 패스 종류

### Function Pass
- 전체 모듈 검사 가능, 단일 함수만 수정
- 예: LICM, CSE, ARC 최적화

### Module Pass
- 전체 모듈을 스캔/변환
- 예: Generic Specializer (top-down 타입 정보 전파)

## 주요 분석 (Analysis)

| 분석 | 역할 |
|------|------|
| AliasAnalysis | 포인터 앨리어싱 |
| CallGraphAnalysis | 호출 그래프 |
| DominatorTreeAnalysis | 지배 트리 |
| LoopAnalysis | 루프 구조 |
| SideEffectAnalysis | 부수 효과 |

## 주요 최적화 패스

- **Inlining**: 함수 인라이닝 (크로스 모듈 포함)
- **Devirtualization**: 가상 메서드 호출을 직접 호출로 변환
- **Generic Specialization**: 제네릭 함수를 구체 타입으로 특수화
- **ARC Optimization**: 불필요한 retain/release 제거 ([[sil-arc-optimization]])
- **Dead Code Elimination**: 도달 불가 코드 제거
- **Closure Optimization**: 클로저 최적화 (특수화, 인라이닝)

## 파일 위치

- `swift/lib/SILOptimizer/` — 전체 옵티마이저
  - `PassManager/` — 패스 매니저
  - `Analysis/` — 분석
  - `ARC/` — ARC 최적화
  - `FunctionSignatureTransforms/` — 함수 시그니처 변환
  - `SILCombiner/` — SIL 결합 최적화
  - `Differentiation/` — 자동 미분

관련 페이지: [[sil-reference]], [[overview]], [[sil-arc-optimization]], [[sil-utilities]], [[debugging-the-compiler]], [[compiler-performance]]
