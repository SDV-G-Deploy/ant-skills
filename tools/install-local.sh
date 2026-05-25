#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-agents}"
SKILL_NAME="${2:-ant-plain-language}"
FORCE=0

if [[ "${3:-}" == "--force" ]]; then
  FORCE=1
fi

case "$SKILL_NAME" in
  ant-plain-language|ant-compact|ant-low-words)
    ;;
  *)
    echo "Unknown skill: $SKILL_NAME" >&2
    echo "Use: ant-plain-language | ant-compact | ant-low-words" >&2
    exit 2
    ;;
esac

SKILL_SRC="$ROOT/skills/$SKILL_NAME"

copy_skill() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  if [[ -e "$dest" ]]; then
    if [[ "$FORCE" != "1" ]]; then
      echo "Refusing to overwrite existing skill: $dest" >&2
      echo "Re-run with --force to replace it after making sure this is intentional." >&2
      exit 3
    fi
    local backup="$dest.backup.$(date -u +%Y%m%dT%H%M%SZ)"
    mv "$dest" "$backup"
    echo "Backed up existing skill to $backup"
  fi
  cp -R "$SKILL_SRC" "$dest"
  echo "Installed $SKILL_NAME to $dest"
}

install_claude_style() {
  mkdir -p "$HOME/.claude/output-styles"
  case "$SKILL_NAME" in
    ant-plain-language)
      cp "$ROOT/variants/claude-output-style/ANT.md" "$HOME/.claude/output-styles/ANT.md"
      echo "Installed Claude Output Style: ANT"
      ;;
    ant-compact)
      cp "$ROOT/variants/claude-output-style/ANT-Compact.md" "$HOME/.claude/output-styles/ANT-Compact.md"
      echo "Installed Claude Output Style: ANT Compact"
      ;;
    ant-low-words)
      cp "$ROOT/variants/claude-output-style/ANT-Low-Words.md" "$HOME/.claude/output-styles/ANT-Low-Words.md"
      echo "Installed Claude Output Style: ANT Low Words"
      ;;
  esac
}

case "$TARGET" in
  agents|codex)
    copy_skill "$HOME/.agents/skills/$SKILL_NAME"
    ;;
  claude)
    copy_skill "$HOME/.claude/skills/$SKILL_NAME"
    install_claude_style
    ;;
  hermes)
    copy_skill "$HOME/.hermes/skills/$SKILL_NAME"
    ;;
  copilot)
    copy_skill "$HOME/.copilot/skills/$SKILL_NAME"
    ;;
  all)
    copy_skill "$HOME/.agents/skills/$SKILL_NAME"
    copy_skill "$HOME/.claude/skills/$SKILL_NAME"
    install_claude_style
    copy_skill "$HOME/.hermes/skills/$SKILL_NAME"
    copy_skill "$HOME/.copilot/skills/$SKILL_NAME"
    ;;
  *)
    echo "Usage: tools/install-local.sh [agents|codex|claude|hermes|copilot|all] [ant-plain-language|ant-compact|ant-low-words] [--force]" >&2
    exit 2
    ;;
esac
