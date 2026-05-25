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
declare -a COPY_KINDS=()
declare -a COPY_SRCS=()
declare -a COPY_DESTS=()
declare -a COPY_LABELS=()

queue_copy() {
  local kind="$1"
  local src="$2"
  local dest="$3"
  local label="$4"
  COPY_KINDS+=("$kind")
  COPY_SRCS+=("$src")
  COPY_DESTS+=("$dest")
  COPY_LABELS+=("$label")
}

queue_skill() {
  local dest="$1"
  queue_copy "dir" "$SKILL_SRC" "$dest" "$SKILL_NAME"
}

queue_claude_style() {
  case "$SKILL_NAME" in
    ant-plain-language)
      queue_copy "file" "$ROOT/variants/claude-output-style/ANT.md" "$HOME/.claude/output-styles/ANT.md" "Claude Output Style: ANT"
      ;;
    ant-compact)
      queue_copy "file" "$ROOT/variants/claude-output-style/ANT-Compact.md" "$HOME/.claude/output-styles/ANT-Compact.md" "Claude Output Style: ANT Compact"
      ;;
    ant-low-words)
      queue_copy "file" "$ROOT/variants/claude-output-style/ANT-Low-Words.md" "$HOME/.claude/output-styles/ANT-Low-Words.md" "Claude Output Style: ANT Low Words"
      ;;
  esac
}

preflight_destinations() {
  local dest
  for dest in "${COPY_DESTS[@]}"; do
    if [[ -e "$dest" && "$FORCE" != "1" ]]; then
      echo "Refusing to overwrite existing path: $dest" >&2
      echo "Re-run with --force to replace it after making sure this is intentional." >&2
      exit 3
    fi
  done
}

install_queued() {
  local i kind src dest label backup
  local stamp
  stamp="$(date -u +%Y%m%dT%H%M%SZ)"
  for i in "${!COPY_DESTS[@]}"; do
    kind="${COPY_KINDS[$i]}"
    src="${COPY_SRCS[$i]}"
    dest="${COPY_DESTS[$i]}"
    label="${COPY_LABELS[$i]}"
    mkdir -p "$(dirname "$dest")"
    if [[ -e "$dest" ]]; then
      backup="$dest.backup.$stamp"
      mv "$dest" "$backup"
      echo "Backed up existing path to $backup"
    fi
    if [[ "$kind" == "dir" ]]; then
      cp -R "$src" "$dest"
    else
      cp "$src" "$dest"
    fi
    echo "Installed $label to $dest"
  done
}

case "$TARGET" in
  agents|codex)
    queue_skill "$HOME/.agents/skills/$SKILL_NAME"
    ;;
  claude)
    queue_skill "$HOME/.claude/skills/$SKILL_NAME"
    queue_claude_style
    ;;
  hermes)
    queue_skill "$HOME/.hermes/skills/$SKILL_NAME"
    ;;
  copilot)
    queue_skill "$HOME/.copilot/skills/$SKILL_NAME"
    ;;
  all)
    queue_skill "$HOME/.agents/skills/$SKILL_NAME"
    queue_skill "$HOME/.claude/skills/$SKILL_NAME"
    queue_claude_style
    queue_skill "$HOME/.hermes/skills/$SKILL_NAME"
    queue_skill "$HOME/.copilot/skills/$SKILL_NAME"
    ;;
  *)
    echo "Usage: tools/install-local.sh [agents|codex|claude|hermes|copilot|all] [ant-plain-language|ant-compact|ant-low-words] [--force]" >&2
    exit 2
    ;;
esac

preflight_destinations
install_queued
