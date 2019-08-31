a = 10

# def my_func(n):
#     c = n ** 2
#     return c
#
#
# def my_func(n):
#     print('global:', a)
#     c = a ** n
#     return print(c)
#
# my_func(2)
# my_func(3)

print('#' * 52 + '  ')
print('# But remember that the scope of a variable is determined by where it is assigned. In particular, any variable'
      ' defined (i.e. assigned a value) inside a function is local to that function, even if the variable name'
      ' happens to be global too! ')


def my_func(n):
    a = 2
    c = a ** 2
    return c


print(a)
print(my_func(8))
print(a)

print('#' * 52 + ' In order to change the value of a global variable within an inner scope, we can use the **global**'
                 ' keyword as follows: ')


def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c


print(a)
print(my_func(3))
print(a)

print('#' * 52 + '  ')
print()


def my_func(n):
    global var
    var = 'hello world'
    return n ** 2


# print(var)    # NameError: name 'var' is not defined

print(my_func(2))
print(var)

print('#' * 52 + '  Remember that whenever you assign a value to a variable without having specified the variable'
                 ' as **global**, it is **local** in the current scope. **Moreover**, it does not matter **where**'
                 ' the assignment in the code takes place, the variable is considered local in the **entire** '
                 ' scope - Python determines the scope of objects at compile-time, not at run-time.')

a = 10
b = 100


def my_func():
    print(a)
    print(b)


my_func()

print('#' * 52 + '  ')

a = 10
b = 100

# def my_func():
#     print(a)
#     print(b)
#     b = 1000  # UnboundLocalError: local variable 'b' referenced before assignment
#
#
# my_func()

print('#' * 52 + '  Of course, functions are also objects, and scoping applies equally to function objects too. '
                 '  For example, we can "mask" the built-in `print` Python function:')

print = lambda x: 'hello {0}!'.format(x)


def my_func(name):
    return print(name)


my_func('world')

del print
