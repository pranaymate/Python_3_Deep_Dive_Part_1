print('#' * 52 + '  When we call help() on a class, function, module, etc, '
                 '  Python will typically display some information:')

help(print)

print('#' * 52 + '  We can define such help using docstrings and annotations.')


def my_func(a, b):
    return a*b

help(my_func)

print('#' * 52 + '  Pretty bare! So lets add some additional help:')


def my_func(a, b):

    'Returns the product of a and b'

    return a*b

help(my_func)

print('#' * 52 + '  Docstrings can span multiple lines using a multi-line string literal:')


def fact(n):
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)


help(fact)

print('#' * 52 + '  Docstrings, when found, are simply attached to the function in the __doc__ property:')

print(fact.__doc__)

print('#' * 52 + '  And the Python help() function simply returns the contents of __doc__')

print('#' * 52 + '  We can also add metadata annotations to a functions parameters and return. '
                 '  These metadata annotations can be any expression (string, type, function call, etc)')


def my_func(a: 'annotation for a',
            b: 'annotation for b') -> 'annotation for return':
    return a * b


help(my_func)

print('#' * 52 + '  The annotations can be any expression, not just strings:')

x = 3
y = 5

def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

help(my_func)

print('#' * 52 + '  Note that these annotations do not force a type on the parameters or the return value - '
                 '  they are simply there for documentation purposes within Python and '
                 '  may be used by external applications and modules, such as IDEs.')

print('#' * 52 + '  Just like docstrings are stored in the __doc__ property, annotations are stored in the'
                 ' __annotations__ property - a dictionary whose keys are the parameter names, '
                 '  and values are the annotation.')

print(my_func.__annotations__)

print('#' * 52 + '  Of course we can combine both docstrings and annotations:')


def fact(n: 'int >= 0') -> int:
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)


help(fact)

print('#' * 52 + '  Annotations will work with default parameters too: just specify the default after the annotation:')


def my_func(a: str = 'a', b:int = 1)->str:
    return a*b


help(my_func)

print(my_func())

print(my_func('abc', 3))


def my_func(a:int=0, *args:'additional args'):
    print(a, args)


print(my_func.__annotations__)

help(my_func)