"""mywc — count lines, words and characters, like Unix wc."""

from ..utils import read_inputs


def count_text(text):
    """Return (lines, words, chars) for one block of text."""
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    words = len(text.split())
    chars = len(text)
    return lines, words, chars


def wc(paths, show_lines=True, show_words=True, show_chars=True):
    """Count each input and return one result line per input."""
    out = []
    for name, text in read_inputs(paths):
        lines, words, chars = count_text(text)
        parts = []
        if show_lines:
            parts.append(str(lines))
        if show_words:
            parts.append(str(words))
        if show_chars:
            parts.append(str(chars))
        out.append(" ".join(parts) + f" {name}")
    return "\n".join(out) + "\n"
