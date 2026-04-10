---
type: reference
category: official-docs
tags: [official-docs, abi, manifesto, runtime]
aliases: [ABI Stability Manifesto]
sources: [swiftlang-swift/docs/ABIStabilityManifesto.md]
---

# ABI Stability Manifesto 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/ABIStabilityManifesto.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/ABIStabilityManifesto.md

## 이 문서는 무엇을 설명하나

ABI 안정화 이전의 배경과 설계 방향을 한 번에 묶어 보여 주는 상위 개념 문서다. 타입 레이아웃, metadata, mangling, calling convention, runtime, stdlib를 같은 프레임에서 본다.

## 핵심 포인트

- source compatibility, module stability, ABI stability를 구분한다.
- Swift ABI를 data layout / metadata / mangling / calling convention / runtime / stdlib 6축으로 정리한다.
- opaque layout, resilience, value witness table, existential container 같은 핵심 어휘를 한 문서 안에서 연결해 준다.
- 언어 성장과 ABI 고정 사이의 긴장을 “ABI-additive change” 개념으로 설명한다.

## 컴파일러와 어떻게 연결되나

- abi-type-layout / abi-type-metadata / abi-mangling / abi-calling-convention
- runtime과 serialization
- library evolution과 resilience
- public ABI surface와 internal convention 구분

## 언어 표면에서 어떻게 들어오면 좋은가

- struct / tuple / enum / class
- generic / existential / closure / throws
- String / Int 같은 표준 라이브러리 타입의 표현
- 공개 API와 binary compatibility

## 같이 보면 좋은 위키 페이지

- [[abi-stability]]
- [[library-evolution]]
- [[abi-type-layout]]
- [[abi-type-metadata]]
- [[abi-mangling]]
- [[abi-calling-convention]]
- [[runtime]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

현재 위키의 ABI 세부 페이지들을 한 장의 상위 rationale 문서에 걸어두는 역할을 한다.
