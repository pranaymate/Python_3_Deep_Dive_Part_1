def counter(initial_value):
    # initial_value is a local variable her

    def inc(increment=1):
        nonlocal initial_value
        # initial_value is a nonlocal (captured) variable here
        initial_value += increment
        return initial_value

    return inc


counter1 = counter(0)

print(counter1(0))
print(counter1())
print(counter1())
print(counter1())
print(counter1(8))

counter2 = counter(1000)

print(counter2(1))
print(counter2())
print(counter2(220))

print('#' * 52 + '  Lets modify this example to now build something that can run,'
                 '  and maintain a count of how many times we have run some function.')


def counter(fn):
    cnt = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


counted_add = counter(add)

print(counted_add.__code__.co_freevars)

print('#' * 52 + '  We can now call the `counted_add` function:')

print(counted_add(1, 2))

print(counted_add(2, 3))


def mult(a, b, c):
    return a * b * c


counted_mult = counter(mult)

print(counted_mult(1, 2, 3))
print(counted_mult(2, 3, 4))

print('#' * 52 + '  Lets take this one step further, and actually store the function name and the number of calls'
                 '  in a global dictionary instead of just printing it out all the time.	')

counters = dict()


def counter(fn):
    cnt = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)

    return inner


counted_add = counter(add)
counted_mult = counter(mult)

print('#' * 52 + '  Note that `counters` is a **global** variable, and therefore **not** a free variable:')

print(counted_add.__code__.co_freevars)
print(counted_mult.__code__.co_freevars)

print('#' * 52 + '  We can now call out functions:')

print(counted_add(1, 2))
print(counted_add(2, 3))
print(counted_mult(1, 2, 'a'))
print(counted_mult(2, 3, 'b'))
print(counted_mult(1, 1, 'abc'))

print(counters)

print('#' * 52 + '  Of course this relies on us creating the **counters** global variable first and making sure we'
                 '  are naming it that way, so instead, were going to pass it as an argument'
                 '  to the **counter** function:')


def counter(fn, counters):
    cnt = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is nonlocal
        return fn(*args, **kwargs)

    return inner


func_counters = dict()
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)

print(counted_add.__code__.co_freevars)

print('#' * 52 + '  As you can see, `counters` is now a free variable.')
print('#' * 52 + '  We can now call our functions:')

for i in range(5):
    counted_add(i, i)

for i in range(10):
    counted_mult(i, i, i)

print(func_counters)

print('#' * 52 + '  Of course, we dont have to assign the "counted" version of our functions a new name'
                 '  - we can simply assign it to the same name!')


def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product


fact = counter(fact, func_counters)

print(fact(0))
print(fact(3))
print(fact(4))

print(func_counters)
