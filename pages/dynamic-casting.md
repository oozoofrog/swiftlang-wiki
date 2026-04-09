---
type: concept
category: compiler
tags: [casting, is, as, runtime, type-system]
aliases: [동적 캐스팅, Dynamic Casting]
sources: [dynamic-casting.md]
---

# 동적 캐스팅 동작

`is`, `as?`, `as!` 연산자의 상세 동작 규격. 원본: `swift/docs/DynamicCasting.md`

## 세 가지 캐스팅 연산자

| 연산자 | 이름 | 반환 |
|--------|------|------|
| `is` | 캐스트 테스트 | `Bool` |
| `as?` | 조건부 캐스트 | `Optional<T>` |
| `as!` | 강제 캐스트 | `T` (실패 시 trap) |

## 불변식

```swift
x is T == ((x as? T) != nil)
(x as? T) == (x is T) ? .some(x as! T) : nil
x as! T  ≡  (x as? T)!
```

`is`와 `as!`는 `as?`로 구현 가능하고, 그 역도 성립.

## 주요 캐스팅 규칙

- **Identity cast**: 자기 타입으로 캐스팅은 항상 성공
- **Class upcast/downcast**: 표준 OOP 규칙
- **Protocol conformance**: 프로토콜 준수 여부로 캐스팅
- **Optional unwrapping**: `T?` → `T` 캐스팅
- **Existential boxing/unboxing**: `Any`/프로토콜 타입 변환
- **Bridging**: Swift ↔ ObjC 타입 브릿징 (`String` ↔ `NSString`)

## 런타임 구현

`swift_dynamicCast` 런타임 함수가 핵심. [[abi-type-metadata]]를 활용하여 타입 호환성 판단.

관련 페이지: [[runtime]], [[abi-type-metadata]], [[glossary-compiler]]
