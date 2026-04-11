---
type: entity
category: compiler
tags: [abi, type-layout, memory, struct, enum]
aliases: [타입 레이아웃, Type Layout]
sources: [abi-type-layout.rst]
---

# ABI: 타입 레이아웃

Swift 타입의 메모리 레이아웃 알고리즘. 원본: `swift/docs/ABI/TypeLayout.rst`

## Struct/Tuple 레이아웃 ("Universal" 알고리즘)

1. size=0, alignment=1로 시작
2. 각 필드를 선언 순서대로:
   - size를 필드 alignment로 올림
   - 필드 offset = 현재 size
   - size += 필드 size
   - alignment = max(alignment, 필드 alignment)
3. stride = size를 alignment로 올림

### C와의 차이

- **size와 stride가 구분됨**: 외부 struct가 내부 struct의 tail padding에 필드 배치 가능
- **zero-size struct 허용**: 집합 내 저장 공간 불필요
- LLVM packed struct로 직접 레이아웃 제어

```
// Swift                    LLVM
struct S { x: Int, y: UInt8 }   → <{ i64, i8 }>
struct Empty {}                  → <{}>
```

## Class 레이아웃

- ObjC 런타임에 의존 (Apple 플랫폼)
- root class는 안정적이어야 함 (metaclass 계층 보존)
- 암시적 root: `SwiftObject` (ObjC 클래스)

## Enum 레이아웃

- 단일 payload enum: payload + extra inhabitants + tag bytes
- 다중 payload enum: payload union + tag
- no-payload enum: C enum과 유사

관련 페이지: [[proposal-enums-and-enum-style-to-type-system-and-layout]], [[proposal-option-sets-to-importer-and-layout]], [[abi-type-metadata]], [[abi-mangling]], [[abi-calling-convention]], [[abi-stability]], [[runtime]]
