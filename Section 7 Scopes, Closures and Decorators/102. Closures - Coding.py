print('#' * 52 + '  Lets examine that concept of a cell to create an indirect reference for variables that are'
                 ' in multiple scopes.')


def outer():
    x = 'python'

    def inner():
        print(x)
    return inner


fn = outer()
print(fn.__code__.co_freevars)

print('#' * 52 + '  As we can see, `x` is a free variable in the closure.')
print(fn.__closure__)

print('#' * 52 + '  Lets see what the memory address of `x` is in the outer function and the inner function. ')
print('#' * 52 + '  To be sure string interning does not play a role, I am going to use an object that'
                 '  we know Python will not automatically intern, like a list.')


def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))

    def inner():
        print('inner:', hex(id(x)))
        print(x)
    return inner


fn = outer()
print(fn.__closure__)
fn()

print('#' * 52 + '  #### Modifying the Free Variable')
print('#' * 52 + '  We know we can modify nonlocal variables by using the `nonlocal` keyword.')


def counter():
    count = 0  # local variable

    def inc():
        nonlocal count  # this is the count variable in counter
        count += 1
        return print(count)

    return inc


c = counter()

c()
c()
c()

print('#' * 52 + '  ##### Shared Extended Scopes')


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2


fn1, fn2 = outer()

print(fn1.__closure__, fn2.__closure__)
print(fn1())
print(fn1())
print(fn1())
print(fn2())

print('#' * 52 + '  ### Multiple Instances of Closures')
print('#' * 52 + '  Recall that **every** time a function is called, a **new** local scope is created.')

from time import perf_counter


def func():
    x = perf_counter()
    print(x, id(x))


func()
func()
func()

print('#' * 52 + '  The same thing happens with closures, they have their own extended scope every time the closure'
                 ' is created:')


def pow(n):
    # n is local to pow
    def inner(x):
        # x is local to inner
        return x ** n
    return inner


square = pow(2)

print(square(5))

cube = pow(3)

print(cube(5))

print('#' * 52 + '  We can see that the cell used for the free variable in both cases is **different**:')

print(square.__closure__)
print(cube.__closure__)

print('#' * 52 + '  In fact, these functions (`square` and `cube`) are **not** the same functions, '
                 '  even though they were "created" from the same `power` function:')

print(id(square), id(cube))

print('#' * 52 + '  Remember when I said the captured variable is a reference established when the closure is created, '
                 '  but the value is looked up only once the function is called?')
print('#' * 52 + '  This can create very subtle bugs in your program.')


def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)

print(add_1(10), add_2(10), add_3(10), add_4(10))

print('#' * 52 + '  But suppose we want to get a little fancier and do it as follows:')
print('#' * 52 + '  Now technically we have 4 functions in the `adders` list:')


def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders


adders = create_adders()
print(adders)

print(adders[3](10))
print(adders[0](10))

print(adders[0](10), adders[1](10), adders[2](10), adders[3](10))

print('#' * 52 + '  When the lambdas are **created** their `n` is the `n` used in the loop - the **same** `n`!!')

print(adders[0].__code__.co_freevars)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[3].__closure__)

print('#' * 52 + '  So, by the time we call `adder[i]`, the free variable `n` (shared between all adders) is set to 4.')

print(hex(id(4)))

print('#' * 52 + '  Correct step to solve this issue')


def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders


adders = create_adders()
print(adders[0].__closure__)
print('#' * 52 + '  Why arent we getting anything in the closure? What about free variables?')
print(adders[0].__code__.co_freevars)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print(adders[3](10))

print('#' * 52 + '  #### Nested Closures')


def incrementer(n):
    def inner(start):
        current = start

        def inc():
            a = 10  # local var
            nonlocal current
            current += n
            return current

        return inc

    return inner


fn = incrementer(2)
print(fn)
print(fn.__code__.co_freevars)
print(fn.__closure__)

inc_2 = fn(100)
print(inc_2)

print(inc_2.__code__.co_freevars)
print(inc_2.__closure__)

print('#' * 52 + '  Here you can see that the second free variable `n`, '
                 '  is pointing to the same cell as the free variable in `fn`.')
print('#' * 52 + '  Note that **a** is a local variable, and is not considered a free variable.')
print('#' * 52 + '  And we can call the closures as follows:')

print(inc_2())
print(inc_2())
print(inc_2())

print('#' * 52 + '  ')

inc_3 = incrementer(3)(200)

print(inc_3())
print(inc_3())
print(inc_3())
