---
type: glossary
category: compiler
tags: [glossary, terminology, lexicon]
aliases: [용어 사전, Lexicon]
sources: [lexicon.md]
---

# 컴파일러 용어 사전

Swift 컴파일러 및 표준 라이브러리 소스 코드에서 사용되는 핵심 용어 정의.
원본: `swift/docs/Lexicon.md`

정의만 빠르게 보고 싶다면 이 페이지를,
용어가 서로 어떻게 엮이는지 보고 싶다면 [[keyword-network]]를 같이 보면 좋다.

## 빠른 묶음 이동

- 타입 체커/진단: [[type-checker]], [[diagnostics]]
- 제네릭/프로토콜: [[generic-signatures]], [[archetypes]], [[substitution-maps]], [[conformances]]
- SIL/소유권/최적화: [[sil-reference]], [[sil-ownership]], [[optimizer-design]], [[sil-optimizer-pass-catalog]]
- 동시성/격리: [[concurrency-data-race-safety]]
- ABI/런타임: [[abi-stability]], [[abi-type-metadata]], [[runtime]], [[library-evolution]]
- 전체 키워드 허브: [[keyword-network]]

## 타입 시스템

| 용어 | 정의 |
|------|------|
| **[[archetypes|archetype]]** | 제네릭 컨텍스트 내 제네릭 파라미터/연관 타입의 플레이스홀더. "rigid type variable" |
| **[[type-checker|canonical type]]** | sugar가 제거된 타입. 포인터 동등 비교로 타입 동치 판단 가능 |
| **[[type-checker|sugared type]]** | 편의 구문으로 작성된 타입 (예: `Int?` = `Optional<Int>`) |
| **[[generic-signatures|reduced type]]** | 제네릭 시그니처 기준으로 더 단순화된 canonical type |
| **[[dynamic-casting|existential type]]** | 프로토콜 합성 타입 (`Any` = zero protocol) |
| **[[generic-signatures|interface type]]** | 제네릭 컨텍스트 밖의 타입. generic signature과 함께 해석 |
| **[[type-checker|contextual type]]** | (1) 컨텍스트 기반 기대 타입 (2) archetype 포함, type parameter 미포함 타입 |
| **[[abi-type-metadata|metatype]]** | 타입을 나타내는 값의 타입. ObjC metaclass의 일반화 |
| **[[generic-signatures|type parameter]]** | generic parameter type 또는 dependent member type |

## SIL 관련

| 용어 | 정의 |
|------|------|
| **[[sil-reference|SIL]]** | Swift Intermediate Language. 고수준 IR, 흐름 감지 진단/최적화/IRGen에 사용 |
| **[[sil-reference|raw SIL]]** | SILGen 직후의 SIL. 데이터플로 요구사항 미검증 상태 |
| **[[sil-reference|canonical SIL]]** | mandatory pass 이후의 SIL. IRGen 입력으로 사용 가능 |
| **[[sil-ownership|OSSA]]** | Ownership SSA. 소유권 불변식을 강제하는 SIL 확장 형식 |
| **[[sil-optimizer-pass-catalog|mandatory passes]]** | SILGen 직후 실행되는 필수 변환. raw SIL → canonical SIL |
| **[[conformances|witness table]]** | conformance의 SIL/런타임 표현. 프로토콜용 vtable |
| **[[abi-type-metadata|VWT]]** | Value Witness Table. 미지 값에 대한 assign/copy/destroy 등 기본 연산 기술 |
| **[[runtime|vtable]]** | 클래스의 오버라이드 가능 메서드 구현 매핑 |

## 컴파일러 일반

| 용어 | 정의 |
|------|------|
| **[[type-checker|Sema]]** | Semantic Analysis. 타입 검사, 검증, 표현식 재작성 패스 |
| **[[how-swift-imports-c-apis|Clang importer]]** | C/ObjC 선언을 Swift에 노출하는 컴파일러 구성 요소 |
| **[[abi-calling-convention|abstraction pattern]]** | 속성/함수 파라미터의 비치환 제네릭 타입. 메모리 표현 제약 결정 |
| **[[abi-calling-convention|reabstraction]]** | abstraction pattern이 다른 값 사용 시 발생하는 암시적 표현 변환 |
| **[[objc-interop|thunk]]** | 호출 규약 조정을 위해 합성되는 함수 (예: ObjC→Swift 브릿지) |
| **[[failable-initializers|DI]]** | Definite Initialization. 초기화되지 않은 변수 읽기 방지 분석 |
| **[[compiler-driver|WMO]]** | Whole-Module Optimization. 모듈 전체를 단일 프로세스에서 컴파일 |
| **[[library-evolution|fragile]]** | 변경 시 바이너리 호환성이 깨지는 타입/함수 |
| **[[library-evolution|resilient]]** | 특정 변경에도 바이너리 호환성이 유지되는 타입/함수 |

## 프로젝트 용어

| 용어 | 정의 |
|------|------|
| **NFC** | No Functionality Change. 동작 변경 없는 커밋 |
| **QoI** | Quality of Implementation. 최소 기대를 넘는 구현 품질 |
| **gardening** | 비실행 코드(문서, README)의 오타/문법 수정 기여 |
| **DNM** | Do Not Merge. 논의/분석 진행 중인 PR 표시 |
| **[[modules|module]]** | (1) API 배포 단위 (2) 컴파일 단위 (3) SIL 모듈 (4) LLVM 모듈 (5) swiftmodule 파일 (6) Clang 모듈 |

## 관련 페이지

- [[keyword-network]]
- [[overview]]
- [[sil-reference]]
- [[type-checker]]
- [[abi-mangling]]
- [[abi-type-metadata]]
- [[runtime]]
- [[dynamic-casting]]
