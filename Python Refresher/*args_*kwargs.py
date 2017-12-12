def my_method(arg1, arg2):
    return arg1 + arg2

my_method(4, 5)

def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(3, 5, 1, 8, 99)

my_list_addition([3, 5, 1, 8, 99])

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 1, 8, 99)

##

def what_are_kwargs(arg1, name, location):
    print(name)
    print(location)

what_are_kwargs(57, location='US', name="John")
