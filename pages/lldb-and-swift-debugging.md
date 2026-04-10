---
type: reference
category: tooling
tags: [lldb, debugging, swift, compiler, expression-evaluator]
aliases: [LLDB와 Swift 디버깅, LLDB, Swift 디버깅]
sources: [debugging-the-compiler.md]
---

# LLDB와 Swift 디버깅

LLDB는 Swift 세계에서 두 얼굴을 가진다.
하나는 일반 Swift 프로그램을 디버깅하는 도구이고,
다른 하나는 Swift Compiler 자체와 그 산출물을 분석하는 핵심 도구다.

## LLDB가 중요한 이유

- 컴파일러를 브레이크포인트 기반으로 추적할 수 있다.
- AST / SIL / IR 관련 내부 객체를 직접 dump할 수 있다.
- Swift 실행 파일과 테스트 바이너리를 실제 런타임 상태에서 볼 수 있다.
- expression evaluation 문제를 통해 compiler + debugger 상호작용까지 볼 수 있다.

## 대표 사용 장면

### 1. 컴파일러 자체 디버깅
- 특정 Sema 함수 진입 확인
- SIL optimizer 패스 진입 전후 상태 관찰
- `dump()` / `print()` 메서드로 내부 객체 상태 확인

관련 페이지:
- [[debugging-the-compiler]]
- [[type-checker]]
- [[optimizer-design]]

### 2. Swift 프로그램 디버깅
- mangled / demangled symbol 확인
- symbolication과 stack/frame 분석
- runtime object / metadata 관련 문제 추적

관련 페이지:
- [[runtime]]
- [[abi-mangling]]
- [[official-docs/swift-repl-and-debugger]]

### 3. Swift expression evaluation 문제 분석
LLDB는 Swift expression evaluator와도 연결된다.
그래서 디버거 문제가 사실상 compiler bug로 이어지거나,
반대로 compiler 변화가 debugger 동작에 영향을 줄 수도 있다.

## 실무적으로 자주 보는 기능

- 브레이크포인트와 조건부 브레이크포인트
- `expr`, `print`, `frame variable`
- 내부 객체의 `dump()` / `print(llvm::errs())`
- mangled 이름 찾기와 수동 symbolication
- LLDB Python script / custom command

## Swift Compiler 관점에서 LLDB를 볼 때

LLDB는 “디버거 하나 더”가 아니라,
Swift 내부 자료구조를 가장 직접적으로 들여다보는 창에 가깝다.
특히 다음과 잘 맞물린다.

- [[debugging-the-compiler]] — 실제 플래그/기법 모음
- [[llvm-backend]] — LLVM 단계 관찰
- [[swift-compiler-build-test-debug-stack]] — 편집→빌드→테스트→디버그 루프 전체

## 흔한 학습 포인트

1. `swiftc -dump-*`류 출력과 LLDB 내부 객체 dump는 서로 보완적이다.
2. SIL/LLVM IR을 파일로 보는 것과 디버거 안에서 객체를 보는 것은 다르다.
3. LLDB 문제는 debugger 단독 문제라기보다 Swift frontend / runtime / expression evaluator 문제와 얽힐 수 있다.

## 추천 읽기 순서

1. [[debugging-the-compiler]]
2. [[official-docs/swift-repl-and-debugger]]
3. [[llvm-backend]]
4. [[runtime]]

## 같이 보면 좋은 페이지

- [[swift-toolchain-stack]]
- [[swift-compiler-build-test-debug-stack]]
- [[debugging-the-compiler]]
- [[official-docs/swift-repl-and-debugger]]
- [[llvm-backend]]
- [[runtime]]
