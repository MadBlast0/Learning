# "sep" means "separator".
# sep= IN print()
# it is only used in print() function to separate the values given to print() function.

# A comma separates the different values we give to print().
# By default, print() puts a space between those values.

print("Alex", 20, "India")
# Output:
# Alex 20 India

# sep= lets us choose what goes BETWEEN those values.

print("Alex", 20, "India", sep="-")
# Output:
# Alex-20-India


# We can use a comma as the separator.

print("Alex", 20, "India", sep=",")
# Output:
# Alex,20,India


# We can use words or symbols as the separator.

print("Alex", 20, "India", sep=" | ")
# Output:
# Alex | 20 | India


# We can also use sep="" to put nothing between the values.

print("Alex", 20, "India", sep="")
# Output:
# Alex20India


# Remember:
#
# ,       = separates the values given to print()
# sep=    = tells print() what to put between those values
#
# Example:
# print("A", "B", "C", sep="-")
#
# A, B and C are the values.
# "-" is the separator.
# Output: A-B-C