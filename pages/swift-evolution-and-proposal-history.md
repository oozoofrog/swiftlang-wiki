---
type: summary
category: learning
tags: [swift, evolution, proposal-history, manifesto, design]
aliases: [Swift Evolution / proposal history, Swift Evolution 허브, proposal history 허브]
sources: [swiftlang-swift/docs/proposals, swiftlang-swift/docs/proposals/archive, swiftlang-swift/docs/proposals/rejected, generics-manifesto.md, ownership-manifesto.md, official-docs/abi-stability-manifesto.md]
---

# Swift Evolution / proposal history

이 페이지는 Swift 언어와 컴파일러를 “지금 구현이 어떤가”가 아니라
“왜 이런 방향으로 왔는가”라는 설계/역사 관점에서 읽기 위한 상위 허브다.

기존 위키에는 [[generics-manifesto]], [[ownership-manifesto]], [[library-evolution]],
[[official-docs/abi-stability-manifesto]], [[swift-concurrency-architecture]]처럼
개별 축의 설계 문서나 결과 상태를 설명하는 페이지는 이미 있다.
하지만 proposal, manifesto, archive, rejected 문서를 한 덩어리의 “언어 진화 지형도”로 묶는 입구는 비어 있었다.

## 이 허브가 묶는 6개 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| 비전 문서 | Swift는 장기적으로 어떤 방향을 지향했는가 | [[generics-manifesto]], [[ownership-manifesto]], [[official-docs/abi-stability-manifesto]] |
| 제안 문서 | 기능은 어떤 문제의식으로 제안되었는가 | [[swift-language-overview]], [[swift-and-swift-compiler]] |
| archive / rejected | 왜 어떤 방향은 접혔고, 어떤 방향은 재구성되었는가 | [[swift-concurrency-architecture]], [[swift-ownership-memory-model]] |
| 구현 연결 | proposal은 어떤 compiler / ABI / runtime 변경으로 이어졌는가 | [[type-checker]], [[sil-reference]], [[runtime]], [[library-evolution]] |
| 언어 표면 vs 내부 구현 | surface syntax와 implementation burden는 어떻게 맞물렸는가 | [[swift-type-system]], [[standard-library-runtime-and-compiler]] |
| 역사 읽기 방법 | 현재 문서와 과거 proposal 문서를 어떻게 함께 읽어야 하는가 | [[swift-compiler-learning-stack]], [[keyword-network]] |

## 왜 이 허브가 필요한가

Swift를 구현 중심으로 공부하다 보면 종종 이런 질문이 생긴다.

- 왜 제네릭은 이런 형태로 설계됐지?
- 왜 ownership은 opt-in 철학을 강조하지?
- 왜 ABI stability / library evolution 문서가 이렇게 보수적이지?
- 왜 어떤 기능은 proposal에 있었지만 실제 언어에는 다른 형태로 들어왔지?

이 질문들은 현재 코드만 봐서는 잘 안 풀린다.
proposal / manifesto / archive 문서를 같이 봐야
“지금의 구현”이 “과거의 설계 선택” 위에 있다는 점이 드러난다.

## 로컬에서 직접 확인되는 역사 재료

이 머신의 로컬 Swift 소스 트리에서 바로 확인되는 주된 역사 재료는 다음이다.

- `swift/docs/proposals/` — 초기/중기 설계 proposal 문서들
- `swift/docs/proposals/archive/` — 현재 기준으로 접혔거나 역사적 의미가 강한 proposal
- `swift/docs/proposals/rejected/` — 채택되지 않은 방향
- `swift/docs/GenericsManifesto.md`
- `swift/docs/OwnershipManifesto.md`
- `swift/docs/ABIStabilityManifesto.md`

반면 공개 Swift Evolution 저장소 자체를 이 로컬 checkout 안에서 직접 확인할 수는 없었다.
즉 지금 로컬에서 읽을 수 있는 것은 “swift 메인 저장소에 남아 있는 설계 역사” 쪽이라고 보는 편이 맞다.

## 자주 헷갈리는 구분

### 1. Swift Evolution vs library evolution
이 둘은 이름이 비슷하지만 다르다.

- Swift Evolution: 언어/기능 설계 제안과 채택의 역사
- library evolution: ABI와 resilience를 전제로 공개 라이브러리를 어떻게 진화시키는가

관련 페이지:
- [[library-evolution]]
- [[official-docs/abi-stability-manifesto]]

### 2. manifesto vs implemented feature
manifesto는 “이미 구현된 명세서”가 아니라
장기 비전, 용어 정리, 설계 공간의 지도에 가깝다.
그래서 manifesto를 읽을 때는 현재 구현 페이지와 꼭 같이 봐야 한다.

관련 페이지:
- [[generics-manifesto]]
- [[ownership-manifesto]]
- [[official-docs/swift-generics-manifesto]]

### 3. archived proposal vs dead idea
archive에 들어갔다고 해서 완전히 의미가 사라진 것은 아니다.
오히려 현재 구현의 전신, 대안, 실패한 추상화 실험을 보여 주는 경우가 많다.
예를 들어 concurrency를 볼 때도 `MemoryAndConcurrencyModel.rst` 같은 문서는 여전히 맥락을 준다.

관련 페이지:
- [[swift-concurrency-architecture]]
- [[swift-task-executor-runtime]]

### 4. proposal history vs source-level implementation doc
proposal은 “왜”를 설명하고,
implementation doc은 “어떻게”를 설명하는 경우가 많다.
둘을 같이 봐야 납득이 된다.

관련 페이지:
- [[type-checker]]
- [[sil-reference]]
- [[runtime]]

## proposal history를 읽는 좋은 방법

### 1. 현재 기능 허브를 먼저 본다
먼저 현재 상태를 요약한 허브를 읽는다.

예:
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]

### 2. 그다음 manifesto / proposal 문서를 본다
현재 구조를 알고 난 뒤 proposal 문서를 보면,
무슨 제약을 풀려 했고 무엇이 아직 미완인지 더 잘 보인다.

바로 이어 읽기 좋은 교차 페이지:
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-declaration-type-checker-to-sema]]
- [[proposal-compilation-model-and-wmo-to-driver]]

### 3. 마지막으로 구현 페이지로 내려간다
proposal의 아이디어가 compiler / runtime / ABI에서 어떤 비용을 치렀는지 확인한다.

예:
- [[type-checker]]
- [[sil-ownership]]
- [[runtime]]
- [[library-evolution]]

## 로컬 Swift 소스에서 같이 볼 경로

### 비전 / 장기 방향 문서
- `swift/docs/GenericsManifesto.md`
- `swift/docs/OwnershipManifesto.md`
- `swift/docs/ABIStabilityManifesto.md`

### proposals 디렉터리 예시
- `swift/docs/proposals/Concurrency.rst`
- `swift/docs/proposals/ValueSemantics.rst`
- `swift/docs/proposals/InoutCOWOptimization.rst`
- `swift/docs/proposals/WholeModuleOptimization.rst`
- `swift/docs/proposals/RemoteMirrors.rst`
- `swift/docs/proposals/ObjCInteroperation.rst`
- `swift/docs/proposals/DeclarationTypeChecker.rst`

### archive / rejected 예시
- `swift/docs/proposals/archive/MemoryAndConcurrencyModel.rst`
- `swift/docs/proposals/archive/ProgramStructureAndCompilationModel.rst`
- `swift/docs/proposals/archive/UnifiedFunctionSyntax.rst`
- `swift/docs/proposals/rejected/ClassConstruction.rst`
- `swift/docs/proposals/rejected/Constructors.rst`
- `swift/docs/proposals/rejected/KeywordArguments.rst`

이 목록만 봐도 Swift 진화사는
문법 제안만의 역사가 아니라,
타입 시스템, ownership, ABI, interop, optimizer, compilation model이 함께 움직인 역사라는 점이 드러난다.

## 추천 읽기 순서

### 큰 그림부터 보는 루트
1. [[swift-ecosystem-map]]
2. [[swift-language-overview]]
3. [[swift-evolution-and-proposal-history]]
4. [[swift-and-swift-compiler]]

### 제네릭 / 타입 시스템 중심
1. [[swift-type-system]]
2. [[generics-manifesto]]
3. [[official-docs/swift-generics-manifesto]]
4. [[swift-evolution-and-proposal-history]]
5. [[proposal-declaration-type-checker-to-sema]]

### ownership / concurrency 중심
1. [[swift-ownership-memory-model]]
2. [[swift-concurrency-architecture]]
3. [[ownership-manifesto]]
4. [[swift-evolution-and-proposal-history]]
5. [[proposal-value-semantics-and-cow-to-ownership]]

### ABI / 배포 / 안정성 중심
1. [[standard-library-runtime-and-compiler]]
2. [[library-evolution]]
3. [[official-docs/abi-stability-manifesto]]
4. [[swift-evolution-and-proposal-history]]
5. [[proposal-compilation-model-and-wmo-to-driver]]

## 같이 보면 좋은 페이지

- [[swift-ecosystem-map]]
- [[swift-language-overview]]
- [[swift-and-swift-compiler]]
- [[swift-type-system]]
- [[swift-ownership-memory-model]]
- [[swift-concurrency-architecture]]
- [[proposal-value-semantics-and-cow-to-ownership]]
- [[proposal-declaration-type-checker-to-sema]]
- [[proposal-compilation-model-and-wmo-to-driver]]
- [[generics-manifesto]]
- [[ownership-manifesto]]
- [[library-evolution]]
- [[official-docs/abi-stability-manifesto]]
- [[official-docs/swift-generics-manifesto]]
- [[keyword-network]]