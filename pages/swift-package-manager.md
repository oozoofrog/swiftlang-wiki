---
type: entity
category: packages
tags: [swiftpm, package-manager, build, dependencies]
aliases: [SwiftPM, Swift Package Manager]
sources: [swiftpm-readme.md]
---

# Swift Package Manager

소스 코드 배포 관리 도구. Swift 패키지의 컴파일, 링크, 의존성 관리, 버전 관리를 담당.

## 핵심 기능

- `swift build` — 패키지 빌드
- `swift test` — 테스트 실행
- `swift package` — 패키지 관리
- macOS + Linux 빌드 시스템 내장
- Xcode 11+에서 iOS/macOS/watchOS/tvOS 통합

## 구성

- `Package.swift` — 패키지 매니페스트 (Swift DSL)
- `Sources/` — 소스 코드
- `Tests/` — 테스트 코드

## 관련 프로젝트

- [[sourcekit-lsp]] — libSwiftPM을 활용한 LSP 구현
- [[swift-build-package]] — Swift Build 시스템

### 디렉토리

`swiftpm/`

관련 페이지: [[overview]], [[swift-driver-package]]
