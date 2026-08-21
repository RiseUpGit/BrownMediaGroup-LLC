# mattpocock/skills — Adaptation Session 2026-08-21

## Repo
`mattpocock/skills`
https://github.com/mattpocock/skills

## Scanned
2026-08-21

## What It Is
229K-star MIT skill framework for Claude Code / Codex / Hermes. 111 `.md` files covering engineering workflows: grilling interviews, spec synthesis, ticket breakdown, architecture review, triage, TDD, bug diagnosis.

## Why It Matters For BMG
- `/grill-with-docs` and `/to-spec` directly replace ad-hoc brainstorming with structured alignment
- `/to-tickets` gives tracer-bullet vertical slices with blocking edges — better than our PEND-XX table
- `/improve-codebase-architecture` generates HTML reports for code reviews on AI-Tracker + BrainStorm
- `/diagnosing-bugs` 4-phase loop is more disciplined than our current systematic-debugging
- `/triage` replaces manual todo state management with a proper state machine

## Verdict
Adopt — 8 engineering skills ported and patched for Hermes/BMG stack.

## Patches Applied
- Claude Code / Codex → Hermes
- `/setup-matt-pocock-skills` → `/setup-brownmediagroup-skills`
- Issue tracker → GitHub Issues via MCP + `.secure/todo.md`
- Ask Matt → Ask Newton
- Removed Claude Code plugin marketplace references

## Locations
- Canonical: `D:/BrownMediaGroup/dev/brownmediagroup/skills/engineering/`
- Team: `G:/BrownMediaGroup/ops/team/skills/engineering/`
- Sync: `D:/BrownMediaGroup/dev/brownmediagroup/skills/sync-team.py`

## Skills Adapted
1. grill-with-docs
2. to-spec
3. to-tickets
4. improve-codebase-architecture
5. triage
6. tdd
7. diagnosing-bugs
8. ask-matt (renamed ask-newton)

## Notes
- mattpocock/skills is MIT — no license barrier
- 1559KB repo, actively maintained (pushed 2026-08-21)
- Did not port all 111 skills — cherry-picked engineering-relevant ones only
- `CONTEXT.md` and `ADR` conventions from upstream can be mapped to BMG `quick-reference.md` and `docs/` folders
