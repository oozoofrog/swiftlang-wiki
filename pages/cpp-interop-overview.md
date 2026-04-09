---
type: summary
category: compiler
tags: [cpp-interop, interoperability, clang]
aliases: [C++ 상호운용성, C++ interoperability]
sources: [cpp-interop-manifesto.md, cpp-interop-status.md]
---

# C++ 상호운용성 개요

Swift는 C++와의 양방향 상호운용성을 실험적으로 지원한다. [[objc-interop]]의 Clang Importer를 확장하여 C++ 선언을 Swift로 가져오고, Swift 선언을 C++ 헤더로 내보낸다.

## 동기

대규모 C++ 코드베이스에서 브리징 코드 없이 Swift를 점진적으로 도입하기 위함이다.

## 현재 상태

- **C++ → Swift**: 함수, 구조체/클래스(값 타입), enum, 네임스페이스, 템플릿, `std::string`/`std::vector` 지원. 예외, 가상 함수, 이동 생성자는 미지원.
- **Swift → C++**: 생성된 `-Swift.h` 헤더로 Swift 함수/구조체/enum/클래스 사용 가능. 클로저, 프로토콜 타입 미지원.
- 활성화: `-cxx-interoperability-mode=default` 플래그.

## 주요 개념

- **Clang 모듈 / 브리징 헤더**: C++ 코드를 Swift에 가져오는 두 방식
- **타입 매핑**: C++ 값 타입 → Swift 값 타입, 참조 카운트 타입은 `import_reference`
- **표준 라이브러리**: `std::string`/`std::vector` 직접 사용 (자동 변환 없음)

## 관련 파일

- `swift/lib/ClangImporter/` — C++ 임포트
- `swift/lib/PrintAsClang/` — C++ 헤더 생성

관련 페이지: [[objc-interop]], [[overview]], [[cpp-calling-swift]], [[cpp-using-from-swift]]
