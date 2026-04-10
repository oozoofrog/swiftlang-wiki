---
type: reference
category: official-docs
tags: [official-docs, sil, ir, ssa]
aliases: [SIL.md, Swift Intermediate Language]
sources: [swiftlang-swift/docs/SIL/SIL.md]
---

# SIL.md 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/SIL/SIL.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/SIL/SIL.md

## 이 문서는 무엇을 설명하나

SIL의 역할, 타입 체계, 함수/값/기본 블록 규칙, linkage, dispatch, memory lifetime까지 포괄하는 공식 레퍼런스다.

## 핵심 포인트

- Swift 소스가 raw SIL, canonical SIL, optimized SIL을 거쳐 LLVM IR로 가는 위치를 명확히 보여 준다.
- formal type / canonical type / lowered SIL type의 차이를 분명히 설명한다.
- SIL이 단순 중간표현이 아니라 ownership, dispatch, witness, vtable, metadata 의미를 담는 언어별 IR라는 점이 핵심이다.
- 후반부로 갈수록 메모리 수명, COW, pack, TBAA 같은 검증 규칙서 성격이 강해진다.

## 컴파일러와 어떻게 연결되나

- SILGen과 SIL parser/printer
- SILVerifier
- SILOptimizer
- IRGen / vtable / witness table 생성

## 언어 표면에서 어떻게 들어오면 좋은가

- 프로토콜 witness와 클래스 디스패치
- 제네릭 / existential / inout
- copy-on-write 컬렉션
- pack expansion과 소유권

## 같이 보면 좋은 위키 페이지

- [[sil-reference]]
- [[sil-instructions]]
- [[sil-types]]
- [[sil-function-attributes]]
- [[sil-function-conventions]]
- [[sil-memory-access]]
- [[sil-utilities]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

개념 페이지 `[[sil-reference]]`와 달리 이 문서는 “SIL 문법과 규칙을 공식 문서 관점으로 어디까지 읽어야 하나”를 안내하는 보조 레퍼런스로 읽는 편이 좋다.
