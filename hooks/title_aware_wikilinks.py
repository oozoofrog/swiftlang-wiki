from __future__ import annotations

import re
from pathlib import Path

try:
    from mkdocs.plugins import event_priority
except Exception:  # pragma: no cover
    event_priority = lambda _priority: (lambda func: func)


ROAMLINK_RE = re.compile(r"""\[\[(.*?)(\#.*?)?(?:\|([\D][^\|\]]+[\d]*))?(?:\|(\d+)(?:x(\d+))?)?\]\]""")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)

_TITLE_MAP_EXACT: dict[str, str] = {}
_TITLE_MAP_FUZZY: dict[str, str] = {}
_AMBIGUOUS_FUZZY: set[str] = set()


def _simplify(name: str) -> str:
    return re.sub(r"[\-_ ]", "", name.lower()).replace(".md", "")


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1].strip()
    return value


def extract_page_title(text: str) -> str | None:
    body = text
    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        fm_text = frontmatter.group(1)
        body = text[frontmatter.end() :]
        for line in fm_text.splitlines():
            if not line.startswith("title:"):
                continue
            title = _strip_quotes(line.split(":", 1)[1])
            if title:
                return title

    heading = H1_RE.search(body)
    if heading:
        return heading.group(1).strip()
    return None


def build_title_maps(docs_dir: Path) -> None:
    _TITLE_MAP_EXACT.clear()
    _TITLE_MAP_FUZZY.clear()
    _AMBIGUOUS_FUZZY.clear()

    for path in sorted(docs_dir.rglob("*.md")):
        title = extract_page_title(path.read_text(encoding="utf-8"))
        if not title:
            continue

        rel_no_ext = path.relative_to(docs_dir).with_suffix("").as_posix()
        _TITLE_MAP_EXACT[rel_no_ext] = title

        fuzzy = _simplify(path.name)
        existing = _TITLE_MAP_FUZZY.get(fuzzy)
        if existing is None:
            _TITLE_MAP_FUZZY[fuzzy] = title
        elif existing != title:
            _AMBIGUOUS_FUZZY.add(fuzzy)
            _TITLE_MAP_FUZZY.pop(fuzzy, None)


def resolve_title(target: str) -> str | None:
    normalized = target.strip().replace("\\", "/")
    if not normalized or normalized.startswith("http://") or normalized.startswith("https://"):
        return None
    if normalized.endswith(".md"):
        normalized = normalized[:-3]

    exact = _TITLE_MAP_EXACT.get(normalized)
    if exact:
        return exact

    fuzzy = _simplify(Path(normalized).name)
    if fuzzy in _AMBIGUOUS_FUZZY:
        return None
    return _TITLE_MAP_FUZZY.get(fuzzy)


def rewrite_bare_wikilinks(markdown: str) -> str:
    def replace(match: re.Match[str]) -> str:
        filename = match.group(1).strip() if match.group(1) else ""
        anchor = match.group(2) or ""
        alias = match.group(3) or ""
        width = match.group(4) or ""
        height = match.group(5) or ""

        if alias or not filename:
            return match.group(0)

        title = resolve_title(filename)
        if not title:
            return match.group(0)

        display = f"{title}{anchor}" if anchor else title
        size = ""
        if width and height:
            size = f"|{width}x{height}"
        elif width:
            size = f"|{width}"

        return f"[[{filename}{anchor}|{display}{size}]]"

    return ROAMLINK_RE.sub(replace, markdown)


@event_priority(100)
def on_config(config, **kwargs):
    build_title_maps(Path(config["docs_dir"]))
    return config


@event_priority(100)
def on_page_markdown(markdown: str, *, page, config, files, **kwargs) -> str:
    if not _TITLE_MAP_EXACT:
        build_title_maps(Path(config["docs_dir"]))
    return rewrite_bare_wikilinks(markdown)
