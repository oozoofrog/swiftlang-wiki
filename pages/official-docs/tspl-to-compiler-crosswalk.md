---
type: reference
category: official-docs
tags: [official-docs, tspl, language, crosswalk]
aliases: [TSPL, The Swift Programming Language]
sources: [swift.org/documentation/tspl/index.html]
---

# TSPL → 컴파일러 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/tspl/index.html`
- 원본 URL: https://www.swift.org/documentation/tspl/

## 이 문서는 무엇을 설명하나

TSPL 본문 자체가 아니라 TSPL로 들어가는 Swift.org 허브를 기준으로, 언어 표면 문서를 컴파일러 위키와 연결해 읽는 교차 안내 페이지다.

## 핵심 포인트

- TSPL은 Swift의 권위 있는 언어 레퍼런스라는 위치를 가진다.
- 허브 페이지는 Tour / Guide / Reference / 번역본으로 진입 경로를 나눈다.
- 따라서 위키에서는 내용 요약보다 “TSPL의 장 주제가 어느 컴파일러 문서와 이어지는가”가 더 중요하다.
- 언어 학습 경로를 Parser / Sema / SIL / ABI 문서로 옮기는 브리지 역할을 한다.

## 컴파일러와 어떻게 연결되나

- Parser와 AST
- TypeChecker / Request Evaluator
- SILGen / SIL
- modules / access-control / literals / conformances

## 언어 표면에서 어떻게 들어오면 좋은가

- declarations와 expressions
- generic / protocol / error handling / access control
- 기본 문법에서 언어 레퍼런스로 가는 학습 흐름

## 같이 보면 좋은 위키 페이지

- [[overview]]
- [[type-checker]]
- [[modules]]
- [[access-control]]
- [[conformances]]
- [[literals]]
- [[generics-manifesto]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

이 페이지는 “TSPL 자체 요약”이 아니라, TSPL을 읽다가 언제 위키의 구현 문서로 건너가면 좋은지 알려 주는 학습 경로 문서다.
