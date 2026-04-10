---
title: Swift Compiler Wiki
---

# Swift Compiler Wiki

Swift 컴파일러 내부 구조에 대한 LLM 생성 지식 베이스.

| 항목 | 값 |
|------|-----|
| 페이지 | 97+ |
| 교차참조 | 752+ |
| 소스 | swift/docs/, 서브프로젝트 README, 코드 분석 |

## 빠른 탐색

- **[프로젝트 개요](overview.md)** — 컴파일러 파이프라인, 모노레포 구성
- **[SIL 레퍼런스](sil-reference.md)** — Swift Intermediate Language 명세
- **[205개 패스 카탈로그](sil-optimizer-pass-catalog.md)** — SIL 옵티마이저 전체 패스 목록
- **[심볼 맹글링](abi-mangling.md)** — ABI 맹글링/디맹글링 체계
- **[타입 체커](type-checker.md)** — 제약 기반 양방향 타입 추론
- **[Generics 책](compiling-swift-generics.md)** — "Compiling Swift Generics" 요약
- **[공식 참고 문서 다운로드](downloads/index.md)** — ZIP/개별 문서 다운로드 허브
- **[공식 문서 해설 허브](official-docs/index.md)** — 다운로드 문서별 위키 정리 페이지
- **[언어 → 컴파일러 교차학습 지도](official-docs/language-to-compiler-crosswalk.md)** — 문법/라이브러리/빌드 지식이 내부 구현과 만나는 지도
- **[Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md)** — actor isolation / Sendable / strict concurrency를 컴파일러 관점에서 정리
- **[용어 사전](glossary-compiler.md)** — 컴파일러 핵심 용어 ~60개

!!! tip "오프라인으로 읽기"
    로컬에 받아서 읽을 자료가 필요하면 [다운로드 허브](downloads/index.md)에서 전체 ZIP 번들이나 개별 참고 문서를 바로 받을 수 있습니다.

## 새로 추가된 읽기 경로

- **언어 입문 → 구현**: [TSPL → 컴파일러 교차 읽기](official-docs/tspl-to-compiler-crosswalk.md) → [타입 체커](type-checker.md) → [SIL 레퍼런스](sil-reference.md)
- **제네릭 중심**: [Compiling Swift Generics PDF 해설](official-docs/compiling-swift-generics-pdf.md) → [Generics Manifesto 해설](official-docs/swift-generics-manifesto.md)
- **값/참조 의미론 중심**: [Value/Reference Types → SIL 소유권 교차 읽기](official-docs/value-reference-types-to-sil-ownership.md) → [SIL 소유권](sil-ownership.md)
- **빌드/도구 중심**: [Swift Compiler 공개 개요 해설](official-docs/swift-compiler-architecture.md) → [Driver Internals 문서 해설](official-docs/driver-internals.md) → [SwiftPM 문서 → 빌드 파이프라인 교차 읽기](official-docs/swiftpm-docs-to-build-pipeline.md)
- **동시성 안전성 중심**: [Swift 6 데이터 경쟁 안전성 검사](concurrency-data-race-safety.md) → [타입 체커](type-checker.md) → [SIL 옵티마이저 패스 카탈로그](sil-optimizer-pass-catalog.md)

## 카테고리

| 카테고리 | 페이지 | 주요 내용 |
|----------|--------|-----------|
| [컴파일러 코어](type-checker.md) | 12 | Parser, Sema, IRGen, Request Evaluator, AST |
| [SIL](sil-reference.md) | 14 | IR 명세, 인스트럭션, 소유권, 옵티마이저, 패스 카탈로그 |
| [ABI](abi-mangling.md) | 7 | 맹글링, 타입 메타데이터/레이아웃, 호출 규약, Library Evolution |
| [Generics](generic-signatures.md) | 5 | 시그니처, 치환 맵, 아키타입, Conformance |
| [Interop](objc-interop.md) | 6 | ObjC, C API 임포트, C++ 양방향 |
| [언어 설계](ownership-manifesto.md) | 8 | 소유권, 동시성 안전성, 에러 처리, 캐스팅, 접근 제어 |
| [기여 가이드](getting-started.md) | 7 | 시작하기, 테스트, CI, FAQ |
| [패키지](swift-syntax-package.md) | 11 | SwiftPM, SourceKit-LSP, SwiftNIO 등 |
