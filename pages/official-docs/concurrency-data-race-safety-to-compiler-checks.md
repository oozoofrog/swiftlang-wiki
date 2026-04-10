---
type: reference
category: official-docs
tags: [official-docs, concurrency, diagnostics, redirect]
aliases: [Concurrency redirect, Swift 6 concurrency migration]
sources: [swift.org/documentation/concurrency/index.html]
---

# Concurrency Data Race Safety → 컴파일러 검사 교차 읽기

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/concurrency/index.html`
- 원본 URL: https://www.swift.org/documentation/concurrency/

## 이 문서는 무엇을 설명하나

다운로드된 파일은 redirect-only이지만, canonical 대상이 Swift 6 concurrency migration guide의 data race safety 주제이므로 이를 컴파일러 검사 관점으로 연결하는 페이지다.

## 핵심 포인트

- 번들 안의 파일 자체에는 동시성 본문이 없고 redirect만 존재한다.
- canonical 주제가 “enable data race safety”인 만큼, 핵심은 async/await 입문보다 strict checking과 migration이다.
- 즉 이 문서를 읽는 이유는 동시성 기능 소개보다 compiler-enforced safety를 따라가는 데 있다.
- 현재 위키에는 전용 concurrency 페이지가 약하므로, 타입 검사·진단·SIL pass 관점의 연결이 특히 중요하다.

## 컴파일러와 어떻게 연결되나

- type-checker의 isolation / Sendable 검사
- diagnostics
- sil-optimizer-pass-catalog의 concurrency 관련 pass
- ownership model과 data race safety의 접점

## 언어 표면에서 어떻게 들어오면 좋은가

- actor
- Sendable
- isolation
- Swift 6 strict concurrency migration

## 같이 보면 좋은 위키 페이지

- [[type-checker]]
- [[diagnostics]]
- [[sil-optimizer-pass-catalog]]
- [[ownership-manifesto]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

redirect-only라 본문 요약은 불가능하지만, 오히려 “Swift 6의 동시성 안전성은 결국 어디서 검사되는가?”를 묻는 지점으로 바꾸면 위키 가치가 생긴다.
