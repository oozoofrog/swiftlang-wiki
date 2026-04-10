# Swift Wiki Operations

이 문서는 `swiftlang/.wiki`를 Claude와 Hermes가 병행 운영할 때의 **실무 운영 규칙**을 정리합니다.

## 역할 분리

- `yoda/`
  - 로컬 문서 허브 / 탐색 / 초안 / 실험
  - 공개 웹에 바로 반영되지 않음
- `.wiki/`
  - 공개 웹 원본 (`https://oozoofrog.dev/swiftlang-wiki/`)
  - GitHub repo: `oozoofrog/swiftlang-wiki`
  - 여기 변경만 웹으로 배포됨

즉, 공개 웹에 넣을 내용은 결국 `.wiki/`에 들어와야 합니다.

## 디렉토리 규칙

- `pages/`
  - MkDocs가 직접 렌더하는 공개 페이지 원본
- `sources/`
  - 원문/근거/ingest 소스
  - 페이지 frontmatter의 `sources:`에서 참조
- `site/`
  - 로컬 빌드 결과물
- `scripts/sync.sh`
  - `.wiki` git 변경을 커밋/푸시하는 기존 스크립트
- `scripts/wikictl.py`
  - Hermes/Claude 공용 운영 CLI

## 가장 자주 쓰는 명령

```bash
cd ~/develop/oozoofrog/swiftlang/.wiki

# 현재 상태 요약
./scripts/wikictl.py status

# 환경/구조 점검 (nav 누락, stale build 등)
./scripts/wikictl.py doctor

# 로컬 빌드
./scripts/wikictl.py build

# 로컬 미리보기
./scripts/wikictl.py serve --port 8000

# GitHub 동기화 (기존 sync.sh 래핑)
./scripts/wikictl.py sync "Wiki sync: ..."
```

## 새 페이지 추가 체크리스트

1. `pages/<page-name>.md` 추가
2. 필요하면 `sources/<source-file>` 추가 또는 기존 소스 연결
3. frontmatter에 다음을 채움
   - `type`
   - `category`
   - `tags`
   - `aliases`
   - `sources` 또는 `references`
4. `mkdocs.yml`의 `nav:`에 페이지 등록
5. `index.md` 인덱스 표에 항목 추가
6. `log.md`에 변경 로그 추가
7. `./scripts/wikictl.py doctor`
8. `./scripts/wikictl.py build`
9. 확인 후 `./scripts/wikictl.py sync`

## yoda에서 공개 위키로 옮길 때

`yoda/`는 authoring 공간이고, `.wiki/`는 publish 공간입니다.

권장 절차:

1. `yoda/`에서 초안/구조/분류 실험
2. 공개 가치가 있는 내용만 `.wiki/pages/`에 재구성
3. 원문 근거가 필요하면 `.wiki/sources/`에 source 형태로 보관
4. `mkdocs.yml`, `index.md`, `log.md`까지 같이 갱신
5. `wikictl.py doctor/build`로 검증
6. `wikictl.py sync`로 배포 repo 반영

## 운영 원칙

- 공개 웹 기준 원본은 항상 `.wiki/`
- `sources/`는 근거 보관용, `pages/`는 독자가 읽는 요약/정리용
- nav에 등록되지 않은 페이지는 사실상 공개 탐색에서 누락되므로 `doctor` 경고를 해결할 것
- build가 stale이면 배포 전에 다시 빌드할 것
- 외부 공개 반영은 항상 `sync` 전에 한 번 더 검토할 것
