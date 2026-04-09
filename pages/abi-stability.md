---
type: concept
category: compiler
tags: [abi, stability, library-evolution, binary-compatibility]
aliases: [ABI 안정성, ABI Stability]
sources: [abi-stability-manifesto.md]
---

# ABI 안정성

Swift ABI 안정성의 목표와 설계. 원본: `swift/docs/ABIStabilityManifesto.md`

## ABI 안정성이란

서로 다른 Swift 컴파일러 버전으로 빌드된 바이너리가 상호 운용 가능하도록 하는 것. Swift 5.0에서 달성.

## 핵심 요소

1. **타입 레이아웃**: struct, class, enum의 메모리 배치 ([[abi-type-layout]])
2. **타입 메타데이터**: 런타임 타입 정보 구조 ([[abi-type-metadata]])
3. **심볼 맹글링**: ABI-public 선언의 고유 심볼 생성 ([[abi-mangling]])
4. **호출 규약**: 함수 파라미터/결과 전달 방식 ([[abi-calling-convention]])
5. **Value Witness Table**: 값 타입 연산 vtable
6. **Protocol Witness Table**: conformance 런타임 표현

## Library Evolution

ABI 안정성 위에 구축된 기능. **resilient** 타입은 내부 구조를 변경해도 바이너리 호환성 유지:
- `@frozen`: 레이아웃 고정 선언 (최적화 가능)
- `@inlinable`: 인라이닝 허용
- 비-frozen struct에 stored property 추가 가능

## Fragile vs Resilient

| 특성 | Fragile | Resilient |
|------|---------|-----------|
| 레이아웃 | 컴파일 타임 결정 | 런타임 조회 |
| 필드 접근 | 직접 오프셋 | 간접 조회 |
| 성능 | 빠름 | 약간 느림 |
| 호환성 | 변경 시 깨짐 | 변경 가능 |

관련 페이지: [[abi-mangling]], [[abi-type-metadata]], [[abi-type-layout]], [[abi-calling-convention]], [[runtime]], [[serialization]]
