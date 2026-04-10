---
type: entity
category: packages
tags: [swift-syntax, parser, macro, syntax-tree]
aliases: [SwiftSyntax]
sources: [swift-syntax-readme.md]
---

# swift-syntax

Swift 소스 코드의 source-accurate 트리 표현(SwiftSyntax tree)을 다루는 라이브러리 세트. Swift 매크로 시스템의 핵심 — 매크로 확장 노드가 SwiftSyntax 노드로 표현되고, 매크로가 SwiftSyntax 트리를 생성하여 소스에 삽입.

## 주요 라이브러리

- **SwiftSyntax**: 구문 트리 자료 구조
- **SwiftParser**: Swift 소스 → SwiftSyntax 트리 파싱
- **SwiftSyntaxBuilder**: 프로그래밍 방식 구문 트리 구성
- **SwiftSyntaxMacros**: 매크로 인프라

## 버전 규칙

메이저 버전이 Swift 릴리스와 정렬: `509` = Swift 5.9, `600` = Swift 6.0

## 탐색 도구

- [swift-ast-explorer.com](https://swift-ast-explorer.com) — 인터랙티브 구문 트리 탐색

### 디렉토리

`swift-syntax/`

관련 페이지: [[overview]], [[keyword-network]], [[swift-macro-tooling-stack]], [[modules]], [[swift-format-package]], [[sourcekit-lsp]], [[swift-testing-package]]
