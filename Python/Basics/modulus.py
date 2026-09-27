
# MODULO (%)

#* **Modulo** → the operation of finding the remainder after division.
# **Modulus** → the remainder/result of that operation.

#xample:

#```xt
#0 ÷ 3 = 3 remainder 1

#0 % 3 = 1
#````
#So, **`%` is called the modulo operator**.



# Modulo means: the remainder left over after division.
#
# The % symbol is called the modulo operator.
#
# Example:
#
# 10 divided by 3 = 3 remainder 1
#
# So:
# 10 % 3 = 1



# BASIC EXAMPLES


print(10 % 3)   # 1
print(20 % 6)   # 2
print(15 % 5)   # 0
print(7 % 2)    # 1



# WHY DO WE GET 0?


# If a number divides evenly,
# there is no remainder.

# 15 divided by 5 = 3 remainder 0

print(15 % 5)   # 0

# 20 divided by 4 = 5 remainder 0

print(20 % 4)   # 0



# MODULO VS DIVISION


# / gives us the division result.

print(10 / 3)

# % gives us only the remainder.

print(10 % 3)



# USING VARIABLES


a = 20
b = 6

print(a % b)    # 2



# MORE EXAMPLES


print(8 % 3)    # 2
print(9 % 3)    # 0
print(10 % 4)   # 2
print(11 % 4)   # 3
print(12 % 4)   # 0
print(13 % 4)   # 1



# A USEFUL PATTERN


# Modulo is often used to check
# whether a number divides evenly.

number = 10

print(number % 2)   # 0

# If the remainder is 0,
# the number divides evenly by 2.


# =========================
# TRY CHANGING THESE
# =========================

number = 25

print(number % 2)
print(number % 3)
print(number % 5)
print(number % 10)