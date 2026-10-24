"""mygrep — print matching lines, like Unix grep."""

import re

from ..utils import read_inputs


def grep(pattern, paths, ignore_case=False, invert=False,
         line_numbers=False):
    """Return the lines matching ``pattern`` (a regular expression)."""
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)
    out = []
    for name, text in read_inputs(paths):
        for i, line in enumerate(text.splitlines(), start=1):
            matched = bool(regex.search(line))
            if invert:
                matched = not matched
            if matched:
                prefix = f"{name}:" if len(paths) > 1 else ""
                if line_numbers:
                    prefix += f"{i}:"
                out.append(prefix + line)
    return "\n".join(out) + ("\n" if out else "")
