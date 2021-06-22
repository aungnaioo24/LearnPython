# A dictionary is similar to an array but works with key and values
# instead of indexes

# example
# phonebook = {} # creating an empty dictionary
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781

# alternative
phonebook = {
    "John": 938477566, "Jack": 938377264, "Jill": 947662781, "Jane": 947772781
}
print(phonebook)

# Removing a value from the dictionary
del phonebook["John"]
print(phonebook)

# or
phonebook.pop("Jane")  # pop() is an inbuilt function in Python that removes and returns last value from the list or
# the given index value
print(phonebook)

phonebook["John"] = 938477566

for name, number in phonebook.items():  # items() method display all items in that dictionary
    print("Phone number of %s is %d" % (name, number))
