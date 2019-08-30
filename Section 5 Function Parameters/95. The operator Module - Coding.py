import operator

print(dir(operator))

print('#' * 52 + '  #### Arithmetic Operators')

print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.pow(2, 3))
print(operator.mod(13, 2))
print(operator.floordiv(13, 2))
print(operator.truediv(3, 2))

print('#' * 52 + '  These would have been very handy in our previous section:')

from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))

print('#' * 52 + '  Instead of defining a lambda, we could simply use **operator.mul**:')

print(reduce(operator.mul, [1, 2, 3, 4]))

print('#' * 52 + '  #### Comparison and Boolean Operators')

print(operator.lt(10, 100))
print(operator.le(10, 10))
print(operator.is_('abc', 'def'))

print('#' * 52 + '  We can even get the truthyness of an object:')

print(operator.truth([1, 2]))
print(operator.truth([]))
print(operator.and_(True, False))
print(operator.or_(True, False))

print('#' * 52 + '  #### Element and Attribute Getters and Setters')

my_list = [1, 2, 3, 4]
print(my_list[1])

print('#' * 52 + '  We can do the same thing using:')

print(operator.getitem(my_list, 1))

print('#' * 52 + '  If the sequence is mutable, we can also set or remove items:')

my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)

operator.delitem(my_list, 3)
print(my_list)

print('#' * 52 + '  We can also do the same thing using the **operator** modules **itemgetter** function.')
print('#' * 52 + '  The difference is that this returns a callable:')

f = operator.itemgetter(2)

print(f(my_list))

x = 'python'
print(f(x))

print('#' * 52 + '  Furthermore, we can pass more than one index to **itemgetter**:')

f = operator.itemgetter(2, 3)

my_list = [1, 2, 3, 4]
print(f(my_list))

x = 'pytyhon'
print(f(x))

print('#' * 52 + '  Similarly, **operator.attrgetter** does the same thing, but with object attributes.')


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()

print(obj.a, obj.b, obj.c)
f = operator.attrgetter('a')
print(f(obj))

my_var = 'b'
print(operator.attrgetter(my_var)(obj))

my_var = 'c'
print(operator.attrgetter(my_var)(obj))

f = operator.attrgetter('a', 'b', 'c')

print(f(obj))

print('#' * 52 + '  Of course, attributes can also be methods.')
print('#' * 52 + '  In this case, **attrgetter** will return the object s **test** method -'
                 '  a callable that can then be called using **()**:')

f = operator.attrgetter('test')
obj_test_method = f(obj)

obj_test_method()

print('#' * 52 + '  Just like lambdas, we do not need to assign them to a variable name in order to use them:')

print(operator.attrgetter('a', 'b')(obj))
print(operator.itemgetter(2, 3)('python'))

print('#' * 52 + '  Of course, we can achieve the same thing using functions or lambdas:')

f = lambda x: (x.a, x.b, x.c)

print(f(obj))
f = lambda x: (x[2], x[3])
print(f([1, 2, 3, 4]))

print(f('python'))

print('#' * 52 + '  ##### Use Case Example: Sorting')

print('#' * 52 + '  Suppose we want to sort a list of complex numbers based on the real part of the numbers:')

a = 2 + 5j
print(a.real)

l = [10 + 1j, 8 + 2j, 5 + 3j]
print(sorted(l, key=operator.attrgetter('real')))

print('#' * 52 + '  Or if we want to sort a list of string based on the last character of the strings:')

l = ['aaz', 'aad', 'aaa', 'aac']
print(sorted(l, key=operator.itemgetter(-1)))

print('#' * 52 + '  Or maybe we want to sort a list of tuples based on the first item of each tuple:')

l = [(2, 3, 4), (1, 2, 3), (4,), (3, 4)]
print(sorted(l, key=operator.itemgetter(0)))

print('#' * 52 + '  #### Slicing')

l = [1, 2, 3, 4]
print(l[0:2])

l[0:2] = ['a', 'b', 'c']
print(l)

del l[3:5]
print(l)

print('#' * 52 + '  We can do the same thing this way:')

l = [1, 2, 3, 4]

print(operator.getitem(l, slice(0, 2)))

operator.setitem(l, slice(0, 2), ['a', 'b', 'c'])
print(l)

operator.delitem(l, slice(3, 5))
print(l)

print('#' * 52 + '  #### Calling another Callable')

x = 'python'
print(x.upper())

print(operator.methodcaller('upper')('python'))

print('#' * 52 + '  Of course, since **upper** is just an attribute of the string object **x**,'
                 '  we could also have used:')

print(operator.attrgetter('upper')(x)())

print('#' * 52 + '  If the callable takes in more than one parameter, '
                 '  they can be specified as additional arguments in **methodcaller**:')


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, c):
        print(self.a, self.b, c)


obj = MyClass()
print(obj.do_something(100))
print(operator.methodcaller('do_something', 100)(obj))

print('#' * 52 + '  ')


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, *, c):
        print(self.a, self.b, c)


print(obj.do_something(c=100))

print(operator.methodcaller('do_something', c=100)(obj))