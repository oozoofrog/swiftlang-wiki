---
type: reference
category: official-docs
tags: [official-docs, generics, manifesto, swift-evolution]
aliases: [Generics Manifesto, Complete Generics]
sources: [swiftlang-swift/docs/GenericsManifesto.md]
---

# Generics Manifesto 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/GenericsManifesto.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/GenericsManifesto.md

## 이 문서는 무엇을 설명하나

Swift 제네릭 시스템의 장기 비전과 용어 체계를 정리한 설계 비전 문서다. 구현 현황보다 “어디까지 가고 싶은가”를 보여준다.

## 핵심 포인트

- 제네릭 기능을 단편 기능 목록이 아니라 하나의 장기적 설계 공간으로 정리한다.
- conditional conformance, generalized existentials, higher-kinded types, variadic generics 같은 논점의 맥락을 제공한다.
- 표현력 증가가 구현 복잡도·런타임 비용·ABI 제약과 어떻게 충돌하는지 드러낸다.
- 언어 설계 논의와 실제 컴파일러 구현 용어 사이의 번역기 역할을 한다.

## 컴파일러와 어떻게 연결되나

- generic signature / requirement machine 계열
- conformance lookup과 overlap checking
- existential opening / dynamic casting
- 표준 라이브러리 ABI와 제네릭 표현

## 언어 표면에서 어떻게 들어오면 좋은가

- protocol extension
- associatedtype와 where clause
- conditional conformance
- parameter packs / `any` / `some` / existential

## 같이 보면 좋은 위키 페이지

- [[swift-evolution-and-proposal-history]]
- [[generics-manifesto]]
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[conformances]]
- [[type-checker]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

이 문서는 “현재 구현 설명서”가 아니라 “설계 비전서”이므로, 구현 중심 페이지들과 함께 읽을 때 가치가 커진다.
