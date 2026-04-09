---
type: entity
category: compiler
tags: [objc, interop, clang-importer, bridging]
aliases: [ObjC 상호운용, Objective-C Interop]
sources: [objc-interop.md]
---

# Objective-C 상호운용

Swift가 Objective-C 코드 및 런타임과 상호운용하는 방식을 설명한다. 모든 Swift 클래스는 ObjC 클래스이기도 하며, 이 상호작용은 ObjC interop을 지원하는 플랫폼에서만 적용된다.

## 핵심 개념

- **메시징**: `objc_msgSend`를 통해 ObjC 메시지를 전송. `@objc` 메서드는 ObjC 메서드 목록에 노출
- **클래스 상속**: ObjC 클래스를 상속하면 동일한 ObjC 클래스 구조가 생성. 순수 Swift 클래스는 내부 `SwiftObject`를 상속
- **컴파일러 생성 클래스**: 바이너리 정적 데이터로 배치, ObjC 구조 뒤에 Swift 전용 필드 추가
- **동적 생성 클래스**: 제네릭 클래스 등은 런타임에 `MetadataAllocator`로 할당 후 `objc_readClassPair`로 등록
- **스텁 클래스**: macOS 10.15+/iOS 13+에서 지원. 크기를 미리 알 수 없는 동적 클래스를 위한 구조
- **브리징 헤더**: ObjC API를 Swift에서 사용 가능하게 하는 진입점
- **셀렉터 디스패치**: `@objc` 속성을 통한 메서드 호출 메커니즘

---

관련 페이지: [[overview]], [[runtime]], [[glossary-compiler]], [[c-to-swift-name-translation]]
