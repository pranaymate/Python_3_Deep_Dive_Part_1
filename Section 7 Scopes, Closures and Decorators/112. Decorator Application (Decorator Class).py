print('#' * 52 + '  If you recalls how we wrote a parameterized decorator, '
                 '  we had to write a decorator factory that took in the arguments for our decorator'
                 '  and then returned the decorator (which could reference the arguments as free variables).')


def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec


@my_dec(10, 20)
def my_func(s):
    print('hello {0}'.format(s))


my_func('world')

print('#' * 52 + '  Now, recall that we can make our class instances callable, '
                 '  simply by implementing the `__call__` method.')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))


my_class = MyClass(10, 20)
my_class()

print('#' * 52 + '  So lets modify this just a bit, and have the `__call__` method be our decorator!')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)

        return inner


@MyClass(10, 20)
def my_func(s):
    print('Hello {0}!'.format(s))


my_func('Python')

print('#' * 52 + '  So as you can see, we can also use callable classes to decorate functions!')
