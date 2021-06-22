# Basic Operators
num = 2 + 4
print(num)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared, cubed)

# concatenating string
my_string = "Hello" + " " + "World"
print(my_string)

# repeating string by multiplying
texts = "Batman" * 10
print(texts)

# operating list
even_num = [2, 4, 6, 8]
odd_num = [1, 3, 5, 7]
all_num = odd_num + even_num
print(all_num)  # result is the concatenating list

# repeating list by multiplying like string
print([1, 2, 3] * 3)

# exercise from LearnPython
x = object()  # I assume that is creating object in python
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(x_list.count(3))

print("x_list contains %d objects" % len(x_list))  # len() = length function of array
print("y_list contains %d objects" % len(y_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")

# list.count(x) function counts how many x in the list

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
