---
type: entity
category: compiler
tags: [modules, import, compilation-unit]
aliases: [모듈, Modules, import]
sources: [modules.md]
---

# Swift 모듈 시스템

Swift에서 모듈은 코드 공유의 기본 단위로 타입/함수/전역 변수 선언을 제공한다. `import`로 모듈을 가져오며 선택적 임포트도 가능하다.

## "모듈"의 6가지 의미

1. **선언 컨테이너**: 타입, 함수, 전역 변수를 담는 단위
2. **네임스페이스**: `Chess.Board`처럼 qualified name으로 선언 구분
3. **컴파일 단위**: 여러 소스 파일이 하나의 모듈을 구성
4. **코드 포함**: 함수 구현을 포함하여 인라이닝 최적화 가능
5. **re-export 메커니즘**: `@exported import`로 다른 모듈을 재노출
6. **Clang 모듈 연동**: C/Objective-C 헤더를 Swift 타입으로 노출

## 핵심 개념

- 모듈 이름은 전역 유일, mangled name에 포함되므로 변경은 ABI 파괴적
- 동일 모듈 내 소스 파일 선언은 암시적 상호 가시
- 이름 충돌 시 현재 파일 > 같은 모듈 > selective > non-selective import 우선순위

관련 페이지: [[serialization]], [[keyword-network]], [[overview]], [[glossary-compiler]], [[access-control]], [[how-swift-imports-c-apis]], [[compiler-driver]], [[library-evolution]]
