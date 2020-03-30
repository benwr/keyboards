import sys

bigrams = {}

with open(sys.argv[1]) as f:
    s = f.read()
    for i, c in enumerate(s[:-1]):
        d = s[i + 1]
        char1 = c.lower()
        char2 = d.lower()
        bigram = c.lower() + d.lower()
        bigrams[bigram] = bigrams.get(bigram, 0) + 1

for b, count in sorted(bigrams.items(), key=lambda x: x[1]):
    print(b, count)

