# end in print()

# Normally print() ends by moving to a new line.
print("Hello")
print("World")
# Output:
# Hello
# World 

# end changes what print() puts after its output.

print("Hello", end="") #always takes from next print and adds it to this print output
print("World") # this will be added to the above print output
print("Bell") # this is not taken by end and is seprate because above print was taken.
# Output:
# HelloWorld
# Bell


# We can put a space instead.

print("Hello", end=" ")
print("World")

# Output:
# Hello World


# We can put any text in end.

print("Hello", end="009")
print("World")

# Output:
# Hello009World


# \n is an escape sequence that means "new line".

print("Hello\nWorld")

# Output:
# Hello
# World


# end="\n" is the normal/default ending of print().
# So these behave the same way:

print("Hello", end="\n") # end took print below but \n moves it to the next line.
print("World")
#Output:
# Hello
# World


# sep controls what goes BETWEEN print() values.
# end controls what comes AFTER all the values.

print("A", 6, 7, sep="~", end="009\n")

# Output:
# A~6~7009
#
# \n then moves to the next line.


# We don't need end to use \n.
# We can put \n directly inside a string.

print("A", 6, 7009, "\nAlex")

# Output:
# A 6 7009
# Alex

# Here "\nAlex" is one string.
# \n moves to the next line, then Alex appears there.