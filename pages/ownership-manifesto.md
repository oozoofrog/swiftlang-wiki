---
type: concept
category: compiler
tags: [ownership, borrowing, move-semantics, manifesto]
aliases: [소유권 매니페스토, Ownership Manifesto]
sources: [ownership-manifesto.md]
---

# 소유권 매니페스토

Swift 소유권 시스템의 비전과 설계. 원본: `swift/docs/OwnershipManifesto.md`

## 문제

Copy-on-write 값 타입은 성공적이지만 한계 존재:
- 참조 카운팅/유일성 테스트 오버헤드
- 예측 불가능한 성능 (오디오 스트리밍 등)
- 값 "탈출"로 인한 필수 힙 할당
- 핫스팟이 암시적 복사일 때 개선 도구 부족

## 소유권이란

**소유권** = 값을 결국 소멸시킬 책임. Swift의 소유권 시스템은 opt-in 기능 집합:

- **Ownership transfer**: 값 이동 (`consuming`/`borrowing` 파라미터)
- **Borrowing**: 값을 소유하지 않고 읽기/수정 (`borrow`/`inout`)
- **Move-only types**: 복사 불가, 명시적 이동만 가능 (`~Copyable`)
- **Non-escaping closures**: 클로저가 호출 범위를 벗어나지 않음을 보장

## 설계 원칙

1. 기존 코드에 영향 없는 **opt-in** 기능
2. 소유권 시스템은 **기존 ARC 위에** 구축
3. Swift의 기존 값/참조 타입 모델과 **일관성** 유지
4. 성능이 중요한 코드에서 **예측 가능한 성능** 제공

## SIL에서의 표현

소유권 모델은 [[sil-ownership|OSSA]]로 SIL에 인코딩:
- `@owned`, `@guaranteed`, `@inout` 파라미터 규약
- `copy_value`, `destroy_value`, `move_value` 인스트럭션

관련 페이지: [[sil-ownership]], [[sil-function-conventions]], [[abi-stability]]
