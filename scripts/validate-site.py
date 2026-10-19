#!/usr/bin/env python3
"""Validate buildless GitHub Pages routes, anchors, assets, and archive counts."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = []
        self.refs = []
        self.h1 = 0
        self.description = False
        self.canonical = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = bool(attrs.get('content'))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = True
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])

pages = {p.resolve(): Page(p) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
errors = []
for path, page in pages.items():
    label = path.relative_to(ROOT)
    if page.h1 != 1 or not page.description or not page.canonical:
        errors.append(f'{label}: requires one h1, description, and canonical URL')
    for ident, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f'{label}: duplicate ID {ident}')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = (ROOT / unquote(url.path).lstrip('/') if url.path.startswith('/')
                  else path.parent / unquote(url.path)) if url.path else path
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.exists():
            errors.append(f'{label}: missing {ref}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{label}: missing anchor {ref}')

research = (ROOT / 'research/index.html').read_text()
experience = (ROOT / 'experience/index.html').read_text()
if research.count('class="archive-entry"') != 8:
    errors.append('Research must preserve four education entries and four research projects')
if len(re.findall(r'<li>\s*<p>', research)) != 20:
    errors.append('Research must preserve 13 publications and seven presentations')
if experience.count('class="experience-entry"') != 10:
    errors.append('Experience must preserve all 10 roles')
for name in ('arthuCV.pdf', 'docs/Santana 2019.pdf',
             'docs/poster-glow.pdf', 'docs/exportli2018.pdf', 'Certificado_Let’s_Code (1).jpg'):
    if not (ROOT / name).is_file():
        errors.append(f'Missing preserved download: {name}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(pages)} pages; metadata, unique IDs, local routes, anchors, assets, archive counts, and preserved downloads.')
