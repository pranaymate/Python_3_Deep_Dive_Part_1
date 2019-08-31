print('#' * 52 + '  First recall our original timer decorator from an earlier video (Decorator Application - Timer):')


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print('Run time: {0:.6f}s'.format(elapsed))
        return result

    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 1) + calc_fib_recurse(n - 2)


def fib(n):
    return calc_fib_recurse(n)


print('#' * 52 + '  We can decorate our Fibonacci function using the **@** syntax, or the longer syntax as follows:')

fib = timed(fib)
print(fib(30))

print(
    '#' * 52 + '  Lets modify this so the timer runs the function multiple times and calculates the average run time:')


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print('Avg Run time: {0:.6f}s'.format(avg_elapsed))
        return result

    return inner


print('#' * 52 + '  And again we decorate it using the long syntax:')


def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib)
print(fib(28))

print('#' * 52 + '  But that value of 10 has been hardcoded. Lets make it a parameter instead')


def timed(fn, num_reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(num_reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / num_reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                         num_reps))
        return result

    return inner


print('#' * 52 + '  Now to decorate our Fibonacci function we **have** to use the long syntax '
                 '  (as we saw in the lecture, the **@** syntax will not work):')


def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib, 5)

print(fib(28))

print('#' * 52 + '  The problem is that we cannot use the `@` decorator syntax because'
                 '  when using that syntax Python passes a **single** argument to the decorator:'
                 '  the function we are decorating - nothing else.')
print('#' * 52 + '  Of course we could just use what we did above, but the decorator syntax is kind of neat,'
                 '  so it would be nice to retain the ability to use it.')

print('#' * 52 + '  Lets try a concrete example:')


def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)

    return inner


@dec
def my_func():
    print('running my_func')


my_func()

print('#' * 52 + '  But what if `dec` was not the decorator itself, but instead created and returned a decorator?')


def dec_factory():
    print('running dec_factory')
    def dec(fn):
        print('running dec')
        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)
        return inner
    return dec


print('#' * 52 + '  So as you can see, calling `dec_generator()` '
                 '  will return that `dec` function which is our decorator:')


@dec_factory()
def my_func(a, b):
    print(a, b)


print('#' * 52 + '  You can see that both `dec_generator` and `dec` were already called.')

my_func(10, 20)

print('#' * 52 + '  And there you go, all we did is basically create a decorator by calling a function (`dec_factory`)'
                 '  and use the return value of that call (the `dec` function) as our actual decorator.')

print('#' * 52 + '  We could have done the decoration this way too:')

dec = dec_factory()


@dec
def my_func():
    print('running my_func')


my_func()

print('#' * 52 + '  Or even this way:')

dec = dec_factory()


def my_func():
    print('running my_func')


my_func = dec(my_func)

my_func()

print('#' * 52 + '  Of course we could even decorate it this way using a single statement:')


def my_func():
    print('running my_func')


my_func = dec_factory()(my_func)

my_func()

print('#' * 52 + '  OK, so now we have decorated our function using, not a decorator, '
                 '  but a decorator factory as follows:')


def dec_factory():
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            return fn(*args, **kwargs)
        return inner
    return dec


@dec_factory()
def my_func(a, b):
    return a + b


print(my_func(10, 20))

print('#' * 52 + '  You should note that in this approach, we are **calling** `dec_factory()`,'
                 '  [note the parentheses `()`], and **then** using the return value'
                 '  (a decorator) to decorate our function.')

print('#' * 52 + '  So, we could pass arguments as we do so without affecting the final outcome')
print('#' * 52 + '  In fact we can even access them from anywhere inside `dec_factory`,'
                 '  including any of the nested functions! ')


def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free vars: ', a, b)  # a and b are free variables!
            return fn(*args, **kwargs)
        return inner
    return dec


@dec_factory(10, 20)
def my_func():
    print('python rocks')


print(my_func())

print('#' * 52 + '  So now, lets go back to our original problem where we wanted our timing decorator to run'
                 '  a number of loops which could be specified as a parameter when decorating the function'
                 '  we want to time.')


def timed(fn, num_reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(num_reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / num_reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                         num_reps))
        return result

    return inner


print('#' * 52 + '  So, all we need to do is create an outer function around our timed decorator, '
                 '  and pass the `num_reps` argument to that outer function instead:')


def timed_factory(num_reps=1):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return timed


@timed_factory(5)
def fib(n):
    return calc_fib_recurse(n)


print(fib(30))

print('#' * 52 + '  Just to put the finishing touch on this, we probably dont want to have our outer function'
                 '  named the way it is (`timed_factory`).')

from functools import wraps


def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator


@timed(5)
def fib(n):
    return calc_fib_recurse(n)


print(fib(30))
