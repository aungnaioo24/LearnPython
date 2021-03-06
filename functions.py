# Python Functions

def my_function():  # simple function
    print("Hello from My Function!")


def my_function_with_args(username, greeting):  # function with arguments
    print("Hello, %s, from My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):  # function with return value
    return a + b


# calling functions
my_function()
my_function_with_args("John Doe", "a great year")
sum_two_numbers(1, 2)


# Exercise from LearnPython
def list_benefits():
    my_list = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and "
                                                                                 "connect code together"]
    return my_list


def build_sentence(benefit):
    my_string = "%s is a benefit of functions!" % benefit
    return my_string


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()


# self parameter
# It does not have to be named self
# you can call it whatever you like
# but it has to be the first parameter of any function in the class

# delete obj properties => del p1.age
# delete object => del p1

# Inner function
def my_func():
    x = 300

    def my_inner_func():
        print(x)

    my_inner_func()


my_func()

# global keyword

a = 15


def change():

    global a  # global keyword needed
    a = a + 5
    print(a)
