---
type: reference
category: official-docs
tags: [official-docs, core-libraries, modules, crosswalk]
aliases: [Swift Core Libraries]
sources: [swift.org/documentation/core-libraries/index.html]
---

# Core Libraries → 컴파일러 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/core-libraries/index.html`
- 원본 URL: https://www.swift.org/documentation/core-libraries/

## 이 문서는 무엇을 설명하나

표준 라이브러리 위의 Core Libraries를 기준으로, 언어 기능처럼 보이는 라이브러리 계층이 모듈/interop/toolchain과 어떻게 엮이는지 보여 주는 페이지다.

## 핵심 포인트

- Foundation, libdispatch, Swift Testing, XCTest를 하나의 교차 플랫폼 라이브러리군으로 소개한다.
- FoundationEssentials 같은 경량 모듈화는 모듈 구조와 공개 표면 설계를 함께 보여 준다.
- Swift Testing은 매크로 기반 테스트 프레임워크라는 점에서 언어·패키지·도구의 경계를 드러낸다.
- Core Libraries는 컴파일러 코어보다 “모듈 경계와 생태계 구조”를 이해하는 데 더 유용하다.

## 컴파일러와 어떻게 연결되나

- modules와 overlay 구조
- Clang Importer / ObjC interop
- 패키지 생태계와 매크로 기반 도구
- cross-platform library packaging

## 언어 표면에서 어떻게 들어오면 좋은가

- Foundation(Data/URL/Date/Locale)
- dispatch 기반 동시성 실행
- Swift Testing의 `@Test`, `#expect`
- XCTest와의 호환성

## 같이 보면 좋은 위키 페이지

- [[swift-foundation-package]]
- [[swift-testing-package]]
- [[how-swift-imports-c-apis]]
- [[objc-interop]]
- [[modules]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

앱 개발자가 매일 쓰는 라이브러리 문서에서 컴파일러 내부로 들어갈 때, 직접적인 진입점은 알고리즘보다 “모듈/interop/toolchain 구조”다.
