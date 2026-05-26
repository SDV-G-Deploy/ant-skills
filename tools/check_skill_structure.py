#!/usr/bin/env python3
"""Basic structure check for the ANT skill package."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_BY_SKILL = {
    "ant-plain-language": [
        "Core rules",
        "Risk gates",
        "Terminal command template",
        "Error explanation template",
    ],
    "ant-compact": [
        "ANT Compact",
        "Output budget",
        "Safety override",
        "Compression rules",
    ],
    "ant-low-words": [
        "ANT Low Words",
        "Output budget",
        "Risk gate",
        "Delete list",
        "Keep list",
    ],
    "ant-product-map": [
        "ANT Product Map",
        "Output Contract",
        "HTML Map Rules",
        "Safety Gates",
        "Quality Bar",
    ],
    "ant-research-run": [
        "ANT Research Run",
        "Core Rule",
        "Workflow",
        "Evidence Table",
        "Synthesize Only After Evidence",
        "Final Check",
    ],
}

REQUIRED_METADATA_FIELDS = [
    "interface:",
    "display_name:",
    "short_description:",
    "default_prompt:",
]


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def parse_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return None
    return match.group(1)


def main() -> int:
    for skill_name, required_phrases in REQUIRED_BY_SKILL.items():
        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        if not skill_file.exists():
            return fail(f"Missing {skill_file.relative_to(ROOT)}")

        text = skill_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            return fail(f"{skill_file.relative_to(ROOT)} must start with YAML frontmatter")

        for field in ["name:", "description:"]:
            if field not in frontmatter:
                return fail(f"{skill_name}: missing required frontmatter field: {field}")

        if f"name: {skill_name}" not in frontmatter:
            return fail(f"{skill_name}: frontmatter name mismatch")

        if len(re.search(r"description:\s*(.*)", frontmatter).group(1).strip()) < 80:
            return fail(f"{skill_name}: description should be specific enough for discovery")

        for required in required_phrases:
            if required not in text:
                return fail(f"{skill_name}: missing section or phrase: {required}")

        metadata_file = skill_file.parent / "agents" / "openai.yaml"
        if not metadata_file.exists():
            return fail(f"{skill_name}: missing agents/openai.yaml")

        metadata = metadata_file.read_text(encoding="utf-8")
        for field in REQUIRED_METADATA_FIELDS:
            if field not in metadata:
                return fail(f"{skill_name}: openai.yaml missing field: {field}")

        if f"${skill_name}" not in metadata:
            return fail(f"{skill_name}: openai.yaml default_prompt must mention ${skill_name}")

    print("PASS: ANT skill structure looks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
