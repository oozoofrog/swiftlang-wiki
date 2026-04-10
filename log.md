# Wiki Log

| 날짜 | 작업 | 대상 | 영향 페이지 | 요약 |
|------|------|------|------------|------|
| 2026-04-09 | init | — | 0 | 위키 초기화 |
| 2026-04-09 | ingest | swift-readme.md, docs-index.md | overview | 프로젝트 개요 페이지 생성 |
| 2026-04-09 | ingest | lexicon.md | glossary-compiler | 컴파일러 용어 사전 생성 |
| 2026-04-09 | ingest | sil-reference.md 외 9개 | 10개 SIL 페이지 | SIL 문서 전체 수집 |
| 2026-04-09 | ingest | optimizer-design.md 외 3개 | optimizer-design, type-checker, debugging-the-compiler, runtime | 컴파일러 내부 문서 수집 |
| 2026-04-09 | ingest | abi-mangling.rst 외 4개 | abi-mangling, abi-type-metadata, abi-type-layout, abi-calling-convention, abi-stability | ABI 문서 5개 수집 |
| 2026-04-09 | ingest | diagnostics.md 외 5개 | diagnostics, request-evaluator, serialization, dependency-analysis, compiler-driver, compiler-performance | 컴파일러 내부 추가 6개 수집 |
| 2026-04-09 | ingest | ownership-manifesto.md 외 3개 | ownership-manifesto, generics-manifesto, error-handling, dynamic-casting | 언어 설계 매니페스토 4개 수집 |
| 2026-04-09 | ingest | swift-syntax-readme.md 외 10개 | swift-syntax-package 외 10개 | 서브프로젝트 README 11개 수집 |
| 2026-04-09 | update | overview.md | overview | 새 26개 페이지 교차참조 추가 |
| 2026-04-09 | lint | — | overview, sil-reference | 고아 페이지 2건 수정 (llbuild-package, sil-initializer-conventions 참조 추가) |
| 2026-04-09 | lint-fix | swift-build-package | swift-build-package | 스파스 페이지 본문 보강 (329B → 950B+) |
| 2026-04-09 | lint-fix | ABI 5개, runtime, glossary 등 | 11개 | ABI 상호 참조 보강 + 컴파일러 내부 역참조 추가 |
| 2026-04-09 | ingest | generics-book-readme.md, abi-generic-signature.md | compiling-swift-generics, generic-signatures, substitution-maps, archetypes, conformances, abi-generic-signature | Generics 책 + GenericSignature ABI 수집 (6페이지) |
| 2026-04-09 | skip | swift/docs/EmbeddedSwift/ | — | 문서가 swift.org로 이전됨, 로컬에 내용 없음 |
| 2026-04-09 | ingest | objc-interop 외 2개 | objc-interop, c-to-swift-name-translation, how-swift-imports-c-apis | Clang/ObjC Interop 3페이지 (에이전트) |
| 2026-04-09 | ingest | modules.md 외 7개 | modules, access-control, literals, failable-initializers, stdlib-programmers-manual, library-evolution, high-level-sil-optimizations, transparent-attr | 언어 기능 + stdlib 8페이지 (에이전트) |
| 2026-04-09 | ingest | cpp-interop 7개 소스 | cpp-interop-overview, cpp-using-from-swift, cpp-calling-swift | C++ Interop 3페이지 (에이전트) |
| 2026-04-09 | ingest | getting-started 외 6개 | getting-started, first-pull-request, compiler-faq, testing-guide, continuous-integration, development-tips | 기여 가이드 6페이지 (에이전트) |
| 2026-04-09 | analyze | 소스 코드 분석 | sil-optimizer-pass-catalog, ast-node-hierarchy, swift-compiler-sources | 코드 구조 분석 3페이지 (Passes.def, *Nodes.def, SwiftCompilerSources/) |
| 2026-04-09 | update | index.md, overview.md | 전체 | 23개 신규 페이지 인덱스 등록 + overview 교차참조 추가 |
| 2026-04-10 | publish | downloads/index.md, mkdocs.yml | downloads, Home, Wiki Index | Swift 공식/준공식 참고 문서 다운로드 허브 추가 + ZIP/개별 파일 정적 자산 배치 |
| 2026-04-10 | publish | official-docs/*.md, downloads/index.md, mkdocs.yml, index.md | 공식/다운로드 문서 21건 개별 해설 + 언어→컴파일러 교차학습 지도 + 위키 내비게이션 확장 |
| 2026-04-10 | publish | concurrency-data-race-safety.md | concurrency, type-checker, diagnostics, sil-optimizer-pass-catalog | Swift 6 데이터 경쟁 안전성 전용 심화 페이지 추가 + 공식 문서 교차 페이지 연결 |
| 2026-04-10 | publish | swift-compiler-7-day-course.md, concurrency-data-race-safety.md | course, source-guided, concurrency | 입문자용 7일 코스 추가 + 실제 로컬 Swift 소스 경로/검증 명령 반영 |
| 2026-04-10 | update | keyword-network.md, glossary-compiler.md 외 저링크 페이지 다수 | keywords, glossary, navigation | 키워드 허브 추가 + glossary 링크화 + 저링크 페이지 교차참조 보강 |
| 2026-04-10 | update | 기여/Interop/SIL 세부 페이지 다수 | keywords, navigation, crossrefs | 2차 연결망 보강: contributor/C++/SIL/ABI 관련 저링크 페이지 교차참조 확장 |
| 2026-04-10 | sanitize | pages/, sources/, files/downloads/, OPERATIONS.md | public pages, source excerpts, bundle metadata | 로컬 맥 경로/사용자명/머신 한정 표현 제거, 공개 경로 표기는 `swift/...` 및 상대경로(`.`/`files/...`) 기준으로 일반화 |
| 2026-04-10 | plan | plans/2026-04-10-complete-swift-wiki-expansion.md | expansion roadmap | Swift + Swift Compiler 전체 위키 완성 목표를 위한 장기 확장 계획 문서 추가 |
| 2026-04-10 | publish | swift-ecosystem-map.md 외 4개, mkdocs.yml, index.md, keyword-network.md | Swift whole-map, learning, navigation | Swift 언어/컴파일러/툴체인/학습 스택/상호관계 상위 허브 5페이지 추가 + 홈/키워드/nav 연결 |
| 2026-04-10 | publish | llvm-backend.md 외 5개, mkdocs.yml, index.md, keyword-network.md | toolchain, infrastructure, contributor workflow | LLVM / Clang Importer / LLDB / CMake·Ninja / lit·FileCheck / build-test-debug 스택 페이지 추가 + 기존 가이드와 상호연결 |
| 2026-04-10 | publish | swift-type-system.md 외 2개, mkdocs.yml, index.md, keyword-network.md | language, semantics, stdlib/runtime, tooling | Swift 타입 시스템 / 매크로·도구 스택 / 표준 라이브러리·런타임·컴파일러 상위 허브 추가 + 기존 언어/도구/stdlib 페이지와 상호연결 |
| 2026-04-10 | publish | swift-ownership-memory-model.md, mkdocs.yml, index.md, keyword-network.md | ownership, memory, concurrency bridge | Swift 소유권·메모리 모델 상위 허브 추가 + 언어/OSSA/runtime/concurrency 문서 사이 역링크 보강 |
| 2026-04-10 | publish | swift-concurrency-architecture.md, mkdocs.yml, index.md, keyword-network.md | concurrency, runtime, migration, compiler bridge | Swift Concurrency 전체 구조 허브 추가 + strict concurrency/ownership/runtime 문서와 상호연결 |
| 2026-04-10 | publish | swift-actor-isolation-and-sendable.md, swift-task-executor-runtime.md, mkdocs.yml, index.md, keyword-network.md | concurrency deep-dive, isolation, runtime | actor/sendable 세부 허브와 task/executor/runtime 세부 허브 추가 + 동시성/런타임/학습 경로 보강 |
| 2026-04-10 | publish | swift-evolution-and-proposal-history.md, mkdocs.yml, index.md, keyword-network.md | design history, manifesto, proposals | Swift Evolution / proposal history 허브 추가 + manifesto/library-evolution/concurrency 문서와 상호연결 |

