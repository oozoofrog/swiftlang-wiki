---
type: reference
category: tooling
tags: [llvm, backend, irgen, codegen, optimization]
aliases: [LLVM 백엔드, LLVM in Swift, Swift LLVM Backend]
sources: [debugging-the-compiler.md, driver.md, compiler-performance.md]
---

# LLVM 백엔드와 Swift

Swift 컴파일러 파이프라인의 마지막 큰 구현 축은 LLVM이다.
Swift는 고수준 언어 의미를 먼저 AST / SIL 수준에서 다루고,
그 뒤 IRGen이 이를 LLVM IR로 낮춘 다음 LLVM이 최종 최적화와 코드 생성을 맡는다.

## 파이프라인에서 LLVM은 어디에 있나

```text
Swift Source
→ Parser / Sema
→ SILGen
→ Mandatory / Optimization Passes
→ IRGen
→ LLVM IR
→ LLVM Passes
→ Assembly / Object Code
```

즉 LLVM은 Swift의 “앞부분 의미 분석”을 담당하지 않는다.
대신 이미 lowering된 표현을 받아
- 저수준 최적화
- 타깃별 코드 생성
- 어셈블리/오브젝트 파일 생성
을 맡는다.

## Swift에서 LLVM을 볼 때 중요한 경계

### 1. SIL과 LLVM IR의 경계
- SIL은 Swift 고유 의미를 많이 보존한다.
- LLVM IR은 더 낮은 수준의 범용 IR이다.
- 따라서 protocol witness, ownership, resilience 같은 Swift 고유 개념은 LLVM 이전 단계에서 많이 정리된다.

관련 페이지:
- [[sil-reference]]
- [[optimizer-design]]
- [[compiler-performance]]

### 2. IRGen의 역할
IRGen은 Swift 의미를 LLVM이 이해할 수 있는 형태로 번역하는 다리다.
이 지점에서
- type metadata 접근
- value layout 반영
- calling convention 적용
- runtime entrypoint 호출
이 구체화된다.

관련 페이지:
- [[abi-type-layout]]
- [[abi-type-metadata]]
- [[abi-calling-convention]]
- [[runtime]]

### 3. 타깃별 코드 생성
LLVM은 실제 CPU/플랫폼 타깃에 맞춘 lowering과 최적화를 수행한다.
그래서 Swift 성능 이슈를 볼 때도
“문제가 SIL 단계인지, LLVM 단계인지”를 분리해서 생각하는 것이 중요하다.

## 언제 LLVM 쪽을 직접 봐야 하나

- `-emit-ir` 결과가 이상할 때
- 특정 최적화가 SIL 이후에 사라지거나 변형될 때
- 어셈블리/오브젝트 레벨 코드 생성 차이를 확인할 때
- target-specific codegen, debug info, linkage를 보고 싶을 때

## 유용한 관찰 명령

- `swiftc -emit-ir file.swift`
- `swiftc -emit-ir -O file.swift`
- `swiftc -emit-assembly file.swift`
- `swiftc -emit-bc file.swift`
- `swiftc -Xllvm -print-before-all ...`
- `swiftc -Xllvm -print-after-all ...`
- `swiftc -Xllvm -filter-print-funcs=<name> ...`

관련 맥락은 [[debugging-the-compiler]]에 더 많이 정리되어 있다.

## 저장소 관점에서 어디를 보면 되나

- `swift/lib/IRGen/` — Swift → LLVM IR bridging
- `llvm-project/llvm/` — LLVM optimizer/backend 본체
- `llvm-project/clang/` — Clang 쪽 공용 인프라와 interop 연계 축

## LLVM을 Swift 관점에서 볼 때 흔한 오해

1. “성능 최적화는 전부 LLVM에서 한다”
   - 아니다. Swift는 많은 고수준 최적화를 SIL 단계에서 먼저 한다.
2. “LLVM IR만 보면 Swift 의미가 다 보인다”
   - 아니다. ownership, abstraction, witness 같은 중요한 의미는 이미 이전 단계에서 많이 사라진다.
3. “LLVM을 이해해야만 Swift 컴파일러를 시작할 수 있다”
   - 초반에는 아니다. 하지만 IRGen/ABI/성능으로 갈수록 점점 중요해진다.

## 추천 읽기 순서

1. [[overview]]
2. [[sil-reference]]
3. [[compiler-performance]]
4. [[debugging-the-compiler]]
5. [[abi-type-layout]]
6. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-and-swift-compiler]]
- [[compiler-performance]]
- [[debugging-the-compiler]]
- [[abi-type-layout]]
- [[runtime]]
