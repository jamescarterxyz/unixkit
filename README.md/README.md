# unixkit 🐚

A tiny Unix-style command line toolkit in pure Python — no dependencies.
Four classic tools, each doing one thing well, composing through pipes
exactly like real Unix tools.

## Tools

| Command | Does what | Example |
|---|---|---|
| `ls` | Lists directory entries | `python -m unixkit ls -l` |
| `cat` | Prints files (or stdin) | `python -m unixkit cat notes.txt` |
| `wc` | Counts lines, words, chars | `python -m unixkit wc -l notes.txt` |
| `grep` | Prints matching lines | `python -m unixkit grep TODO notes.txt` |

## The Unix way: pipes

```bash
python -m unixkit cat notes.txt | python -m unixkit grep TODO
python -m unixkit cat notes.txt | python -m unixkit wc -l
```

## Project structure

```mermaid
flowchart TB
    User(["User / Terminal"]) --> CLI["unixkit/cli.py<br/>argparse dispatcher"]
    CLI --> LS["commands/ls.py<br/>list directory"]
    CLI --> CAT["commands/cat.py<br/>print files"]
    CLI --> WC["commands/wc.py<br/>count lines/words/chars"]
    CLI --> GREP["commands/grep.py<br/>match lines (regex)"]
    CAT & WC & GREP --> UTILS["utils.py<br/>read files or stdin"]
    LS --> OS["os.listdir / os.path"]
    CLI --> OUT(["stdout"])
```

```text
unixkit/
├── unixkit/
│   ├── __init__.py      # version
│   ├── __main__.py      # python -m unixkit entry point
│   ├── cli.py           # argument parsing + dispatch
│   ├── utils.py         # read files or stdin
│   └── commands/
│       ├── ls.py        # directory listing
│       ├── cat.py       # print files
│       ├── wc.py        # line/word/char counts
│       └── grep.py      # regex line matching
├── tests/
│   └── test_unixkit.py  # unit tests + a real pipe test
└── README.md
```

## How data flows

```mermaid
flowchart LR
    A["cat notes.txt"] -->|"stdout"| B["grep TODO"]
    B -->|"stdout"| C["wc -l"]
    C -->|"stdout"| D(["Terminal"])
```

Every tool reads files — or stdin when no file is given — and writes
plain text to stdout. That is the whole Unix philosophy: small tools,
text streams, composable pipes.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Requirements

Python 3.10+ only. No third-party packages.
