import sys

if len(sys.argv) < 2:
    print("Usage: python file_count.py sample.txt")
    sys.exit()

fname = sys.argv[1]

lines = 0
words = 0
letters = 0

with open(fname, 'r') as f:
    for line in f:
        lines += 1
        words += len(line.split())
        letters += len(line)

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
