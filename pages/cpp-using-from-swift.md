---
type: entity
category: compiler
tags: [cpp-interop, importing-cpp]
aliases: [C++를 Swift에서 사용, using C++ from Swift]
sources: [cpp-interop-getting-started.md, cpp-interop-user-manual.md]
---

# C++를 Swift에서 사용하기

Swift에서 C++ API를 호출하려면 상호운용 모드를 활성화하고 Clang 모듈 또는 브리징 헤더로 C++ 선언을 가져온다.

## 활성화

컴파일러 플래그 `-cxx-interoperability-mode=default` 추가.
- **Xcode**: Other Swift Flags에 추가
- **SwiftPM**: `.interoperabilityMode(.Cxx)`
- **CMake**: `CMAKE_Swift_FLAGS`에 설정

## C++ 모듈 임포트

`module.modulemap`으로 C++ 헤더를 모듈 정의 후 `import ModuleName`으로 사용. `import CxxStdlib`로 표준 라이브러리 접근.

## 타입 매핑

- **Owned 타입**: `std::string`, `std::vector` 등은 Swift 값 타입. 복사 생성자/소멸자 자동 호출.
- **참조 타입**: `import_reference` 속성으로 커스텀 참조 카운트 타입을 ARC에 통합.
- **이터레이터**: `begin()`/`end()` 반환 시 자동 `Sequence` 준수.
- **Unsafe 타입**: `import_unsafe` 속성으로 명시적 임포트.

## 호출 규약

인라인 함수, 함수 템플릿(호출 시 인스턴스화) 지원. `const` 참조 → 값 전달, 비-`const` 참조 → `inout`. 예외의 Swift 전파는 미정의 동작이며, 가상 함수/이동 생성자/C++20 모듈은 미지원.

관련 페이지: [[cpp-interop-overview]], [[keyword-network]], [[c-to-swift-name-translation]], [[how-swift-imports-c-apis]], [[objc-interop]], [[modules]], [[cpp-calling-swift]]
