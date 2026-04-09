---
type: entity
category: compiler
tags: [abi, calling-convention, function, registers]
aliases: [호출 규약, Calling Convention]
sources: [abi-calling-convention.rst]
---

# ABI: 호출 규약

Swift 함수의 호출 규약. 원본: `swift/docs/ABI/CallingConvention.rst`

## Swift 호출 규약 개요

Swift는 C 호출 규약과 별도의 자체 호출 규약을 사용한다:

- **소유권 전달**: 파라미터 소유권이 호출 규약의 핵심 — owned, guaranteed, inout
- **간접 반환**: 큰 값은 간접 반환 (caller가 메모리 할당)
- **에러 반환**: 별도 에러 레지스터로 throwing 함수의 에러 전달
- **self 파라미터**: 메서드에서 마지막 파라미터로 전달

## 파라미터 전달

- **작은 값**: 레지스터로 직접 전달
- **큰 값/address-only**: 포인터로 간접 전달
- `@in`, `@inout`, `@owned`, `@guaranteed` → [[sil-function-conventions]] 참조

## 특수 레지스터 (Apple 플랫폼)

- **self**: 별도 레지스터
- **error**: throwing 함수의 에러 결과
- **context**: 클로저 컨텍스트 포인터

관련 페이지: [[sil-function-conventions]], [[abi-mangling]], [[abi-type-metadata]], [[abi-type-layout]], [[abi-stability]], [[runtime]]
