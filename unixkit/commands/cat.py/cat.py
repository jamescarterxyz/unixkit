"""mycat — print files, like Unix cat."""

from ..utils import read_inputs


def cat(paths):
    """Concatenate the given files (or stdin) and return the text."""
    return "".join(text for _, text in read_inputs(paths))
