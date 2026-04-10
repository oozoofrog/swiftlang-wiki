---
title: Swift Compiler Wiki
---

# Swift Compiler Wiki

Swift 컴파일러 내부 구조에 대한 LLM 생성 지식 베이스.

| 항목 | 값 |
|------|-----|
| 페이지 | 71+ |
| 교차참조 | 338+ |
| 소스 | swift/docs/, 서브프로젝트 README, 코드 분석 |

## 빠른 탐색

- **[프로젝트 개요](overview.md)** — 컴파일러 파이프라인, 모노레포 구성
- **[SIL 레퍼런스](sil-reference.md)** — Swift Intermediate Language 명세
- **[205개 패스 카탈로그](sil-optimizer-pass-catalog.md)** — SIL 옵티마이저 전체 패스 목록
- **[심볼 맹글링](abi-mangling.md)** — ABI 맹글링/디맹글링 체계
- **[타입 체커](type-checker.md)** — 제약 기반 양방향 타입 추론
- **[Generics 책](compiling-swift-generics.md)** — "Compiling Swift Generics" 요약
- **[공식 참고 문서 다운로드](downloads/index.md)** — ZIP/개별 문서 다운로드 허브
- **[용어 사전](glossary-compiler.md)** — 컴파일러 핵심 용어 ~60개

## 카테고리

| 카테고리 | 페이지 | 주요 내용 |
|----------|--------|-----------|
| [컴파일러 코어](type-checker.md) | 12 | Parser, Sema, IRGen, Request Evaluator, AST |
| [SIL](sil-reference.md) | 14 | IR 명세, 인스트럭션, 소유권, 옵티마이저, 패스 카탈로그 |
| [ABI](abi-mangling.md) | 7 | 맹글링, 타입 메타데이터/레이아웃, 호출 규약, Library Evolution |
| [Generics](generic-signatures.md) | 5 | 시그니처, 치환 맵, 아키타입, Conformance |
| [Interop](objc-interop.md) | 6 | ObjC, C API 임포트, C++ 양방향 |
| [언어 설계](ownership-manifesto.md) | 7 | 소유권, 에러 처리, 캐스팅, 접근 제어 |
| [기여 가이드](getting-started.md) | 7 | 시작하기, 테스트, CI, FAQ |
| [패키지](swift-syntax-package.md) | 11 | SwiftPM, SourceKit-LSP, SwiftNIO 등 |
