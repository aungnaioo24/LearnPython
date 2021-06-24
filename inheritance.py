# A parent class
class Person:
    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name

    def print_name(self):
        print(self.firstname, self.lastname)


# create object and use function
p = Person("Jane", "Doe")
p.print_name()


class Student(Person):
    def __init__(self, f_name, l_name):  # the child class will no longer inherit the parent's __init__() function
        # to keep inheritance of the parent's init, code like the following
        Person.__init__(self, f_name, l_name)

        # super() function can be also used but don't add self parameter
        # It automatically inherit the method and properties from its parent
        # super().__init__(f_name, l_name)

        self.graduation_year = 2022


s = Student("John", "Doe")
s.print_name()

# Note
# If we add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden
