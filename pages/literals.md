---
type: concept
category: compiler
tags: [literals, type-inference, type-checker]
aliases: [리터럴, Literals, 리터럴 타입 추론]
sources: [literals.md]
---

# 리터럴의 타입 체킹과 추론

Swift에서 리터럴 표현식은 `ExpressibleBy*Literal` 프로토콜을 통해 타입이 결정된다. 컨텍스트에서 기대 타입이 주어지면 해당 프로토콜 준수 여부로 리터럴 타입을 선택하고, 컨텍스트가 없으면 모듈 범위의 기본 타입(`StringLiteralType` 등)을 사용한다.

## 타입 체커 알고리즘

1. 컨텍스트에서 `ExpressibleBy*Literal` 준수 타입 필터링
2. `associatedtype`(예: `StringLiteralType`)으로 `_ExpressibleByBuiltin*Literal` 찾기
3. 빌트인 생성자와 사용자 정의 생성자로 표현식 트리 구성

## 핵심 개념

- **2단계 구조**: `_ExpressibleByBuiltin*Literal`(stdlib, 원시 데이터) -> `ExpressibleBy*Literal`(사용자 타입)
- 정수/부동소수점은 무한 정밀도 처리 후 범위 검사
- 배열/딕셔너리는 가변 인자, 문자열 보간은 `StringInterpolation`으로 처리

관련 페이지: [[type-checker]], [[keyword-network]], [[generic-signatures]], [[runtime]], [[tspl-to-compiler-crosswalk]], [[overview]]
