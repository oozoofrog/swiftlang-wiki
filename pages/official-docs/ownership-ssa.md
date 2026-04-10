---
type: reference
category: official-docs
tags: [official-docs, sil, ownership, ossa]
aliases: [Ownership SSA, OSSA]
sources: [swiftlang-swift/docs/SIL/Ownership.md]
---

# Ownership SSA 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/SIL/Ownership.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/SIL/Ownership.md

## 이 문서는 무엇을 설명하나

Ownership SSA(OSSA)의 ownership kind, borrow scope, lifetime-ending use, safe interior pointer 규칙을 설명하는 SIL 소유권 사양서다.

## 핵심 포인트

- 모든 SIL 값에 None / Owned / Guaranteed / Unowned 중 하나의 ownership kind를 부여한다.
- borrow와 consume가 CFG 전체에서 어떤 수명 규칙을 가져야 하는지 명시한다.
- forwarding instruction이 ownership을 어떻게 전파하는지 세밀하게 정의한다.
- interior pointer와 lexical lifetime 규칙까지 다뤄 use-after-free를 SIL 수준에서 차단한다.

## 컴파일러와 어떻게 연결되나

- OSSA verifier
- borrow checking 계열 로직
- ARC / ownership canonicalization
- move-only / noncopyable 검증

## 언어 표면에서 어떻게 들어오면 좋은가

- borrow / consume / move-only 값
- `inout`와 주소 기반 접근
- 참조 카운팅과 deinit 관찰 가능성
- 내부 포인터를 노출하는 API 설계

## 같이 보면 좋은 위키 페이지

- [[swift-ownership-memory-model]]
- [[sil-ownership]]
- [[ownership-manifesto]]
- [[sil-memory-access]]
- [[sil-arc-optimization]]
- [[sil-instructions]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

값/참조 타입 글이나 ownership manifesto를 읽은 뒤 이 문서로 오면 “언어 의미론이 IR 규칙으로 어떻게 강제되는가”가 보인다.
