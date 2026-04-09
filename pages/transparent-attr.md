---
type: concept
category: sil
tags: [transparent, attributes, inlining]
aliases: [투명 속성, @_transparent, transparent]
sources: [transparent-attr.md]
---

# @_transparent 속성

`@_transparent`는 "이 연산을 프리미티브 연산처럼 취급하라"는 의미로, 컴파일러와 컴파일된 프로그램 모두가 구현을 "투과"하여 본다. 데이터플로우 진단 이전에 반드시 인라이닝되어야 하며, `-Onone`에서도 적용된다.

## 핵심 특성

- 데이터플로우 관련 진단 전에 **반드시** 인라이닝 (에러 포착에 필요)
- 암시적으로 inlinable: 구현 변경이 기존 바이너리에 영향 없음
- public 또는 `@usableFromInline`일 때 공개 심볼만 참조 가능
- 디버그 시 single-stepping에서 건너뜀

## 사용 판단 기준

`@_transparent`는 매우 제한적으로 사용해야 한다. 구현이 변경될 수 있거나, private 함수를 호출하거나, `-Onone`에서의 인라이닝이 문제가 된다면 `@inlinable` + `@inline(__always)`를 사용해야 한다.

관련 페이지: [[sil-function-attributes]], [[optimizer-design]]
