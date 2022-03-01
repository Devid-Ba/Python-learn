fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From '):
        #line = line.strip()
            #print(line.split(" ")[1])
            line = line.split(' ', 3)
            print(line[1])
            #print(line)
            

            #print(line)
            count += 1
    #print(line)


print("There were", count, "lines in the file with From as the first word")
