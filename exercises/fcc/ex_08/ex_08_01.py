
han = open('/Users/devidbarattini/Desktop/Pylearn/mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    #if line == '' :
        #print('Skip Blank')
        #continue
    wds = line.split()
    #print('Words:', wds)
    #guardian patternsS
    #if len(wds) < 3 :
        #continue
        #guardian in a compound statment
    if len(wds) < 3 or wds[0] != 'From' :
        #print('Ignore')
        continue
    print(wds[2])