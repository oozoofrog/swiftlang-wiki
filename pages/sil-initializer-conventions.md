---
type: entity
category: sil
tags: [sil, initializer, conventions]
aliases: [SIL 초기화 규약]
sources: [sil-initializer-conventions.md]
---

# SIL 초기화 규약

SIL에서 이니셜라이저의 표현 규약. 원본: `swift/docs/SIL/SILInitializerConventions.md`

## 구조체/열거형 이니셜라이저

- `self`는 `@out` 간접 결과로 전달
- 이니셜라이저 내부에서 `self`의 각 stored property를 초기화

## 클래스 이니셜라이저

- Designated initializer: 전체 초기화 책임
- Convenience initializer: `self.init(...)` 위임

## 실패 가능 이니셜라이저

- `init?` → Optional 결과 반환
- 실패 시 이미 초기화된 stored property를 소멸 후 `nil` 반환

관련 페이지: [[proposal-initialization-and-accessors-to-property-model]], [[proposal-initializer-inheritance-to-modern-init-model]], [[proposal-constructors-and-class-construction-to-init-model]], [[sil-reference]], [[keyword-network]], [[sil-function-conventions]], [[failable-initializers]], [[sil-memory-access]], [[sil-ownership]]
