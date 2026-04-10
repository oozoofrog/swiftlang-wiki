---
type: reference
category: official-docs
tags: [official-docs, generics, book, compiler-architecture]
aliases: [generics.pdf, Compiling Swift Generics PDF]
sources: [download.swift.org/docs/assets/generics.pdf]
---

# Compiling Swift Generics PDF 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `pdf`
- 다운로드 번들 경로: `download.swift.org/docs/assets/generics.pdf`
- 원본 URL: https://download.swift.org/docs/assets/generics.pdf

## 이 문서는 무엇을 설명하나

Swift 컴파일러의 제네릭 구현을 설명하는 책의 배포용 PDF 아티팩트다. 오프라인 읽기용 산출물이지만, 내용상으로는 제네릭 구현과 컴파일러 구조 입문서를 함께 겸한다.

## 핵심 포인트

- 제네릭 파라미터, requirement, conformance, substitution이 컴파일 과정에서 어떻게 표현되는지 따라갈 수 있다.
- 책의 초반부는 제네릭만이 아니라 Swift 컴파일러 전체 파이프라인을 함께 소개한다.
- 배포 포맷이 PDF라서 내부 링크/북마크를 따라가며 탐색형으로 읽기 좋다.
- README와 함께 보면 “문서 소스 → PDF 빌드 → 배포물”의 관계가 분명해진다.

## 컴파일러와 어떻게 연결되나

- generic signature canonicalization과 requirement 처리
- substitution map / archetype / conformance 모델
- SILGen과 generic specialization
- IRGen의 metadata / witness 전달

## 언어 표면에서 어떻게 들어오면 좋은가

- `func foo<T>(_:)` 형태의 generic declaration
- `where` 절과 protocol constraints
- `associatedtype` / existential / `some` / `any`
- 표준 라이브러리의 generic API 사용 패턴

## 같이 보면 좋은 위키 페이지

- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[archetypes]]
- [[conformances]]
- [[abi-generic-signature]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

동봉된 README 기준 이 PDF는 작업 중인 책의 렌더링 결과물이다. 즉 “정식 레퍼런스 문서”이면서 동시에 현재 진행형 설계 기록의 성격도 가진다.
