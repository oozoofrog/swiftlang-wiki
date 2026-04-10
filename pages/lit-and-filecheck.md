---
type: reference
category: tooling
tags: [lit, filecheck, testing, test-suite, compiler]
aliases: [lit와 FileCheck, lit/FileCheck, Swift 테스트 인프라]
sources: [testing.md, debugging-the-compiler.md]
---

# lit와 FileCheck

Swift 컴파일러 테스트 문화를 이해하려면 lit와 FileCheck를 알아야 한다.
일반 앱 개발에서 익숙한 unit test 프레임워크만으로는 Swift 컴파일러 저장소의 테스트 구조를 설명하기 어렵다.

## 한 줄 요약

- lit는 테스트 실행기다.
- FileCheck는 출력 패턴 검증기다.
- Swift 컴파일러의 많은 테스트는 둘의 조합으로 돌아간다.

## 왜 중요한가

Swift 컴파일러 테스트는 단순히 함수 결과만 보는 게 아니라,
- 특정 진단 메시지가 나오는지
- 특정 SIL/IR 출력이 생기는지
- 특정 옵션에서 파이프라인이 어떻게 동작하는지
를 검증해야 한다.

이때 lit + FileCheck 조합이 매우 강력하다.

## 핵심 구성 요소

### lit
- 테스트 디렉터리를 순회하고
- `RUN:` 지시문을 실행하며
- 환경/조건/플랫폼별 테스트 제어를 담당한다.

### FileCheck
- 실행 결과 텍스트에서 원하는 패턴이 존재하는지 검사한다.
- 진단 텍스트, SIL, LLVM IR, 어셈블리 등 다양한 출력 검증에 쓰인다.

## Swift 저장소에서 자주 보는 요소

- `// RUN:` — 실행 명령
- `// CHECK:` — 기대 출력 패턴
- `%target-swift-frontend` — 프론트엔드 호출 치환 변수
- `REQUIRES:` — 플랫폼/기능 조건
- primary / validation / unit test 분리

## 어떤 종류의 문제에 적합한가

- 진단 회귀 테스트
- 파서/타입체커 출력 변화 테스트
- SIL/IR 출력 확인
- 특정 최적화 패스 동작 검증
- 재현용 축소 테스트 케이스 고정

## 일반 unit test와 어떻게 다른가

- Swift Testing/XCTest는 런타임 로직 검증에 적합하다.
- lit/FileCheck는 “컴파일러가 뭘 출력하고 어떤 변환을 했는지” 검증하는 데 적합하다.
- 둘은 대체 관계가 아니라 역할이 다르다.

관련 페이지:
- [[testing-guide]]
- [[swift-testing-package]]
- [[debugging-the-compiler]]

## 실무적으로 같이 익히면 좋은 것

- `utils/run-test`
- 빌드 디렉터리 구조 이해
- SIL / LLVM IR 덤프 플래그
- 최소 재현 케이스 축소

## 추천 읽기 순서

1. [[testing-guide]]
2. [[debugging-the-compiler]]
3. [[swift-compiler-build-test-debug-stack]]
4. [[sil-reference]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-compiler-build-test-debug-stack]]
- [[testing-guide]]
- [[debugging-the-compiler]]
- [[swift-testing-package]]
