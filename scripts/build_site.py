"""Build the public reading site with Python's standard library only.

Sources remain in docs/source. This renderer deliberately supports only the
Markdown constructs used here and escapes raw HTML. It does not parse comments.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from html.parser import HTMLParser
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SOURCE = DOCS / "source"
PAGES = [
    ("index", "빠른 시작", "시작하기"),
    ("formats", "지원 형태 한눈에", "시작하기"),
    ("timeline", "D1·D2·Point", "시간축 용어"),
    ("existing", "기존 댓글 읽기", "작성과 읽기"),
    ("ranges", "구간과 강조", "작성과 읽기"),
    ("people", "인물과 합방", "작성과 읽기"),
    ("sharing", "자료 공유하기", "자료 가져오기"),
    ("summary", "요약과 JSON 가져오기", "자료 가져오기"),
    ("files", "파일 형식과 예제", "자료 가져오기"),
    ("cuts", "컷 작업과 MP4 저장", "작업과 저장"),
    ("limits", "한계와 문제 해결", "더 알아보기"),
    ("reference", "작성 기준", "더 알아보기"),
    ("contact", "문의·오류 제보", "더 알아보기"),
    ("policy", "이용 정책", "더 알아보기"),
]
LINKS = {"PEOPLE.md": "people.html", "IMPORT.md": "files.html",
         "ROSTER.md": "files.html#참가자와-역할-이름-가져오기",
         "SPEC.md": "reference.html", "SUPPORT.md": "formats.html",
         "README.md": "index.html", "VALIDATION.md": "reference.html#검증-범위"}
VERSIONS = json.loads((DOCS / 'guide-versions.json').read_text(encoding='utf-8'))
APP_VERSION = VERSIONS['stable']
HISTORY = ROOT / 'guide-history'


@dataclass
class SiteContext:
    version: str
    status: str
    pages: list
    prefix: str
    assets: dict
    source_ref: str = 'main'

    def asset(self, target: str) -> str:
        return self.prefix + self.assets.get(target, target)

    def version_menu(self, key: str) -> str:
        items = []
        for release in VERSIONS['versions']:
            version = release['version']
            available = (HISTORY / version / 'source' / (key + '.md')).exists()
            page = key if available else 'index'
            target = self.prefix + f'versions/{version}/{page}.html'
            items.append(f'<a href="{target}">{html.escape(release["label"])}</a>')
        label = next(r['label'] for r in VERSIONS['versions'] if r['version'] == self.version)
        return (f'<details class="guide-version"><summary>{html.escape(label)}</summary>'
                f'<nav aria-label="문서 버전"><a href="{self.prefix}{key}.html">현재 stable 안내</a>'
                + ''.join(items) + f'<a href="{self.prefix}history.html">버전 기록 모두 보기</a></nav></details>')


def new_tab_attributes(target: str) -> str:
    parsed = urlsplit(target)
    if parsed.scheme in {'https', 'http'} or Path(parsed.path).suffix.lower() in {'.json', '.txt', '.md', '.png', '.jpg', '.jpeg'}:
        return ' target="_blank" rel="noopener noreferrer" title="새 탭에서 열기"'
    return ''


def slug(text: str) -> str:
    value = re.sub(r"[`*_]", "", text).strip().lower()
    return re.sub(r"[^\w가-힣-]+", "-", value, flags=re.UNICODE).strip("-") or "section"


def rewrite_link(target: str, context: SiteContext) -> str:
    if target.startswith('../assets/'):
        return context.asset(target[3:])
    if target.startswith('../versions/'):
        return context.prefix + target[3:]
    if target.startswith('../../examples/'):
        return target[6:]
    if target.startswith('../../'):
        name = target[6:].split('#', 1)[0]
        if name not in {'LICENSE', 'CONTRIBUTING.md', 'VALIDATION.md'}:
            raise ValueError('unsupported repository-root document link')
        return 'https://github.com/ttaem00/cva-ttaempad-timeline-spec/blob/' + context.source_ref + '/' + target[6:]
    if target.startswith("examples/"):
        return target
    base, _, fragment = target.partition("#")
    if base in {key+'.md' for key,_,_ in context.pages}:
        return base[:-3]+'.html'+('#'+fragment if fragment else '')
    if base in LINKS:
        mapped = LINKS[base]
        return mapped + ("#" + fragment if fragment and "#" not in mapped else "")
    return target


def inline(text: str, context: SiteContext) -> str:
    # Protect complete inline code before parsing links or emphasis.
    protected: list[str] = []
    def code(match):
        protected.append("<code>" + html.escape(match.group(1)) + "</code>")
        return f"\x00{len(protected)-1}\x00"
    text = re.sub(r"`([^`]+)`", code, text)
    text = html.escape(text)
    def link(match):
        target = rewrite_link(html.unescape(match.group(2)), context)
        if urlsplit(target).scheme not in ("", "https", "http", "mailto"):
            raise ValueError("unsupported link scheme")
        return '<a href="' + html.escape(target, quote=True) + '"' + new_tab_attributes(target) + '>' + match.group(1) + '</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)
    for index, code_html in enumerate(protected):
        text = text.replace(f"\x00{index}\x00", code_html)
    return text


def image_figure(alt: str, target: str, context: SiteContext) -> str:
    """Render a local screenshot, never an embed or an editor resource."""
    # Markdown lives in docs/source; generated pages live one level above it.
    if target.startswith('../assets/'):
        target = target[3:]
    parsed = urlsplit(target)
    if (parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or
            not target.startswith('assets/') or '\\' in target):
        raise ValueError('images must be local docs/assets PNG or JPEG files')
    mapped_target = context.assets.get(target, target)
    destination = (DOCS / unquote(mapped_target)).resolve()
    if not destination.is_relative_to((DOCS / 'assets').resolve()) or destination.suffix.lower() not in {'.png', '.jpg', '.jpeg'}:
        raise ValueError('images must be local docs/assets PNG or JPEG files')
    raw = destination.read_bytes()
    if len(raw) > 20 * 1024 * 1024:
        raise ValueError('screenshot is too large')
    width = height = 0
    if destination.suffix.lower() == '.png':
        if len(raw) < 24 or raw[:8] != b'\x89PNG\r\n\x1a\n' or raw[12:16] != b'IHDR':
            raise ValueError('image is not a PNG')
        width, height = int.from_bytes(raw[16:20], 'big'), int.from_bytes(raw[20:24], 'big')
    elif raw[:2] == b'\xff\xd8':
        offset = 2
        while offset + 4 <= len(raw) and raw[offset] == 255:
            marker = raw[offset + 1]
            if marker == 255:
                offset += 1
                continue
            length = int.from_bytes(raw[offset + 2:offset + 4], 'big')
            if length < 2 or offset + 2 + length > len(raw):
                break
            if marker in {0xc0, 0xc2} and length >= 8:
                height = int.from_bytes(raw[offset + 5:offset + 7], 'big')
                width = int.from_bytes(raw[offset + 7:offset + 9], 'big')
                break
            offset += 2 + length
    if not alt.strip() or not width or not height:
        raise ValueError('image needs alternative text and valid dimensions')
    safe_target, safe_alt = html.escape(context.prefix + mapped_target, quote=True), html.escape(alt, quote=True)
    return (f'<figure class="screen-figure"><a class="image-open" href="{safe_target}" target="_blank" rel="noopener noreferrer" aria-label="{safe_alt} — 이미지 확대">'
            f'<img src="{safe_target}" alt="{safe_alt}" width="{width}" height="{height}" loading="lazy" decoding="async">'
            '</a><figcaption>이미지를 선택하면 확대합니다. 원본은 새 탭에서도 볼 수 있습니다.</figcaption></figure>')


def render_markdown(text: str, context: SiteContext, ids=None):
    lines = text.splitlines()
    output, headings, paragraph = [], [], []
    if ids is None:
        ids = {}
    index = 0
    def flush():
        if paragraph:
            output.append("<p>" + inline(" ".join(paragraph), context) + "</p>")
            paragraph.clear()
    while index < len(lines):
        line = lines[index]
        if line.startswith(":::details "):
            flush()
            title = line[len(":::details "):].strip()
            if not title:
                raise ValueError("details needs a label")
            base = slug(title); count = ids.get(base, 0); ids[base] = count + 1
            anchor = base + (f"-{count+1}" if count else "")
            body = []; index += 1
            while index < len(lines) and lines[index].strip() != ":::":
                if lines[index].startswith(":::details "):
                    raise ValueError("nested details are not supported")
                body.append(lines[index]); index += 1
            if index == len(lines):
                raise ValueError("unclosed details")
            rendered, inner_headings = render_markdown("\n".join(body), context, ids)
            headings.append((3, title, anchor)); headings.extend(inner_headings)
            output.append(f'<details class="doc-details"><summary id="{anchor}">{inline(title, context)}</summary><div class="doc-details-body">{rendered}</div></details>')
        elif line.strip() == ":::" or line.startswith(":::details"):
            raise ValueError("invalid details delimiter")
        elif line.startswith("```"):
            flush()
            language = line[3:].strip() or "text"
            body = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                body.append(lines[index]); index += 1
            if index == len(lines):
                raise ValueError("unclosed code fence")
            output.append('<div class="code-example"><span class="code-label">' + html.escape(language.upper()) +
                          '</span><pre><code>' + html.escape("\n".join(body)) + '</code></pre></div>')
        elif match := re.fullmatch(r"!\[([^\]]+)\]\(([^)]+)\)\s*", line):
            flush()
            output.append(image_figure(match[1], match[2], context))
        elif match := re.match(r"^(#{1,6})\s+(.+)$", line):
            flush()
            level, title = len(match[1]), match[2]
            base = slug(title); count = ids.get(base, 0); ids[base] = count + 1
            anchor = base + (f"-{count+1}" if count else "")
            headings.append((level, title, anchor))
            output.append(f'<h{level} id="{anchor}">{inline(title, context)}</h{level}>')
        elif line.startswith("|") and index + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[index+1]):
            flush()
            rows = []
            while index < len(lines) and lines[index].startswith("|"):
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")]); index += 1
            index -= 1
            header = '<thead><tr>' + ''.join('<th scope="col">' + inline(cell, context) + '</th>' for cell in rows[0]) + '</tr></thead>'
            body = '<tbody>' + ''.join('<tr>' + ''.join('<td>' + inline(cell, context) + '</td>' for cell in row) + '</tr>' for row in rows[2:]) + '</tbody>'
            output.append('<div class="table-scroll" tabindex="0" role="region" aria-label="가로로 이동할 수 있는 표"><table>' + header + body + '</table></div>')
        elif re.match(r"^(?:- |\d+\. )", line):
            flush()
            ordered = bool(re.match(r"^\d+\. ", line)); kind = "ol" if ordered else "ul"
            items = []
            while index < len(lines) and re.match(r"^\d+\. " if ordered else r"^- ", lines[index]):
                items.append(re.sub(r"^\d+\. " if ordered else r"^- ", "", lines[index])); index += 1
            index -= 1
            output.append(f'<{kind}>' + ''.join('<li>' + inline(item, context) + '</li>' for item in items) + f'</{kind}>')
        elif line.startswith("> "):
            flush(); output.append('<blockquote><p>' + inline(line[2:], context) + '</p></blockquote>')
        elif not line.strip():
            flush()
        else:
            paragraph.append(line.strip())
        index += 1
    flush()
    return "\n".join(output), headings


def navigation(current: str, context: SiteContext) -> str:
    parts, previous_group = [], None
    for key, label, group in context.pages:
        if group != previous_group:
            if previous_group is not None:
                parts.append('</div>')
            group_id = 'nav-' + slug(group)
            parts.append(f'<div class="nav-section" role="group" aria-labelledby="{group_id}"><p id="{group_id}" class="nav-group">{group}</p>')
            previous_group = group
        parts.append(f'<a href="{key}.html"' + (' aria-current="page"' if key == current else '') + '>' + label + '</a>')
    parts.append('</div>')
    return "\n".join(parts)


def page_template(key, label, article, headings, previous, next_page, context: SiteContext):
    toc = ''.join(f'<a class="toc-depth-{level}" href="#{anchor}">{html.escape(title)}</a>' for level, title, anchor in headings if level == 2)
    prev_next = ''.join(f'<a href="{item[0]}.html"><small>{direction}</small><span>{item[1]} {arrow}</span></a>'
                        for item, direction, arrow in [(previous, "이전 문서", "←"), (next_page, "다음 문서", "→")] if item)
    status = {'stable': 'stable', 'preview': '미리보기', 'archive': '이전 기록'}[context.status]
    if context.prefix:
        note = f'{context.version} · {status} — 보존된 당시 안내입니다.'
        if context.status == 'preview':
            note = f'{context.version} 미리보기 — 현재 stable은 {APP_VERSION}입니다.'
    else:
        note = f'{APP_VERSION} · stable 안내'
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{label} · CVA-탬패드 댓글 안내</title>
  <meta name="description" content="CVA-탬패드가 읽는 댓글 시각과 목차, 구간, 인물, 파일 형식을 예제로 설명합니다.">
  <meta name="color-scheme" content="light">
  <link rel="icon" href="{context.asset('assets/app-icon.png')}" type="image/png">
  <link rel="stylesheet" href="{context.prefix}assets/site.css">
  <script src="assets/search-index.js" defer></script><script src="{context.prefix}assets/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">본문으로 건너뛰기</a>
  <header class="site-header">
    <a class="brand" href="index.html"><img src="{context.asset('assets/app-icon.png')}" alt="" width="36" height="36"><span>CVA-탬패드<small>댓글 시간축 안내</small></span></a>
    <button class="search-open" type="button" hidden><span>문서 검색</span><kbd aria-hidden="true">/</kbd></button>
    <nav class="header-actions" aria-label="제품 링크"><a class="product-link" target="_blank" rel="noopener noreferrer" title="새 탭에서 열기" href="https://ttaem.com/brand/ttaempad">제품 소개 <span aria-hidden="true">↗</span></a><a class="store-cta" target="_blank" rel="noopener noreferrer" title="새 탭에서 열기" href="https://chromewebstore.google.com/detail/ajokeikoipagcdnpdkkbamidkjgeghon/preview?hl=ko&amp;authuser=0">Chrome 스토어 보기 <span aria-hidden="true">↗</span></a></nav>
  </header>
  <div class="site-layout">
    <aside class="sidebar">{context.version_menu(key)}<details class="nav-drawer" open><summary>문서 목차</summary><nav aria-label="문서">{navigation(key, context)}</nav><div class="sidebar-foot"><a href="https://github.com/ttaem00/cva-ttaempad-timeline-spec" target="_blank" rel="noopener noreferrer">공개 문서 저장소 ↗</a></div></details></aside>
    <main id="main" tabindex="-1"><p class="eyebrow">CVA-TTAEMPAD / COMMENT GUIDE</p><p class="version-note">{note} <a href="{context.prefix}history.html">버전 기록</a></p><article>{article}</article><nav class="page-turn" aria-label="이전 다음 문서">{prev_next}</nav><footer>원문과 의도를 보존하며, 확인한 장면을 시간축에 담습니다.<br><a href="source/{key}.md" target="_blank" rel="noopener noreferrer">이 문서의 Markdown 원본</a> · <a href="mailto:ttaem00@naver.com">문의·제보</a> · <a href="{context.prefix}policy.html">이용 정책</a></footer></main>
    <aside class="toc"><nav aria-label="현재 문서 목차"><p>이 문서에서</p>{toc}</nav></aside>
  </div>
  <dialog id="search-dialog" aria-labelledby="search-title"><form method="dialog" class="search-head"><h2 id="search-title">문서 검색</h2><button aria-label="검색 닫기">닫기</button></form><label for="search-input">찾을 내용</label><input id="search-input" type="search" placeholder="예: 들여쓰기, 괄호, 합방" autocomplete="off"><p id="search-status" role="status">단어를 입력하면 문서를 찾습니다.</p><div id="search-results"></div></dialog>
  <dialog id="image-dialog" class="image-dialog" closedby="any" aria-labelledby="image-title"><form method="dialog" class="image-head"><h2 id="image-title">이미지 확대</h2><button autofocus aria-label="이미지 닫기">닫기</button></form><div class="image-scroll"><img id="image-preview" alt=""></div><p class="image-foot"><a id="image-original" target="_blank" rel="noopener noreferrer">원본 크기로 새 탭에서 보기 ↗</a></p></dialog>
  <noscript><p class="no-script">본문과 목차는 그대로 읽을 수 있습니다. 검색은 브라우저의 페이지 찾기(Ctrl+F)를 사용하세요.</p></noscript>
</body></html>
'''


class LinkReader(HTMLParser):
    def __init__(self):
        super().__init__(); self.targets = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            if values['id'] in self.ids: raise ValueError('duplicate HTML id')
            self.ids.add(values['id'])
        for name in ('href', 'src'):
            if name in values: self.targets.append(values[name])


def validate_site():
    for source_file in DOCS.rglob('*.html'):
        key = source_file.relative_to(DOCS).as_posix(); parser = LinkReader()
        parser.feed(source_file.read_text(encoding='utf-8'))
        for target in parser.targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc: continue
            destination = (source_file.parent / unquote(parsed.path)).resolve() if parsed.path else source_file
            if not destination.is_relative_to(DOCS): raise ValueError('link outside deployed docs directory')
            if not destination.exists(): raise ValueError(f'missing local link: {key}: {target}')
            if parsed.fragment and destination.suffix == '.html':
                dest_parser = LinkReader(); dest_parser.feed(destination.read_text(encoding='utf-8'))
                if unquote(parsed.fragment) not in dest_parser.ids: raise ValueError(f'missing fragment: {key}: {target}')


def verify_history():
    """Do not turn a normal rebuild into an edit of a preserved release."""
    if VERSIONS['authoringVersion'] != APP_VERSION:
        raise ValueError('authoring version differs from stable; promote explicitly')
    versions = VERSIONS['versions']
    if len({r['version'] for r in versions}) != len(versions):
        raise ValueError('duplicate guide version')
    if [r['version'] for r in versions if r['status'] == 'stable'] != [APP_VERSION]:
        raise ValueError('exactly one stable version is required')
    for release in versions:
        version = release['version']
        if not re.fullmatch(r'\d+\.\d+\.\d+', version) or release['status'] not in {'stable', 'preview', 'archive'}:
            raise ValueError('invalid version metadata')
        base = HISTORY / version
        integrity = json.loads((base / 'integrity.json').read_text(encoding='utf-8'))
        files = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} - {'integrity.json'}
        if integrity['version'] != version or files != set(integrity['files']):
            raise ValueError('preserved version inventory changed')
        for name, digest in integrity['files'].items():
            if hashlib.sha256((base / name).read_bytes()).hexdigest() != digest:
                raise ValueError(f'preserved version changed: {version}/{name}')
        assets = json.loads((base / 'assets.json').read_text(encoding='utf-8'))
        for target in assets.values():
            if not re.fullmatch(r'assets/versioned/[0-9a-f]{64}\.(png|jpg|jpeg)', target):
                raise ValueError('invalid preserved image path')
            if hashlib.sha256((DOCS / target).read_bytes()).hexdigest() != Path(target).stem:
                raise ValueError('preserved image changed')


def build_pages(source: Path, output: Path, context: SiteContext):
    output.mkdir(parents=True, exist_ok=True)
    search = []
    for index, (key, label, _) in enumerate(context.pages):
        text = (source / (key + '.md')).read_text(encoding='utf-8')
        article, headings = render_markdown(text, context)
        rendered = page_template(key, label, article, headings, context.pages[index-1] if index else None,
                                 context.pages[index+1] if index+1 < len(context.pages) else None, context)
        (output / (key + '.html')).write_text(rendered, encoding='utf-8', newline='\n')
        source_copy = output / 'source' / (key + '.md')
        if source_copy.resolve() != (source / (key + '.md')).resolve():
            source_copy.parent.mkdir(parents=True, exist_ok=True)
            source_copy.write_text(text, encoding='utf-8', newline='\n')
        search.append({'title':label, 'url':key+'.html', 'text':re.sub(r'[`#*_]', '', text)})
        for level, title, anchor in headings:
            if level in (2, 3): search.append({'title':label+' · '+title,'url':key+'.html#'+anchor, 'text':title})
    (output / 'assets').mkdir(exist_ok=True)
    (output / 'assets/search-index.js').write_text('window.DOC_SEARCH = '+json.dumps(search,ensure_ascii=False).replace('<','\\u003c')+';\n',encoding='utf-8',newline='\n')


def copy_examples(source: Path, output: Path):
    for example in source.rglob('*'):
        if example.is_file():
            destination = output / 'examples' / example.relative_to(source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(example.read_bytes().replace(b'\r\n', b'\n'))


def main():
    verify_history()
    rows = []
    for release in VERSIONS['versions']:
        version = release['version']
        description = {'preview': '다음 버전 기능을 먼저 살펴보는 미리보기', 'stable': '기본 안내의 기준 버전',
                       'archive': '당시 작성된 이전 안내'}[release['status']]
        rows.append(f'| [{release["label"]}](../versions/{version}/index.html) | {description} |')
    history = ('# 버전 기록\n\n기본 문서는 **'+APP_VERSION+' stable**을 기준으로 읽습니다. '
               '다른 버전은 왼쪽 버전 메뉴에서 고를 수 있습니다.\n\n| 버전 | 안내 |\n|---|---|\n'
               + '\n'.join(rows) + '\n\n이전 안내의 본문·예제·이미지는 당시 모습으로 보존합니다. '
               '미리보기의 기능은 현재 stable 안내와 구분합니다.\n')
    (SOURCE / 'history.md').write_text(history, encoding='utf-8', newline='\n')
    stable_assets = json.loads((HISTORY / APP_VERSION / 'assets.json').read_text(encoding='utf-8'))
    root_pages = PAGES + [('history', '버전 기록', '더 알아보기')]
    build_pages(SOURCE, DOCS, SiteContext(APP_VERSION, 'stable', root_pages, '', stable_assets))
    copy_examples(ROOT / 'examples', DOCS)  # Keep already shared public JSON URLs valid.
    for release in VERSIONS['versions']:
        version = release['version']; preserved = HISTORY / version
        pages = [p for p in PAGES if (preserved / 'source' / (p[0] + '.md')).exists()]
        integrity = json.loads((preserved / 'integrity.json').read_text(encoding='utf-8'))
        context = SiteContext(version, release['status'], pages, '../../',
                              json.loads((preserved / 'assets.json').read_text(encoding='utf-8')), integrity['sourceCommit'])
        destination = DOCS / 'versions' / version
        build_pages(preserved / 'source', destination, context)
        copy_examples(preserved / 'examples', destination)
    (DOCS / '.nojekyll').write_bytes(b'')
    validate_site()
    artifact_paths = [p for p in DOCS.rglob('*') if p.is_file() and p.name != 'build-manifest.json']
    manifest = {'format':'cva-ttaempad.reading-site.v2','documentVersion':'0.4','consumer':APP_VERSION,
                'pages':len(root_pages), 'versions':[r['version'] for r in VERSIONS['versions']],
                'generated':{p.relative_to(ROOT).as_posix():hashlib.sha256(
                    p.read_bytes().replace(b'\r\n', b'\n') if p.suffix in {'.json', '.js', '.md', '.html', '.css', '.txt'}
                    else p.read_bytes()).hexdigest() for p in sorted(artifact_paths)}}
    (DOCS/'build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'Reading site build and local links PASS; {len(root_pages)} stable pages; {len(VERSIONS["versions"])} preserved versions')


if __name__ == '__main__':
    main()
