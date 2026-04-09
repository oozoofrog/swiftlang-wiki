---
type: entity
category: compiler
tags: [diagnostics, errors, warnings, fix-it]
aliases: [진단, Diagnostics]
sources: [diagnostics.md]
---

# 진단 시스템 (Diagnostics)

Swift 컴파일러 진단 메시지 작성 가이드라인. 원본: `swift/docs/Diagnostics.md`

## 진단 분류

- **Error**: 코드 의도가 불명확하거나 즉시 크래시를 야기하는 경우
- **Warning**: 코드 의도는 명확하지만 즉시 크래시하지 않는 경우. Swift에서는 **경고를 비활성화할 수 없음** (방언 분화 방지)
- **Note**: 직전 error/warning에 첨부되는 추가 정보

## 작성 가이드라인

- 단일 구/문장, 마침표 없음
- 신문 헤드라인 스타일 — 불필요한 관사 생략
- 컴파일러가 코드를 이해했음을 보여주는 정보 포함
- "규칙"으로 표현: `'super.init' cannot be called outside of an initializer`
- `'`로 속성/심볼 이름 인용 (terms of art는 평문)

## Fix-it

- 한 가지 명확한 수정만 있을 때 제공
- 기계적으로 적용 가능해야 함
- 사용자의 의도를 바꾸지 않아야 함

## 교육적 노트 (Educational Notes)

`swift/userdocs/diagnostics/` 디렉토리에 `.md` 파일로 작성. `EducationalNotes.def`에서 진단 ID와 연결. 사용자에게 `-print-educational-notes` 플래그로 표시.

관련 페이지: [[overview]], [[type-checker]], [[debugging-the-compiler]], [[error-handling]]
