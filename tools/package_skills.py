#!/usr/bin/env python3
"""Create zip archives for each ANT skill."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)

for skill_dir in sorted((ROOT / "skills").iterdir()):
    if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").exists():
        continue
    zip_path = OUT / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in skill_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(skill_dir.parent))
    print(zip_path.relative_to(ROOT))
