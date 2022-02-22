name = input('Enter file:')
if not len(name):
    name = "mbox-short.txt"

from_prefix = "From: "
counts = {}
with open(name) as file:
    for line in file:
        if not line.startswith(from_prefix):
            continue
        line = line.strip()
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

max_email, count = max(counts.items(), key=lambda pair: pair[1])
print(max_email, count)