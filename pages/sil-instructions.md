---
type: entity
category: sil
tags: [sil, instructions, opcodes]
aliases: [SIL 인스트럭션]
sources: [sil-instructions.md]
---

# SIL 인스트럭션

SIL 인스트럭션 목록 레퍼런스. 원본: `swift/docs/SIL/Instructions.md`

SIL 인스트럭션은 Swift 프로그램의 연산을 표현하는 단위이다. SSA 형식이므로 각 인스트럭션은 하나의 결과 값을 정의(또는 결과 없음)한다.

## 주요 인스트럭션 카테고리

- **Allocation/Deallocation**: `alloc_stack`, `alloc_ref`, `alloc_box`, `dealloc_stack` 등
- **Memory Access**: `load`, `store`, `copy_addr`, `begin_access`, `end_access`
- **Reference Counting**: `strong_retain`, `strong_release`, `copy_value`, `destroy_value`
- **Function Application**: `apply`, `try_apply`, `partial_apply`, `begin_apply`
- **Control Flow**: `br`, `cond_br`, `switch_enum`, `return`, `unreachable`
- **Type Conversion**: `upcast`, `unconditional_checked_cast`, `thin_to_thick_function`
- **Struct/Tuple**: `struct`, `struct_extract`, `tuple`, `tuple_extract`
- **Enum**: `enum`, `unchecked_enum_data`, `select_enum`

## OSSA 전용 인스트럭션

- `copy_value` / `destroy_value` — 소유권 명시적 복사/소멸
- `begin_borrow` / `end_borrow` — 대여 범위 표시
- `move_value` — 소유권 이전

관련 페이지: [[sil-reference]], [[sil-types]], [[sil-ownership]], [[sil-memory-access]]
