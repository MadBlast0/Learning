# A variable has a name and a value

name = "Alex"
age = 20

print(name)
print(age)

# Python reads the program from top to bottom

name = "Sam"
print(name)

# The second assignment replaces the current value

name = "Alex"
name = "Sam"
print(name)

# We cannot directly combine a string and an integer with +

name = "Alex"
age = 25

# Convert the integer to a string first

message = name + " is " + str(age)
print(message)