def outer():
    x = 'python'

    def inner():
        print("{0} rocks!".format(x))

    inner()


outer()

print('#' * 52 + '  Returning the inner function')


def outer():
    x = 'python'

    def inner():
        print("{0} rocks!".format(x))

    return inner  # when we return inner, we are actually "returning" the closure


fn = outer()
fn()


def outer():  # Here the value of x is shared between two scopes:
    x = 'python'  # outer

    def inner():  # closure
        print(x)

    return inner  # The label x is in two different scopes but always reference the same "value"


print('#' * 52 + '  Python does this by creating a cell as an intermediary object')
print('#' * 52 + '  In effect, both variables x (in outer and inner), point to the same cell')


def outer():
    a = 100
    x = 'python'

    def inner():
        a = 10 # local variable
        print("{0} rocks!".format(x))

    return inner


fn = outer()     # fn --> inner + extended scope x
fn()
print(fn)

# Introspection
print('#' * 52 + '  Introspection')


def outer():
    a = 100
    x = 'python'

    def inner():
        a = 10 # local variable
        print("{0} rocks!".format(x))

    return inner


fn = outer()

print(fn.__code__.co_freevars)  # --> ('x,')  (a is not a free variable)
print(fn.__closure__)           # --> (<cell at 0xA500


def outer():
    x = 'python'
    print(hex(id(x)))

    def inner():
        print(hex(id(x)))
        print("{0} rocks!".format(x))
    return inner


fn = outer()
fn()

print('#' * 52 + '  Modyfying free variables')


def counter():           #  closure
    count = 0            # count is a free variable
                         # it is bound to the cell count

    def inc():
        nonlocal count
        count += 1
        return count
    return inc


fn = counter()    # --> fn --> inc + count --> 0
print(fn())              # counts indirect reference changed from the object 0 to the object 1)
print(fn())
print(fn())
print(fn())

print('#' * 52 + '  Multiple Instance of Closures')


def counter():           #  closure
    count = 0            # count is a free variable
                         # it is bound to the cell count

    def inc():
        nonlocal count
        count += 1
        return count
    return inc


f1 = counter()
f2 = counter()

print(f1())
print(f1())
print(f1())
print(f1())
print(f2())

print('#' * 52 + '  Shared Extended Scopes')


def counter():           #  closure
    count = 0            # count is a free variable
                         # it is bound to the cell count

    def inc1():
        nonlocal count   # count is a fee variable - bound to count in the extended scope
        count += 1
        return count

    def inc2():
        nonlocal count   # count is a fee variable - bound to the same count
        count += 1
        return count

    return inc1, inc2    # returns a tuple containing both closures


f1, f2 = counter()

print(f1())
print(f2())
print(f1())

print('#' * 52 + '  Shared Extended Scopes')
print('#' * 52 + '  You may think this shared extended scope is highly unusual… but its not!')


def adder(n):
    def inner(x):
        return x + n

    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1(10))
print(add_2(10))
print(add_3(10))

print('#' * 52 + '  Nested Closure')


def incremental(n):
    # inner +n is a closure
    def inner(start):
        current = start
        # inc + current + n is a closure

        def inc():
            nonlocal current
            current += n
            return current

        return inc
    return inner


fn = incremental(2)
print(fn.__code__.co_freevars)  # n, n = 2
inc_2 = fn(100)
print(inc_2.__code__.co_freevars)  # 'current', 'n', current = 100, n = 2

print(inc_2())
print(inc_2())
