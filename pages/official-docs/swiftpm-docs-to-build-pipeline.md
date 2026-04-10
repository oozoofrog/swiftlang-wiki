---
type: reference
category: official-docs
tags: [official-docs, swiftpm, build, redirect]
aliases: [Package Manager, SwiftPM docs redirect]
sources: [swift.org/documentation/package-manager/index.html]
---

# SwiftPM 문서 → 빌드 파이프라인 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/package-manager/index.html`
- 원본 URL: https://www.swift.org/documentation/package-manager/

## 이 문서는 무엇을 설명하나

다운로드된 파일 자체는 redirect placeholder이므로, canonical SwiftPM 문서 주제를 현재 위키의 build pipeline 문서와 연결해 읽는 안내 페이지다.

## 핵심 포인트

- 번들 안의 실제 파일에는 본문이 없고 canonical SwiftPM DocC 문서로 리다이렉트만 걸려 있다.
- 따라서 이 페이지는 “문서 없음”을 숨기지 않고, 대신 SwiftPM이 위키 내부 어디와 연결되는지 정리한다.
- Package.swift 표면 DSL은 결국 swift-driver, llbuild, dependency analysis와 만난다.
- 패키지 매니저를 언어 기능처럼 보지 말고 build orchestration 관점으로 읽는 편이 좋다.

## 컴파일러와 어떻게 연결되나

- swift-package-manager
- swift-driver-package / compiler-driver
- llbuild-package / swift-build-package
- dependency-analysis

## 언어 표면에서 어떻게 들어오면 좋은가

- Package.swift DSL
- targets / products / dependencies
- `swift build` / `swift test` / `swift package`
- Sources / Tests 디렉터리 구조

## 같이 보면 좋은 위키 페이지

- [[swift-package-manager]]
- [[swift-driver-package]]
- [[compiler-driver]]
- [[llbuild-package]]
- [[swift-build-package]]
- [[dependency-analysis]]
- [[sourcekit-lsp]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

redirect-only 파일이라 실제 본문을 요약할 수는 없다. 대신 “왜 SwiftPM 문서를 읽으면 driver/llbuild로 넘어가야 하는가”를 명확히 한다.
