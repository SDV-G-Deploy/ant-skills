#!/usr/bin/env python3
"""Validate generated ANT release archives."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SKILLS = ["ant-compact", "ant-low-words", "ant-plain-language", "ant-product-map"]

FORBIDDEN_PARTS = {"__pycache__"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo"}


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def validate_archive(skill: str) -> int:
    archive = DIST / f"{skill}.zip"
    if not archive.exists():
        return fail(f"Missing archive: {archive.relative_to(ROOT)}")

    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()

    required = [f"{skill}/SKILL.md", f"{skill}/agents/openai.yaml"]
    for name in required:
        if name not in names:
            return fail(f"{archive.name}: missing {name}")

    for name in names:
        parts = set(Path(name).parts)
        if parts & FORBIDDEN_PARTS or Path(name).suffix in FORBIDDEN_SUFFIXES:
            return fail(f"{archive.name}: contains build artifact {name}")
        if not name.startswith(f"{skill}/"):
            return fail(f"{archive.name}: unexpected top-level path {name}")

    return 0


def main() -> int:
    for skill in SKILLS:
        result = validate_archive(skill)
        if result:
            return result

    checksums = DIST / "SHA256SUMS"
    if not checksums.exists():
        return fail("Missing dist/SHA256SUMS")

    checksum_text = checksums.read_text(encoding="utf-8")
    for skill in SKILLS:
        if f"{skill}.zip" not in checksum_text:
            return fail(f"dist/SHA256SUMS missing {skill}.zip")

    print("PASS: release archives look OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
