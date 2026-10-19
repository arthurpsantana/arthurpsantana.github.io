# Website redesign brief — Arthur Santana

## Purpose
Redesign https://arthurpsantana.github.io/ as a balanced technical portfolio at the intersection of computational linguistics, applied AI engineering, LLM evaluation, and linguistic research. Audience: AI/NLP recruiters, technical hiring managers, researchers, and potential consulting clients.

This is a content-preserving redesign, not permission to invent or discard material. Inspect the repository as the source of truth for existing roles, dates, publications, conference presentations, projects, links, and assets. Ask for confirmation before changing factual claims.

## Approved visual direction
- Contemporary Research × Technology: editorial sophistication paired with modern engineering portfolio conventions.
- Warm off-white/light neutrals with restrained blue accents; coordinated deep-charcoal dark theme.
- Light/dark toggle; honor system preference on first visit, persist explicit selection.
- Statement-first homepage, generous whitespace, clear hierarchy, subtle borders, minimal motion.
- Suggested fonts (not mandatory): Newsreader for editorial headings, Inter for body/UI, IBM Plex Mono for small technical labels. Check licensing and performance; use sensible fallbacks.
- Avoid neon AI clichés, heavy gradients, glassmorphism, stock robots, distracting animations.
- Illustrate project cards with original, abstract SVGs or simple conceptual diagrams; avoid suggesting they reproduce NDA-protected architectures.

### Initial color tokens (proposals, tune for accessibility)
Light: background #F7F7F4, surface #FFFFFF, text #22272B, secondary text #59636C, accent #3867A8.
Dark: background #161B22, surface #222A35, text #F2F4F6, secondary text #AAB5C2, accent #83B5FF.
Use CSS variables / design tokens and verify contrast in both themes.

## Information architecture
Multi-page site with shared responsive navigation:
- Home (`/`)
- Projects (`/projects/`) and individual case-study pages
- Experience (`/experience/`)
- Research (`/research/`)
- Contact (`/contact/`)
Routes are proposed; adapt to the existing framework and GitHub Pages setup. Avoid broken links; preserve old URLs with redirects or compatible anchors where possible.

### Homepage
1. Navigation with name/brand, page links, and theme toggle.
2. Statement-first hero:
   - Eyebrow: `Arthur Santana, Ph.D. · Computational Linguist` (verify preferred public name against existing site)
   - Approved headline: **Building and evaluating intelligent language systems.**
   - Proposed supporting copy (editable): `I combine computational linguistics, NLP engineering, and systematic AI evaluation to develop more reliable language technologies.`
   - Primary CTA: View Projects. Secondary: Download CV or Contact.
3. Four featured project cards, in this order:
   1. Multi-LLM Collaboration Framework
   2. Conversational AI Quality & Failure Analysis
   3. Automated Competency Mapping & Assessment
   4. Brazilian Portuguese Speech & Phonology
4. Expertise: AI/NLP engineering; AI evaluation & quality; speech and linguistic research.
5. Compact professional highlights with link to Experience.
6. Research highlights / selected publications with link to Research.
7. Contact links and footer.
Do not replicate the full CV or full publication list on the homepage.

### Projects
A browsable portfolio with category filters if straightforward and accessible: AI Engineering & NLP, AI Evaluation & Quality, Linguistic Research. Each card has title, short summary, category, optional verified tags, and link to a dedicated case study. Avoid fake buttons or nonworking filters.

Case-study template:
- Title and short summary
- Context / challenge
- My role and verified contributions
- Technical or methodological approach (only publicly shareable information)
- Results / insights / limitations (only verified claims)
- Artifacts / links (only approved, public resources)
- Optional status note distinguishing prototype, implemented, designed, or proposed work

#### Project 1: Multi-LLM Collaboration Framework
**Confirmed:** Task-agnostic framework coordinating outputs from multiple LLMs. An aggregator evaluates and synthesizes candidate responses using predefined rubrics. Hallucination-checking stages contribute quality control. Current aggregator does not send feedback for additional generation rounds. Partial implementation/prototype, developed in client context, NDA-protected. No code/public source access and no permission to disclose proprietary details.

Safe public-facing summary proposal: `A task-agnostic multi-LLM collaboration approach that evaluates candidate responses against predefined rubrics and synthesizes a consolidated output, with hallucination checks supporting quality assurance.`

Do not depict a purported exact internal architecture, disclose prompts, reproduce internal evaluation criteria, name clients, or claim comparative improvements without verified data. Conceptual, non-proprietary illustrations only. The project is **not** specifically a lesson-plan generator; educational content was one application context. Do not call it a multi-agent system without confirmation.

#### Project 2: Conversational AI Quality & Failure Analysis
Candidate case study about voice/conversational AI evaluation, recurring failure patterns, intent classification, and overtriggering of account-holder support rules. Client work: publication permissions, exact contributions, methods, metrics, and examples are **not yet verified**. Draft conservatively; use no real conversations, customer data, or client identifiers. Require editorial approval before publication.

#### Project 3: Automated Competency Mapping & Assessment
Candidate case study about comparing educational competency frameworks, structured rubric-based equivalence/coverage analysis, and AI-assisted assessment. Implementation extent, ownership, metrics, and disclosure permissions are **not yet verified**. Do not claim deployed automation or disclose client-owned rubrics without approval.

#### Project 4: Brazilian Portuguese Speech & Phonology
Research-focused entry linking to the detailed Research page and individual existing research projects. Preserve precise topics, citations, links, and scholarly distinctions from the current website. Do not invent findings.

### Experience
Preserve **all** existing professional roles, organizations, dates, and factual details. Present reverse-chronological entries with role, organization, dates, short summary, and verified contributions. Link to relevant case studies where appropriate. Retain meaningful technical detail but improve scanning. Education can be summarized here and expanded under Research.

### Research
Preserve the **complete academic archive**, including existing research projects, journal articles, book chapters, conference proceedings/presentations, coauthors, venues, dates, and URLs. Group material by type and/or year; make long lists browsable with accessible headings, filters, or disclosure controls. Include academic background and visiting scholar experience as supported by the existing site. Do not lose citation details or public document links.

### Contact
Simple email, LinkedIn, GitHub, and downloadable CV using verified existing URLs. No contact form required. Do not invent addresses or profile links.

## Responsive / accessibility / performance
- Desktop and mobile layouts; no horizontal overflow; readable typography and generous tap targets.
- Semantic headings, visible focus states, accessible navigation, meaningful link labels, proper alt text.
- Theme contrast testing, reduced-motion support, keyboard-operable menus and filters.
- SEO title/description per page, Open Graph metadata if practical, canonical URLs, sensible sitemap.
- Avoid heavy JS for static content; optimize fonts and assets.

## Implementation phases
**Phase 0 — Audit:** Inspect repo and inventory content/assets/routes. Identify stack, GitHub Pages deployment, existing URLs, and risks. Present plan for approval. Do not start major rewrite before approval.

**Phase 1 — Foundations:** Shared layout, design tokens, typography, header/footer, responsive navigation, light/dark theme.

**Phase 2 — Homepage:** Implement approved headline, curated sections, and four featured cards with temporary editorial-review markers where details are unverified.

**Phase 3 — Interior pages:** Projects index and case-study structure, Experience, Research archive, Contact. Migrate all existing content accurately.

**Phase 4 — Polish and QA:** Validate content completeness, links, mobile layouts, accessibility, theme behavior, build/deployment, SEO, and regressions.

## Acceptance criteria
- Site deploys correctly to the existing GitHub Pages address.
- All five top-level destinations work, with functional project pages and mobile navigation.
- Theme toggle works and both themes are readable.
- All four selected projects appear on homepage and Projects page.
- No confidential materials or unverified claims are published.
- All existing experience entries, research projects, publications, and conference presentations remain accessible.
- Existing public URLs and CV download continue working, or have intentional replacements.
- Responsive, keyboard-accessible, and no obvious broken links or console errors.

## Open editorial decisions — do not guess
- Exact existing role descriptions, chronology, publications, links, and preferred display name: verify in repository.
- Publicly approved copy and evidence for professional client case studies 2 and 3.
- Whether any case study can include outcomes, diagrams, or anonymized examples.
- Whether existing site architecture supports the proposed routes directly.
- Whether a current CV PDF should be preserved or separately updated.

## Initial instruction to Codex
`Read AGENTS.md and docs/website-redesign.md. Audit the current repository and list all existing content, routes, assets, and deployment constraints. Propose a phased redesign plan that preserves the complete academic archive and professional history. Identify any missing information or confidentiality risks. Do not begin major implementation until I approve the plan.`
