#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / 'pages'
SOURCES_DIR = ROOT / 'sources'
SITE_DIR = ROOT / 'site'
MKDOCS_YML = ROOT / 'mkdocs.yml'
SYNC_SH = ROOT / 'scripts' / 'sync.sh'


def extract_nav_page_paths(text: str) -> list[str]:
    lines = text.splitlines()
    try:
        nav_index = next(i for i, line in enumerate(lines) if line.strip() == 'nav:')
    except StopIteration:
        return []

    seen: set[str] = set()
    out: list[str] = []
    for line in lines[nav_index + 1 :]:
        if not line.strip():
            continue
        if not line.startswith(' ') and not line.startswith('-'):
            break
        match = re.search(r'([A-Za-z0-9_./-]+\.md)\s*$', line.strip())
        if not match:
            continue
        page = match.group(1)
        if page not in seen:
            seen.add(page)
            out.append(page)
    return out


def find_unlisted_pages(root: Path = ROOT) -> list[str]:
    mkdocs_text = (root / 'mkdocs.yml').read_text()
    nav_pages = set(extract_nav_page_paths(mkdocs_text))
    docs_dir = root / 'pages'
    found = []
    for path in sorted(docs_dir.rglob('*.md')):
        rel = path.relative_to(docs_dir).as_posix()
        if rel not in nav_pages:
            found.append(rel)
    return found


def site_is_stale(root: Path = ROOT) -> bool:
    site_index = root / 'site' / 'index.html'
    if not site_index.exists():
        return True
    built_mtime = site_index.stat().st_mtime
    watched = [root / 'mkdocs.yml']
    watched.extend((root / 'pages').rglob('*.md'))
    for path in watched:
        if path.exists() and path.stat().st_mtime > built_mtime:
            return True
    return False


def read_site_url(root: Path = ROOT) -> str | None:
    text = (root / 'mkdocs.yml').read_text()
    for line in text.splitlines():
        if line.startswith('site_url:'):
            return line.split(':', 1)[1].strip()
    return None


def run_git(args: Sequence[str], *, root: Path = ROOT) -> str:
    return subprocess.check_output(['git', *args], cwd=root, text=True).strip()


def count_git_changes(root: Path = ROOT) -> tuple[int, int]:
    modified = run_git(['diff', '--name-only', 'HEAD', '--', '.'], root=root)
    untracked = run_git(['ls-files', '--others', '--exclude-standard'], root=root)
    modified_count = len([line for line in modified.splitlines() if line.strip()])
    untracked_count = len([line for line in untracked.splitlines() if line.strip()])
    return modified_count, untracked_count


def build_status_snapshot(root: Path = ROOT) -> dict[str, object]:
    modified, untracked = count_git_changes(root)
    remote = None
    branch = None
    try:
        remote = run_git(['remote', 'get-url', 'origin'], root=root)
    except Exception:
        remote = None
    try:
        branch = run_git(['branch', '--show-current'], root=root)
    except Exception:
        branch = None
    return {
        'root': root,
        'pages': len(list((root / 'pages').glob('*.md'))),
        'sources': len(list((root / 'sources').glob('*'))),
        'modified': modified,
        'untracked': untracked,
        'unlisted_pages': find_unlisted_pages(root),
        'site_stale': site_is_stale(root),
        'site_url': read_site_url(root),
        'remote': remote,
        'branch': branch,
    }


def resolve_mkdocs_command(root: Path = ROOT) -> list[str]:
    venv_python = root / '.venv' / 'bin' / 'python'
    if venv_python.exists():
        return [str(venv_python), '-m', 'mkdocs']
    mkdocs = shutil.which('mkdocs')
    if mkdocs:
        return [mkdocs]
    raise SystemExit('mkdocs executable not found. Install requirements or create .venv first.')


def cmd_status(_: argparse.Namespace) -> int:
    snap = build_status_snapshot(ROOT)
    dirty = int(snap['modified']) + int(snap['untracked'])
    print(f"Wiki root: {snap['root']}")
    print(f"Branch: {snap['branch'] or '(unknown)'}")
    print(f"Remote: {snap['remote'] or '(none)'}")
    print(f"Site URL: {snap['site_url'] or '(unset)'}")
    print(f"Pages: {snap['pages']} | Sources: {snap['sources']}")
    print(f"Git changes: modified {snap['modified']}, untracked {snap['untracked']}, total {dirty}")
    print(f"Site build stale: {'yes' if snap['site_stale'] else 'no'}")
    if snap['unlisted_pages']:
        print('Pages missing from mkdocs nav:')
        for page in snap['unlisted_pages']:
            print(f'  - {page}')
    else:
        print('Pages missing from mkdocs nav: none')
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    snap = build_status_snapshot(ROOT)
    mkdocs_cmd = resolve_mkdocs_command(ROOT)
    issues: list[str] = []
    if not (ROOT / '.venv' / 'bin' / 'python').exists():
        issues.append('.venv/bin/python missing')
    if not mkdocs_cmd:
        issues.append('mkdocs command unavailable')
    if snap['unlisted_pages']:
        issues.append(f"{len(snap['unlisted_pages'])} pages missing from mkdocs nav")
    if snap['site_stale']:
        issues.append('site build is stale')
    if issues:
        print('Doctor found issues:')
        for issue in issues:
            print(f'  - {issue}')
        return 1
    print('Doctor OK: wiki environment looks healthy.')
    print(f"Pages: {snap['pages']} | Sources: {snap['sources']} | Site URL: {snap['site_url']}")
    return 0


def cmd_build(_: argparse.Namespace) -> int:
    mkdocs_cmd = resolve_mkdocs_command(ROOT)
    return subprocess.call([*mkdocs_cmd, 'build'], cwd=ROOT)


def cmd_serve(args: argparse.Namespace) -> int:
    mkdocs_cmd = resolve_mkdocs_command(ROOT)
    return subprocess.call([*mkdocs_cmd, 'serve', '-a', f'{args.host}:{args.port}'], cwd=ROOT)


def cmd_sync(args: argparse.Namespace) -> int:
    cmd = [str(SYNC_SH)]
    if args.message:
        cmd.extend(args.message)
    return subprocess.call(cmd, cwd=ROOT)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Hermes/Claude wiki automation helper for swiftlang/.wiki')
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('status', help='Show wiki status summary').set_defaults(func=cmd_status)
    sub.add_parser('doctor', help='Validate local wiki environment').set_defaults(func=cmd_doctor)
    sub.add_parser('build', help='Build the MkDocs site').set_defaults(func=cmd_build)

    serve = sub.add_parser('serve', help='Serve the MkDocs site locally')
    serve.add_argument('--host', default='127.0.0.1')
    serve.add_argument('--port', type=int, default=8000)
    serve.set_defaults(func=cmd_serve)

    sync = sub.add_parser('sync', help='Commit and push wiki changes using existing sync.sh')
    sync.add_argument('message', nargs=argparse.REMAINDER)
    sync.set_defaults(func=cmd_sync)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == '__main__':
    raise SystemExit(main())
