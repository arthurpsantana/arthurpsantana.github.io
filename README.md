# Arthur Santana — technical portfolio

A buildless, static portfolio for GitHub Pages. Pages are plain HTML; the shared design system is in `stylesheets/portfolio.css`. Navigation, filtering, and legacy anchor handling use small scripts in `javascript/`.

The homepage currently previews a return to the original Material CV template. It uses the existing Bootstrap, Materialize, Font Awesome, and `style_dark_gray.css` assets with `stylesheets/template-home.css` for responsive layouts and accessibility. The homepage menu has been removed; visitors use the section links to open the full pages. It reuses the archive-redirect script without loading the original template's JavaScript plugins. Interior pages retain the previous redesign pending visual approval.

## Local preview

From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Use an HTTP server: root-relative routes and assets are intended for the existing `arthurpsantana.github.io` domain.

## Validation

```sh
python3 scripts/validate-site.py
node --check javascript/portfolio.js
```

The validator checks all HTML pages for local links, anchors, assets, page metadata, unique IDs, archive counts, and preserved downloadable resources. Before publication, also review the desktop and mobile layouts, keyboard navigation, filters, external scholarly links, and editorial copy.

## Editing and deployment

There is no dependency installation or build step. Serve the repository root with GitHub Pages; `.nojekyll` keeps the static files unchanged. The existing repository's Pages source/branch setting must be confirmed in GitHub before publication. This redesign does not change those settings or publish automatically.

- Top-level pages: `index.html`, `projects/`, `experience/`, `research/`, `contact/`.
- Case studies: individual directories under `projects/`.
- Shared header and footer markup is repeated across nine HTML pages; keep those copies synchronized when editing navigation.
- Update `sitemap.xml` when adding or removing a public page.
- Keep existing PDF and image paths stable. The current CV is `arthuCV.pdf`; all research downloads remain in place. CV links include a content-hash version parameter to avoid serving an older cached copy. Refresh that parameter when replacing the PDF.
- Legacy academic homepage anchors redirect to the Research archive when JavaScript is available and retain visible destination links otherwise.
- Legacy theme assets are retained for migration traceability but are not loaded by the redesigned pages.

## Editorial status

The approved brief is currently `website-redesign.md` in the repository root, although `AGENTS.md` references `docs/website-redesign.md`.

Project 2 now provides an owner-supplied, high-level description of conversational voice-agent evaluation, without client identifiers, real conversations, operating procedures, or internal reports. Project 3 now describes the owner-provided rubric-design and evaluation contributions at a high level; detailed methods, comparative findings, and disclosure approval remain pending. Project 2 describes evaluation of an existing deployed agent, without claiming authorship or responsibility for its deployment. Project 3 does not claim production deployment. The Multi-LLM Framework is described as a confidential partial prototype, using the approved public scope. The owner approved replacing the conflicting CCR experience description; the original copy is retained outside this repository for private review.

Role dates, “current” labels, external-sandhi project status, original scholarly citations, and existing CV selection are preserved. Confirm their currency before making factual updates. A GitHub profile link has not been added because none was verified in the original site.

The owner has requested light mode only. Dark-mode controls, stored preference handling, and system dark-mode styles have been removed from all pages.
