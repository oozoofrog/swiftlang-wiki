---
type: entity
category: sil
tags: [sil, memory, access, exclusivity]
aliases: [SIL 메모리 접근]
sources: [sil-memory-access.md]
---

# SIL 메모리 접근 모델

SIL에서 메모리 접근의 배타성(exclusivity) 모델. 원본: `swift/docs/SIL/SILMemoryAccess.md`

## 접근 종류

- **read**: 읽기 전용 접근
- **modify**: 수정 접근 (배타적)
- **init**: 초기화 접근
- **deinit**: 소멸 접근

## 접근 범위

`begin_access` / `end_access` 인스트럭션으로 접근 범위를 명시한다. 배타성 규칙은 Swift의 메모리 안전성 보장의 핵심이다.

## 접근 강제 수준

- **static**: 컴파일 타임 검증
- **dynamic**: 런타임 검사
- **unsafe**: 검사 없음

관련 페이지: [[proposal-in-place-operations-to-writeback-and-cow]], [[proposal-initialization-and-accessors-to-property-model]], [[sil-reference]], [[keyword-network]], [[sil-instructions]], [[sil-ownership]], [[concurrency-data-race-safety]], [[runtime]]
