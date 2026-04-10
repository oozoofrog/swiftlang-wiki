---
type: reference
category: official-docs
tags: [official-docs, api-design, language, crosswalk]
aliases: [API Design Guidelines]
sources: [swift.org/documentation/api-design-guidelines/index.html]
---

# API Design Guidelines → 컴파일러 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/api-design-guidelines/index.html`
- 원본 URL: https://www.swift.org/documentation/api-design-guidelines/

## 이 문서는 무엇을 설명하나

Swift 스타일의 공개 API 명명 규칙을 컴파일러/도구 관점과 연결해 읽는 보조 페이지다.

## 핵심 포인트

- 핵심 원칙은 “Clarity at the point of use”다.
- argument label, property vs method, default argument, documentation comment 규칙을 체계적으로 제시한다.
- 언어 표면의 이름 짓기 원칙이 importer, diagnostics, library evolution과도 연결된다는 점이 중요하다.
- 직접 구현 문서는 아니지만, 공개 표면이 어떻게 고정·전파되는지 이해하는 입문 축이 된다.

## 컴파일러와 어떻게 연결되나

- Clang Importer 이름 변환
- diagnostics 문구와 용어 선택
- library evolution과 module interface surface
- 공개 API를 읽는 개발자 경험 설계

## 언어 표면에서 어떻게 들어오면 좋은가

- argument labels
- initializer/factory naming
- property vs function 선택
- documentation comments와 API 표면

## 같이 보면 좋은 위키 페이지

- [[library-evolution]]
- [[c-to-swift-name-translation]]
- [[how-swift-imports-c-apis]]
- [[access-control]]
- [[diagnostics]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

문법 규칙처럼 보이는 naming guideline이 실제로는 importer와 diagnostics까지 관통한다는 점에서 “표면 언어 ↔ 구현 UX” 연결점이 된다.
