"""Command-line dispatcher for unixkit.

Usage:
    python -m unixkit ls [-a] [-l] [path]
    python -m unixkit cat [file ...]
    python -m unixkit wc [-l] [-w] [-c] [file ...]
    python -m unixkit grep [-i] [-v] [-n] PATTERN [file ...]

With no file argument, cat/wc/grep read from stdin, so tools compose
with pipes exactly like Unix tools:

    python -m unixkit cat notes.txt | python -m unixkit grep TODO
"""

import argparse
import sys

from .commands import cat, grep, ls, wc


def build_parser():
    parser = argparse.ArgumentParser(
        prog="unixkit",
        description="A tiny Unix-style toolkit: ls, cat, wc, grep.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ls = sub.add_parser("ls", help="list directory entries")
    p_ls.add_argument("path", nargs="?", default=".")
    p_ls.add_argument("-a", action="store_true",
                      help="show hidden entries")
    p_ls.add_argument("-l", action="store_true",
                      help="long format (type and size)")

    p_cat = sub.add_parser("cat", help="print files")
    p_cat.add_argument("files", nargs="*")

    p_wc = sub.add_parser("wc", help="count lines, words, chars")
    p_wc.add_argument("files", nargs="*")
    p_wc.add_argument("-l", action="store_true", help="lines only")
    p_wc.add_argument("-w", action="store_true", help="words only")
    p_wc.add_argument("-c", action="store_true", help="chars only")

    p_grep = sub.add_parser("grep", help="print matching lines")
    p_grep.add_argument("pattern")
    p_grep.add_argument("files", nargs="*")
    p_grep.add_argument("-i", action="store_true",
                        help="ignore case")
    p_grep.add_argument("-v", action="store_true",
                        help="invert match")
    p_grep.add_argument("-n", action="store_true",
                        help="show line numbers")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.command == "ls":
        sys.stdout.write(ls.list_dir(args.path, args.a, args.l))
    elif args.command == "cat":
        sys.stdout.write(cat.cat(args.files))
    elif args.command == "wc":
        only = args.l or args.w or args.c
        sys.stdout.write(wc.wc(args.files,
                                show_lines=not only or args.l,
                                show_words=not only or args.w,
                                show_chars=not only or args.c))
    elif args.command == "grep":
        sys.stdout.write(grep.grep(args.pattern, args.files,
                                   ignore_case=args.i,
                                   invert=args.v,
                                   line_numbers=args.n))


if __name__ == "__main__":
    main()
