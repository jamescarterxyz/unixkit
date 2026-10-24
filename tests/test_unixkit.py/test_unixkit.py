"""Tests for unixkit commands."""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from unixkit.commands import cat, grep, ls, wc


class TestUnixkit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.f1 = os.path.join(self.tmp.name, "a.txt")
        self.f2 = os.path.join(self.tmp.name, "b.txt")
        with open(self.f1, "w") as f:
            f.write("hello world\nTODO: fix this\nhello again\n")
        with open(self.f2, "w") as f:
            f.write("nothing here\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_cat(self):
        self.assertIn("hello world", cat.cat([self.f1]))

    def test_wc(self):
        lines, words, chars = wc.count_text("a b\nc\n")
        self.assertEqual((lines, words, chars), (2, 3, 6))

    def test_grep(self):
        out = grep.grep("hello", [self.f1])
        self.assertEqual(len(out.strip().splitlines()), 2)

    def test_grep_invert(self):
        out = grep.grep("hello", [self.f1], invert=True)
        self.assertIn("TODO", out)

    def test_ls(self):
        out = ls.list_dir(self.tmp.name)
        self.assertIn("a.txt", out)
        self.assertIn("b.txt", out)

    def test_cli_pipe(self):
        """cat | grep must compose through a real shell pipe."""
        py = sys.executable
        cmd = (f"{py} -m unixkit cat {self.f1} | "
               f"{py} -m unixkit grep TODO")
        proc = subprocess.run(cmd, shell=True, capture_output=True,
                              text=True, cwd=os.path.join(
                                  os.path.dirname(__file__), ".."))
        self.assertIn("TODO: fix this", proc.stdout)


if __name__ == "__main__":
    unittest.main()
