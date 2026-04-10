---
type: entity
category: sil
tags: [sil, types, type-system]
aliases: [SIL 타입]
sources: [sil-types.md]
---

# SIL 타입

SIL 타입 시스템에 대한 레퍼런스. 원본: `swift/docs/SIL/Types.md`

SIL 타입은 Swift의 타입 시스템 위에 구축되며, 값의 메모리 표현과 소유권 규약을 명시한다. SIL에서 타입은 address type과 object type으로 구분된다.

- **Object type** (`$T`): 로드 가능한 값. 레지스터에 저장 가능
- **Address type** (`$*T`): 메모리 주소를 나타냄. 포인터와 유사

## 주요 타입 분류

- **Loadable type**: 크기가 알려져 있어 직접 로드/저장 가능
- **Address-only type**: 크기 미정 또는 소유권 규칙으로 인해 주소로만 접근
- **Trivial type**: 복사/소멸 시 참조 카운팅 불필요 (예: `Int`, `Float`)

관련 페이지: [[sil-reference]], [[keyword-network]], [[sil-instructions]], [[sil-ownership]], [[sil-function-conventions]], [[abi-type-layout]], [[abi-type-metadata]]
