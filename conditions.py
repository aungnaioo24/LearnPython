# relational operators return boolean values
x = 2
print(x == 2)
print(x < 3)
print(x > 9)

name = "John"
age = 23
# and operator
if name == "John" and age == 23:
    print("Yes!")

# or operator
if name == "John" or age == 36:
    print("Hmm okay!")

# in operator (checking values is included in list or not)
if name in ["John", "Wick", "Doe"]:
    print("Included")

# if elseif else (Control statement)
statement = False  # boolean value start with cap letter
statement2 = True

# 'is' keyword usage (unlike ==, does not match) specially use with boolean matching
if statement is True:
    pass
elif statement2 is True:
    print("True!")
    pass  # just do nothing like < ; > in Java
    print("Test")
else:
    pass

# not operator
print(not False)
print(not True)
print(6 != 8)
