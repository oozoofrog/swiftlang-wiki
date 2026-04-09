---
type: entity
category: compiler
tags: [driver, compilation-model, build-system, incremental]
aliases: [컴파일러 드라이버, Swift Driver]
sources: [driver.md]
---

# Swift 컴파일러 드라이버

Swift 컴파일 모델과 드라이버 동작. 원본: `swift/docs/Driver.md`

## 핵심 개념

- **모듈**: 하나의 API 배포 단위. 같은 모듈의 파일은 반드시 같은 컴파일 단위
- **드라이버**: `swift`/`swiftc` 실행 시 호출. 직접 컴파일하지 않고 다른 도구 조율
- **프론트엔드**: `swift -frontend`. 실제 컴파일 수행 (구현 세부사항, 인터페이스 불안정)

## 왜 "파일당 하나의 빌드 규칙"이 안 되는가

Swift에서 파일은 같은 모듈의 다른 파일의 선언을 암시적으로 볼 수 있다. 따라서 하나의 파일 컴파일에도 다른 모든 파일의 지식이 필요.

## 세 단계 서브프로세스

1. **Emit module**: 전체 소스 파일을 파싱하여 모듈 정보 생성
2. **Compile**: 각 소스 파일을 오브젝트 파일로 컴파일 (병렬 가능)
3. **Link**: 오브젝트 파일을 실행 파일/라이브러리로 링크

## 증분 빌드

드라이버가 [[dependency-analysis]] 정보를 활용하여 변경에 영향받는 파일만 재컴파일.

관련 페이지: [[dependency-analysis]], [[swift-driver-package]], [[overview]]
