---
type: reference
category: meta
tags: [wiki, chronology, timeline, coverage]
aliases: [위키 연대기, 위키 지식 연대기, knowledge chronology]
sources: [log.md]
---

# 위키 지식 연대기

이 페이지는 Swiftlang wiki의 지식 추가·확장 흐름을 별도로 기록하는 연대기다.
개별 지식 페이지는 주제 자체 설명에 집중하고,
위키의 확장 메타 정보는 여기로 모은다.

## 기록 원칙

- 새 상위 허브, 대규모 문서 수집, 공식 문서 해설 묶음, proposal 교차 읽기 묶음처럼
  지식 범위가 넓어지는 변화 위주로 기록한다.
- lint, sanitize, 내부 정리 같은 유지보수 작업은 필요할 때만 최소한으로 언급한다.
- 새 배치가 추가될 때마다 이 페이지도 함께 갱신한다.

## 2026-04-10

### 상위 허브 확장

이날 위키는 개별 문서 모음에서
상위 지도와 학습 허브가 있는 구조로 크게 확장됐다.

추가/정비된 대표 허브:
- [[swift-ecosystem-map]]
- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]
- [[standard-library-runtime-and-compiler]]
- [[swift-toolchain-stack]]
- [[swift-macro-tooling-stack]]
- [[swift-compiler-learning-stack]]
- [[swift-compiler-build-test-debug-stack]]

### 공식 문서 / 다운로드 축 확장

공식 문서를 위키 안에서 다시 읽을 수 있도록
다운로드 허브와 해설 허브가 크게 보강됐다.

대표 페이지:
- [[downloads/index]]
- [[official-docs/index]]
- [[official-docs/language-to-compiler-crosswalk]]
- [[official-docs/swift-documentation-index]]
- [[official-docs/swift-compiler-architecture]]
- [[official-docs/compiling-swift-generics-pdf]]
- [[official-docs/swift-intermediate-language]]
- [[official-docs/high-level-optimizations-in-sil]]
- [[official-docs/abi-stability-manifesto]]

### 동시성 / 입문 경로 확장

동시성 관련 현재 구현 설명과 입문 경로가 보강됐다.

대표 페이지:
- [[concurrency-data-race-safety]]
- [[swift-compiler-7-day-course]]
- [[swift-concurrency-architecture]]
- [[swift-actor-isolation-and-sendable]]
- [[swift-task-executor-runtime]]

### 설계 역사 / proposal 교차 읽기 축 확장

Swift 설계 문서를 현재 구현 문맥과 함께 읽을 수 있도록
history 허브와 crosswalk 묶음이 본격적으로 추가됐다.

대표 허브:
- [[swift-evolution-and-proposal-history]]

추가된 주요 교차 읽기 페이지:
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-in-place-operations-to-writeback-and-cow]]
- [[proposal-optimizer-effects-and-attributes-to-sil-optimizer]]
- [[proposal-declaration-type-checker-to-sema]]
- [[proposal-compilation-model-and-wmo-to-driver]]
- [[proposal-enums-and-enum-style-to-type-system-and-layout]]
- [[proposal-typestate-to-initialization-and-lifetime-model]]
- [[proposal-option-sets-to-importer-and-layout]]
- [[proposal-c-export-and-bridging-to-importer]]
- [[proposal-c-pointer-interop-to-unsafe-pointer-model]]
- [[proposal-objc-interop-to-importer-and-dispatch]]
- [[proposal-initialization-and-accessors-to-property-model]]
- [[proposal-initializer-inheritance-to-modern-init-model]]
- [[proposal-constructors-and-class-construction-to-init-model]]
- [[proposal-remote-mirrors-to-runtime-reflection]]

## 2026-04-09

### 기반 문서군 구축

첫날에는 위키의 기본 뼈대를 이루는 핵심 문서들이 수집·정리됐다.

대표 페이지/묶음:
- [[overview]]
- [[glossary-compiler]]
- [[sil-reference]] 및 SIL 관련 페이지들
- [[optimizer-design]]
- [[type-checker]]
- [[runtime]]
- [[abi-mangling]], [[abi-type-metadata]], [[abi-type-layout]], [[abi-calling-convention]], [[abi-stability]]
- [[ownership-manifesto]]
- [[generics-manifesto]]
- [[error-handling]]
- [[dynamic-casting]]

### 제네릭 / interop / 패키지 / 기여 가이드 확장

기초 코어 위에 제네릭, interop, 주요 패키지, 기여 관련 문서가 붙기 시작했다.

대표 페이지:
- [[compiling-swift-generics]]
- [[generic-signatures]]
- [[substitution-maps]]
- [[archetypes]]
- [[conformances]]
- [[objc-interop]]
- [[c-to-swift-name-translation]]
- [[how-swift-imports-c-apis]]
- [[cpp-interop-overview]]
- [[cpp-using-from-swift]]
- [[cpp-calling-swift]]
- [[swift-syntax-package]]
- [[swift-driver-package]]
- [[swift-package-manager]]
- [[sourcekit-lsp]]
- [[getting-started]]
- [[testing-guide]]
- [[continuous-integration]]

### 코드 구조 분석 페이지 추가

문서 기반 요약만이 아니라,
실제 Swift 소스 트리 구조를 바탕으로 한 코드 분석 페이지도 들어왔다.

대표 페이지:
- [[sil-optimizer-pass-catalog]]
- [[ast-node-hierarchy]]
- [[swift-compiler-sources]]

## 같이 보면 좋은 페이지

- [[index]]
- [[swift-ecosystem-map]]
- [[swift-evolution-and-proposal-history]]
- [[keyword-network]]
- [[swift-compiler-learning-stack]]
