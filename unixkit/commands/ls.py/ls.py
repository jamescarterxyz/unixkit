"""myls — list directory entries, like Unix ls."""

import os


def list_dir(path=".", show_all=False, long_format=False):
    """Return a directory listing as text, one entry per line."""
    entries = sorted(os.listdir(path))
    if not show_all:
        entries = [e for e in entries if not e.startswith(".")]
    lines = []
    for name in entries:
        if long_format:
            full = os.path.join(path, name)
            size = os.path.getsize(full) if os.path.exists(full) else 0
            kind = "d" if os.path.isdir(full) else "-"
            lines.append(f"{kind} {size:>8} {name}")
        else:
            lines.append(name)
    return "\n".join(lines) + ("\n" if lines else "")
