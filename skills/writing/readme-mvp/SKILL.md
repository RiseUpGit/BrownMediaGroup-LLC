# README MVP — Front Page Fill

**Write a public-facing README.md front page for any BrownMediaGroup repo in MVP style.**

Use when the user asks to "fill out the README", "write a front page", "make the repo look decent on GitHub", or when a new/empty repo needs its first public-facing markdown file. Covers both active-code repos and placeholder/public repos.

## Output Shape

Every README MVP follows this order:

1. **Title** — repo name, one line
2. **Owner / Status / Last updated** — BrownMediaGroup / Joe Brown, active state, date
3. **What It Is** — 2-4 sentences on what the project actually does, from the user's perspective
4. **Architecture / Tech Stack** — brief diagram or bullet list of the actual stack
5. **Build / Install** — the exact commands Joe uses on this machine, not generic instructions
6. **Current Status / Version** — what's working, what's next, exact version number if applicable
7. **Related Projects** — links to sibling BMG repos
8. **License** — Proprietary / MIT / whatever applies

## Rules

- **Family-first framing** for BrownMediaGroup-LLC and any public-facing repo
- **Brand palette** only if the README renders on a website; GitHub-flavored markdown only needs text
- **No self-congratulatory lines** unless the user explicitly requests that tone
- **No proprietary details in public repos**: open-source stack facts only (Tauri, Rust, llama.cpp, etc.). Keep Sam internals, agent orchestration, model names, and product logic out of public READMEs
- **One repo, one README**: do not create README duplicates across paths. If a stale README exists in a stale folder, ignore the stale folder
- **MVP means actionable, not exhaustive**: 50-120 lines. The user can expand later
- **Verification**: after writing, `git add README.md && git commit && git push` immediately. Do not batch README commits

## Public vs Private Repo Rules

**Public repos** (RiseUp-1, Starbeam, BrownMediaGroup-LLC):
- Family-owned/family-operated framing
- No internal tooling details (no Sam, no Newton, no Hermes references)
- Model/agent-agnostic language
- Revenue pillars if describing the business: (1) repair/recurring support, (2) YouTube funnel, (3) software products, (4) licensing/affiliates

**Private repos** (BrainStorm, Sam-Agent, FCHT-Agent):
- Full technical detail allowed
- Architecture diagrams, tool lists, version numbers
- Build instructions specific to Black Beauty hardware

## Canonical Source

Brand palette and family details live in `F:/obsidian/black beauty/BrownMediaGroup/Brand Assets.md`. Always check it before writing public-facing copy.

## Commit Message Convention

```
docs: MVP front-page README for <repo-name>
```

Push immediately after commit via post-commit hook or manual `git push`.

## Pitfalls

- Do not leave a placeholder README ("# Project", "Coming soon") — fill it out or don't commit it
- Do not copy the same README across repos — each repo gets content specific to its actual code
- Do not include Windows-specific paths in public READMEs (C:/Users/Joe Brown/...)
- Do not mention Tauri: MSSA / MSI build internals in public repos unless the user approves
- For repos with no code yet, write what the project *will* do, not what it currently does
