---
type: entity
category: compiler
tags: [serialization, swiftmodule, bitcode, binary-format]
aliases: [직렬화, Serialization, swiftmodule]
sources: [serialization.md]
---

# 바이너리 직렬화 형식

Swift 모듈의 바이너리 직렬화 형식. 원본: `swift/docs/Serialization.md`

## 용도

1. **swiftmodule 파일**: 모듈의 공개 인터페이스
2. **SIB** (Swift Intermediate Binary): Sema/SILGen 이후 상태 캡처
3. **디버그 정보**: 타입 고수준 인트로스펙션
4. **비공개 API 디버그**: 인터랙티브 디버깅용

## LLVM Bitstream 형식

LLVM IR용으로 설계된 바이너리 컨테이너를 재활용:

- **Block**: 파일 영역, 길이가 시작에 기록되어 빠른 스킵 가능
- **Record**: 최대 64비트 데이터 필드
- 블록 내 특정 오프셋으로 점프 가능
- 형식 변경이 즉시 기존 파일을 무효화하지 않음

## 버전 관리

| 변경 유형 | major | minor |
|-----------|-------|-------|
| 하위 호환 변경 | 유지 | 유지 |
| 이전 컴파일러 로드 불가 | 유지 | 증가 |
| 이후 컴파일러 로드 불가 | 증가 | (리셋) |

현재: major=0, minor가 항상 증가 (모든 변경이 호환성 파괴).

## 파일 위치

- `swift/lib/Serialization/` — 직렬화 구현

관련 페이지: [[overview]], [[keyword-network]], [[modules]], [[abi-stability]], [[library-evolution]], [[runtime]], [[compiler-driver]]
