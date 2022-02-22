from sys import argv
# sets parameters for what to import so the script name .py file and the filename .txt file
script, filename = argv
#sets up txt as a variable to open the filename argument
txt = open(filename)

print(f"Here's your file {filename} ;")
# actually open and prints the file
print(txt.read())

print('Type the filename again:')
file_again = input()

txt_again = open(file_again)

print(txt_again.read())

