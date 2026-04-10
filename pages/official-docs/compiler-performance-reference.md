---
type: reference
category: official-docs
tags: [official-docs, performance, compiler, tooling]
aliases: [Compiler Performance, Swift Compiler Performance]
sources: [swiftlang-swift/docs/CompilerPerformance.md]
---

# Compiler Performance 문서 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `markdown`
- 다운로드 번들 경로: `swiftlang-swift/docs/CompilerPerformance.md`
- 원본 URL: https://github.com/swiftlang/swift/blob/main/docs/CompilerPerformance.md

## 이 문서는 무엇을 설명하나

Swift 컴파일 시간의 구조적 원인, 측정 도구, 회귀 격리 절차, scale test 전략을 설명하는 성능 실무 레퍼런스다.

## 핵심 포인트

- primary-file / batch / WMO 모드 차이가 성능 관찰에 직접적인 영향을 준다.
- 표현식 타입 추론 폭증, 모듈 로딩, SIL/LLVM 비용 같은 병목이 어떻게 구분되는지 설명한다.
- `-debug-time-*`, `-print-stats`, Instruments, perf 등 도구 체계가 매우 구체적이다.
- 회귀 분석은 환경 정규화 → 단일 frontend 격리 → 카운터 비교 → testcase 축소 순서가 핵심이다.

## 컴파일러와 어떻게 연결되나

- compiler-driver와 batch/WMO 전략
- type-checker 병목 관찰
- SILOptimizer / IRGen / LLVM 비용 측정
- UnifiedStatsReporter와 process-stats-dir.py

## 언어 표면에서 어떻게 들어오면 좋은가

- 복잡한 표현식과 제네릭 코드
- 모듈 의존성 / C-ObjC import
- 최적화 수준 차이
- 대형 value type과 inlineable 코드

## 같이 보면 좋은 위키 페이지

- [[compiler-performance]]
- [[compiler-driver]]
- [[dependency-analysis]]
- [[debugging-the-compiler]]
- [[optimizer-design]]
- [[type-checker]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

성능 문제를 볼 때는 “언어 기능 자체가 느린가?”보다 “어느 단계가 느린가?”를 먼저 분리하는 문서다.
