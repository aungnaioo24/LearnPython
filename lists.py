# List
my_list = [1, 2, 3]  # creating list
# empty list can be created, my_list = []
print(my_list[0])
print(my_list[1])
print(my_list[2])

for x in my_list:
    print(x)

# my_list[10] will be error like Java

# List exercise from LearnPython
numbers = [1, 2, 3]
strings = ['hello', 'world']
names = ['John', 'Eric', "Jessica"]  # no prob with single quote and double quote
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


this_list = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(this_list)

this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print(this_list)


# other list method => loop, list comprehension, sort, copy, join, and other methods
