# tuple
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

# Items can't be added, changed or removed to tuple - unchangeable
# if you want to change items, change type first from tuple to list
# the order will not change in tuple and allow duplicates
this_tuple = ("orange", "apple", "banana", "cherry", "orange")
print(this_tuple)
print(type(this_tuple))

# unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(red)

# unpacking a tuple using asterisk
fruits = ("apple", "mango", "papaya", "pineapple", "cherry", "coconut")
(green, *tropic, red, brown) = fruits
print(tropic)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(red)

"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and not indexed. No duplicate members.
    Dictionary is a collection which is ordered* and changeable. No duplicate members.

"""

# other functions for tuples are almost the same as lists, dictionaries

# list test
this_list = ["bird", "cat", "dog"]
print(type(this_list))

# dictionary test
this_dict = {
    "read": "book",
    "write": "pen",
    "color": "paint"
}
print(type(this_dict))
