import sys

counts = {}

with open(sys.argv[1]) as f:
    for c in f.read():
        char = c.lower()
        counts[char] = counts.get(char, 0) + 1

for c, count in sorted(counts.items(), key=lambda x: x[1]):
    print(c, count)

