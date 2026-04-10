---
type: entity
category: documentation
tags: [testing, lit, filecheck, test-suite]
aliases: [테스팅 가이드, Testing Guide]
sources: [testing.md]
---

# Swift 테스트 가이드

컴파일러, 런타임, 표준 라이브러리 테스트 실행 및 작성법.

## 테스트 수트

| 구분 | 위치 |
|------|------|
| Primary | `swift/test/` |
| Validation | `swift/validation-test/` |
| Unit | `swift/unittests/` |

## 실행 방법

- 전체: `utils/build-script --test`
- 개별: `utils/run-test --build-dir $BUILD test/Parse`
- lit 직접: `lit.py -sv $BUILD/test-macosx-x86_64/Parse/`

## 테스트 작성

- `// RUN:` 실행 명령, `// CHECK:` 기대 출력
- `%target-swift-frontend` 치환 변수로 프론트엔드 호출
- `FileCheck`으로 출력 패턴 검증
- `REQUIRES:`로 플랫폼/조건 제어

관련 페이지: [[overview]], [[keyword-network]], [[swift-compiler-build-test-debug-stack]], [[lit-and-filecheck]], [[debugging-the-compiler]], [[getting-started]], [[continuous-integration]], [[first-pull-request]], [[compiler-faq]]
