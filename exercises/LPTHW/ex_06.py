#this sets the first varible
types_of_people = 10
#this line attaches a variable into a string
x = f"there are {types_of_people} types of people"

#setting more variables
binary = "binary"
do_not = "don't"
#this adds 2 variables each containing a string to a 3rd string and adds it all together
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e )


