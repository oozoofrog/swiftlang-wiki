---
type: entity
category: compiler
tags: [performance, profiling, compilation-time]
aliases: [컴파일러 성능, Compiler Performance]
sources: [compiler-performance.md]
---

# 컴파일러 성능 측정

Swift 컴파일러 성능 분석 방법. 원본: `swift/docs/CompilerPerformance.md`

## 측정 차원

- **Wall clock time**: 전체 컴파일 시간
- **Frontend time**: 파싱 + 타입 검사 + SILGen
- **SIL optimization time**: 최적화 패스 시간
- **LLVM time**: IR 최적화 + 코드 생성
- **Memory usage**: 피크 메모리 사용량

## 주요 도구

- `-Xfrontend -debug-time-compilation`: 컴파일 단계별 시간
- `-Xfrontend -debug-time-function-bodies`: 함수별 타입 검사 시간
- `-Xfrontend -debug-time-expression-type-checking`: 표현식별 타입 검사 시간
- `-stats-output-dir`: 통계를 JSON으로 출력
- **compilation-timer**: 프론트엔드/백엔드 시간 분리

## 일반적 병목

1. **타입 검사 폭발**: 복잡한 표현식/오버로드 해소
2. **제네릭 특수화**: 많은 제네릭 인스턴스화
3. **모듈 크기**: 큰 swiftmodule 역직렬화

관련 페이지: [[type-checker]], [[keyword-network]], [[optimizer-design]], [[debugging-the-compiler]], [[compiler-driver]], [[dependency-analysis]], [[official-docs/compiler-performance-reference]]
