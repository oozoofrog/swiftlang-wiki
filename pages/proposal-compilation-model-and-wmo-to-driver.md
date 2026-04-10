---
type: reference
category: learning
tags: [swift, proposal, compilation-model, wmo, driver, build-system]
aliases: [Compilation model / WMO proposals, compilation model과 WMO 교차 읽기]
sources: [swiftlang-swift/docs/proposals/archive/ProgramStructureAndCompilationModel.rst, swiftlang-swift/docs/proposals/WholeModuleOptimization.rst]
---

# Compilation Model / WMO proposals → driver 교차 읽기

이 페이지는
`swift/docs/proposals/archive/ProgramStructureAndCompilationModel.rst`와
`swift/docs/proposals/WholeModuleOptimization.rst`를
현재 Swift driver / dependency analysis / SwiftPM / llbuild / compiler performance 관점으로 다시 읽는 교차 페이지다.

## 이 proposal 묶음이 흥미로운 이유

두 문서는 같은 층을 본다.

- Swift 프로그램을 어떤 단위로 나눠 빌드할 것인가
- 모듈/컴포넌트/증분 빌드/WMO를 어떤 모델로 다룰 것인가
- compiler가 file-by-file C 모델과 왜 다르게 움직여야 하는가

즉 현재 위키의
[[compiler-driver]], [[dependency-analysis]], [[swift-driver-package]], [[swift-package-manager]], [[llbuild-package]]
같은 페이지를 역사적으로 거슬러 올라가게 해 주는 자료다.

## ProgramStructureAndCompilationModel.rst의 핵심 포인트

### 1. C translation unit 모델을 넘어서려는 문제의식
이 문서는 아주 초기 단계에서
C/Unix식 번역 단위 모델이
Swift 같은 언어에는 너무 빈약하다고 본다.

문제의식:
- 파일 시스템 레이아웃
- 빌드 시스템
- 리소스
- 버저닝/SDK
- incremental compilation
- API/SPI 경계
를 언어/도구 모델이 더 잘 품어야 한다는 것이다.

### 2. component / subcomponent / ownership domain 비전
문서는 top-level component, namespace, subcomponent, source file 같은 개념을 제안한다.
이 중 상당수는 오늘날 그대로 사용자 모델이 되지는 않았지만,
문제 자체는 사라지지 않았다.

현재 구현 쪽에 남은 흔적/대체물은 대략 이런 식으로 읽을 수 있다.

- top-level build / module 감각 → [[compiler-driver]], [[swift-package-manager]]
- dependency graph / build orchestration → [[dependency-analysis]], [[llbuild-package]]
- API/SPI / resilience / shipping unit → [[library-evolution]], [[abi-stability]]

즉 proposal의 어휘는 일부 바뀌었지만,
Swift가 “프로그램 구조와 빌드 모델을 언어 차원 문제로 본다”는 감각은 계속 남아 있다.

## WholeModuleOptimization.rst의 핵심 포인트

### 1. WMO는 단순 플래그가 아니라 compilation model의 변화다
문서는 WMO를 단순 optimization level이 아니라,
모듈 전체를 한 번에 볼 수 있을 때 가능한 interprocedural optimization 환경으로 본다.

핵심 효과:
- 더 넓은 inlining
- 더 많은 generic specialization 기회
- dead function 제거
- interprocedural analysis 개선

### 2. SCC 기반 pass management
이 문서에서 가장 중요한 부분 중 하나는
call graph SCC를 중심으로 pass를 조직하자는 제안이다.

즉 함수 하나씩이 아니라
강하게 연결된 호출 집합 단위로 bottom-up / top-down 분석을 하자는 이야기다.
이건 WMO의 진짜 난점이 단순 “전체 모듈을 본다”가 아니라
“그 정보를 어떤 pass manager / analysis framework 위에서 굴리느냐”라는 점을 보여 준다.

### 3. incremental WMO / parallel WMO
문서는 이미 아주 일찍부터
WMO가 build time을 늘릴 수 있으니
- incremental WMO
- serialized analysis result
- dependency tracking
- parallel SIL / IRGen 가능성
을 고민한다.

즉 오늘날의 Swift build/toolchain 성격을 이해하려면
이 문서를 단순 optimizer 문서가 아니라 driver / build system 역사로 읽는 편이 맞다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. Driver / compilation pipeline
현재 구조의 직접 연결축:
- [[compiler-driver]]
- [[dependency-analysis]]
- [[swift-driver-package]]

### 2. Build orchestration
proposal의 build model 감각은 오늘날
- [[swift-package-manager]]
- [[llbuild-package]]
- [[swift-compiler-build-test-debug-stack]]
으로 더 잘 드러난다.

### 3. Performance / WMO 실전
WMO proposal은 실제로는 다음 페이지와 같이 읽어야 의미가 커진다.

- [[compiler-performance]]
- [[official-docs/compiler-performance-reference]]
- [[llvm-backend]]

## proposal을 읽을 때 주의할 점

### 1. 초기 build-model proposal을 현재 사용자 모델로 오해하면 안 된다
component / subcomponent / manifest 같은 개념은
오늘날 그대로 Swift 사용자 언어 모델이 되지 않았다.
하지만 그 문서가 던진 질문은
여전히 driver / package manager / build graph 문제 안에 남아 있다.

### 2. WMO는 optimizer 문서이면서 build 문서다
WMO를 그냥 최적화 테크닉으로만 읽으면 절반만 읽는 셈이다.
이 문서는 pass scheduling, dependency tracking, incremental rebuild 문제까지 묶고 있다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/archive/ProgramStructureAndCompilationModel.rst`
- `swift/docs/proposals/WholeModuleOptimization.rst`
- `swift/docs/Driver.md`
- `swift/lib/Driver/` 관련 구현은 별도 저장소/패키지 축과 함께 봐야 함

현재 위키 연결:
- [[compiler-driver]]
- [[dependency-analysis]]
- [[swift-driver-package]]
- [[swift-package-manager]]
- [[llbuild-package]]
- [[compiler-performance]]

## 추천 읽기 순서

1. [[proposal-compilation-model-and-wmo-to-driver]]
2. [[compiler-driver]]
3. [[dependency-analysis]]
4. [[swift-driver-package]]
5. [[swift-package-manager]]
6. [[llbuild-package]]
7. [[compiler-performance]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[swift-toolchain-stack]]
- [[swift-compiler-build-test-debug-stack]]
- [[compiler-driver]]
- [[dependency-analysis]]
- [[swift-driver-package]]
- [[swift-package-manager]]
- [[llbuild-package]]
- [[compiler-performance]]
- [[keyword-network]]
