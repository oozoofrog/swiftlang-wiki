---
type: summary
category: tooling
tags: [swift, macro, swiftsyntax, sourcekit, tooling, ide, formatting]
aliases: [매크로/도구 스택, Swift 매크로 도구 스택, SwiftSyntax SourceKit 허브]
sources: [swift-syntax-readme.md, sourcekit-lsp-readme.md, swift.org/documentation/index.html]
---

# Swift 매크로·도구 스택

Swift의 도구 생태계는 단순히 “컴파일러 주변부”가 아니다.
특히 SwiftSyntax, SourceKit-LSP, formatter, 매크로 시스템은
Swift 언어의 표면 문법과 컴파일러 프론트엔드 사이를 실제로 이어 주는 층이다.

## 이 페이지가 묶는 것

| 축 | 역할 | 연결 페이지 |
|---|---|---|
| SwiftSyntax | source-accurate 구문 트리와 파싱/생성 도구 | [[swift-syntax-package]] |
| 매크로 시스템 | 구문 트리를 기반으로 소스 확장을 만드는 언어 확장 메커니즘 | [[swift-syntax-package]], [[swift-testing-package]] |
| SourceKit-LSP | IDE/에디터 경험을 제공하는 언어 서비스 층 | [[sourcekit-lsp]] |
| formatter / linting | 구문 구조를 기반으로 코드 스타일을 정리 | [[swift-format-package]] |
| build/editor integration | SwiftPM / compile database / sourcekitd / clangd와의 연결 | [[swift-package-manager]], [[sourcekit-lsp]], [[clang-importer]] |

## 왜 이 층이 중요한가

Swift를 “언어”와 “컴파일러”만으로 보면,
실제 개발자가 매일 접하는 도구 경험이 빠진다.
하지만 실제 Swift 경험은 다음이 같이 만들어 낸다.

- 컴파일러 프론트엔드
- 구문 트리 라이브러리
- IDE language service
- formatter / test / macro 인프라

즉 이 층은 언어 구현이 개발자 경험으로 변환되는 자리다.

## SwiftSyntax가 중심축인 이유

SwiftSyntax는 단순 파서 래퍼가 아니다.
이 패키지는
- SwiftParser
- SwiftSyntax tree
- SwiftSyntaxBuilder
- SwiftSyntaxMacros
를 통해
문법 이해, 구문 생성, 매크로 확장, 포매팅 도구까지 하나의 생태계로 묶는다.

관련 페이지:
- [[swift-syntax-package]]
- [[swift-format-package]]

## 매크로를 이 스택에서 봐야 하는 이유

Swift 매크로는 언어 기능이면서 동시에 도구 기능이기도 하다.
표면적으로는 언어 확장이지만,
실제 작성/검증 경험은 SwiftSyntax와 테스트/디버깅 도구에 크게 의존한다.

그래서 매크로는
- 언어 설계
- 구문 트리 조작
- 도구 생태계
를 동시에 건드리는 주제다.

관련 페이지:
- [[swift-syntax-package]]
- [[swift-testing-package]]
- [[swift-language-overview]]

## SourceKit-LSP의 위치

SourceKit-LSP는 “컴파일러와 에디터 사이의 서비스 층”에 가깝다.
코드 완성, 정의로 이동, 심볼 검색, 크로스 언어 편집 경험이 여기서 나온다.
또 SwiftPM과 compile database, sourcekitd/clangd의 연결도 중요하다.

관련 페이지:
- [[sourcekit-lsp]]
- [[swift-package-manager]]
- [[clang-importer]]

## formatter와 tooling의 의미

formatter는 표면적으로는 스타일 도구지만,
실제로는 구문 트리를 신뢰 가능한 방식으로 읽고 다시 써야 한다.
그래서 formatter 계층은 SwiftSyntax 생태계가 얼마나 성숙한지 보여 주는 좋은 예시다.

관련 페이지:
- [[swift-format-package]]
- [[swift-syntax-package]]

## 추천 읽기 순서

1. [[swift-syntax-package]]
2. [[swift-format-package]]
3. [[sourcekit-lsp]]
4. [[swift-package-manager]]
5. [[clang-importer]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-syntax-package]]
- [[sourcekit-lsp]]
- [[swift-format-package]]
- [[swift-package-manager]]
