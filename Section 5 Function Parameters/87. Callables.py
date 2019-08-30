print('#' * 52 + '  ### Callables')
print(
    '#' * 52 + '  A callable is an object that can be called (using the **()** operator), and always returns a value.')
print('#' * 52 + '  We can check if an object is callable by using the built-in function **callable**')

print(callable(print))
print(callable(len))

l = [1, 2, 3]
print(callable(l.append))

s = 'abc'
print(callable(s.upper))

print('#' * 52 + '  ##### Callables **always** return a value:')

result = print('hello')
print(result)

l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)

s = 'abc'
result = s.upper()
print(result)

print('#' * 52 + '  ##### Classes are callable:')

from decimal import Decimal

print(callable(Decimal))

result = Decimal('10.5')
print(result)

print('#' * 52 + '  ##### Class instances may be callable:')


class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0

    def __call__(self, x=1):
        self.counter += x
        print(self.counter)


my_obj = MyClass()  # initializing

print(callable(my_obj.__init__))
print(callable(my_obj.__call__))

my_obj()
my_obj()
my_obj(10)
