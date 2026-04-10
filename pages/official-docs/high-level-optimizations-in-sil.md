---
type: reference
category: official-docs
tags: [official-docs, sil, optimizer, semantics]
aliases: [High-Level SIL Optimizations, @_semantics]
sources: [swiftlang-swift/docs/HighLevelSILOptimizations.rst]
---

# High-Level Optimizations in SIL 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `rst`
- 다운로드 번들 경로: `swiftlang-swift/docs/HighLevelSILOptimizations.rst`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/HighLevelSILOptimizations.rst

## 이 문서는 무엇을 설명하나

표준 라이브러리의 고수준 연산에 semantic tag를 붙여 SIL 옵티마이저가 도메인 지식을 활용하도록 만드는 규칙 문서다.

## 핵심 포인트

- Array/String/Span 같은 표준 라이브러리 연산을 일반 함수 호출이 아니라 의미적 원자 연산처럼 이해하게 만든다.
- `@_semantics`와 `@_effects`가 인라이닝 시점과 최적화 가능성을 어떻게 제어하는지 설명한다.
- 초기 단계에서는 의미를 보존하고 후기 단계에서 인라이닝하는 전략이 핵심이다.
- 표준 라이브러리 구현과 옵티마이저가 문서화된 계약으로 연결된다는 점이 중요하다.

## 컴파일러와 어떻게 연결되나

- SILOptimizer
- semantic annotation 기반 분석
- effect analysis와 availability folding
- stdlib 의미 보존형 최적화

## 언어 표면에서 어떻게 들어오면 좋은가

- Array / String / fixed storage 연산
- `@_semantics`, `@_effects` 같은 언더스코어 속성
- `if #available`
- 고수준 컨테이너 사용 패턴

## 같이 보면 좋은 위키 페이지

- [[high-level-sil-optimizations]]
- [[optimizer-design]]
- [[sil-reference]]
- [[sil-optimizer-pass-catalog]]
- [[stdlib-programmers-manual]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

언어 표면의 `Array.count` 같은 간단한 표현이 실제로는 옵티마이저에 특별대우되는 의미 연산이라는 점을 보여 주는 좋은 문서다.
