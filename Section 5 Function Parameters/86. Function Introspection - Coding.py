print('#' * 52 + '  ### Function Introspection')


def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n

    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n - 1)


fact.short_description = "factorial function"

print(fact.short_description)

print('#' * 52 + '  We can see all the attributes that belong to a function using the **dir** function:')

print(dir(fact))

print('#' * 52 + '  We can see our **short_description** attribute, as well as some attributes we have seen before:'
                 '  **__annotations__** and **__doc__**:')

print(fact.__doc__)

print(fact.__annotations__)

print('#' * 52 + '  Well revisit some of these attributes later in this course, but lets take a look at a few here:')


def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass


f = my_func

print('#' * 52 + '  The **__name__** attribute holds the functions name:')

print(my_func.__name__)

print(f.__name__)

print('#' * 52 + '  The **__defaults__** attribute is a tuple containing any positional parameter defaults:')

print(my_func.__defaults__)
print(my_func.__kwdefaults__)

print('#' * 52 + '  Lets create a function with some local variables:')


def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b


print(my_func('a', 100))

print('#' * 52 + '  The **__code__** attribute contains a **code** object:')

print(my_func.__code__)

print('#' * 52 + '  This **code** object itself has various properties:')

print(dir(my_func.__code__))

print('#' * 52 + '  Attribute **__co_varnames__** is a tuple containing the parameter names and local variables:')

print(my_func.__code__.co_varnames)

print('#' * 52 + '  Attribute **co_argcount** returns the number of arguments (minus any \* and \*\* args)')

print(my_func.__code__.co_argcount)

print('#' * 52 + '  #### The **inspect** module')

import inspect

print(inspect.isfunction(my_func))

print('#' * 52 + '  By the way, there is a difference between a function and a method!'
                 '  A method is a function that is bound to some object:')

print(inspect.ismethod(my_func))


class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass


print('#' * 52 + '  **Instance methods** are bound to the **instance** of a class (not the class itself)')
print('#' * 52 + '  **Class methods** are bound to the **class**, not instances')
print('#' * 52 + '  **Static methods** are no bound either to the class or its instances')

print(inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance))
print(inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class))
print(inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static))

my_obj = MyClass()

print(inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance))
print(inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class))
print(inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static))

print('#' * 52 + '  If you just want to know if something is a function or method:')

print(inspect.isroutine(my_func))
print(inspect.isroutine(MyClass.f_instance))
print(inspect.isroutine(my_obj.f_class))
print(inspect.isroutine(my_obj.f_static))

print('#' * 52 + '  #### Introspecting Callable Code')
print('#' * 52 + '  We can get back the source code of our function using the **getsource()** method:')

print(inspect.getsource(fact))
print(inspect.getsource(MyClass.f_instance))
print(inspect.getsource(my_obj.f_instance))

print('#' * 52 + '  We can also find out where the function was defined:')

print(inspect.getmodule(fact))
print(inspect.getmodule(print))
import math

print(inspect.getmodule(math.sin))

print('#' * 52 + '  ')

# setting up variable
i = 10


# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass


print(inspect.getcomments(my_func))

print('#' * 52 + '  #### Introspecting Callable Signatures')


# TODO: Provide implementation
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass


print(inspect.signature(my_func))

print(type(inspect.signature(my_func)))

sig = inspect.signature(my_func)

print(dir(sig))

for param_name, param in sig.parameters.items():
    print(param_name, param)

print('#' * 52 + '  ')


def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')

    print('{0}\n{1}\n'.format(inspect.getcomments(f),
                              inspect.cleandoc(f.__doc__)))

    print('{0}\n{1}'.format('Inputs', '-' * len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')

    print('{0}\n{1}'.format('\n\nOutput', '-' * len('Output')))
    print(sig.return_annotation)


print_info(my_func)

print('#' * 52 + '  #### A Side Note on Positional Only Arguments')

help(divmod)

print(divmod(10, 3))
# print(divmod(x=10, y=3))  # TypeError: divmod() takes no keyword arguments

print('#' * 52 + '  Similarly, the string **replace** function also takes positional-only arguments,'
                 '  however, the documentation does not indicate this!')

help(str.replace)

print('#' * 52 + '  ')

print('abcdefg'.replace('abc', 'xyz'))

# print('abcdefg'.replace(old='abc', new='xyz'))  # TypeError: replace() takes no keyword arguments
