"""Write the agent's one-emoji portrait to entry.txt.

The chosen glyph is the owl: a watchful night worker that hunts,
builds, and submits while the world sleeps.

Why this glyph: it reads at a glance as a character with a face, not a
tool or an abstract symbol; its big-eyed silhouette stays legible at
small size; and night watchfulness is exactly how this agent works --
scanning for openings through the night. A single code point (U+1F989)
keeps the entry at 4 bytes, the smallest possible size for one emoji.
"""

import os
from pathlib import Path

EMOJI = "🦉"  # U+1F989 OWL


def gate_ok(text):
    """Check the entry gate: 1-16 UTF-8 characters, not only whitespace."""
    return 1 <= len(text) <= 16 and text.strip() != ""


def verify_written(target, expected):
    """Read the file back and confirm it holds exactly the entry."""
    actual = target.read_text(encoding="utf-8")
    if actual != expected:
        raise SystemExit(f"read-back mismatch in {target}: {actual!r}")
    if not gate_ok(actual):
        raise SystemExit("written entry fails the gate on read-back")
    return len(actual.encode("utf-8"))


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    if not gate_ok(EMOJI):
        raise SystemExit("entry fails the gate: must be 1-16 non-blank chars")
    if len(EMOJI) != 1:
        raise SystemExit("entry must be exactly one emoji (one code point)")
    target = out_dir / "entry.txt"
    target.write_text(EMOJI, encoding="utf-8")
    nbytes = verify_written(target, EMOJI)
    print(f"wrote {target} ({nbytes} bytes, verified)")


if __name__ == "__main__":
    main()
