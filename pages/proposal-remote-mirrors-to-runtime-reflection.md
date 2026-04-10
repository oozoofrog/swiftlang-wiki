---
type: reference
category: learning
tags: [swift, proposal, remote-mirrors, reflection, runtime, metadata]
aliases: [Remote Mirrors proposal 교차 읽기, remote mirrors to runtime reflection]
sources: [swiftlang-swift/docs/proposals/RemoteMirrors.rst]
---

# Remote Mirrors proposal → runtime/reflection 교차 읽기

이 페이지는 `swift/docs/proposals/RemoteMirrors.rst`를
현재 Swift runtime, type metadata, reflection, LLDB/debugging 관점으로 다시 읽는 교차 페이지다.

## 이 proposal이 설명하는 핵심 문제

문서의 질문은 매우 실용적이다.

- 죽어 있거나 이상한 상태의 프로세스에서 코드를 실행하지 않고
- heap object graph를 읽고
- field layout과 reference kind를 파악하고
- leak / cycle / post-mortem debugging을 지원하려면
런타임 메타데이터를 어떻게 설계해야 하는가?

즉 이 proposal은 “Mirror 기능 하나 더”가 아니라,
Swift runtime metadata를 debugging / out-of-process inspection 용도로 어떻게 재구성할 것인가를 다룬다.

## proposal의 핵심 포인트

### 1. nominal type metadata를 reflection/debugging에 재활용하려 한다
문서는 기존 metadata와 Mirrors 구현을 버리는 대신,
generic metadata / nominal type descriptor / field type metadata를 재구성해서
in-process / out-of-process reflection 양쪽에 쓰려 한다.

이 점은 현재 다음 페이지와 직접 이어진다.

- [[abi-type-metadata]]
- [[runtime]]

### 2. generic type metadata만으로는 부족하다
proposal은 generic metadata가
allocation size는 알려 줘도 field type과 reference kind까지는 충분히 알려 주지 못한다고 본다.
그래서 field type metadata, symbolic type reference, interpreter-like library가 필요하다고 설명한다.

이건 Swift metadata가
단순 런타임 dispatch용이 아니라 debugger/tooling에서도 쓰이는 기반이라는 점을 드러낸다.

### 3. out-of-process reflection은 “코드를 실행하지 않는 것”이 핵심 제약이다
이 문서의 가장 중요한 제약은
대상 프로세스 안에서 함수를 호출할 수 없다는 점이다.
그래서 lazy function 호출 기반 reflection은 불충분하고,
정적/직렬화 가능한 metadata 표현이 필요하다고 본다.

즉 remote mirrors proposal은
metadata layout, stripping, field names, strong/weak/unowned reference kind까지
모두 debugging 현실과 연결해서 본다.

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. type metadata / runtime
proposal을 읽고 나면 먼저 봐야 할 페이지:
- [[abi-type-metadata]]
- [[runtime]]

### 2. LLDB / debugger 경험
remote mirrors가 겨냥한 사용 사례는
사실상 debugger / heap inspection / leak/cycle analysis 쪽이다.
그래서 다음 페이지와도 잘 맞는다.

- [[lldb-and-swift-debugging]]
- [[official-docs/swift-repl-and-debugger]]

### 3. ownership / reference kind
문서는 strong / weak / unowned reference 구분을 중요하게 본다.
이건 ownership과 직접 만나는 지점이다.

관련 페이지:
- [[swift-ownership-memory-model]]
- [[sil-ownership]]

## proposal을 읽을 때 특히 흥미로운 부분

### heap allocation 종류 분류
문서는 class instance, ObjC instance, boxes, contexts, blocks, metatypes, opaque value buffer를 구분해서 설명한다.
이 분류는 runtime 문서를 훨씬 실감 나게 읽게 해 준다.

### Mirrors와 debugging의 접점
현재 사용자 관점의 reflection과
tooling/debugging 관점의 reflection이
사실 같은 metadata 기반을 공유할 수 있다는 발상이 핵심이다.

### binary size / metadata stripping
문서는 reflection metadata를 얼마나 남길 것인가도 고민한다.
즉 reflection은 단지 기능 문제가 아니라
size / secrecy / release build 정책 문제이기도 하다.

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/RemoteMirrors.rst`
- `swift/docs/ABI/TypeMetadata.rst`
- `swift/include/swift/Runtime/`

현재 위키 연결:
- [[abi-type-metadata]]
- [[runtime]]
- [[lldb-and-swift-debugging]]
- [[swift-ownership-memory-model]]

## 이 문서를 읽을 때 주의할 점

- proposal의 구조를 현재 runtime 구현과 1:1 대응시키면 안 된다.
- 하지만 “metadata를 debugging-friendly하게 만들려는 압력”이 어디서 오는지는 매우 잘 보여 준다.
- 따라서 ABI / runtime / debugger를 함께 공부할 때 가치가 크다.

## 추천 읽기 순서

1. [[proposal-remote-mirrors-to-runtime-reflection]]
2. [[abi-type-metadata]]
3. [[runtime]]
4. [[lldb-and-swift-debugging]]
5. [[swift-ownership-memory-model]]

## 같이 보면 좋은 페이지

- [[swift-evolution-and-proposal-history]]
- [[abi-type-metadata]]
- [[runtime]]
- [[lldb-and-swift-debugging]]
- [[swift-ownership-memory-model]]
- [[sil-ownership]]
- [[keyword-network]]
