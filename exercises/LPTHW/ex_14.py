from sys import argv

script, user_name = argv
prompt = '>>> ' 

print(F"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(F"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f""" 
Alright, So you said {likes} about liking me.
You line in {lives}. Not sure where that is.
and you have a {computer} computer. Nice.
""")

pet = input()
print(f"Do you have any Pets? {pet}?")

print("I love pets")
print("hello world")
