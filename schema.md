---
wiki: "swiftlang-wiki"
project: "swiftlang"
created: "2026-04-09"
version: 1
---

# Wiki Schema

## 프로젝트 컨텍스트
- **프로젝트**: swiftlang (Swift 컴파일러 모노레포)
- **언어**: Swift, C++
- **빌드 시스템**: CMake, Swift Package Manager
- **주요 구성**: Swift 컴파일러, LLVM/Clang 백엔드, 표준 라이브러리, 패키지 매니저, 개발 도구

## 페이지 타입

| 타입 | 설명 | 예시 |
|------|------|------|
| entity | 구체적 대상 (모듈, 서브시스템, 도구) | `silgen.md` |
| concept | 추상적 아이디어나 패턴 | `ownership-ssa.md` |
| summary | 영역 전체 개요 | `overview.md` |
| glossary | 용어 정의 | `glossary-compiler.md` |
| analysis | 질의 결과로 생성된 분석 | `sil-pipeline-analysis.md` |

## 카테고리

| 카테고리 | 설명 | 주요 디렉토리 |
|----------|------|---------------|
| compiler | Swift 컴파일러 코어 (AST, Parse, Sema, IRGen) | `swift/lib/`, `swift/include/` |
| sil | SIL IR, SILGen, SIL Optimizer | `swift/lib/SIL*`, `swift/docs/SIL/` |
| stdlib | 표준 라이브러리, Foundation | `swift/stdlib/`, `swift-foundation/` |
| tools | SourceKit, swift-format, swift-inspect 등 | `swift/tools/`, `sourcekit-lsp/` |
| packages | SPM 패키지 생태계 | `swiftpm/`, `swift-syntax/`, `swift-driver/` |
| llvm | LLVM/Clang 백엔드 | `llvm-project/` |
| testing | 테스트 프레임워크 및 인프라 | `swift-testing/`, `swift/test/` |
| documentation | 문서 및 가이드 | `swift/docs/` |

## 규칙
- **페이지 이름**: kebab-case, 최대 64자, `.md` 확장자
- **교차참조**: `[[page-name]]` 형식 (Obsidian 호환)
- **소스**: `.wiki/sources/`에 저장, 불변 (LLM은 읽기만)
- **Frontmatter 출처 구분**:
  - `sources`: 원본 소스 파일 참조 (`sources/` 내 파일명). ingest된 페이지에 사용
  - `references`: 위키 페이지 참조 (`pages/` 내 파일명, 확장자 제외). analysis 페이지에 주로 사용
- **태그**: 소문자, frontmatter의 tags 배열에 기록
- **별칭**: frontmatter의 aliases 배열에 기록 (한국어/영어 등)
