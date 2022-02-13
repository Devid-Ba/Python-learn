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

    for k,v in count.items():     #it took me a while do understand that this indentation was wrong.                     
        lst.append((k,v))          #it has to be in line with[for line in han]
        #print(k,v)                #im just having a tought time understanding why?             
                                #is it because it symbolizes a new code block?
    lst.sort()                   #and saying okay that block is done now do your own thing?                     
    for k,v in lst:                                    
        print (k,v)                                    