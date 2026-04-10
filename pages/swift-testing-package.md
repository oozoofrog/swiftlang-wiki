---
type: entity
category: testing
tags: [swift-testing, test-framework, macros]
aliases: [Swift Testing]
sources: [swift-testing-readme.md]
---

# Swift Testing

Swift 언어의 현대적 테스트 프레임워크. 매크로 기반 API로 간결한 테스트 작성.

## 핵심 기능

- `@Test` 매크로: 테스트 함수 선언
- `#expect`: 조건 검증 (XCTAssert 대체)
- `@Suite`: 테스트 스위트 그룹화
- Parameterized testing: 입력 조합 자동 테스트
- Swift concurrency 네이티브 지원

## XCTest와의 차이

| 특성 | XCTest | Swift Testing |
|------|--------|---------------|
| API 스타일 | 클래스 기반 | 매크로 기반 |
| 검증 | `XCTAssert*` | `#expect`, `#require` |
| 파라미터화 | 수동 | 내장 |
| 병렬 실행 | 제한적 | async 네이티브 |

### 디렉토리

`swift-testing/`

관련 페이지: [[overview]], [[keyword-network]], [[swift-syntax-package]], [[testing-guide]], [[core-libraries-to-compiler-crosswalk]], [[concurrency-data-race-safety]], [[sourcekit-lsp]]
