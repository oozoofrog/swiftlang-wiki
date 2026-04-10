---
type: reference
category: official-docs
tags: [official-docs, stdlib, runtime, crosswalk]
aliases: [Standard Library]
sources: [swift.org/documentation/standard-library/index.html]
---

# Standard Library → 컴파일러 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/standard-library/index.html`
- 원본 URL: https://www.swift.org/documentation/standard-library/

## 이 문서는 무엇을 설명하나

표준 라이브러리 개요를 기준으로, 언어의 기본 타입·컬렉션·프로토콜이 컴파일러와 런타임에 어떻게 걸쳐 있는지 연결해 읽는 페이지다.

## 핵심 포인트

- 표준 라이브러리는 Swift 프로그램의 base layer이며, 소스와 테스트는 메인 swift 저장소에 있다.
- Standard Library Preview Package는 Swift Evolution 이후의 신규 API 배포 흐름을 보여 준다.
- 설계 섹션은 stdlib/public/core, stdlib/public/runtime, SDK overlays라는 층을 드러낸다.
- 즉 표준 라이브러리 학습은 곧 runtime, ABI, SIL, language evolution을 함께 보는 일이다.

## 컴파일러와 어떻게 연결되나

- runtime과 stdlib/public/runtime 경계
- ABI type layout과 library evolution
- Builtin 접근과 SIL 최적화
- overlay와 모듈 경계

## 언어 표면에서 어떻게 들어오면 좋은가

- Int / String / Array / Dictionary
- 프로토콜 기반 알고리즘
- 값 의미론과 copy-on-write
- Swift Evolution으로 추가되는 API

## 같이 보면 좋은 위키 페이지

- [[stdlib-programmers-manual]]
- [[runtime]]
- [[abi-type-layout]]
- [[library-evolution]]
- [[dynamic-casting]]
- [[literals]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

“언어 자체”로 느껴지는 기본 타입들이 실제로는 stdlib / runtime / ABI 설계의 결과라는 점을 확인하는 관문이다.
