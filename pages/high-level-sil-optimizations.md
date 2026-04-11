---
type: concept
category: sil
tags: [sil, optimizer, semantics, currency-types]
aliases: [고수준 SIL 최적화, High-Level SIL Optimizations, @_semantics]
sources: [high-level-sil-optimizations.rst]
---

# 고수준 SIL 최적화

표준 라이브러리 컨테이너에 `@_semantics` 속성을 부여하여 옵티마이저가 도메인 특화 최적화를 수행하는 메커니즘. 컨테이너가 Swift로 구현되어 전통적 최적화만으로는 한계가 있다.

## @_semantics 속성

`@_semantics("array.count")`처럼 태그를 부여하면 옵티마이저가 호출을 원자적 연산으로 취급. 초기 파이프라인에서 인라이닝 보류 후 고수준 최적화, 후기 단계에서 인라이닝하여 저수준 최적화 수행.

## 주요 태그

- **Array**: `array.init`, `array.get_element`, `array.check_subscript`, `array.make_mutable`, `array.mutate_unknown`
- **String**: `string.concat`, `string.makeUTF8`
- **Fixed Storage** (Span, InlineArray): `fixed_storage.get_count`, `fixed_storage.check_index`
- **@_effects**: `readnone`, `readonly`, `releasenone` 등 부작용 명세

관련 페이지: [[proposal-optimizer-effects-and-attributes-to-sil-optimizer]], [[proposal-in-place-operations-to-writeback-and-cow]], [[optimizer-design]], [[keyword-network]], [[sil-reference]], [[glossary-compiler]], [[standard-library-to-compiler-crosswalk]], [[sil-optimizer-pass-catalog]], [[transparent-attr]]
