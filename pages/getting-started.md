---
type: summary
category: documentation
tags: [getting-started, build, setup]
aliases: [시작하기, Getting Started]
sources: [getting-started.md]
---

# Swift 개발 환경 설정

Swift 컴파일러 기여를 위한 환경 구성과 편집-빌드-테스트-디버그 루프 안내.

## 요구 사항

- macOS 또는 Ubuntu Linux, 디스크 150GB+, RAM 8GB+
- Python 3, Git 2.x

## 핵심 워크플로우

1. `git clone` 후 `utils/update-checkout --clone`
2. `utils/build-script -r --debug-swift-frontend`로 빌드
3. Ninja 직접 사용(`ninja bin/swift-frontend`)으로 증분 빌드
4. `utils/build-script --test` 또는 `lit.py`로 테스트
5. LLDB로 컴파일러 디버깅

## 빌드 가속

- `sccache`로 빌드 캐싱
- `--bootstrapping=hosttools`로 빌드 시간 단축

관련 페이지: [[overview]], [[keyword-network]], [[swift-compiler-build-test-debug-stack]], [[cmake-and-ninja-build]], [[compiler-driver]], [[testing-guide]], [[development-tips]], [[compiler-faq]], [[continuous-integration]], [[debugging-the-compiler]]
