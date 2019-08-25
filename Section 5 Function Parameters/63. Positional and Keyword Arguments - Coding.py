def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(1, 2, 3)


def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))

# def fn(a, b=2, c):
#     print(a, b, c)

# File "<ipython-input-4-2180ec769037>", line 1
#     def fn(a, b=2, c):
#           ^
# SyntaxError: non-default argument follows default argument


def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(10, 20, 30)

my_func(10, 20)

my_func(10)

# my_func()
#
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-d82eda95de40> in <module>()
# ----> 1 my_func()
#
# TypeError: my_func() missing 1 required positional argument: 'a'


def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(c=30, b=20, a=10)

my_func(10, c=30, b=20)

# my_func(10, b=20, 30)

#   File "<ipython-input-13-ea05eeab2151>", line 1
#     my_func(10, b=20, 30)
#                      ^
# SyntaxError: positional argument follows keyword argument

my_func(10, c=30)

my_func(a=30, c=10)

my_func(c=10, a=30)