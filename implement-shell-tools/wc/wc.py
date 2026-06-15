import argparse

parser = argparse.ArgumentParser(prog="wc", description="Print  newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.")
parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
parser.add_argument("-l", "--line", help="print the newline counts", action="store_true")
parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

lines = 0
words = 0
bytes = 0

l = True
w = True
c = True

if args.words or args.line or args.bytes:
    l = args.line
    w = args.words
    c = args.bytes

file_data = {}
file_data_with_newline = {}

for file in args.path:
    f = open(file)
    file_data[file] = f.read().split("\n")

for file in args.path:
    f = open(file)
    file_data_with_newline[file] = f.read()

def print_helper(line, word, byte, file_name):
    parts = []
    if l:
        parts.append(str(line))
    if w:
        parts.append(str(word))
    if c:
        parts.append(str(byte))
    parts.append(file_name)
    print(" ".join(parts))
    
for f in file_data:
    word_per_line = 0
    byte_per_line = 0
    for line in file_data[f]:
        word_per_line += len(line.split())
    for line in file_data_with_newline[f]:
        byte_per_line += len(line.encode("utf-8"))
    lines += len(file_data[f]) - 1
    words += word_per_line
    bytes += byte_per_line
    print_helper(len(file_data[f]) - 1, word_per_line, byte_per_line, f)

if len(args.path) > 1:
    print_helper(lines, words, bytes, "total")