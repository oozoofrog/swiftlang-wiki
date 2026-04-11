---
type: entity
category: compiler
tags: [clang-importer, c-interop, name-translation]
aliases: [C-Swift 이름 변환, C to Swift Name Translation]
sources: [c-to-swift-name-translation.md, c-to-swift-omit-needless-words.md]
---

# C에서 Swift로의 이름 변환

Clang Importer가 C/ObjC 선언을 Swift로 임포트할 때 이름을 변환하는 규칙을 설명한다. 단어 경계 분리, 열거형 접두사 제거, 메서드 이름 변환 등이 적용되며, Cocoa 명명 규칙을 Swift API 디자인 가이드라인에 맞게 바꾸는 것이 목적이다.

## 핵심 개념

- **단어 경계 분리**: 대소문자 전환, 밑줄, 숫자 등으로 식별자를 단어로 분리 (예: `XMLReader` -> `XML Reader`)
- **열거형 임포트**: 속성에 따라 `@objc` enum, OptionSet, 에러 구조체 등으로 변환. 케이스명은 공통 접두사를 제거하고 소문자화
- **ObjC 메서드**: `init` 패밀리는 이니셜라이저로, 팩토리 메서드는 `convenience init`으로 변환
- **불필요한 단어 생략**: 반환/매개변수/컨텍스트 타입을 기반으로 중복 타입명을 자동 제거하는 휴리스틱
- **CF 타입**: `objc_bridge` 속성으로 인식, Swift 클래스로 임포트 시 `Ref` 접미사 제거
- **swift_wrapper**: typedef를 RawRepresentable 구조체로 임포트

---

관련 페이지: [[proposal-option-sets-to-importer-and-layout]], [[proposal-c-export-and-bridging-to-importer]], [[clang-importer]], [[objc-interop]], [[overview]], [[glossary-compiler]]
