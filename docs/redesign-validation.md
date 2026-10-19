# Redesign validation — 2026-10-18

## Implemented

- Nine buildless HTML pages: Home, Projects, Experience, Research, Contact, and four project overviews.
- Shared warm-neutral/blue design, system typography, conceptual SVG illustrations, light/dark themes, mobile navigation, and project category filters.
- Static content remains available without JavaScript. Theme selection follows system preference initially and persists an explicit choice when storage is available.
- Existing CV and research download paths remain unchanged. Legacy academic homepage anchors resolve to Research, with visible fallback links when JavaScript is unavailable.
- No new dependencies or build requirements. GitHub Pages settings have not been changed; nothing has been deployed.

## Preservation checks

- 10 professional roles; four education/visiting-scholar entries; four research projects; 13 publication/proceedings entries; seven conference presentations.
- Original citation text, presentation text, full research descriptions, and non-CCR role contributions were compared against the original HTML with whitespace normalized.
- The owner approved replacing conflicting CCR claims with the brief’s high-level partial-prototype description. Original CCR wording is retained in a private local review document outside the deployment source.
- Both original CV PDFs, all three research PDFs, certificate image, and legacy image/font assets remain present.

## Automated and browser checks

- `python3 scripts/validate-site.py`: all nine pages passed local routes, anchors, assets, metadata, unique IDs, archive-count and download checks.
- Both active JavaScript files passed `node --check`; changes passed `git diff --check`.
- Theme text tokens meet WCAG AA against both backgrounds/surfaces: minimum contrast 5.33:1 in light mode and 6.91:1 in dark mode.
- Headless Chrome checked all nine routes at 1440, 768, 390, and 320 CSS pixels: no horizontal overflow detected.
- No JavaScript exceptions or local HTTP errors were observed during the final browser run.
- Browser interaction checks passed mobile menu expansion, Escape-key focus return, cross-page theme persistence, project filtering, and the legacy publications-anchor redirect.
- Desktop/mobile light screenshots and dark Research screenshots were visually inspected.

## External links and pending review

An HTTP HEAD check covered 17 unique external profile/scholarly links. Eleven returned 200, five returned 403, and one returned 404. A 403 response does not establish that a link is broken; access may be restricted for automated requests. Original URLs were preserved.

- Returned 404: `http://www.gel.org.br/ProgramacaoFinal2015.php#tab2` (2015 GEL presentation abstract).
- Returned 403: Academia profile, both Academia posters, ResearchGate profile, and the ExpOrtLi WordPress abstract PDF.

Please verify those destinations manually or supply approved replacements. No replacement URLs have been invented.

Editorial items remain: verification and disclosure approval for projects 2 and 3; confirmation of existing “current” role dates and the external-sandhi project’s status; primary CV selection; verified GitHub profile URL. The current CV download remains `arthuCV.pdf`.

Actual GitHub Pages deployment and manual assistive-technology testing remain unverified.

## Original-template homepage preview

At the owner’s request, the homepage now reuses the original Material CV styles, portrait card, sidebar navigation, profile links, and experience timeline. Featured project descriptions and status notes remain, with plain section headings and no project illustrations on the homepage. The interior pages are unchanged pending approval of this direction.

The homepage retains system-default/persistent theme behavior and keyboard navigation. The full static validator and 36 route/viewport browser checks passed during this revision, including mobile menu/Escape focus, cross-page themes, filters, and legacy archive redirects. No JavaScript exceptions or local HTTP errors were observed. Desktop, tablet, mobile, and dark-theme homepage screenshots were reviewed; the original diagonal portrait border was adjusted to avoid text overlap and dashed rendering artifacts.

## Light-only update

At the owner’s request, all nine pages now use light mode only. Theme controls, initialization script references, preference persistence, and dark-mode CSS were removed. The earlier theme checks above describe the previous version. Navigation, project filtering, and archive redirects remain in the active script.

## Updated CV

The owner replaced `arthuCV.pdf` and removed `arthursantanaCV2025.pdf`. All 10 active CV links point to the replacement PDF with content-hash cache version `fe2b93e1adfd`. The validator now checks the current CV rather than requiring the removed historical copy.
