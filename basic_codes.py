# comment

"""
 comment block
 multiple lines
"""

# print a syntax
print("Hello Python World")

# Indentation
x = 1
if x == 1:
    # indentation can be tab or four space
    print("returning true Indentation Test")

# Variables and Types
# Python is completely object oriented, and not "statically typed"

# get the type of a variable by type() function
print(type(15))

# Number
my_int = 7
print(my_int)

# Float
my_float = 7.0
print(my_float)
my_float = float(8)  # float() function makes int to float values
print(my_float)

# String
my_string = 'String output from single quote'
print(my_string)
my_string = "String output from double quote"
print(my_string)
my_string = "Don't worry about apostrophes"
print(my_string)
my_string = 'Don"t worry about apostrophes'
print(my_string)
my_string = 'App''le'  # my research that joining strings but doesn't work with variables
print(my_string)
my_string = 'I don\'t care.\nI use backslash (\\).'  # like java, c++, etc., the same method
print(my_string)

# simultaneous assignment
a, b = 3, 4
print(a, b)

# this will not work (missing operators, concat and plus)
# print(1+2+"three")

# Exercise from LearnPython Website
my_string = "hello"
my_float = 10.0
my_int = 20

if my_string == "hello":
    print("String: %s" % my_string)
if my_float == 10.0:
    print("Float: %f" % my_float)
if my_int == 20:
    print("Integer: %d" % my_int)

# testing equalling int and float values return true or not
if 20 == 20.0:
    print('true')

# String formatting (s, d, f)
name = "John"
age = 23
print("%s is %d years old." % (name, age))

my_list = [1, 2, 3]
print("A list: %s" % my_list)  # object can be formatted using %s

my_float = 34.892445
# %.<num>f - Floating point numbers with a fixed amount of digits to the right of the dot.
print("Float: %.3f" % my_float)

my_string = "apple"
print("String: %x and %X" % (15, 15))  # %x/%X - Integers in hex representation (lowercase/uppercase)
# output: f and F
