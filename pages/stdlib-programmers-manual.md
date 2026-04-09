---
type: entity
category: stdlib
tags: [stdlib, guide, conventions]
aliases: [표준 라이브러리 프로그래머 매뉴얼, Standard Library Programmers Manual]
sources: [stdlib-programmers-manual.md]
---

# 표준 라이브러리 프로그래머 매뉴얼

stdlib 기여자를 위한 가이드로, 코딩 규칙, 내부 어노테이션, 성능 패턴, resilience 작업 방법을 다룬다. `stdlib/public/core`, Darwin/Windows 오버레이, `stdlib/private`를 포괄한다.

## 코딩 규칙

- **80자 줄 제한** 엄격 적용, 들여쓰기는 2칸 스페이스
- 긴 인자 목록은 줄바꿈 시 항목별 개별 줄 배치 (한 줄에 여러 항목 금지)
- 접근 수준은 항상 명시(`internal` 포함), extension이 아닌 개별 멤버에 표기
- Leading Underscore Rule: 공식 공개 API가 아닌 모든 심볼에 밑줄 포함 필수

## 내부 도구

- `_fastPath`/`_slowPath`: 분기 확률 힌트 (LLVM branch weight)
- `_precondition`/`_debugPrecondition`/`_internalInvariant`: 3단계 assertion
- `@_transparent`: 진단 전 인라이닝 강제, CRISP 패턴 등

관련 페이지: [[overview]], [[compiler-performance]]
