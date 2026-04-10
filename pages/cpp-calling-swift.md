---
type: entity
category: compiler
tags: [cpp-interop, exposing-swift]
aliases: [C++에서 Swift 호출, calling Swift from C++]
sources: [cpp-calling-swift-from-cpp.md, cpp-swift-type-representation.md]
---

# C++에서 Swift 호출하기

Swift 컴파일러가 생성하는 C++ 헤더(`ModuleName-Swift.h`)를 `#include`하여 Swift API를 C++에서 사용한다. Clang에서만 컴파일 가능하며 C++17 이상 필요(C++20 권장).

## 생성 헤더

Swift 모듈은 C++ 네임스페이스로 매핑된다. `MyModule::myFunction()`처럼 접근.

## Swift 타입의 C++ 표현

- **기본 타입**: `Int` → `swift::Int`, `Float` → `float`, `Bool` → `bool`
- **구조체**: 불투명 버퍼(`alignas(N) char buffer[M]`) 내장 C++ 클래스. 복사/소멸 자동 생성.
- **Resilient 타입**: 크기에 따라 인라인 버퍼 또는 힙 할당(boxed).
- **Enum**: C++ 클래스로 표현, 연관값 접근용 메서드 생성.
- **Class**: ARC가 C++ 복사 생성자/소멸자에 통합.

## 지원 현황

| 기능 | 상태 |
|------|------|
| 최상위 함수 | 지원 |
| 구조체/enum/클래스 | 지원 |
| 프로퍼티 getter/setter | 지원 |
| 제네릭 함수 | 부분 (제약 조건 없는 경우) |
| 클로저, 프로토콜 타입 | 미지원 |

## 관련 파일

- `swift/lib/PrintAsClang/` — C++ 헤더 생성기
- `swift/test/Interop/SwiftToCxx/` — 테스트

관련 페이지: [[cpp-interop-overview]], [[keyword-network]], [[abi-mangling]], [[modules]], [[cpp-using-from-swift]], [[objc-interop]], [[swift-compiler-architecture]]
