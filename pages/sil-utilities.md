---
type: entity
category: sil
tags: [sil, utilities, infrastructure]
aliases: [SIL 유틸리티]
sources: [sil-utilities.md]
---

# SIL 유틸리티

SIL 분석 및 변환을 위한 유틸리티 인프라. 원본: `swift/docs/SIL/SIL-Utilities.md`

## 주요 유틸리티

- **InstructionUtils**: 인스트럭션 패턴 매칭 및 조작
- **BasicBlockUtils**: 기본 블록 분할, 병합
- **SILCloner**: SIL 함수/블록 복제
- **OwnershipUtils**: 소유권 분석 헬퍼

## 분석 (Analysis)

최적화 패스가 사용하는 미리 계산된 정보:
- **AliasAnalysis**: 포인터 앨리어싱 분석
- **CallGraphAnalysis**: 호출 그래프
- **DominatorTreeAnalysis**: 지배 트리
- **LoopAnalysis**: 루프 구조
- **EscapeAnalysis**: 값 탈출 분석

관련 페이지: [[sil-reference]], [[optimizer-design]]
