---
type: reference
category: official-docs
tags: [official-docs, lldb, debugger, repl]
aliases: [REPL and Debugger, Swift LLDB]
sources: [swift.org/documentation/lldb/index.html]
---

# REPL and Debugger 해설

다운로드 번들에 포함된 공식/준공식 문서를 위키 관점으로 다시 정리한 페이지다.

- 원문 유형: `html`
- 다운로드 번들 경로: `swift.org/documentation/lldb/index.html`
- 원본 URL: https://www.swift.org/documentation/lldb/

## 이 문서는 무엇을 설명하나

Swift의 REPL과 디버거가 왜 LLDB 위에 결합돼 있는지, playground 지원이 어떤 구조로 연결되는지 설명하는 공개 개요다.

## 핵심 포인트

- Swift REPL은 별도 인터프리터가 아니라 LLDB 기반 디버거 경험과 결합돼 있다.
- 정확한 타입 관찰과 표현식 평가를 위해 컴파일러와 디버거 버전이 맞아야 한다.
- REPL과 디버거를 하나로 보는 이유를 통합 디버깅, 오류 후 조사, 풍부한 표현식 평가 관점에서 설명한다.
- PlaygroundSupport / PlaygroundLogger처럼 Xcode 주변 도구도 함께 언급한다.

## 컴파일러와 어떻게 연결되나

- LLDB expression evaluator
- debugging-the-compiler
- toolchain snapshot과 Xcode playground 지원
- Swift 타입 메타데이터 관찰

## 언어 표면에서 어떻게 들어오면 좋은가

- REPL 사용법
- 표현식 평가
- fatal error 이후 상태 조사
- playground API와 값 로깅

## 같이 보면 좋은 위키 페이지

- [[debugging-the-compiler]]
- [[getting-started]]
- [[overview]]
- [[language-to-compiler-crosswalk]]

## 읽는 방법 메모

도구 문서지만, Swift가 런타임·메타데이터·표현식 평가를 얼마나 깊게 디버거와 공유하는지 보여 준다는 점에서 ABI/런타임 학습과도 연결된다.
