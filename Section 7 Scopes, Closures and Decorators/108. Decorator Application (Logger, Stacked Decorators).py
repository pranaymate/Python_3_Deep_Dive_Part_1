print('#' * 52 + '  In this example were going to create a utility decorator that will log function calls '
                 '  (to the console, but in practice you would be writing your logs to a file '
                 '  (e.g. using Pythons built-in logger), or to a database, etc.')


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__, run_dt))
        return result

    return inner


@logged
def func_1():
    pass


@logged
def func_2():
    pass


func_1()
func_2()

print('#' * 52 + '  Now we may additionaly also want to time the function. '
                 '  We can certainly include the code to do so in our logged decorator, '
                 '  but we could also just use the @timed decorator we already wrote by stacking our decorators.')


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end - start))
        return result

    return inner


@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


print(factorial(10))

print('#' * 52 + '  Note that the order in which we stack the decorators can make a difference!')
print('#' * 52 + '  Remember that this is because our stacked decorators essentially amounted to:')


def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


factorial = timed(logged(factorial))

print(factorial(10))

print('#' * 52 + '  But in the following case, the logged decorator will run first, followed by the timed decorator:')


def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


factorial = logged(timed(factorial))

print(factorial(10))

print('#' * 52 + '  Or, using the @ notation:')


@logged
@timed
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


print(factorial(10))


@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


print(factorial(10))

print('#' * 52 + '  To make this clearer, lets write two very simple decorators as follows:')


def dec_1(fn):
    def inner():
        print('running dec_1')
        return fn()
    return inner


def dec_2(fn):
    def inner():
        print('running dec_2')
        return fn()
    return inner


@dec_1
@dec_2
def my_func():
    print('running my_func')


my_func()

print('#' * 52 + '  But if we change the order of the decorators:')


@dec_2
@dec_1
def my_func():
    print('running my_func')


my_func()



