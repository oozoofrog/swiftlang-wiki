---
type: reference
category: official-docs
tags: [official-docs, driver, build, tooling]
aliases: [Driver Internals, Driver Design & Internals]
sources: [swiftlang-swift/docs/DriverInternals.md]
---

# Driver Internals 문서 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/DriverInternals.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/DriverInternals.md

## 이 문서는 무엇을 설명하나

Swift 드라이버의 Action DAG, Job 생성, scheduling, batch mode, task queue 개념을 설명하는 드라이버 내부 개요다.

## 핵심 포인트

- 드라이버를 Parse → Pipeline → Build → Schedule → Batch → Execute 단계로 본다.
- Action은 고수준 작업, Job은 실제 subprocess invocation이라는 구분이 중요하다.
- output file map과 dependency graph가 빌드 시스템 연동의 핵심이다.
- batch mode는 frontend 프로세스 수와 중복 초기 비용을 줄이기 위한 전략이다.

## 컴파일러와 어떻게 연결되나

- compiler-driver
- dependency-analysis
- swift-driver-package
- ToolChain / Action / Job / Compilation / TaskQueue

## 언어 표면에서 어떻게 들어오면 좋은가

- 모듈 단위 컴파일
- 파일 간 암시적 가시성
- 증분 빌드와 링크 단계
- `swiftc` 실행 모델

## 같이 보면 좋은 위키 페이지

- [[compiler-driver]]
- [[dependency-analysis]]
- [[swift-driver-package]]
- [[overview]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

현대 `swift-driver` 구현과 1:1로 같진 않지만, build system 관점에서 Swift가 왜 “파일 하나만 독립 컴파일”하기 어려운지를 이해하는 데 여전히 유효하다.
