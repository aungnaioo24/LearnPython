# String length
a_string = "Hello world!"
print(len(a_string))

# indexing String
print(a_string.index('o'))  # count start from 0

# counting specific letters from String
print(a_string.count('l'))

# subString between specific two letters
print(a_string[3:7])
print(a_string[3:-2])
print(a_string[3:-1:3])  # lo world => 3 give 2 letter skip after 1 char, 2 give 1 char, 1 give no char skip

# reverse string
print(a_string[::-1])

# upper/lower cases
print(a_string.upper())
print(a_string.lower())

print(a_string.startswith("Hello"))  # check the starting value
print(a_string.endswith("asd"))  # check the ending value

print(a_string.split(" "))  # split into two values
my_list = a_string.split(" ")
print(my_list[1])  # output of split second value
