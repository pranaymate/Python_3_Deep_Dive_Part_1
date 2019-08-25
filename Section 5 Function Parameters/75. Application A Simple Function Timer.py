
import time


def time_it(fn, *args, rep=5, **kwargs):
    print(args, rep, kwargs)


time_it(print, 1, 2, 3, sep='-')


print('#' * 52 + ' Lets modify our function to actually run the print function with any positional'
                 ' and keyword args (except for rep) passed to it:  ')


def time_it(fn, *args, rep=5, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep='-')

print('#' * 52 + ' We can even add more arguments:  ')

time_it(print, 1, 2, 3, sep='-', end=' *** ', rep=3)

print()
print('#' * 52 + ' Now all that iss really left for us to do is to time the function and return the average time:  ')


def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


print('#' * 52 + ' Lets write a few functions we might want to time:')
print('#' * 52 + ' We will create three functions that all do the same thing:'
                 ' calculate powers of n**k for k in some range of integer values ')


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))


print('#' * 52 + ' Lets run these functions and see the results:')

print(compute_powers_1(2, end=5))
print(compute_powers_2(2, end=5))
print(list(compute_powers_3(2, end=5)))

print('#' * 52 + ' Finally lets run these functions through our time_it function and see the results:')

print(time_it(compute_powers_1, n=2, end=20000, rep=4))
print(time_it(compute_powers_2, 2, end=20000, rep=4))
print(time_it(compute_powers_3, 2, end=20000, rep=4))

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
