---
type: entity
category: sil
tags: [sil, function, attributes]
aliases: [SIL 함수 속성]
sources: [sil-function-attributes.md]
---

# SIL 함수 속성

SIL 함수에 적용 가능한 속성 레퍼런스. 원본: `swift/docs/SIL/FunctionAttributes.md`

SIL 함수는 인라인 정책, 최적화 힌트, 시맨틱 어노테이션 등 다양한 속성을 가질 수 있다.

## 주요 속성 카테고리

- **인라인 제어**: `[always_inline]`, `[never_inline]`, `[transparent]`
- **시맨틱**: `[_semantics "..."]` — 컴파일러가 특별 처리하는 함수 식별
- **최적화**: `[Onone]` — 최적화 비활성화
- **가시성**: `[serialized]` — 모듈 외부 인라인 허용

관련 페이지: [[sil-reference]], [[sil-function-conventions]]
