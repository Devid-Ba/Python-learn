#name = input('Enter file:')
if True or len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if line.startswith('From: '):
        line = line.strip()
        words = line.split(" ")[1]
        if words in words:
            counts[words] = counts.get(words, 0) + 1

bigcount = None
bigword = None
for words, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = count

print(bigword, bigcount)