---
type: summary
category: learning
tags: [swift, type-system, generics, existential, opaque, metatype]
aliases: [Swift 타입 시스템, Swift Type System, 타입 시스템 개요]
sources: [type-checker.md, swift.org/documentation/tspl/index.html, swiftlang-swift/docs/Generics/README.md, swiftlang-swift/docs/GenericsManifesto.md]
---

# Swift 타입 시스템

이 페이지는 Swift 타입 시스템을 상위 레벨에서 묶는 허브다.
기존 위키에는 제네릭, conformances, archetype, literals, dynamic casting 같은 세부 페이지가 이미 있지만,
그것들을 하나의 타입 시스템 이야기로 연결해 주는 상위 설명은 비어 있었다.

## Swift 타입 시스템을 이루는 큰 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| 기본 타입 모델 | 값 타입과 참조 타입은 어떻게 구분되는가 | [[swift-ownership-memory-model]], [[official-docs/value-reference-types-to-sil-ownership]], [[dynamic-casting]], [[runtime]] |
| 추론과 제약 | 타입은 어떻게 추론되고 오버로드는 어떻게 선택되는가 | [[type-checker]], [[literals]], [[diagnostics]] |
| 제네릭 | 파라미터화된 타입/함수는 어떻게 의미를 갖는가 | [[compiling-swift-generics]], [[generic-signatures]], [[substitution-maps]] |
| 프로토콜 | conformance와 associated type은 어떻게 다뤄지는가 | [[conformances]], [[archetypes]], [[generics-manifesto]] |
| existential / opaque | `any`와 `some`은 어떤 추상화 경계를 가지는가 | [[archetypes]], [[dynamic-casting]], [[official-docs/swift-generics-manifesto]] |
| ABI / runtime 연결 | 타입은 메모리와 바이너리에서 어떻게 표현되는가 | [[abi-type-metadata]], [[abi-type-layout]], [[abi-generic-signature]], [[runtime]] |

## 왜 Swift 타입 시스템이 중요한가

Swift의 많은 특징은 사실상 타입 시스템 이야기다.

- 제네릭과 프로토콜 중심 설계
- 값 의미론과 copy-on-write
- literal defaulting과 contextual typing
- `some` / `any` / metatype / associated type
- concurrency에서의 `Sendable`

즉 Swift를 깊게 이해한다는 것은 상당 부분 Swift 타입 시스템을 이해한다는 뜻과 겹친다.

## 컴파일러 관점에서는 어떻게 보이나

### 1. Parser 이후 Sema의 중심 문제
타입 시스템은 파서가 아니라 의미 분석 단계에서 본격적으로 드러난다.
표현식, 선언, 제네릭 제약, 오버로드 후보가 모두 제약 시스템 문제로 모인다.

관련 페이지:
- [[type-checker]]
- [[request-evaluator]]
- [[diagnostics]]

### 2. Generic signature와 conformance 모델
Swift 타입 시스템의 고유한 난이도는 제네릭 + 프로토콜 + associated type 결합에서 크게 나온다.
여기서 generic signature, substitution map, archetype, conformance lookup이 핵심 도구가 된다.

관련 페이지:
- [[generic-signatures]]
- [[substitution-maps]]
- [[archetypes]]
- [[conformances]]

### 3. 타입 시스템과 ABI/runtime의 접점
타입은 단순한 정적 검사 대상이 아니다.
메타데이터, 레이아웃, calling convention, existential container, witness table 같은 런타임/ABI 구조와 직접 이어진다.

관련 페이지:
- [[abi-type-metadata]]
- [[abi-type-layout]]
- [[abi-calling-convention]]
- [[runtime]]

## Swift 타입 시스템에서 자주 헷갈리는 쌍

- nominal type vs structural type
- interface type vs contextual type
- generic parameter vs archetype
- existential vs opaque type
- static type vs runtime type
- source-level type vs lowered SIL type

이런 구분은 세부 페이지에 흩어져 있기 때문에,
이 허브를 기준으로 필요한 쪽으로 내려가면 덜 헤맨다.

## 추천 읽기 순서

### 언어 사용자 관점
1. [[swift-language-overview]]
2. [[official-docs/tspl-to-compiler-crosswalk]]
3. [[type-checker]]
4. [[dynamic-casting]]

### 구현 관점
1. [[type-checker]]
2. [[compiling-swift-generics]]
3. [[generic-signatures]]
4. [[archetypes]]
5. [[conformances]]
6. [[runtime]]

### ABI / runtime 관점
1. [[abi-type-metadata]]
2. [[abi-type-layout]]
3. [[abi-generic-signature]]
4. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-concurrency-architecture]]
- [[swift-ownership-memory-model]]
- [[type-checker]]
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[conformances]]
- [[runtime]]
- [[keyword-network]]
