print('#' * 52 + '  Here we go back to an example we have seen in the past - timing how long it takes to run '
                 '  a certain function.')


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str,
                                                      elapsed))
        return result

    return inner


print('#' * 52 + '  ')
print('#' * 52 + ' Lets write a function that calculates the n-th Fibonacci number: ')
print('#' * 52 + '  We will implement this using three different methods:')
print('#' * 52 + '  1. recursion')
print('#' * 52 + '  2. a loop')
print('#' * 52 + '  3. functional programming (reduce)')
print('')
print('')
print('#' * 52 + '  Using Recursion')


def calc_recursive_fib(n):
    if n <=2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


print(calc_recursive_fib(3))
print(calc_recursive_fib(6))


@timed
def fib_recursed(n):
    return calc_recursive_fib(n)


print(fib_recursed(33))
print(fib_recursed(34))
print(fib_recursed(35))


print('#' * 52 + '  There is a reason we did not decorate our recursive function directly!')


@timed
def fib_recursed_2(n):
    if n <=2:
        return 1
    else:
        return fib_recursed_2(n-1) + fib_recursed_2(n-2)


print(fib_recursed_2(10))

print('#' * 52 + '  Since we are calling the function recursively, '
                 '  we are actually calling the decorated function recursively. ')
print('#' * 52 + '  In this case I wanted the total time to calculate the n-th number, '
                 '  not the time for each recursion.')
print('#' * 52 + '  You will notice from the above how inefficient the recursive method is: '
                 '  the same fibonacci numbers are calculated repeatedly! ')
print('#' * 52 + '  This is why as the value of n start increasing beyond 30 we start seeing considerable slow downs.')
print('')
print('')

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  Using a Loop')


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(3))
print(fib_loop(6))
print(fib_loop(34))
print(fib_loop(35))

print('#' * 52 + '  As you can see this method is much more efficient!')

print('')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('')
print('#' * 52 + '  Using Reduce')

'''We first need to understand how we are going to calculate the Fibonnaci sequence using reduce:

n=1:
(1, 0) --> (1, 1)

n=2:
(1, 0) --> (1, 1) --> (1 + 1, 1) = (2, 1)  : result = 2 

n=3
(1, 0) --> (1, 1) --> (2, 1) --> (2+1, 2) = (3, 2)  : result = 3

n=4
(1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3)  : result = 5

In general each step in the reduction is as follows:

previous value = (a, b)
new value = (a+b, a)

If we start our reduction with an initial value of (1, 0), we need to run our "loop" n times.

We therefore use a "dummy" sequence of length n to create n steps in our reduce.
'''

from functools import reduce


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]


print(fib_reduce(3))
print(fib_reduce(6))
print(fib_reduce(34))
print(fib_reduce(35))

print('')
print('')
print('#' * 52 + '  Now we can run a quick comparison between the various timed implementations:')

print(fib_recursed(35))
print(fib_loop(35))
print(fib_reduce(35))

print('#' * 52 + '  Even though the recursive algorithm is by far the easiest to understand, it is also the slowest.')
print('#' * 52 + '  We will see how to fix this in an upcoming video using a technique called memoization.')
print('#' * 52 + '  First lets focus on the loop and reduce variants. ')
print('#' * 52 + '  Our timing is not very effective since we only time a single calculation for each - '
                 '  there could be some variance if we run these tests multiple times:')

for i in range(10):
    result = fib_loop(10000)
print('#' * 52 + '  ')
print('#' * 52 + '  ')
for i in range(10):
    result = fib_reduce(10000)

print('#' * 52 + '  In general it is better to time the same function call multiple times and '
                 '  generate and average of the run times.')
print('#' * 52 + '  In the meantime observe that the simple loop approach seems to perform about twice '
                 '  as fast as the reduce approach!!')
print('#' * 52 + '  The moral of this side note is that simply because you can do something in Python using '
                 '  some fancy or cool technique does not mean you should!')
print('')
print('#' * 52 + '  We technically could write our reduce-based function as a one liner:')

from functools import reduce

fib_1 = timed(lambda n: reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                               range(n),
                               (0, 1))[0])

print(fib_loop(100))

print(fib_1(100))




