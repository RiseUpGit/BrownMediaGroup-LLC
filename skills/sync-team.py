#!/usr/bin/env python3
import os, shutil
from datetime import datetime

skills = ['grill-with-docs', 'to-spec', 'to-tickets', 'improve-codebase-architecture', 'triage', 'tdd', 'diagnosing-bugs', 'ask-matt']

src_base = 'D:/BrownMediaGroup/dev/brownmediagroup/skills/engineering'
team_base = 'G:/BrownMediaGroup/ops/team/skills/engineering'

os.makedirs(team_base, exist_ok=True)

for skill in skills:
    src = f'{src_base}/{skill}/SKILL.md'
    if not os.path.exists(src):
        print(f'SKIP missing: {src}')
        continue
    with open(src) as f:
        content = f.read()
    # Global replacements
    content = content.replace('mattpocock/skills', 'BrownMediaGroup/skills')
    content = content.replace('/setup-matt-pocock-skills', '/setup-brownmediagroup-skills')
    content = content.replace('Matt Pocock', 'Newton')
    # Write team copy
    dst = f'{team_base}/{skill}/SKILL.md'
    with open(dst, 'w') as f:
        f.write(content)
    print(f'Copied {skill} -> {dst}')

print('Team skills sync complete')
