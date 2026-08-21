# External Skill Repo Adaptation

**Adapt external engineering skill repos (like mattpocock/skills) to the BrownMediaGroup/Hermes stack.**

Use when the user asks to "check out", "adapt", "port", or "use skills from" an external skill repository. Covers download, patch, dual-write to canonical + team folders, and skill registration.

## Workflow

### 1. Evaluate the external repo
- Check license (MIT/Apache = safe; GPL/copyleft = flag for user)
- Check star count and activity (pushed_at) for maintenance signal
- Read the README to understand the skill taxonomy and trigger model
- List all `.md` skill files before downloading

### 2. Download
- Create `D:/BrownMediaGroup/dev/brownmediagroup/skills/<category>/` if it doesn't exist
- Download each `SKILL.md` to its own subfolder matching the source structure
- Example: `skills/engineering/grill-with-docs/SKILL.md`

### 3. Patch for BMG stack
Required patches for every skill from an external repo:
- Replace Claude Code / Codex / other agent names → **Hermes**
- Replace external issue tracker setup references → **GitHub Issues via MCP** or **`.secure/todo.md`**
- Replace setup commands → `/setup-brownmediagroup-skills`
- Replace author/brand names → **Newton** or **BrownMediaGroup**
- Remove plugin-marketplace references (we use Hermes skill_manage, not npm plugins)

### 4. Dual-write
Write patched skills to BOTH locations:
- **Canonical**: `D:/BrownMediaGroup/dev/brownmediagroup/skills/<category>/`
- **Team folder**: `G:/BrownMediaGroup/ops/team/skills/<category>/`

Use the sync script at `D:/BrownMediaGroup/dev/brownmediagroup/skills/sync-team.py` to propagate future changes.

### 5. Commit + push
```bash
git add skills/<category>/
git commit -m "feat: adapt <name> skills from <source-repo>"
git push origin HEAD
```

### 6. Register in Hermes
After pushing, install the skills into the active Hermes profile via `skill_manage` so they appear in the skills list. Do not assume downloading to disk makes them available to Hermes.

## Category Mapping

Map external skill categories to Hermes categories:
- `engineering/*` → `software-development/` or `devops/`
- `productivity/*` → `productivity/`
- `writing/*` → `writing/`
- Custom/external categories → ask user where they want them

## Pitfalls

- Do not push external skills to public repos (RiseUp-1, Starbeam) without explicit approval — most stay local/private
- Do not overwrite existing BMG skills without checking for overlap first
- Do not embed the upstream repo's `.git/` directory inside the skills folder
- Do not assume all 111 skills from a large repo are useful — evaluate and cherry-pick
- Skills that reference `CONTEXT.md`, `ADR`, or `AGENT-BRIEF.md` from the upstream conventions need patching to reference BMG equivalents (`.secure/todo.md`, `quick-reference.md`, daily logs)

## Related

- `bmg-repo-workflow` — visibility rules, per-item commits, push discipline
- `external-tool-evaluation` — when to adopt vs reference vs skip an external tool
