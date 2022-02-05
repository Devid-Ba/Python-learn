fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = []
for line in fh:
    line = line.strip(' ')
    print(line)
    for word in line.split(' '):
        print(word)
        if word not in lst:
            lst.append(word)
        #print(lst)
print(sorted(lst))
#print(line)
