---
type: entity
category: compiler
tags: [clang-importer, c-apis, mapping]
aliases: [C API 임포트, How Swift Imports C APIs]
sources: [how-swift-imports-c-apis.md]
---

# Swift의 C API 임포트 방식

Swift가 C 기반 언어의 API를 모듈 임포트 또는 브리징 헤더를 통해 Swift API로 매핑하는 방식을 설명한다. 이는 Swift FFI의 기반으로, 기존 C 라이브러리와의 상호운용성을 제공한다.

## 핵심 개념

- **기본 타입 매핑**: C 타입은 Swift typealias로 매핑 (`int` -> `CInt`, `long` -> `CLong`, `double` -> `CDouble`)
- **함수 임포트**: C 함수는 인자 레이블 없는 Swift 함수로 임포트. `NS_SWIFT_NAME`으로 커스터마이즈 가능
- **포인터 변환**: `const T *` -> `UnsafePointer<T>`, `T *` -> `UnsafeMutablePointer<T>`. 널러빌리티에 따라 Optional 결정
- **구조체/유니온**: struct로 임포트. 유니온은 각 필드가 스토리지를 공유하는 계산 프로퍼티로 변환
- **열거형**: 속성에 따라 `@objc enum`, `OptionSet`, `RawRepresentable` struct 등으로 임포트
- **매크로**: 정수/부동소수점 리터럴 매크로만 Swift 상수로 변환. 복합 매크로는 미지원

---

관련 페이지: [[proposal-option-sets-to-importer-and-layout]], [[proposal-c-export-and-bridging-to-importer]], [[proposal-c-pointer-interop-to-unsafe-pointer-model]], [[clang-importer]], [[c-to-swift-name-translation]], [[objc-interop]], [[overview]]
