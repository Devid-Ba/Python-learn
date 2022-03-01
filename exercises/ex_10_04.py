import re

fhandle = open("py4e-data.txt", 'r')

data = []
for line in fhandle:
    line = line.strip()
    #print(line)
    numbers = re.findall(('[0-9]+'), line)
    if not numbers:
        continue
    else:
        for number in numbers:
            data.append(int(number))


print(sum(data))