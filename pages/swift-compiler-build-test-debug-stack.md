---
type: summary
category: tooling
tags: [build, test, debug, workflow, compiler, infrastructure]
aliases: [빌드-테스트-디버그 스택, Swift Compiler 실무 루프, Build Test Debug Stack]
sources: [getting-started.md, testing.md, debugging-the-compiler.md]
---

# Swift Compiler 빌드·테스트·디버그 스택

이 페이지는 Swift Compiler 기여자의 실무 루프를 한 장으로 묶은 허브다.
즉 “코드를 읽고 → 고치고 → 빌드하고 → 테스트하고 → 디버깅하고 → CI까지 확인하는 흐름”을 연결해서 본다.

## 전체 루프

```text
편집
→ 빌드 구성 확인
→ 증분 빌드
→ 관련 테스트 실행
→ 실패 시 디버깅
→ 재현 케이스 축소
→ CI 검증
```

## 단계별 핵심 도구

| 단계 | 핵심 도구 | 관련 페이지 |
|---|---|---|
| 초기 설정 | build-script, checkout, toolchain setup | [[getting-started]] |
| 빌드 그래프/증분 빌드 | CMake, Ninja | [[cmake-and-ninja-build]] |
| 프론트엔드/파이프라인 이해 | driver, dependency analysis | [[compiler-driver]], [[dependency-analysis]] |
| 테스트 실행 | lit, FileCheck, run-test | [[lit-and-filecheck]], [[testing-guide]] |
| 디버깅 | LLDB, dump flags, SIL/IR 출력 | [[lldb-and-swift-debugging]], [[debugging-the-compiler]] |
| 최적화/백엔드 추적 | SIL dump, LLVM IR, pass bisect | [[sil-reference]], [[llvm-backend]], [[optimizer-design]] |
| 최종 검증 | validation / CI | [[continuous-integration]], [[first-pull-request]] |

## 왜 이 허브가 필요한가

기존 문서들은 각각
- 환경 설정
- 테스트 작성
- 디버깅 테크닉
- 드라이버 구조
를 따로 설명한다.
하지만 실제 기여는 이 문서들을 번갈아 오가는 루프로 진행된다.
그래서 이 페이지는 개별 도구보다 “실제 작업 흐름” 중심으로 정리한다.

## 대표 시나리오

### 1. 진단 버그 수정
- 관련 표현식 재현
- 프론트엔드 출력 / 타입체커 흐름 확인
- lit/FileCheck 테스트 추가
- LLDB나 dump 플래그로 내부 상태 확인

연결 페이지:
- [[diagnostics]]
- [[testing-guide]]
- [[lit-and-filecheck]]
- [[lldb-and-swift-debugging]]

### 2. 최적화/성능 문제 조사
- SIL 전후 출력 비교
- 특정 패스 bisect
- 필요하면 LLVM IR까지 내려가 확인

연결 페이지:
- [[optimizer-design]]
- [[sil-optimizer-pass-catalog]]
- [[llvm-backend]]
- [[compiler-performance]]

### 3. 빌드/인프라 문제 조사
- CMakeLists / 타깃 등록 확인
- Ninja 증분 빌드 루프 확인
- 드라이버/SwiftPM/llbuild 경계 확인

연결 페이지:
- [[cmake-and-ninja-build]]
- [[compiler-faq]]
- [[swift-driver-package]]
- [[llbuild-package]]

## 최소 실무 루프

1. [[getting-started]]
2. [[cmake-and-ninja-build]]
3. [[testing-guide]]
4. [[lit-and-filecheck]]
5. [[debugging-the-compiler]]
6. [[lldb-and-swift-debugging]]
7. [[continuous-integration]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-compiler-learning-stack]]
- [[getting-started]]
- [[testing-guide]]
- [[debugging-the-compiler]]
- [[continuous-integration]]
