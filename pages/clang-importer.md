---
type: reference
category: tooling
tags: [clang, clang-importer, objc, c-interop, cxx-interop, modules]
aliases: [Clang Importer, Clang 임포터, Swift의 Clang Importer]
sources: [how-swift-imports-c-apis.md, c-to-swift-name-translation.md, objc-interop.md]
---

# Clang Importer

Clang Importer는 Swift가 C / Objective-C 세계와 연결되는 핵심 구성 요소다.
Swift가 기존 시스템 라이브러리와 Apple 플랫폼 API, 그리고 더 넓게는 C/C++ 생태계와 상호운용할 수 있는 기반이 여기서 만들어진다.

## 한 줄 요약

- Clang은 C 계열 언어 프론트엔드다.
- Swift는 Clang Importer를 통해 C/ObjC 선언을 Swift API처럼 보이게 만든다.
- C++ interop도 이 축의 확장선에 놓여 있다.

## Clang Importer가 하는 일

### 1. 선언 임포트
- C 함수, typedef, struct, enum, macro 일부를 Swift 표면으로 옮긴다.
- Objective-C 클래스, 메서드, 프로퍼티, nullability, lightweight generics 등을 Swift 관점으로 변환한다.

### 2. 이름 재작성
- C/ObjC의 이름은 그대로 노출되지 않는다.
- Swift API Design Guidelines에 맞게 더 자연스러운 Swift 이름으로 매핑된다.

관련 페이지:
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]

### 3. 모듈/오버레이 연결
- Clang module과 Swift module이 맞물리도록 중간 다리 역할을 한다.
- Foundation 같은 영역에서는 overlay 구조가 중요하게 등장한다.

관련 페이지:
- [[modules]]
- [[swift-foundation-package]]
- [[official-docs/core-libraries-to-compiler-crosswalk]]

### 4. C++ interop의 기반 제공
Swift의 C++ interop는 별도 주제처럼 보이지만,
실제 구현 관점에서는 Clang 기반 interop 축의 확장으로 이해하는 편이 자연스럽다.

관련 페이지:
- [[cpp-interop-overview]]
- [[cpp-using-from-swift]]
- [[cpp-calling-swift]]

## 왜 중요한가

Swift는 독립 언어지만, 현실 세계에서는 기존 C/ObjC API와의 연결 없이는 제대로 쓰기 어렵다.
특히 Apple 플랫폼에서는 시스템 프레임워크 접근 대부분이 이 축을 통과한다.
즉 Clang Importer는 단순 FFI 유틸리티가 아니라,
Swift 생태계 전체가 현실 시스템과 접속하는 관문에 가깝다.

## 저장소 관점에서 어디를 보면 되나

- `swift/lib/ClangImporter/` — C/ObjC/C++ 선언 임포트 핵심
- `swift/lib/PrintAsClang/` — Swift 선언을 C/Clang 관점으로 다시 표현하는 축
- `llvm-project/clang/` — Clang 프론트엔드 본체와 공용 인프라

## Clang Importer를 배울 때 같이 알아야 하는 것

- module 개념
- nullability / pointer 모델
- naming transformation
- Objective-C runtime 친화적 모델
- C++ interop의 제약과 확장

## 추천 읽기 순서

1. [[how-swift-imports-c-apis]]
2. [[c-to-swift-name-translation]]
3. [[objc-interop]]
4. [[modules]]
5. [[cpp-interop-overview]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-language-overview]]
- [[objc-interop]]
- [[how-swift-imports-c-apis]]
- [[c-to-swift-name-translation]]
- [[cpp-interop-overview]]
