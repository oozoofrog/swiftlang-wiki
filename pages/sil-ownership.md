---
type: concept
category: sil
tags: [sil, ownership, ossa, memory-safety]
aliases: [OSSA, Ownership SSA, SIL 소유권]
sources: [sil-ownership.md]
---

# SIL 소유권 모델 (OSSA)

Ownership SSA는 SIL 값의 소유권 불변식을 정적으로 검증하는 시스템이다. 원본: `swift/docs/SIL/Ownership.md`

## 소유권 종류

SIL 값은 다음 중 하나의 소유권을 가진다:

- **Owned**: 값의 소유자. 소멸 책임이 있음 (`destroy_value`)
- **Guaranteed**: 대여된 값. 대여 범위 내에서만 유효 (`begin_borrow`/`end_borrow`)
- **Unowned**: 소유권 없음. 참조 카운팅과 무관
- **None**: 소유권 개념이 적용되지 않는 trivial 값

## 핵심 불변식

1. 모든 owned 값은 정확히 한 번 소멸되어야 한다
2. guaranteed 값은 대여 범위 안에서만 사용 가능
3. 값의 모든 사용은 해당 값의 수명 내에 있어야 한다

## 파이프라인에서의 위치

```
SILGen(OSSA) → Mandatory Passes(OSSA) → 일부 Optimization(OSSA)
→ OSSA Lowering → Plain SSA → IRGen
```

OSSA lowering 이후에는 소유권 검증이 불가능하다.

관련 페이지: [[sil-reference]], [[sil-instructions]], [[sil-arc-optimization]]
