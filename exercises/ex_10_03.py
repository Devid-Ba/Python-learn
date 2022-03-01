han = open("mbox-short.txt")

count = dict()
lst = []

for line in han:
    if line.startswith("From "):
        num = line.split()[5]
        hrs = num.split(':')
        #print(hrs)
        count[hrs[0]] = count.get(hrs[0],0) + 1
    else:
        continue
    #print(count)
        
    #print(count)

    for k,v in count.items():                          
        lst.append((k,v)) 
        #print(k,v)                              
    
    lst.sort()                                        
    for k,v in lst:                                    
        print (k,v)                                    