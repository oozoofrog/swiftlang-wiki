---
type: reference
category: meta
tags: [wiki, taxonomy, frontmatter, metadata, editorial]
aliases: [위키 taxonomy, 위키 frontmatter taxonomy, 위키 분류 체계, frontmatter 규칙]
sources: [wiki-knowledge-base-principles.md, wiki-editor-checklist.md, wiki-page-templates.md]
---

# 위키 taxonomy / frontmatter 규칙

이 문서는 Swiftlang wiki에서
`type`, `category`, `tags`, `aliases`, `sources`를 어떤 기준으로 고르는지 정하는 메타 문서다.

원칙 문서가 "왜"를,
체크리스트가 "무엇을 확인할지"를,
템플릿이 "어떻게 시작할지"를 다룬다면,
이 문서는 "어떤 frontmatter 값을 넣을지"를 정한다.

기준 문서:
- [[wiki-knowledge-base-principles]]
- [[wiki-editor-checklist]]
- [[wiki-page-templates]]

## 1. frontmatter 각 필드가 답하는 질문

| 필드 | 질문 | 역할 |
|------|------|------|
| `type` | 이 페이지는 어떤 역할을 하는가? | 허브인지, 개념 설명인지, 구체 대상 설명인지, 참고/교차 읽기인지 구분 |
| `category` | 이 페이지는 어느 지식 영역에 속하는가? | compiler, sil, learning, official-docs 같은 도메인 분류 |
| `tags` | 어떤 키워드로 찾아야 하는가? | 검색, 그래프 탐색, 연관 페이지 발견에 쓰는 짧은 라벨 |
| `aliases` | 독자가 어떤 이름으로 들어올 수 있는가? | 한글/영문 이름, 약칭, 자주 쓰는 표현 |
| `sources` | 무엇을 근거로 썼는가? | 원문 문서, 관련 페이지, 소스 파일 경로 |

핵심 구분:
- `type`은 페이지의 형식/역할이다
- `category`는 페이지가 다루는 주제 영역이다
- `tags`는 탐색용 키워드다

즉 같은 `reference` 페이지라도
`official-docs`, `learning`, `meta` 중 어느 `category`에 들어갈지는 달라질 수 있다.

## 2. frontmatter를 고르는 순서

새 페이지를 만들 때는 아래 순서로 고른다.

1. 이 페이지의 역할을 정한다 → `type`
2. 이 페이지가 속한 주제 영역을 정한다 → `category`
3. 검색/탐색 키워드를 고른다 → `tags`
4. 독자가 들어올 별칭을 정한다 → `aliases`
5. 근거 문서를 적는다 → `sources`

순서를 거꾸로 잡으면
태그는 그럴듯한데 페이지 역할이 흐릿해지는 경우가 많다.

## 3. `type` 선택 규칙

현재 public wiki에서 새 페이지에 권장하는 `type`은 아래 네 가지다.

| type | 언제 쓰는가 | 대표 예 |
|------|-------------|---------|
| `summary` | 큰 그림 허브, 상위 지도, 학습 루트 | [[swift-ecosystem-map]], [[swift-compiler-learning-stack]] |
| `concept` | 추상 개념, 의미 규칙, 시맨틱 모델 | [[abi-stability]], [[sil-ownership]] |
| `entity` | 구체 구성요소, 도구, 문서, 서브시스템 | [[type-checker]], [[runtime]], [[swift-syntax-package]] |
| `reference` | 교차 읽기, 공식 문서 해설, 메타 문서, 참고형 페이지 | [[proposal-value-semantics-and-cow-to-ownership]], [[wiki-editor-checklist]] |

빠른 판정 기준:
- 큰 그림을 묶고 읽기 경로를 설계한다 → `summary`
- 추상 규칙/개념을 설명한다 → `concept`
- 이름이 붙은 구성요소/도구/문서를 설명한다 → `entity`
- 비교, 교차 읽기, 가이드, 메타, 참고 문서다 → `reference`

보조 규칙:
- meta page는 보통 `type: reference` + `category: meta`를 쓴다
- crosswalk page는 거의 항상 `type: reference` + `category: learning`이다
- 공식 문서 해설 페이지는 대체로 `type: reference` + `category: official-docs`다
- glossary 성격의 새 페이지는 `type: reference`에 `glossary` 태그를 붙이는 쪽을 우선한다

### 헷갈릴 때

#### `concept` vs `entity`
- 개념/규칙/성질이 주인공이면 `concept`
- 특정 시스템/도구/파일/문서/모듈이 주인공이면 `entity`

예:
- ownership 자체 설명 → `concept`
- TypeChecker 설명 → `entity`

#### `summary` vs `reference`
- 상위 구조와 읽기 경로를 설계하면 `summary`
- 비교/참고/교차 해설이 중심이면 `reference`

예:
- [[swift-type-system]] → `summary`
- proposal → implementation 교차 읽기 → `reference`

## 4. `category` 선택 규칙

`category`는 페이지 형식이 아니라
주제 영역을 나타낸다.

즉 허브라고 해서 무조건 `learning`은 아니고,
공식 문서 해설이라고 해서 무조건 `documentation`도 아니다.

현재 새 페이지에 권장하는 주된 `category`는 아래와 같다.

| category | 언제 쓰는가 | 대표 예 |
|----------|-------------|---------|
| `learning` | 학습 허브, 읽기 경로, crosswalk, 큰 그림 입구 | [[swift-compiler-7-day-course]], [[proposal-declaration-type-checker-to-sema]] |
| `compiler` | 컴파일러 코어, Sema, AST, request, runtime 인접 내부 구조 | [[type-checker]], [[runtime]], [[request-evaluator]] |
| `sil` | SIL IR, SILGen, ownership, optimizer, pass 구조 | [[sil-reference]], [[sil-optimizer-pass-catalog]] |
| `official-docs` | 공식/준공식 문서 해설, 다운로드 문서 대응 페이지 | [[official-docs/swift-intermediate-language]], [[official-docs/abi-stability-manifesto]] |
| `tooling` | 툴체인, 빌드/디버그 인프라, importer, LLVM/LLDB/도구 축 | [[swift-toolchain-stack]], [[clang-importer]], [[lit-and-filecheck]] |
| `packages` | Swift 하위 패키지/서브프로젝트/패키지 생태계 | [[swift-package-manager]], [[swift-driver-package]] |
| `stdlib` | 표준 라이브러리와 그 인접 주제 | [[stdlib-programmers-manual]] |
| `documentation` | 기여/설정/가이드/FAQ 등 운영성 문서 | [[getting-started]], [[testing-guide]] |
| `meta` | 위키 운영 원칙, 연대기, 체크리스트, 템플릿 | [[wiki-knowledge-base-principles]], [[wiki-page-templates]] |
| `testing` | 테스트 프레임워크 자체가 주제일 때 | [[swift-testing-package]] |

보조 규칙:
- `category`는 "이 페이지가 무엇을 다루는가"에 답해야 한다
- `category`는 "이 페이지가 긴가 짧은가", "허브인가 아닌가"를 표현하지 않는다
- `meta`는 위키 자체를 다룰 때만 쓴다. Swift 주제 허브에는 쓰지 않는다
- 예전의 `tools` 표기는 새 페이지에서 쓰지 않고 `tooling`으로 통일한다

### 자주 헷갈리는 구분

#### `learning` vs `meta`
- Swift 주제를 배우기 위한 길잡이/교차 읽기면 `learning`
- 위키 자체의 운영 규칙/편집 규칙이면 `meta`

#### `documentation` vs `official-docs`
- 원문 공식 문서 해설/대응 페이지면 `official-docs`
- 기여 가이드, 팁, FAQ, 실무 안내면 `documentation`

#### `tooling` vs `packages`
- 툴체인/도구/빌드/디버그 인프라를 설명하면 `tooling`
- 특정 패키지/서브프로젝트 자체를 설명하면 `packages`

## 5. `tags` 선택 규칙

`tags`는 분류 체계라기보다
검색과 연결을 위한 탐색용 키워드다.

권장 규칙:
- 보통 3~8개 정도로 유지한다
- 소문자 위주로 쓴다
- 가능하면 짧고 재사용 가능한 단어를 쓴다
- 제목을 그대로 반복하기보다, 독자가 찾을 키워드를 고른다
- 너무 비슷한 동의어를 여러 개 늘어놓지 않는다

좋은 태그 조합 예:
- 허브 페이지: `[swift, ownership, concurrency, learning]`
- 개념 페이지: `[abi, runtime, resilience]`
- 공식 문서 해설: `[official-docs, generics, manifesto]`
- 메타 페이지: `[wiki, taxonomy, frontmatter, editorial]`

피해야 할 것:
- 문장처럼 긴 태그
- 거의 같은 의미의 중복 태그 나열
- 제목 복붙만 한 태그 구성
- 페이지 역할을 전부 태그로만 때우는 방식

즉 `tags`는
`type`과 `category`를 대체하는 게 아니라,
그 위에 검색성을 얹는 층이다.

## 6. `aliases` 선택 규칙

`aliases`는 실제 진입 단어를 적는다.

권장 규칙:
- 한글 이름과 영문 이름이 모두 자연스러우면 둘 다 넣는다
- 약칭/약어가 실제로 널리 쓰이면 넣는다
- 대소문자만 다른 중복 별칭은 줄인다
- 거의 같은 표현을 6~7개씩 과하게 넣지 않는다

좋은 예:
- `aliases: [위키 편집 체크리스트, 편집 체크리스트, wiki checklist]`
- `aliases: [Clang Importer, Clang 임포터, Swift의 Clang Importer]`

## 7. `sources` 선택 규칙

`sources`는 이 페이지가 어디서 왔는지를 남기는 최소한의 근거 필드다.

권장 규칙:
- 직접 읽은 원문 문서/파일을 적는다
- 메타/허브/교차 읽기 페이지라면 기준이 되는 관련 페이지나 원문 묶음을 적는다
- 막연한 설명보다 파일명/문서명을 적는다

예:
- 원문 해설 페이지 → `sources: [swiftlang-swift/docs/TypeChecker.md]`
- 메타 페이지 → `sources: [wiki-knowledge-base-principles.md, wiki-editor-checklist.md]`
- 교차 읽기 페이지 → proposal 문서와 현재 구현 기준 페이지를 함께 적는다

## 8. page kind별 빠른 추천 조합

| page kind | 추천 type | 추천 category | 메모 |
|-----------|-----------|----------------|------|
| 상위 허브 / 지도 | `summary` | `learning` 또는 해당 도메인 | 읽기 경로가 있으면 더 좋다 |
| 컴파일러 코어 구성요소 | `entity` | `compiler` | TypeChecker, RequestEvaluator 같은 named subsystem |
| 추상 의미/규칙 설명 | `concept` | `compiler`, `sil`, `stdlib` 중 하나 | ownership, ABI stability 같은 주제 |
| 공식 문서 해설 | `reference` | `official-docs` | 원문과 위키 해설의 브리지 |
| proposal → implementation 교차 읽기 | `reference` | `learning` | crosswalk 성격이 핵심 |
| 패키지/서브프로젝트 소개 | `entity` | `packages` | swift-driver, SwiftPM 등 |
| 툴체인/디버그/빌드 도구 | `entity` 또는 `reference` | `tooling` | 도구 자체냐 참고형 가이드냐에 따라 갈린다 |
| 위키 운영 문서 | `reference` | `meta` | 원칙, 체크리스트, 템플릿, taxonomy |

## 9. legacy / 예외 처리

현재 위키에는 역사적으로 남은 예외가 조금 있다.
새 페이지를 만들 때는 그 예외를 그대로 복사하지 않는 쪽이 좋다.

현재 주의할 점:
- 일부 오래된 문서는 예전 `type`/`category` 습관이 남아 있을 수 있다
- 과거에는 landing page나 glossary page에 축약/별도 frontmatter 관성이 있었지만, 수정 시점에 canonical 값으로 흡수하는 쪽을 우선한다

원칙은 단순하다.
새 문서이거나 손보는 문서일수록
예외를 늘리기보다
기존 축으로 흡수하는 편이 낫다.

## 10. 자주 나는 실수

### 1. `type`과 `category`를 같은 것으로 취급함
증상:
- 허브 페이지라서 `category: learning`만 보고 `type`도 대충 고름
- meta 문서라서 그냥 `type: meta` 같은 식으로 적고 싶어짐

대응:
- `type`은 형식
- `category`는 주제 영역
으로 분리해서 생각한다

### 2. 태그에 모든 걸 몰아넣음
증상:
- `type`/`category`는 애매하게 두고 태그만 잔뜩 붙임

대응:
- 역할은 `type`
- 주제는 `category`
- 검색성은 `tags`
순서로 정한다

### 3. meta 문서가 아닌데 `category: meta`를 붙임
증상:
- 상위 허브라서 meta처럼 보인다는 이유로 `meta`를 붙임

대응:
- 위키 자체를 다룰 때만 `meta`
- Swift 지식 허브는 보통 `learning` 또는 해당 도메인 category

### 4. aliases를 번역 목록처럼 과하게 늘림
증상:
- 거의 같은 표현을 많이 넣음

대응:
- 실제로 독자가 검색할 진입 표현만 남긴다

## 11. 추천 작업 순서

실전에서는 이 순서가 가장 덜 꼬인다.

1. [[wiki-page-templates]]에서 페이지 틀을 고른다
2. 이 문서에서 `type/category/tags`를 결정한다
3. [[wiki-editor-checklist]]로 연결/검증 항목을 확인한다
4. build/doctor/tests/status까지 끝낸다

## 같이 보면 좋은 페이지

- [[wiki-knowledge-base-principles]]
- [[wiki-editor-checklist]]
- [[wiki-page-templates]]
- [[wiki-knowledge-chronicle]]
- [[index]]
