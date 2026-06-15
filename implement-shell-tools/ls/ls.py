import argparse
from os import listdir

parser = argparse.ArgumentParser(prog="ls", description="List directory contents.  Ignore files and directories starting with a '.' by default")
parser.add_argument("-1", dest="one", help="List one file per line.", action="store_true")
parser.add_argument("-a", help="Do not ignore hidden files (files with names that start with '.').", action="store_true")
parser.add_argument("path", help="The directory path (optional).", default=".", nargs="?")

args = parser.parse_args()

path = args.path

show_hidden = args.a
one_per_line = args.one

contents = []

for f in listdir(path):
    if not show_hidden and f[0] != ".":
        contents.append(f)
    if show_hidden:
        contents.append(f)

contents.sort()

if one_per_line:
    print("\n".join(contents))
else:
    print("  ".join(contents))
