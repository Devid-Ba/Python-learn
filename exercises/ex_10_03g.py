name = "mbox-short.txt"
handle = open(name)

hcount = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')
        #print(hr)                    #Select hour (5th index) and split string with colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue
    print(hcount)

for k,v in hcount.items():                           #k = hour, v = count
    hlst.append((k,v))
    print(k,v)                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print (k,v)                                      #print counts sorted by hour