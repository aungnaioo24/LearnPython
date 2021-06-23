# Class
class MyClass:
    variable = "message"

    # A static method is bound to the class and not the object of the class
    # A static method can't access or modify class state
    @staticmethod  # should declare for static method like this
    def my_function():
        print("This is a message inside class.")

    # other method example for using data member, we don't need @staticmethod in this case
    """
    # self represents the instance(individual obj of it's class) of the class
    def my_function(self):
        print("This is a %s inside class." % variable)
    """


# assign the class
my_object = MyClass()
print(my_object.variable)

my_object2 = MyClass()

# can change the value of data member like this
my_object2.variable = "changed text"
print(my_object2.variable)

# accessing object function
my_object.my_function()


# Exercise from LearnPython
class Vehicles:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicles()
car1.name = "Ferrari"
car1.color = "red"
car1.value = 60000.0

car2 = Vehicles()
car2.name = "Mercedes"
car2.color = "blue"
car2.value = 10000.0

print(car1.description())
print(car2.description())

# Inheritance
# class Person: => Parent class
# class Student(Person): => Child class
