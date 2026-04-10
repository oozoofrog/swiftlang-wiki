---
type: entity
category: tools
tags: [sourcekit-lsp, lsp, ide, code-completion]
aliases: [SourceKit-LSP, LSP]
sources: [sourcekit-lsp-readme.md]
---

# SourceKit-LSP

Swift 및 C 계열 언어를 위한 Language Server Protocol 구현. 원본: `sourcekit-lsp/README.md`

## 핵심 기능

- 코드 완성, 정의로 이동, 심볼 검색 등 지능형 편집 기능
- **sourcekitd** (Swift)와 **clangd** (C/C++/ObjC) 위에 구축
- 강력한 소스 코드 인덱스 + 크로스 언어 지원
- SwiftPM 프로젝트 및 `compile_commands.json` (CMake 등) 지원

## 중요 제약

글로벌 인덱스와 Swift 모듈을 **백그라운드에서 빌드하지 않음**. 크로스 모듈/글로벌 기능은 프로젝트를 최근에 빌드해야 동작. 실험적 백그라운드 인덱싱 옵션 존재.

## 번들

Swift 툴체인(swift.org)과 Xcode에 포함.

### 디렉토리

`sourcekit-lsp/`

관련 페이지: [[overview]], [[keyword-network]], [[swift-macro-tooling-stack]], [[swift-package-manager]], [[swift-syntax-package]], [[how-swift-imports-c-apis]], [[compiler-driver]]
