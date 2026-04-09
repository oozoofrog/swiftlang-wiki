---
type: entity
category: sil
tags: [sil, function, conventions, calling-convention]
aliases: [SIL 함수 규약]
sources: [sil-function-conventions.md]
---

# SIL 함수 호출 규약

SIL 함수의 파라미터/결과 전달 규약. 원본: `swift/docs/SIL/SILFunctionConventions.md`

## 파라미터 규약

- **@in**: 간접 전달, callee가 소유권 획득
- **@inout**: 간접 전달, 수정 가능, caller가 소유권 유지
- **@owned**: 직접 전달, callee가 소유권 획득
- **@guaranteed**: 직접 전달, caller가 소유권 유지 (대여)

## 결과 규약

- **@out**: 간접 반환
- **@owned**: 직접 반환, caller가 소유권 획득
- **@unowned**: 직접 반환, 소유권 없음

관련 페이지: [[sil-reference]], [[sil-function-attributes]], [[sil-ownership]]
