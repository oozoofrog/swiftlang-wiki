---
type: entity
category: compiler
tags: [runtime, abi, memory-management, type-metadata]
aliases: [Swift 런타임, Runtime ABI]
sources: [runtime.md]
---

# Swift 런타임

Swift 런타임 ABI 인터페이스. 원본: `swift/docs/Runtime.md`

## 핵심 기능

1. **메모리 관리**: 할당 및 참조 카운팅
   - `swift_allocObject` / `swift_deallocObject`
   - `swift_retain` / `swift_release`
   - `swift_allocBox` / `swift_deallocBox`

2. **런타임 타입 시스템**:
   - Dynamic casting (`is`, `as?`, `as!`)
   - 제네릭 인스턴스화
   - 프로토콜 conformance 등록

## 디맹글링

`swift_stdlib_demangleName` — Swift 맹글된 심볼 이름을 사람이 읽을 수 있는 형식으로 변환.

맹글링 규격: `swift/docs/ABI/Mangling.rst`

## 파일 위치

- `swift/stdlib/public/runtime/` — 런타임 구현
- `swift/lib/SwiftDemangle/` — 디맹글링 라이브러리
- `swift/include/swift/Runtime/` — 런타임 헤더

관련 페이지: [[overview]], [[standard-library-runtime-and-compiler]], [[abi-mangling]], [[abi-type-metadata]], [[abi-type-layout]], [[abi-stability]], [[dynamic-casting]], [[glossary-compiler]]
