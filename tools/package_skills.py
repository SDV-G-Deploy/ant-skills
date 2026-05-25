#!/usr/bin/env python3
"""Create zip archives and checksums for each ANT skill."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)
checksums: list[tuple[str, str]] = []

for skill_dir in sorted((ROOT / "skills").iterdir()):
    if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").exists():
        continue
    zip_path = OUT / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in skill_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(skill_dir.parent))
    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    checksums.append((digest, zip_path.name))
    print(zip_path.relative_to(ROOT))

(OUT / "SHA256SUMS").write_text(
    "".join(f"{digest}  {name}\n" for digest, name in sorted(checksums)),
    encoding="utf-8",
)
print((OUT / "SHA256SUMS").relative_to(ROOT))
