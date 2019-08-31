print('#' * 52 + '  Functions defined inside anther function can reference variables from that enclosing scope, '
                 '  just like functions can reference variables from the global scope.')


def outer_func():
    x = 'hello'

    def inner_func():
        print(x)

    inner_func()


outer_func()

print('#' * 52 + '  Functions defined inside anther function can reference variables from that enclosing scope,'
                 '  just like functions can reference variables from the global scope.')


def outer_func():
    x = 'hello'

    def inner1():
        def inner2():
            print(x)

        inner2()

    inner1()


outer_func()

print('#' * 52 + '  But if we **assign** a value to a variable, it is considered part of the local scope,'
                 '  and potentially **masks** enclsogin scope variable names:')


def outer():
    x = 'hello'

    def inner():
        x = 'python'

    inner()
    print(x)


outer()

print('#' * 52 + '  As you can see, **x** in **outer** was not changed.')
print('#' * 52 + '  To achieve this, we can use the **nonlocal** keyword:')


def outer():
    x = 'hello'
    print(x)

    def inner():
        nonlocal x
        x = 'python'

    inner()
    print(x)


outer()

print('#' * 52 + '  Of course, this can work at any level as well:')


def outer():
    x = 'hello'

    def inner1():
        def inner2():
            nonlocal x
            x = 'python'

        inner2()

    inner1()
    print(x)


outer()

print('#' * 52 + '  ')


def outer():
    x = 'hello'

    def inner1():
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)

    inner1()
    print('outer:', x)


outer()

print('#' * 52 + '  We can change this behavior by making the variable `x` in `inner` nonlocal as well:')


def outer():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)

    inner1()
    print('outer:', x)


outer()

print('#' * 52 + '  ')

x = 100


def outer():
    x = 'python'  # masks global x

    def inner1():
        nonlocal x  # refers to x in outer
        x = 'monty' # changed x in outer scope

        def inner2():
            nonlocal x  # refers to x in global scope
            x = 'hello'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)


outer()
print(x)
