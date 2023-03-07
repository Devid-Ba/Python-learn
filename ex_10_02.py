"""Print the hour emails are seen at and the count of emails for that time.

For example, for 3 emails sent at noon, print `12 3`.

"""
import collections
import operator

hours = []
with open("mbox-short.txt") as file:
    for line in file:
        if line.startswith("From "):
            first_colon = line.index(":")
            hour = line[first_colon-2:first_colon]  # Assume 24-hour time.
            hours.append(hour)

hour_counts = collections.Counter(hours)
for hour, count in sorted(hour_counts.items(), key=operator.itemgetter(0)):
    print(hour, count)
