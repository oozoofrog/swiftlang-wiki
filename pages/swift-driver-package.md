---
type: entity
category: packages
tags: [swift-driver, compiler-driver, build-system]
aliases: [Swift Driver Package]
sources: [swift-driver-readme.md]
---

# swift-driver (패키지)

Swift 컴파일러 드라이버의 Swift 재구현. 레거시 C++ 드라이버를 대체. 원본: `swift-driver/README.md`

## 아키텍처 원칙

- **Swift 코드베이스**: 확장성, 유지보수성, 견고성
- **라이브러리 기반**: 빌드 도구와 더 나은 통합
- **기존 기술 활용**: SwiftPM, llbuild 레버리지
- **실험 플랫폼**: 컴파일 서버, 통합 빌드 그래프 등

## 사용법

`swiftc`/`swift` 심볼릭 링크로 기존 드라이버 대체 가능:
```
ln -s /path/to/built/swift-driver $SOME_PATH/swiftc
SWIFT_EXEC=$SOME_PATH/swiftc swift build
```

### 디렉토리

`swift-driver/`

관련 페이지: [[compiler-driver]], [[overview]]
