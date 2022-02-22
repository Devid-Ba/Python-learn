print("What file can I help you with?", end =' ')

filename = input()
txt = open(filename)

print("Opening your file", {filename})
print(txt.read())

