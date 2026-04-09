---
type: entity
category: compiler
tags: [abi, mangling, demangling, symbols]
aliases: [맹글링, Mangling, 디맹글링, Demangling]
sources: [abi-mangling.rst]
---

# ABI: 심볼 맹글링

Swift의 안정적 심볼 맹글링 체계. 원본: `swift/docs/ABI/Mangling.rst`

## 맹글링 접두사

| 접두사 | 버전 |
|--------|------|
| `$s` | Swift stable mangling (현재) |
| `@__swiftmacro_` | 매크로 파일명 맹글링 |
| `_T0` | Swift 4.0 |
| `$S` | Swift 4.2 |
| `$e` | Embedded Swift (불안정) |

## 맹글링 구조

**Post-fix 순서**: 식별자가 먼저 오고, 이후 타입 연산자가 해석 방법을 결정한다.

```
4Test3FooC   // trailing 'C'가 Foo를 Test 모듈의 class로 지정
```

- 연산자는 단일 문자(중요) 또는 여러 문자+숫자(부가) 형태
- 모듈 이름이 항상 맹글링 시작 부분에 위치 → 공통 접두사 최적화

## Symbolic Reference

바이너리 내에서 타입 참조를 효율화하기 위해 포인터를 직접 임베딩:

- 제어 문자 `\x01`~`\x17`: 상대 참조 (4바이트)
- 제어 문자 `\x18`~`\x1F`: 절대 참조 (포인터 크기)
- 컴파일러가 생성한 메타데이터에만 유효
- 외부 입력의 맹글링 이름에서는 symbolic reference를 **거부해야 함**

## 디맹글링

`swift_stdlib_demangleName` 함수가 맹글링된 심볼을 사람이 읽을 수 있는 이름으로 변환.

### 파일 위치

- `swift/lib/SwiftDemangle/` — 디맹글링 라이브러리
- `swift/include/swift/Demangling/` — 디맹글러 헤더
- `swift/stdlib/public/runtime/` — 런타임 디맹글링 지원

관련 페이지: [[runtime]], [[abi-type-metadata]], [[abi-type-layout]], [[abi-calling-convention]], [[abi-stability]], [[glossary-compiler]]
