"""Shared helpers for unixkit commands."""

import sys


def read_inputs(paths):
    """Read text from files, or from stdin when no path is given.

    Returns a list of (name, text) pairs. ``name`` is the file path,
    or "<stdin>" when reading from standard input.
    """
    if not paths:
        return [("<stdin>", sys.stdin.read())]
    out = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            out.append((path, f.read()))
    return out
