---
type: reference
category: official-docs
tags: [official-docs, compiler, architecture, swift-org]
aliases: [Swift Compiler, Compiler Architecture]
sources: [swift.org/documentation/swift-compiler/index.html]
---

# Swift Compiler 공개 개요 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/swift-compiler/index.html`
- 원본 URL: https://www.swift.org/documentation/swift-compiler/

## 이 문서는 무엇을 설명하나

Swift.org 공개 문서 관점에서 컴파일러 저장소와 프론트엔드 파이프라인을 짧게 소개하는 입문용 아키텍처 허브다.

## 핵심 포인트

- main swift 저장소와 swift-driver 저장소를 함께 보여 준다.
- Parser → Sema → ClangImporter → SILGen → Mandatory SIL → SIL Optimizations → IRGen → LLVM IR 흐름을 압축 정리한다.
- 프론트엔드가 코드 생성뿐 아니라 IDE 지원도 제공한다고 명시한다.
- 구현 디렉터리와 단계 이름을 바로 매핑해 색인 역할을 한다.

## 컴파일러와 어떻게 연결되나

- lib/Parse / lib/Sema / lib/ClangImporter / lib/SILGen / lib/IRGen
- SILOptimizer와 swift-driver
- IDE 지원용 front-end 서비스

## 언어 표면에서 어떻게 들어오면 좋은가

- C/Objective-C interop
- 타입 검사와 AST
- ARC / generic specialization / 디버거 지원

## 같이 보면 좋은 위키 페이지

- [[overview]]
- [[compiler-driver]]
- [[diagnostics]]
- [[sil-reference]]
- [[optimizer-design]]
- [[debugging-the-compiler]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

기존 `[[overview]]`보다 훨씬 짧고 대외적이다. 그래서 “공개 소개 페이지”와 “내부 위키 요약”의 차이를 설명하는 허브로 쓰기 좋다.
