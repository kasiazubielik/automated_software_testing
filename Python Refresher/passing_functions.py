def methodception(another):
    return another()

def add_two_numbers():
    return 32 + 32

# print(methodception(add_two_numbers))
# we pass the add_two_numbers as a parameter
# and methodception is gonna run that method(add_two_numbers)

# print(methodception(lambda: 32 + 32))

my_list = [2, 23, 52, 98]
print(list(filter(lambda x: x != 23, my_list)))
# it keeps only some values, its a function and its iterable
# ==
def not_thirteen(x):
    return x != 23
print(list(filter(not_thirteen, my_list)))
# ==
print([x for x in my_list if x!=23]) # list comprahention



(lambda x: x*3)(5)
# ==
def f(x):
    return x*3

f(5)
