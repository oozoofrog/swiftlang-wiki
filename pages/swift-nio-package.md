---
type: entity
category: packages
tags: [swift-nio, networking, async-io, event-loop]
aliases: [SwiftNIO]
sources: [swift-nio-readme.md]
---

# SwiftNIO

크로스 플랫폼 비동기 이벤트 기반 네트워크 프레임워크. 고성능 네트워크 서버/클라이언트 구현 기반.

## 핵심 개념

- **EventLoop**: 이벤트 기반 비동기 I/O
- **Channel**: 네트워크 연결 추상화
- **ChannelHandler**: 파이프라인 기반 데이터 처리
- **ByteBuffer**: 효율적 바이트 버퍼
- **EventLoopFuture/Promise**: 비동기 결과 처리

## 아키텍처

Netty(Java)에서 영감. 채널 파이프라인으로 인바운드/아웃바운드 핸들러 체이닝.

### 디렉토리

`swift-nio/`

관련 페이지: [[overview]], [[keyword-network]], [[core-libraries-to-compiler-crosswalk]], [[swift-package-manager]], [[swift-testing-package]], [[concurrency-data-race-safety]]
