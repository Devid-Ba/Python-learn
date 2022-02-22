fh = open('/Users/devidbarattini/Desktop/Pylearn/mbox-short.txt')
count = 0
total_confidence = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        lx = line.find(" ")
        num = float(line[lx+1:]) 
        #print(my_num)
        total_confidence = total_confidence + num
        count = count + 1

print("average_spam_confidence: ",total_confidence/count)





