---
type: entity
category: sil
tags: [sil, ir, intermediate-representation, pipeline]
aliases: [SIL, Swift Intermediate Language]
sources: [sil-reference.md]
---

# SIL (Swift Intermediate Language)

SIL은 Swift 컴파일러의 고수준 중간 표현(IR)으로, SSA(Static Single Assignment) 형식이며 풍부한 시맨틱 정보를 유지한다.

## 세 가지 표현

1. **In-memory**: 컴파일러 내부 자료 구조. 최적화 패스가 사용
2. **Textual**: `.sil` 파일. 사람이 읽을 수 있는 형식 (Swift 구문 확장)
3. **Binary**: `.swiftmodule` 파일. 컴파일러 버전 간 호환 불가

## 컴파일러 파이프라인에서의 위치

```
Parser → Sema → SILGen(raw SIL) → Mandatory Passes(canonical SIL)
→ Optimization Passes → IRGen(LLVM IR) → LLVM Backend
```

- **Raw SIL**: SILGen 직후. SSA 그래프 불완전, 데이터플로 오류 허용. `assign` 등 비정규 인스트럭션 포함
- **Canonical SIL**: mandatory pass 이후. 데이터플로 오류 제거, 인스트럭션 정규화 완료. IRGen 입력 가능

## Ownership SSA (OSSA)

SSA 값의 소유권 불변식을 강제하는 확장 형식:
- use-after-free 및 메모리 누수를 정적으로 검증
- SILGen이 OSSA를 생성하며, mandatory + 일부 optimization 단계까지 유지
- 특정 시점에 plain SSA로 "lowering" — 이후 소유권 검증 불가

## 핵심 SIL 문서

| 문서 | 내용 |
|------|------|
| [[sil-types]] | SIL 타입 시스템 |
| [[sil-instructions]] | SIL 인스트럭션 목록 |
| [[sil-ownership]] | 소유권 모델 상세 |
| [[sil-function-attributes]] | 함수 속성 |
| [[sil-function-conventions]] | 함수 호출 규약 |
| [[sil-memory-access]] | 메모리 접근 모델 |
| [[sil-arc-optimization]] | ARC 최적화 |
| [[sil-utilities]] | SIL 유틸리티 |
| [[sil-initializer-conventions]] | 이니셜라이저 규약 |

## 파일 위치

- `swift/lib/SIL/` — SIL 자료 구조 구현
- `swift/lib/SILGen/` — AST → SIL 생성
- `swift/lib/SILOptimizer/` — 최적화 패스
- `swift/lib/SIL/Parser/` — 텍스트 SIL 파서
- `swift/include/swift/SIL/` — SIL 헤더

관련 페이지: [[overview]], [[optimizer-design]], [[debugging-the-compiler]], [[compiler-performance]], [[glossary-compiler]]
