# China Council of Lions Clubs Constitution Skill (`lions-clubs-constitution`)

> **GitHub Description**: China Council of Lions Clubs (CCLC) official constitution Agent Skill (multilingual · portable): built from six official documents — Charter, Working Rules, Financial Management System, Membership Fee Measures, Member Code of Conduct, and Visual Identity Manual A/B — providing clause lookup, compliance review, fee guidance, VI rules, and document drafting. Covers 18 languages (Hong Kong/Macau/Taiwan, Japanese, Korean, Russian, English, French, German, Spanish, Portuguese, Arabic, Vietnamese, Thai, Indonesian, Filipino, Burmese, Kazakh, Uzbek, Swahili). Works on DSH / OpenClaw / Hermes / WorkBuddy / Doubao Work / Qwen Work. Maintained by: Jingwei Service Team, YU Haifeng (Lion Brother).
>
> **Version**: v1.0.0 ｜ **Created**: 2025-09-28 ｜ **Maintainer**: Jingwei Service Team, YU Haifeng (Lion Brother)
>
> An official-attributed, portable Agent Skill for the China Council of Lions Clubs, built from the federation's official foundational documents ("constitution"), providing clause lookup, compliance review, and document drafting for every service team, every member, and every kind of agent.
>
> **Skill standard**: follows the **Anthropic Agent Skills** standard (directory-based skill with `SKILL.md` containing YAML frontmatter).
> **Authoritative source (official)**: official documents of the China Council of Lions Clubs. Copyright of the documents belongs to the **China Council of Lions Clubs**; the official originals prevail.
> **License**: MIT (with a special notice on official-document copyright; see `LICENSE`).

## What this is

`lions-clubs-constitution` is a portable **Agent Skill** (compatible with the Anthropic Agent Skills format) that turns the six official CCLC documents ("the constitution") into a knowledge base and workflow an AI agent can directly reference:

| Official document | Version | In this skill |
| --- | --- | --- |
| Charter of the China Council of Lions Clubs | Approved by the Ministry of Civil Affairs 2021-10-15 | `references/章程.md` |
| CCLC Working Rules | Current | `references/工作规则.md` |
| CCLC Financial Management System | Revised 2023-04-25 | `references/财务管理制度.md` |
| CCLC Membership Fee Measures | Effective 2023-07-01 | `references/会费收取办法.md` (transcribed + original page images) |
| CCLC Member Code of Conduct | Current | `references/会员行为准则.md` |
| CCLC Visual Identity Manual A / B | Current | text + `assets/vis/` all page images |

## Directory structure

```
lions-clubs-constitution/
├── SKILL.md                      # Main skill file (agent entry point)
├── README.md                     # Chinese README
├── README.en.md                  # English README
├── LICENSE                       # MIT + official-document copyright notice
├── references/                   # Official documents as text (authoritative)
│   ├── 章程.md                   #   Charter (full)
│   ├── 工作规则.md               #   Working Rules (12 chapters)
│   ├── 财务管理制度.md           #   Financial System (23 chapters)
│   ├── 会费收取办法.md           #   Fee Measures (12 clauses) + quick table
│   ├── 会员行为准则.md           #   Member Code of Conduct (18 articles)
│   ├── VI手册A.md                #   VI Manual A (index)
│   ├── VI手册B.md                #   VI Manual B (representative offices)
│   ├── VI规范文字版.md           #   VI rules as text (geometry/color/prohibitions)
│   ├── templates.md              #   6 official document templates
│   ├── 路由索引.md               #   topic → source routing table
│   ├── manifest.md               #   source manifest (all 7 docs covered)
│   └── assets/会费办法/          #   original fee-measures page images
├── assets/vis/manualA|manualB/   # VI Manual all page images (A 23 + B 32 + zoom)
├── i18n/                         # Multilingual reference cards (18 languages)
│   ├── README.md                 #   region → language matrix & usage
│   ├── generate_summaries.py      #   card generator (shared facts, consistent numbers)
│   └── <zh-Hant|en|ja|ko|ru|fr|de|es|pt|ar|vi|th|id|tl|my|kk|uz|sw>/
│       └── summary.md            #   core reference card in that language
└── scripts/
    └── search_clauses.py         # clause search script
```

## Capabilities (tasks an agent can do)

1. **Clause Q&A** — answer with the clause cited as "per《X》Article Y".
2. **Compliance review** — 5-step check for activities/fundraising/PR/finance; output "pass / revise / reject" list.
3. **Service-team guidance** — team setup (25 founders), rotation (Mar–Apr general meeting, captain team ≤13), meetings, approval flow.
4. **Fee guidance** — entry/annual/transfer fee standards, deadlines, late consequences, remittance rules.
5. **VI review** — logo usage, combination rules, prohibited forms; conclude "usable / needs fix / unusable" with the manual page cited.
6. **Document drafting** — notices, membership/transfer applications, activity plans, finance notes, recommendation reports.
7. **Multilingual** — 18 language cards under `i18n/`; the agent auto-loads the user's language; final judgments defer to the Chinese official original.

## Install & invoke

### Option A: As a DSH / Anthropic Agent Skill
Place the `lions-clubs-constitution/` directory into the agent's skills directory (e.g. `~/.claude/skills/` or the DSH session skill dir). The agent auto-loads `SKILL.md` when a Lions-related intent is detected.

### Option B: Any agent / workflow
Mount this directory as a knowledge base; instruct the agent to read `SKILL.md` first, then search `references/` per its guide. Use `scripts/search_clauses.py` to locate clauses fast:

```bash
python3 scripts/search_clauses.py 会费
python3 scripts/search_clauses.py 服务队 工作规则
python3 scripts/search_clauses.py 标识 会员行为准则
```

### Option C: GitHub / SkillHub
Keep `SKILL.md` at the skill root so most platforms recognize it. Suggested topics/tags: `lions`, `lions-clubs`, `china-lions`, `ngo`, `constitution`, `governance`, `compliance`, `agent-skills`.

## Multi-agent platform support

Open directory structure, vendor-neutral. General rule: hand the skill directory to the agent with the note "when a Lions-related request appears, read `SKILL.md` first, then search `references/` per its guide".

| Agent / Platform | How to load | Entry | Note |
| --- | --- | --- | --- |
| **Deepseek Harness (DSH)** | session skill dir, or `skill` tool loads `lions-clubs-constitution` | `SKILL.md` | auto-loads on intent |
| **OpenClaw** | as Agent Skill / knowledge pack | `SKILL.md` | supports SKILL.md standard |
| **Hermes** | as skill dir or RAG knowledge base | `SKILL.md` + `references/` | use `search_clauses.py` |
| **WorkBuddy** | as workflow skill / knowledge source | `SKILL.md` | templates in `templates.md` |
| **Doubao Work (ByteDance)** | enterprise knowledge base / skill import | `SKILL.md` | ready in Chinese |
| **Qwen Work (Alibaba)** | assistant knowledge base / plugin import | `SKILL.md` + `references/` | large docs via search script |

## Usage principles (for the agent)

1. **Look up the clause before answering**, and cite the basis.
2. **Verify numbers** (amounts, counts, deadlines) word-for-word against `references/`.
3. **Admit out-of-scope** items and point to the CCLC secretariat / representative office.
4. **Conclude VI checks** as usable / needs fix / unusable, and name the violation.

## Officialness statement

- This skill is an **assistive tool compiled by Jingwei Service Team, YU Haifeng (Lion Brother)** from the CCLC official foundational documents; it is **not** an official software product of the federation. Its authority comes from the included official documents; the official originals prevail.
- It follows the **Anthropic Agent Skills** standard and is freely distributable across the platforms above; when distributing, keep the version/author/official-source header in `SKILL.md` and the `LICENSE`.
- Included documents are copyrighted by the **China Council of Lions Clubs** and are for internal study, meeting, and compliance assistance only; the visual identity (lion emblem, etc.) is governed by the VI Manual and **must not be used commercially** (Member Code of Conduct, Article 8).
- If the official documents are updated, follow the latest approved version and bump the semantic version `MAJOR.MINOR.PATCH`.

---

**Maintainer: Jingwei Service Team, YU Haifeng (Lion Brother) ｜ Version v1.0.0 ｜ Created 2025-09-28**
