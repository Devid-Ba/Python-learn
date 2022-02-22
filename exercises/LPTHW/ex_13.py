from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("the script is called:", script)
print("Who is on First?", end=' ')
one = input()
print("Your first variable is:", first)
print("who is on Second?", end=' ')
two = input()
print("Your second variable is:", second)
print("Who's on third?", end=' ')
three = input()
print("Your thitd variable is:", third)




print(f"{one} is on first, {two} is on second and {three} is on third")
