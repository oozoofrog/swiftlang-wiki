---
type: reference
category: official-docs
tags: [official-docs, diagnostics, tooling, contributor-guide]
aliases: [Diagnostics, Diagnostics authoring]
sources: [swiftlang-swift/docs/Diagnostics.md]
---

# Diagnostics 작성 가이드 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/Diagnostics.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/Diagnostics.md

## 이 문서는 무엇을 설명하나

Swift 진단 메시지의 작성 규칙, fix-it 원칙, diagnostic group 구조, verifier 테스트 문법을 정리한 기여자용 문서다.

## 핵심 포인트

- error / warning / note를 언제 어떻게 구분할지 명확한 기준을 준다.
- 메시지 문체, 코드 표기, 문장 길이, 확실성 표현까지 세세한 작성 원칙이 있다.
- fix-it은 기계 적용 가능한 단 하나의 명백한 수정일 때만 붙여야 한다.
- diagnostic verifier 문법이 상세해서 테스트 기반 진단 개발에 바로 쓸 수 있다.

## 컴파일러와 어떻게 연결되나

- Diagnostics*.def와 DiagnosticGroups.def
- type-checker / Sema의 오류 보고
- diagnostic verifier와 문서화 파이프라인
- DocC / userdocs 진단 카탈로그

## 언어 표면에서 어떻게 들어오면 좋은가

- 오류와 경고 모델
- 속성/키워드/토큰 명명
- 문서 코멘트와 진단 UX
- 학습자에게 보이는 오류 메시지 품질

## 같이 보면 좋은 위키 페이지

- [[diagnostics]]
- [[debugging-the-compiler]]
- [[error-handling]]
- [[overview]]
- [[type-checker]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

현재 위키의 `[[diagnostics]]`가 시스템 구조를 요약한다면, 이 문서는 “좋은 오류 메시지를 어떻게 작성하나”에 초점을 둔다.
