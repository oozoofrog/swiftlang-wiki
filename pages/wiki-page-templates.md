---
type: reference
category: meta
tags: [wiki, templates, editorial, page-creation]
aliases: [위키 생성 템플릿, 페이지 템플릿, wiki templates]
sources: [wiki-knowledge-base-principles.md, wiki-editor-checklist.md]
---

# 위키 생성 템플릿

이 문서는 Swiftlang wiki에서 반복해서 쓰는 페이지 틀을 모아 둔 공개 템플릿 문서다.
복사해서 시작하되,
기계적으로 채우기보다 페이지 역할에 맞게 조정해서 쓴다.

기준 문서:
- [[wiki-knowledge-base-principles]]
- [[wiki-editor-checklist]]

## 1. subject page 템플릿

```markdown
---
type: concept
category: compiler
tags: [swift, <topic>, <subtopic>]
aliases: [<한글 이름>, <영문 이름>]
sources: [<source-file-or-doc>]
---

# <페이지 제목>

<한두 문장으로 이 주제가 무엇인지 정의>

## 핵심 개념

- <핵심 개념 1>
- <핵심 개념 2>
- <핵심 개념 3>

## 왜 중요한가

<이 주제가 타입 시스템/런타임/ABI/interop/optimizer 중 어디와 연결되는지 설명>

## 구현 또는 구조

- <구성요소 1>
- <구성요소 2>
- <구성요소 3>

## 관련 페이지

- <page-a 링크>
- <page-b 링크>
- <page-c 링크>
```

권장 사용처:
- 개념 설명
- 구성요소 설명
- 특정 문서/명세 요약

## 2. hub page 템플릿

```markdown
---
type: summary
category: learning
tags: [swift, <area>, hub, learning]
aliases: [<한글 허브명>, <영문 허브명>]
sources: [<source-a>, <source-b>]
---

# <허브 제목>

이 페이지는 <큰 주제>를
<큰 그림 / 학습 허브 / 상위 지도>로 묶는 허브다.

## <주제>를 이루는 큰 축

| 축 | 핵심 질문 | 연결 페이지 |
|---|---|---|
| <축 1> | <질문> | <관련 페이지 링크>, <관련 페이지 링크> |
| <축 2> | <질문> | <관련 페이지 링크>, <관련 페이지 링크> |
| <축 3> | <질문> | <관련 페이지 링크>, <관련 페이지 링크> |

## 왜 중요한가

<큰 그림이 왜 필요한지 설명>

## 자주 헷갈리는 구분

- <A vs B>
- <C vs D>

## 추천 읽기 순서

1. <page-1 링크>
2. <page-2 링크>
3. <page-3 링크>

## 같이 보면 좋은 페이지

- <page-a 링크>
- <page-b 링크>
- <page-c 링크>
```

권장 사용처:
- 전체 지도
- 분야 허브
- 학습 경로 허브

## 3. crosswalk page 템플릿

```markdown
---
type: reference
category: learning
tags: [swift, proposal, <topic>, <current-context>]
aliases: [<교차 읽기 별칭>]
sources: [swiftlang-swift/docs/proposals/<Foo>.rst]
---

# <역사 문서/제안 묶음> → <현재 구현 문맥> 교차 읽기

이 페이지는 `swift/docs/proposals/<Foo>.rst`를
현재 Swift의 <context> 문맥으로 다시 읽는 교차 페이지다.

## 이 문서(묶음)가 다루는 핵심 문제

- <질문 1>
- <질문 2>
- <질문 3>

## <원문 A>의 핵심 포인트

### 1. <포인트>
<설명>

### 2. <포인트>
<설명>

## <원문 B>의 핵심 포인트

### 1. <포인트>
<설명>

## 현재 구현과 어떻게 이어 읽으면 좋은가

### 1. <현재 축>
- <관련 페이지 링크>
- <관련 페이지 링크>

### 2. <현재 축>
- <관련 페이지 링크>
- <관련 페이지 링크>

## 이 문서를 읽을 때 주의할 점

- <역사 문법과 현재 구현의 차이>
- <개념적 유사성과 실제 채택 구분>

## 로컬 Swift 소스에서 같이 볼 경로

- `swift/docs/proposals/<Foo>.rst`
- `swift/docs/<...>`
- `swift/lib/<...>`

현재 위키 연결:
- <관련 페이지 링크>
- <관련 페이지 링크>

## 추천 읽기 순서

1. <관련 페이지 링크>
2. <관련 페이지 링크>
3. <관련 페이지 링크>

## 같이 보면 좋은 페이지

- <관련 페이지 링크>
- <관련 페이지 링크>
- <관련 페이지 링크>
```

권장 사용처:
- proposal → implementation
- official docs → compiler implementation
- historical doc → modern context

## 4. meta page 템플릿

```markdown
---
type: reference
category: meta
tags: [wiki, <meta-topic>, editorial]
aliases: [<한글 이름>, <영문 이름>]
sources: [<related-meta-docs>]
---

# <메타 페이지 제목>

이 문서는 Swiftlang wiki의 <운영/원칙/체크리스트/연대기>를 다루는 메타 페이지다.

## 목적

- <목적 1>
- <목적 2>
- <목적 3>

## 핵심 규칙 또는 구조

### 1. <항목>
<설명>

### 2. <항목>
<설명>

## 사용 방법

1. <step 1>
2. <step 2>
3. <step 3>

## 같이 보면 좋은 페이지

- <관련 메타 페이지 링크>
- <관련 메타 페이지 링크>
- [[index]]
```

권장 사용처:
- 원칙
- 연대기
- 체크리스트
- 편집 가이드

## 5. frontmatter 선택 가이드

### type
- `summary` — 큰 그림 허브
- `concept` — 개념 설명
- `entity` — 특정 구성요소/문서/도구 설명
- `reference` — 교차 읽기, 참고, 메타 문서
- `meta`는 category로 쓰고 type은 대개 `reference`

### category
- `learning` — 학습 허브, 교차 읽기
- `compiler` — compiler 내부 개념/구성요소
- `sil` — SIL 관련
- `stdlib` — 표준 라이브러리 관련
- `meta` — 위키 운영/원칙/체크리스트/연대기

## 6. 템플릿 사용 시 주의점

- 템플릿을 그대로 복붙하되, 빈 섹션은 남기지 않는다
- 페이지 역할과 안 맞는 섹션은 지운다
- subject page에 위키 내부 메타 히스토리를 넣지 않는다
- 새 페이지를 만들면 nav/허브/키워드/역링크까지 한 배치로 연결한다

## 같이 보면 좋은 페이지

- [[wiki-knowledge-base-principles]]
- [[wiki-editor-checklist]]
- [[wiki-knowledge-chronicle]]
- [[index]]
