---
type: entity
category: compiler
tags: [abi, type-metadata, runtime, reflection]
aliases: [타입 메타데이터, Type Metadata]
sources: [abi-type-metadata.rst]
---

# ABI: 타입 메타데이터

모든 Swift 타입의 런타임 메타데이터 레코드 레이아웃. 원본: `swift/docs/ABI/TypeMetadata.rst`

## 개요

Swift 런타임은 프로그램에서 사용되는 모든 타입에 대해 **메타데이터 레코드**를 유지한다:
- 비제네릭 nominal 타입: 컴파일러가 정적 생성
- 제네릭 인스턴스, 튜플, 함수 등: 런타임이 lazy 생성
- **두 메타데이터 포인터가 같으면 같은 타입**

## 공통 레이아웃

모든 메타데이터는 공통 헤더를 공유:

| 오프셋 | 필드 | 설명 |
|--------|------|------|
| -1 | **Value Witness Table** | 값 시맨틱(allocate, copy, destroy) 연산 vtable |
| 0 | **kind** | 메타데이터 종류 식별 |

## Kind 값

| 값 | 타입 |
|----|------|
| 0 | Class (ObjC 상호운용 시 isa 포인터) |
| 1 | Struct |
| 2 | Enum |
| 3 | Optional |
| 8 | Opaque (Builtin 프리미티브) |
| 9 | Tuple |
| 10 | Function |
| 12 | Protocol (합성, Any 포함) |
| 13 | Metatype |
| >2047 | ObjC 상호운용 클래스 (isa 포인터) |

## 타입별 추가 레이아웃

- **Struct**: nominal type descriptor + generic argument vector + field offsets
- **Class**: superclass pointer + vtable entries
- **Enum**: nominal type descriptor + generic arguments + payload 정보
- **Tuple**: 요소 수 + 레이블 + 요소 타입 포인터

관련 페이지: [[abi-type-layout]], [[abi-mangling]], [[abi-calling-convention]], [[abi-stability]], [[runtime]], [[dynamic-casting]], [[glossary-compiler]]
