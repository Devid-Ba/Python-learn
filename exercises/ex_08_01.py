
han = open('/Users/devidbarattini/Desktop/Pylearn/mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    #if line == '' :
        #print('Skip Blank')
        #continue
    wds = line.split()
    #print('Words:', wds)
    #guardian patterns
    #if len(wds) < 3 :
        #continue
    if len(wds) < 3 or wds[0] != 'From' :
        #print('Ignore')
        continue
    print(wds[2])