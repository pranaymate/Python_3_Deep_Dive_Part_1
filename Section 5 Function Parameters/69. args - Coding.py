
print('#' * 52 + ' Recall from iterable unpacking:')
a, b, *c = 10, 20, 'a', 'b'
print(a, b)
print(c)

print('#' * 52 + ' We can use a similar concept in function definitions to allow for arbitrary'
                 ' numbers of positional parameters/arguments:')

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)


func1(1, 2, 'a', 'b')

print('#' * 52 + ' Unlike iterable unpacking, *args will be a tuple, not a list.')
print('#' * 52 + ' The name of the parameter args can be anything you prefer')
print('#' * 52 + ' You cannot specify positional arguments after the *args parameter - '
                 ' this does something different that we will cover in the next lecture.')


def func1(a, b, *my_vars):
    print(a)
    print(b)
    print(my_vars)


func1(10, 20, 'a', 'b', 'c')


def func1(a, b, *c, d):
    print(a)
    print(b)
    print(c)
    print(d)

# func1(10, 20, 'a', 'b', 100)  # TypeError: func1() missing 1 required keyword-only argument: 'd'


print('#' * 52 + ' Lets see how we might use this to calculate the average of an arbitrary number of parameters.')


def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count


print(avg(2, 2, 4, 4))


def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count


print(avg(2, 2, 4, 4))
print(avg())

print('#' * 52 + ' But we may not want to allow specifying zero arguments, '
                 ' in which case we can split our parameters into a required (non-defaulted) positional argument, '
                 ' and the rest:')


def avg(a, *args):
    count = len(args) + 1
    total = a + sum(args)
    return total/count


print(avg(2, 2, 4, 4))


print('#' * 52 + ' Unpacking an iterable into positional arguments')


def func1(a, b, c):
    print(a)
    print(b)
    print(c)


l = [10, 20, 30]

# func1(l)          # TypeError: func1() missing 2 required positional arguments: 'b' and 'c'


print('#' * 52 + ' But we could unpack the list, and then pass it to as the function arguments:')
print(*l,)
func1(*l)

print('#' * 52 + ' What about mixing positional and keyword arguments with this?')


def func1(a, b, c, *d):
    print(a)
    print(b)
    print(c)
    print(d)

# func1(10, c=20, b=10, 'a', 'b') # SyntaxError: positional argument follows keyword argument

