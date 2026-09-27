# =========================
# PYTHON OPERATORS
# =========================

# Operators are symbols/keywords that perform an operation
# on values.


# =========================
# ARITHMETIC OPERATORS
# =========================

# =  assignment
#     Gives a value to a variable.

age = 20


# +  addition
#     Adds values together.

print(10 + 5)       # 15


# -  subtraction
#     Subtracts one value from another.

print(10 - 5)       # 5


# *  multiplication
#     Multiplies values.

print(10 * 5)       # 50


# /  division
#     Divides values.
#     The result of / is always a float in Python.

print(10 / 5)       # 2.0
print(10 / 3)       # 3.3333333333333335


# %  modulo
#     Gives the "remainder of that devision" that was left over after division.

print(10 % 3)       # 1
print(20 % 6)       # 2
print(15 % 5)       # 0


# //  floor division
#      Divides and removes the decimal part of the result.
#      in the end we get the whole number that we can use as int(integer) in python.

print(10 // 3)      # 3
print(20 // 6)      # 3


# **  exponentiation
#     Raises a number to a power.

print(2 ** 3)       # 8  means multiplying 2 by itself 3 times: 2 * 2 * 2 = 8
print(5 ** 2)       # 25 means multiplying 5 by itself 2 times: 5 * 5 = 25


# =========================
# COMPARISON OPERATORS
# =========================

# Comparison operators compare two values.
# The result is either True or False.


# >  greater than

print(10 > 5)       # True
print(3 > 5)        # False


# <  less than

print(3 < 5)        # True
print(10 < 5)       # False


# >=  greater than or equal to

print(10 >= 10)     # True
print(10 >= 5)      # True
print(3 >= 5)       # False


# <=  less than or equal to

print(5 <= 5)       # True
print(3 <= 5)       # True
print(10 <= 5)      # False


# ==  equal to
#     Checks whether two values are equal.

print(10 == 10)     # True
print(10 == 5)      # False


# !=  not equal to
#     Checks whether two values are different.

print(10 != 5)      # True
print(10 != 10)     # False


# =========================
# LOGICAL OPERATORS
# =========================

# Logical operators combine or modify conditions.


# and
# Both conditions must be True.

print(10 > 5 and 10 < 20)     # True


# or
# At least one condition must be True.

print(10 > 20 or 10 < 20)     # True


# not
# Reverses True to False and False to True.

print(not True)                # False
print(not False)               # True


# =========================
# ASSIGNMENT OPERATORS
# =========================

# These assign values to variables.


# =  assign a value

number = 10


# +=  add and assign

number += 5
print(number)                  # 15


# -=  subtract and assign

number -= 5
print(number)                  # 10


# *=  multiply and assign

number *= 2
print(number)                  # 20


# /=  divide and assign

number /= 2
print(number)                  # 10.0


# //=  floor divide and assign

number //= 3
print(number)                  # 3.0


# %=  modulo and assign

number %= 2
print(number)                  # 1.0


# **=  exponentiate and assign

number = 2
number **= 3
print(number)                  # 8


# =========================
# QUICK REFERENCE
# =========================

# Arithmetic:
# =    assignment
# +    addition
# -    subtraction
# *    multiplication
# /    division
# %    modulo / remainder
# //   floor division
# **   exponentiation


# Comparison:
# >    greater than
# <    less than
# >=   greater than or equal to
# <=   less than or equal to
# ==   equal to
# !=   not equal to


# Logical:
# and  both conditions must be True
# or   at least one condition must be True
# not  reverses True/False


# Assignment:
# =    assign
# +=   add and assign
# -=   subtract and assign
# *=   multiply and assign
# /=   divide and assign
# //=  floor divide and assign
# %=   modulo and assign
# **=  exponentiate and assign