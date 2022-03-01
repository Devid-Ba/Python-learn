from sys import argv

script, filename, user_name = argv

txt = open(filename)

print(f"Hey {user_name} here is your{filename}:")

print(txt.read())