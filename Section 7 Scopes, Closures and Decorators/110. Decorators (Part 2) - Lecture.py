# The timed decorator
def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):  # HARDCODED VALUE 10
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result

    return inner


@timed
def my_func():
    pass


# OR

my_func = timed(my_func)

print('#' * 52 + '  One Approach')


def timed(fn, reps):  # extra parameter
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):  # FREE VARIABLE
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(avg_elapsed)
        return result

    return inner


my_func = timed(my_func, 10)  # will be work


@timed(10)  # ########## BAD, BAD, BAD !!! Will not work
def my_func():
    pass


print('#' * 52 + '  Nested closures to the rescue!')


def outer(reps):
    def timed(fn):  # extra parameter
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):  # FREE VARIABLE BOUND to reps in outer
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result

        return inner

    return timed

my_func = outer(10)(my_func) # GOOD  will be work

@outer(10)
def my_func():
    pass

