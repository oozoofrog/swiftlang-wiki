---
type: entity
category: packages
tags: [llbuild, build-system, low-level, ninja]
aliases: [llbuild]
sources: [llbuild-readme.md]
---

# llbuild

저수준 빌드 시스템 라이브러리. SwiftPM과 Swift Build의 실행 엔진.

## 핵심 컴포넌트

- **BuildSystem**: 높은 수준의 빌드 추상화
- **Core Engine**: 의존성 기반 작업 실행
- **Ninja compatibility**: Ninja 빌드 파일 호환

## 아키텍처

llbuild는 작업(task) 간 의존성을 추적하고, 변경된 입력에 따라 최소한의 작업만 재실행. 증분 빌드의 핵심.

### 디렉토리

`llbuild/`

관련 페이지: [[swift-package-manager]], [[swift-build-package]]
