fhand = open('/Users/devidbarattini/Desktop/Pylearn/mbox-short.txt')

count = 0
numbers_added = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        line_numbers = line.find(" ")
        number = float(line[line_numbers+1:])
        count += 1
        numbers_added += number
        average = numbers_added / count
    

print("average:",average)

    
    