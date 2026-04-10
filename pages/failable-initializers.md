---
type: concept
category: compiler
tags: [initializers, failable, optional]
aliases: [실패 가능한 이니셜라이저, Failable Initializers, init?]
sources: [failable-initializers.md]
---

# 실패 가능한 이니셜라이저 (init?)

실패 가능한 이니셜라이저는 초기화 중 오류 발생 시 nil을 반환하거나 에러를 throw할 수 있다. 편의 이니셜라이저의 실패는 단순하지만, 지정 이니셜라이저의 실패는 부분 초기화된 객체의 정리가 핵심 과제이다.

## 지정 이니셜라이저 실패 시나리오

`super.init()` 위임 **이후** 실패: 완전 초기화된 self를 release (deinit 실행됨)
`super.init()` 위임 **이전** 실패: 부분 초기화된 stored property만 정리 (deinit 미실행)

## 해결 방법

- **Pure Swift**: `partialDeinit` vtable 진입점으로 초기화된 프로퍼티만 역순 정리
- **Objective-C**: 숨겨진 비트 플래그로 슬라이스 초기화 추적, `-release`로 해제

DI(Definite Initialization) 패스가 추적을 담당, struct는 완전 지원됨.

관련 페이지: [[proposal-initialization-and-accessors-to-property-model]], [[proposal-initializer-inheritance-to-modern-init-model]], [[proposal-constructors-and-class-construction-to-init-model]], [[sil-initializer-conventions]], [[keyword-network]], [[type-checker]], [[diagnostics]], [[sil-function-conventions]], [[dynamic-casting]], [[overview]]
