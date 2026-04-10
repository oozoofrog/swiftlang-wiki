---
type: reference
category: tooling
tags: [cmake, ninja, build, infrastructure, swift-compiler]
aliases: [CMake와 Ninja, Swift 빌드 인프라, CMake/Ninja 빌드]
sources: [getting-started.md, debugging-the-compiler.md]
---

# CMake와 Ninja 빌드 인프라

Swift 저장소를 실제로 빌드할 때 가장 자주 마주치는 인프라 축은 CMake와 Ninja다.
초보자에게는 `utils/build-script`만 보이기 쉽지만,
그 아래 실제 빌드 그래프를 정의하고 실행하는 핵심은 이 둘이다.

## 역할 분담

### CMake
- 빌드 그래프를 정의한다.
- 어떤 타깃이 어떤 소스/라이브러리/도구에 의존하는지 기술한다.
- 새 파일 추가, 서브디렉터리 등록, 타깃 연결 같은 구조적 변경이 여기서 반영된다.

### Ninja
- CMake가 만든 그래프를 빠르게 실행한다.
- 증분 빌드가 빠르고, 개별 타깃을 바로 다시 빌드하기 좋다.
- 실무에서는 `ninja bin/swift-frontend` 같은 형태가 자주 나온다.

## Swift 저장소에서 왜 중요한가

- 컴파일러는 대규모 다중 저장소/다중 타깃 빌드다.
- `build-script`는 편의 래퍼지만, 실제 빌드 구성과 실행 문제는 CMake/Ninja에서 드러난다.
- 새 소스 파일을 추가했는데 링크/빌드 문제가 나면 CMake 등록 누락일 때가 많다.

관련 페이지:
- [[getting-started]]
- [[development-tips]]
- [[compiler-faq]]

## 실무 루프에서 어떻게 쓰이나

1. `utils/build-script`로 초기 구성
2. 그 뒤 빠른 반복은 Ninja 직접 호출
3. 문제가 복잡해지면 `--dry-run`이나 긴 명령줄 분해로 실제 호출 구조 확인

예시 축:
- 초기 빌드/구성: [[getting-started]]
- 빠른 반복: [[development-tips]]
- 긴 명령줄/실행 흐름 분석: [[debugging-the-compiler]]

## CMake/Ninja를 배울 때 중요 포인트

- 새 파일/타깃 추가 시 CMakeLists 반영 여부
- build-script와 실제 하위 도구 호출의 관계
- compile database와 편집기 도구의 연결
- Swift frontend, stdlib, driver가 서로 다른 빌드 하위단위를 가진다는 점

## 흔한 오해

1. “Swift는 SwiftPM만 알면 빌드 구조를 이해할 수 있다”
   - 아니다. 컴파일러 본체 기여에는 CMake/Ninja 감각이 여전히 중요하다.
2. “Ninja는 그냥 빠른 make 대체품이다”
   - Swift 저장소에서는 증분 개발 루프를 크게 좌우하는 실무 도구다.
3. “build-script만 알면 된다”
   - 초반엔 그렇지만, 문제 분석과 타깃 수준 수정으로 갈수록 하위 계층 이해가 필요하다.

## 추천 읽기 순서

1. [[getting-started]]
2. [[development-tips]]
3. [[compiler-faq]]
4. [[swift-compiler-build-test-debug-stack]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-compiler-build-test-debug-stack]]
- [[getting-started]]
- [[development-tips]]
- [[compiler-faq]]
