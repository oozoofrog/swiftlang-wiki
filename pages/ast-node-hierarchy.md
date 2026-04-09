---
type: entity
category: compiler
tags: [ast, nodes, declarations, expressions, statements, types]
aliases: [AST 노드 계층, AST Node Hierarchy]
sources: []
---

# AST 노드 계층 구조

Swift 컴파일러의 AST 노드 분류. `*Nodes.def` 파일에서 추출.

## 정의 파일

| 파일 | 노드 종류 |
|------|----------|
| `DeclNodes.def` | 선언 (Decl) |
| `ExprNodes.def` | 표현식 (Expr) |
| `StmtNodes.def` | 문 (Stmt) |
| `TypeNodes.def` | 타입 (Type) |
| `TypeReprNodes.def` | 타입 표현 (TypeRepr) |

## Decl (선언) 계층

```
Decl
├── ValueDecl (이름이 있는 선언)
│   ├── TypeDecl
│   │   ├── NominalTypeDecl
│   │   │   ├── ClassDecl, StructDecl, EnumDecl, ProtocolDecl
│   │   │   └── BuiltinTupleDecl, ActorDecl
│   │   ├── TypeAliasDecl, AssociatedTypeDecl
│   │   ├── GenericTypeParamDecl
│   │   └── OpaqueTypeDecl, ModuleDecl
│   ├── AbstractStorageDecl
│   │   ├── VarDecl (ParamDecl 포함)
│   │   └── SubscriptDecl
│   ├── AbstractFunctionDecl
│   │   ├── FuncDecl (AccessorDecl 포함)
│   │   ├── ConstructorDecl
│   │   └── DestructorDecl
│   ├── EnumElementDecl
│   └── MacroDecl
├── ImportDecl, PatternBindingDecl, EnumCaseDecl
├── OperatorDecl (PrefixOperator, PostfixOperator, InfixOperator)
├── PrecedenceGroupDecl
├── ExtensionDecl, IfConfigDecl
├── MacroExpansionDecl, UsingDecl
└── MissingDecl, MissingMemberDecl
```

## Type (타입) 분류

| 카테고리 | 예시 |
|----------|------|
| **Nominal** | StructType, ClassType, EnumType, ProtocolType |
| **Sugared** | TypeAliasType, ParenType, ArraySliceType, OptionalType |
| **Builtin** | BuiltinIntegerType, BuiltinFloatType, BuiltinRawPointerType |
| **Function** | FunctionType, GenericFunctionType |
| **Metatype** | MetatypeType, ExistentialMetatypeType |
| **Reference** | ReferenceStorageType (weak, unowned, unmanaged) |
| **Artificial** | SILFunctionType, SILBoxType, SILMoveOnlyWrappedType |

## TypeRepr (타입 구문 표현)

파서가 생성하는 구문 트리 — Sema에서 실제 Type으로 해석:
- `IdentTypeRepr` → 이름 조회로 타입 결정
- `ArrayTypeRepr` → `[Element]` 구문
- `OptionalTypeRepr` → `T?` 구문
- `FunctionTypeRepr` → `(A) -> B` 구문
- `CompositionTypeRepr` → `P1 & P2` 프로토콜 합성

## 파일 위치

- `swift/include/swift/AST/Decl.h` — Decl 클래스 계층
- `swift/include/swift/AST/Expr.h` — Expr 클래스 계층
- `swift/include/swift/AST/Stmt.h` — Stmt 클래스 계층
- `swift/include/swift/AST/Types.h` — Type 클래스 계층
- `swift/include/swift/AST/TypeRepr.h` — TypeRepr 클래스 계층

관련 페이지: [[overview]], [[type-checker]], [[glossary-compiler]], [[sil-reference]]
