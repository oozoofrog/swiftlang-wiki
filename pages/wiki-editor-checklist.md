---
type: reference
category: meta
tags: [wiki, checklist, editorial, workflow, quality]
aliases: [위키 편집 체크리스트, 편집 체크리스트, wiki checklist]
sources: [wiki-knowledge-base-principles.md]
---

# 위키 편집 체크리스트

이 문서는 Swiftlang wiki에서
새 페이지를 만들거나 기존 페이지를 크게 수정할 때 쓰는 공개 체크리스트다.

원칙 문서가 "왜"를 설명한다면,
이 문서는 실제 편집 순간에 "무엇을 확인할지"를 묻는다.

기준 문서:
- [[wiki-knowledge-base-principles]]

## 빠른 사용법

가장 단순한 사용 순서:
1. 페이지 유형을 먼저 고른다
2. 해당 체크리스트를 훑는다
3. 연결 작업까지 끝낸다
4. build/doctor/tests로 검증한다
5. clean 상태까지 확인한다

## 1. 공통 체크리스트

모든 페이지에 공통으로 묻는 질문:

- [ ] 이 페이지는 주제를 직접 설명하는가?
- [ ] subject page 안에 위키 내부 사정/작업 히스토리가 섞여 있지 않은가?
- [ ] 문서의 중심 개념과 범위가 첫 1~3문단 안에 드러나는가?
- [ ] 관련 페이지로 이어지는 링크가 충분한가?
- [ ] 독자가 다음에 어디를 읽어야 할지 보이는가?
- [ ] 과장/단정 없이 현재 상태와 역사적 문맥의 경계를 지켰는가?
- [ ] frontmatter(type/category/tags/aliases/sources)가 [[wiki-frontmatter-taxonomy]] 기준과 맞는가?

## 2. 새 subject page 체크리스트

대상 예:
- 개념 페이지
- entity 페이지
- 특정 구현/구성요소 설명 페이지

확인할 것:
- [ ] 이 페이지가 다루는 대상이 한 문장으로 정의되는가?
- [ ] 핵심 개념/역할/구현 위치가 분명한가?
- [ ] 관련 허브 또는 세부 페이지와 연결되는가?
- [ ] "이 페이지가 왜 필요한가"를 위키 내부 사정보다 주제 중요성으로 설명하는가?
- [ ] 관련 페이지 / 추천 읽기 순서가 있는가?

## 3. 새 hub page 체크리스트

대상 예:
- 상위 지도
- 분야별 허브
- 학습 허브

확인할 것:
- [ ] 허브가 묶는 축(3개 이상)이 명확한가?
- [ ] 각 축이 어떤 질문을 푸는지 보이는가?
- [ ] 세부 페이지로 내려가는 경로가 있는가?
- [ ] 큰 그림과 세부 페이지가 반복되지 않고 역할이 구분되는가?
- [ ] 추천 읽기 순서나 학습 경로가 있는가?

## 4. 새 crosswalk page 체크리스트

대상 예:
- proposal → implementation
- 공식 문서 → compiler 구현
- 역사 문서 → 현재 구조

확인할 것:
- [ ] 어떤 역사/원문 문서를 읽는지 분명한가?
- [ ] 당시 문제의식이 무엇이었는지 설명하는가?
- [ ] 오늘날 무엇이 남고 무엇이 달라졌는지 구분하는가?
- [ ] 현재 어떤 구현 페이지와 이어 읽어야 하는지 제시하는가?
- [ ] 원문 문법/속성이 현재 그대로라고 암시하지 않는가?

## 5. meta page 체크리스트

대상 예:
- 원칙
- 연대기
- 체크리스트
- 템플릿

확인할 것:
- [ ] 위키 운영/발전/편집 규칙을 다루는가?
- [ ] subject page에 들어가면 안 되는 메타 정보를 받아주는가?
- [ ] 다른 meta page와 역할이 중복되지 않는가?
- [ ] 위키 운영의 기준선으로 재사용 가능한가?

## 6. 연결 체크리스트

새 페이지를 만들었으면 거의 항상 같이 확인:

- [ ] `mkdocs.yml` nav 반영
- [ ] `pages/index.md` 빠른 탐색 또는 읽기 경로 반영
- [ ] 적절한 허브 페이지 반영
- [ ] `pages/keyword-network.md` 반영
- [ ] 필요한 reverse link 추가
- [ ] meta 성격 변화라면 [[wiki-knowledge-chronicle]] 반영
- [ ] `log.md` 기록 추가

## 7. 숫자/상태 체크리스트

카운트를 보여 주는 페이지를 건드렸다면:
- [ ] page count 최신화
- [ ] crossref count 최신화
- [ ] count 수정 후 build 다시 수행

## 8. 검증 체크리스트

위키 작업은 아래까지 가야 끝이다.

- [ ] `python3 scripts/wikictl.py build`
- [ ] `python3 scripts/wikictl.py doctor`
- [ ] `pytest tests/test_wikictl.py -q`
- [ ] `python3 scripts/wikictl.py status`
- [ ] `Pages missing from mkdocs nav: none`
- [ ] `Site build stale: no`
- [ ] `git status --short --branch`가 clean

## 9. 자주 나는 문제

### 1. subject page에 메타 서술이 들어감
증상:
- "기존 위키에는 ..."
- "이번 배치에서 ..."
- "이 페이지를 추가했다"

대응:
- subject page에서는 삭제
- 필요하면 [[wiki-knowledge-chronicle]]로 이동

### 2. 페이지는 생겼는데 그래프가 약함
증상:
- nav에만 있고 역링크가 거의 없음
- keyword-network에서 못 찾음
- 허브 페이지에 안 걸림

대응:
- 허브 / keyword-network / reverse link를 한 배치로 보강

### 3. count를 고쳤더니 site가 stale
증상:
- build 후 숫자 수정, 그런데 다시 build 안 함

대응:
- count 수정 후 build 재실행

## 10. 최소 완료 기준

이 중 하나라도 빠졌으면 아직 끝난 게 아니다.

- [ ] 페이지 내용 완성
- [ ] 그래프 연결 완성
- [ ] meta/chronology/log 반영 완료
- [ ] 검증 완료
- [ ] clean status 확인 완료

## 같이 보면 좋은 페이지

- [[wiki-knowledge-base-principles]]
- [[wiki-page-templates]]
- [[wiki-frontmatter-taxonomy]]
- [[wiki-knowledge-chronicle]]
- [[index]]
