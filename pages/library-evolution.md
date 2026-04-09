---
type: concept
category: compiler
tags: [library-evolution, resilience, abi]
aliases: [라이브러리 진화, Library Evolution, 복원력, Resilience]
sources: [library-evolution.rst]
---

# 라이브러리 진화 (Library Evolution)

Swift 5부터 ABI 안정 플랫폼에서 지원되는 라이브러리 진화 모델. 바이너리 호환성을 깨지 않고 라이브러리를 변경할 수 있도록 하며, 이전/이후 버전 클라이언트 모두와의 호환성(backwards/forwards compatibility)을 목표로 한다.

## 핵심 속성

- `@frozen`: struct/enum의 저장 레이아웃을 고정하여 직접 접근 허용, 대신 멤버 추가 불가
- `@inlinable`: 함수 본문을 클라이언트에 인라인 가능하게 공개, ABI 공개 심볼만 참조 가능
- `@usableFromInline`: internal 선언을 인라인 코드에서 사용 가능하게 노출

## 허용되는 변경

- 기본값 있는 매개변수 추가, non-frozen enum 케이스 추가
- 새 프로토콜 준수 추가, stored property 기본값 변경

기본 원칙: 처음 공개 시의 선택이 미래 진화를 제한하지 않도록 설계.

관련 페이지: [[abi-stability]], [[overview]], [[runtime]]
