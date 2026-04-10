---
type: reference
category: official-docs
tags: [official-docs, generics, book, build-docs]
aliases: [Generics README, Compiling Swift Generics README]
sources: [swiftlang-swift/docs/Generics/README.md]
---

# Compiling Swift Generics README 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/Generics/README.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/Generics/README.md

## 이 문서는 무엇을 설명하나

제네릭 책의 다운로드 경로, 빌드 방법, 읽기 권장 환경, 현재 집필 상태를 설명하는 유지보수용 README다.

## 핵심 포인트

- 책의 범위를 명시한다: Swift에서 parametric polymorphism을 컴파일러가 어떻게 구현하는지 다룬다.
- 배포 PDF URL과 로컬 빌드 절차를 함께 제공해 소스 문서와 산출물을 연결한다.
- `make`, `latexmk`, 수동 `pdflatex` 순서를 모두 보여줘 문서 재생산성이 높다.
- 미완성 장과 편집이 더 필요한 장을 공개적으로 표시해 문서의 상태를 이해하게 해 준다.

## 컴파일러와 어떻게 연결되나

- docs/Generics의 문서화 파이프라인
- completion / minimization 같은 미작성 generics 주제
- 컴파일러 개요와 generics 심화 사이의 브리지

## 언어 표면에서 어떻게 들어오면 좋은가

- generic 함수와 타입
- existential / protocol constraint
- 언어 표면에서 구현 문서로 건너가는 입문 경로

## 같이 보면 좋은 위키 페이지

- [[compiling-swift-generics]]
- [[overview]]
- [[generic-signatures]]
- [[generics-manifesto]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

문서 소스 자체가 어떤 상태인지 알려 주는 “메타 문서”라서, 책을 읽기 전에 먼저 읽으면 학습 기대치를 조정하기 좋다.
