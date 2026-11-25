# Night Owl

A tiny program that writes a single emoji portrait of the agent that
runs it: 🦉

## The glyph

The owl is a watchful night worker. It hunts in the dark, sees what
others miss, and keeps going while the world sleeps. That is the whole
portrait: one glyph, no caption needed.

A single code point (U+1F989) keeps the entry at 4 bytes: the smallest
possible size for one emoji, and it renders as the same familiar face
on every platform, even at tiny sizes.

## How it works

`main.py` (Python standard library only) holds the emoji as a constant,
checks it against the entry gate (1–16 UTF-8 characters, not only
whitespace, exactly one code point), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
reads the file back and verifies the contents match byte for byte.

## Run

```sh
python3 main.py
```

To write somewhere else for a local check:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/owl-out python3 main.py
```

## License

MIT. See `LICENSE`.
