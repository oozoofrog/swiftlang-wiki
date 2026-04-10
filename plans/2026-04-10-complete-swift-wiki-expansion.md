# Complete Swift + Swift Compiler Wiki Expansion Plan

> **For Hermes:** Expand this wiki in waves. Keep using the current hub-first + selective deepening strategy: every major source gets a bridge page, and the highest-value areas get dedicated deep-dive pages.

**Goal:** Turn the current compiler-focused wiki into a complete Swift + Swift Compiler knowledge base covering the language, compiler internals, toolchain, ecosystem, and learning paths.

**Architecture:** Keep two layers. Layer 1 is a stable set of hub pages that explain the whole terrain and route readers by intent. Layer 2 is a growing set of deep reference pages for the core areas: type system, SIL, ABI, runtime, tooling, build/test infrastructure, interop, and ecosystem packages.

**Tech Stack:** MkDocs Material, roamlinks wiki links, markdown pages in `pages/`, static artifacts in `files/`, validation via `scripts/wikictl.py`.

---

## Scope Definition

This wiki should eventually answer all of the following:

1. What Swift is as a language.
2. What the Swift compiler is as an implementation.
3. How the Swift language, standard library, runtime, compiler, and toolchain fit together.
4. Which technologies someone must learn to understand or contribute to the Swift compiler.
5. How the broader Swift ecosystem (SwiftPM, SwiftSyntax, SourceKit-LSP, Foundation, NIO, Testing, etc.) connects back to the compiler.
6. How to move from beginner-level Swift knowledge to compiler-level understanding without losing the big picture.

## Information Architecture

### Layer 1: Master Hubs

Create and maintain these top-level pages:
- `pages/swift-ecosystem-map.md`
- `pages/swift-language-overview.md`
- `pages/swift-and-swift-compiler.md`
- `pages/swift-toolchain-stack.md`
- `pages/swift-compiler-learning-stack.md`

These pages should remain short, stable, and heavily linked.

### Layer 2: Deep-Dive Families

Continue expanding these families:
- Language semantics: modules, access control, literals, error handling, ownership, concurrency
- Compiler core: parser, AST, request evaluator, Sema, diagnostics, dependency analysis
- IR pipeline: SIL, ownership SSA, optimizer, IRGen, LLVM backend
- ABI/runtime: mangling, metadata, layout, calling conventions, resilience, runtime
- Interop: Clang importer, ObjC, C, C++
- Toolchain/build/test: driver, SwiftPM, llbuild, Swift Build, CMake, Ninja, lit, FileCheck, LLDB, CI
- Ecosystem packages: SwiftSyntax, SourceKit-LSP, Foundation, Testing, Collections, NIO, formatters

## Wave Plan

### Wave 1: Whole-map pages
- Add the 5 hub pages above.
- Add them to `mkdocs.yml` navigation.
- Add them to `pages/index.md` quick navigation and category table.
- Add them to `pages/keyword-network.md` as entry points.

### Wave 2: Toolchain and infrastructure deepening
- Add dedicated pages for LLVM, Clang, LLDB, CMake, Ninja, lit, and FileCheck.
- Add a build/test/debugging crosswalk page connecting those tools to current contribution workflows.
- Strengthen links from `getting-started`, `testing-guide`, `development-tips`, and `debugging-the-compiler`.

### Wave 3: Swift language completeness
- Add higher-level synthesis pages for the Swift type system, memory model, protocol-oriented design, macro system, module system, and standard library model.
- Connect language-facing docs to compiler-facing pages more systematically.

### Wave 4: Ecosystem completeness
- Expand package/tool pages and add hub pages for app/tool authors, library authors, and compiler contributors.
- Add more “Swift in practice ↔ compiler internals” bridge pages.

## Editorial Rules

1. Public-facing path examples use generic repo-root labels like `swift/...`, never machine-specific placeholders.
2. Hub pages explain relationships; deep pages explain mechanisms.
3. Every new page must link both upward (to a hub) and sideways (to siblings).
4. Prefer reusable learning routes over isolated summaries.
5. When a source document is shallow or redirect-only, create a crosswalk page rather than pretending the source itself is detailed.

## Verification Checklist

After each wave:
- Run `python3 scripts/wikictl.py build`
- Run `python3 scripts/wikictl.py doctor`
- Run `python3 tests/test_wikictl.py`
- Update `pages/index.md`
- Update `pages/keyword-network.md`
- Update `log.md`

## Definition of Done for the Project

The wiki is “complete enough” when a reader can start from any of these entry points and never get lost:
- “I want to learn Swift as a language.”
- “I want to understand how Swift is implemented.”
- “I want to contribute to the compiler.”
- “I want to understand the full Swift toolchain.”
- “I want to see how libraries, build tools, IDE tools, and runtime concerns connect back to the compiler.”
