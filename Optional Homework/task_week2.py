# Immutable Data Types

a = 10
print("Initial value of a:", a)
print("Initial ID:", id(a))  # id() shows the memory address

a += 5
print("New value of a:", a)
print("New ID:", id(a))

b = 3.14
print("\nInitial value of b:", b)
print("Initial ID:", id(b))

b = b * 2
print("New value of b:", b)
print("New ID:", id(b))



# Leap Year Checker

year = input("Enter desired year: ")

# Convert from string to int
year = int(year)

# Check leap year rule
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year.")
else:
    print("This isn't a leap year.")



# Ternary Conditional Operator

number = -3
result = "Positive" if number >= 0 else "Negative"
print(result)



# Boolean Logic Practice

x = 5
y = 0
z = -3

# 1. Are all three numbers greater than 0?
print("All > 0:", x > 0 and y > 0 and z > 0)

# 2. Is at least one number equal to 0?
print("At least one is 0:", x == 0 or y == 0 or z == 0)

# 3. Are none of the numbers negative?
print("None are negative:", not (x < 0 or y < 0 or z < 0))



# Type Conversion and Identity

x = 100
y = -30
z = 0

# Conversions between types
print("Conversions:")
print("float(x):", float(x))
print("bool(x):", bool(x))

print("int(y):", int(y))
print("bool(y):", bool(y))

print("float(z):", float(z))
print("bool(z):", bool(z))  # False for 0

# Comparing object identities
a = 100
b = 100.0
c = bool(100)

print("\nValues:")
print("a =", a, "| id:", id(a))
print("b =", b, "| id:", id(b))
print("c =", c, "| id:", id(c))

# Value vs identity comparison
print("\nValue comparisons:")
print("a == b:", a == b)
print("a is b:", a is b)  # False, different types

print("a == c:", a == c)
print("a is c:", a is c)  # False, different types