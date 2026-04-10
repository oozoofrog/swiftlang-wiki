---
type: entity
category: documentation
tags: [faq, how-to, development]
aliases: [컴파일러 FAQ, Compiler FAQ]
sources: [faq.md]
---

# 컴파일러 개발 FAQ

Swift 컴파일러 개발 시 자주 묻는 질문 모음.

## 빌드 / CMake

- **새 파일 추가**: `CMakeLists.txt`에 등록 필수 (누락 시 링크 에러)
- **빌드 속도**: `sccache`, `--skip-*` 플래그, 단일 아키텍처 빌드

## 로컬 툴체인 사용

- `SWIFT_EXEC=/path/to/swiftc swift build`로 패키지 빌드
- Xcode Build Settings에 `SWIFT_EXEC` 추가

## 문서 검색

- `git grep --ignore-case "패턴"` 또는 ripgrep 활용
- Documentation Index 참고

관련 페이지: [[getting-started]], [[keyword-network]], [[debugging-the-compiler]], [[overview]], [[development-tips]], [[testing-guide]], [[continuous-integration]]
