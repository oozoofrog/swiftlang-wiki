---
type: entity
category: packages
tags: [swift-build, build-system, swb, xcode]
aliases: [Swift Build, SWB]
sources: [swift-build-readme.md]
---

# Swift Build

[[llbuild-package|llbuild]] 위에 구축된 고수준 빌드 시스템. Xcode 프로젝트, Swift 패키지, Swift Playground 빌드에 사용.

## 사용 방법

| 방식 | 명령 |
|------|------|
| SwiftPM | `swift build --build-system swiftbuild` (프리뷰) |
| Xcode | `swift package --disable-sandbox launch-xcode` — 수정된 빌드 서비스로 Xcode 실행 |
| xcodebuild | `swift package --disable-sandbox run-xcodebuild -- [args]` |

## 아키텍처

- **SWBBuildServiceBundle**: Xcode가 로드하는 빌드 서비스 프로세스
- **SWBTaskConstruction**: 빌드 계획 → 빌드 그래프 생성
- **llbuild 기반**: 의존성 추적 및 증분 빌드 실행 엔진으로 [[llbuild-package|llbuild]] 사용

## 디버깅

Xcode에서 `Debug > Attach to Process by PID or Name...` → `SWBBuildServiceBundle` 입력 후 launch-xcode 실행.

## 테스트

`swift test`로 전체 테스트 스위트 실행. 테스트 프로젝트 모델 객체를 사용하여 빌드 그래프를 검증.

### 디렉토리

`swift-build/`

관련 페이지: [[swift-package-manager]], [[llbuild-package]], [[overview]]
