---
type: entity
category: compiler
tags: [debugging, lldb, sil-dump, diagnostics]
aliases: [컴파일러 디버깅]
sources: [debugging-the-compiler.md]
---

# 컴파일러 디버깅 가이드

Swift 컴파일러와 중간 표현을 디버깅하는 기법 모음. 원본: `swift/docs/DebuggingTheCompiler.md`

## IR 덤프 명령

| 단계 | 명령어 |
|------|--------|
| Parser (AST) | `swiftc -dump-ast -O file.swift` |
| SILGen (raw SIL) | `swiftc -emit-silgen -O file.swift` |
| Mandatory passes | `swiftc -emit-sil -Onone file.swift` |
| 최적화 후 SIL | `swiftc -emit-sil -O file.swift` |
| LLVM IR | `swiftc -emit-ir -O file.swift` |
| 어셈블리 | `swiftc -emit-assembly -O file.swift` |

## SIL 디버깅

- `-Xllvm -sil-print-all`: 모든 패스 후 SIL 출력
- `-Xllvm -sil-print-only-function=<name>`: 특정 함수만 출력
- `-Xllvm -sil-print-before=<pass>`: 특정 패스 전 SIL 출력
- `-Xllvm -sil-print-after=<pass>`: 특정 패스 후 SIL 출력

## LLDB 디버깅

- `expr $0.dump()` — SIL 노드 덤프
- `expr $0.print(llvm::errs())` — 출력
- `breakpoint set -n swift::SILFunction::dump` — SIL 함수 덤프에 브레이크포인트

## 유용한 도구

- `split-cmdline` (`utils/dev-scripts/`) — 긴 명령줄 분할
- `ViewCFG` — Regex 기반 CFG 시각화
- `bug_reducer` — SIL 테스트 케이스 축소

## SIL 옵티마이저 디버깅

- `-Xllvm -sil-opt-pass-count=<N>`: N번째 패스까지만 실행 (bisect 가능)
- 패스 카운트 bisect으로 버그 유발 패스 식별

관련 페이지: [[swift-compiler-build-test-debug-stack]], [[lldb-and-swift-debugging]], [[llvm-backend]], [[sil-reference]], [[optimizer-design]], [[overview]]
