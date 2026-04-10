---
type: reference
category: official-docs
tags: [official-docs, ownership, value-semantics, crosswalk]
aliases: [Value And Reference Types In Swift]
sources: [swift.org/documentation/articles/value-and-reference-types.html]
---

# Value/Reference Types → SIL 소유권 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/articles/value-and-reference-types.html`
- 원본 URL: https://www.swift.org/documentation/articles/value-and-reference-types.html

## 이 문서는 무엇을 설명하나

값 타입과 참조 타입의 차이를 설명하는 사용자 문서를 SIL ownership, ARC, ABI layout과 연결해서 읽는 안내 페이지다.

## 핵심 포인트

- struct/enum/tuple는 value type, class/actor/closure는 reference type으로 소개한다.
- 핵심 교육 포인트는 local reasoning과 shared mutable state의 차이다.
- Array/Dictionary/String도 value type이라는 설명은 곧 copy-on-write와 runtime 설계로 이어진다.
- “class보다 struct를 먼저 고려하라”는 권고를 ownership/ARC 관점으로 재해석할 수 있다.

## 컴파일러와 어떻게 연결되나

- sil-ownership과 sil-memory-access
- sil-arc-optimization
- abi-type-layout
- runtime과 copy-on-write 구현

## 언어 표면에서 어떻게 들어오면 좋은가

- struct vs class
- actor / closure의 참조 의미론
- 복사 semantics와 shared mutable state
- Array / Dictionary / String의 값 의미론

## 같이 보면 좋은 위키 페이지

- [[sil-ownership]]
- [[sil-arc-optimization]]
- [[sil-memory-access]]
- [[abi-type-layout]]
- [[runtime]]
- [[ownership-manifesto]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

표면 언어에서 배우는 “값/참조 타입” 차이는 내부적으로 ownership model, ARC, layout, COW로 흩어진다. 이 페이지는 그 흩어진 축을 다시 묶는다.
