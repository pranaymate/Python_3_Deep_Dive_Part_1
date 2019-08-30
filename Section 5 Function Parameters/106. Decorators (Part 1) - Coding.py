print('#' * 52 + '  Recall the example in the last section where we wrote a simple closure to count how many times '
                 '  a function had been run:')


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner

def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b

help(add)

print(id(add))

print('#' * 52 + '  Now we create a closure using the add function as an argument to the counter function:')

add = counter(add)

print('#' * 52 + '  And you wiill note that add is no longer the same function as before. '
                 '  Indeed the memory address add points to is no longer the same:')

print(id(add))

print(add(1, 2))
print(add(2, 2))


print('#' * 52 + '  What happened is that we put our add function through'
                 '  the counter function - we usually say that we decorated our function add.')
print('#' * 52 + '  And we call that counter function a decorator.')
print('#' * 52 + '  There is a shorthand way of decorating our function without having to type:')

# func = counter(func)


@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c


print(mult(1, 2, 3))
print(mult(2, 2, 2))

print('#' * 52 + '  Lets do a little bit of introspection on our two decorated functions:')
print(add.__name__)
print(mult.__name__)

print('#' * 52 + '  As you can see, the name of the function is no longer add or mult, '
                 '  but instead it is the name of that inner function in our decorator.')

help(add)
help(mult)

print('#' * 52 + '  As you can see, we have also lost our docstring and parameter annotations!')
print('#' * 52 + '  What about introspecting the parameters of add and mult:')

import inspect
print(inspect.getsource(add))
print('#' * 52 + '  ')
print(inspect.getsource(mult))

print('#' * 52 + '  Even the signature is gone:')
print(inspect.signature(add))
print(inspect.signature(mult))

print('#' * 52 + '  Even the parameter defaults documentation is are gone:')
print(inspect.signature(add).parameters)

print('#' * 52 + '  In general, when we create decorated functions, we end up "losing" a lot '
                 '  of the metadata of our original function!')
print('#' * 52 + '  However, we can put that information back in - it can get quite complicated.')
print('#' * 52 + '  Lets see how we might be able to do that for some simple things, '
                 '  like the docstring and the function name.')


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner


@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b


help(add)
print(add.__name__)

print('#' * 52 + '  At least we have the docstring and function name back... ')
print('#' * 52 + '  But what about the parameters?')
print('#' * 52 + '  Our real add function takes two positional parameters, '
                 '  but because the closure used a generic way of accepting *args and **kwargs, '
                 '  we lose this information')
print('#' * 52 + '  We can use a special function in the functools module, called wraps. '
                 '  In fact, that function is a decorator itself!')

from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b


help(add)

print('#' * 52 + '  Yay!!! Everything is back to normal.')

print(inspect.getsource(add))
print(inspect.signature(add))
print(inspect.signature(add).parameters)