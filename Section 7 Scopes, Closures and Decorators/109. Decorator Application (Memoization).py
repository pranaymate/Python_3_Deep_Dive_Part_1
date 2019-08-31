print('#' * 52 + '  Lets go back to our Fibonacci example:')


def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(6))

print('#' * 52 + '  We can approach this using a simple class and a dictionary that stores'
                 '  any Fibonacci number that is already been calculated:')


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


f = Fib()

print(f.fib(1))
print(f.fib(6))
print(f.fib(7))

print('#' * 52 + '  Lets see how we could rewrite this using a closure:')


def fib():
    cache = {1: 1, 2: 2}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib


f = fib()

print(f(10))

print('#' * 52 + '  Now lets see how we would implement this using a decorator:')

from functools import wraps


def memoize_fib(fn):
    cache = dict()

    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoize_fib
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(3))
print(fib(10))
print(fib(6))

print('#' * 52 + '  As you can see, we are hitting the cache when the values are available.')
print('#' * 52 + '  Now, we made our memoization decorator "hardcoded" to single argument functions - '
                 '  we could make it more generic.')


def memoize(fn):
    cache = dict()

    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return inner


@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(6))
print(fib(7))

print('#' * 52 + '  Of course, with this rather generic memoization decorator we can memoize other functions too:')


def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)


print(fact(5))
print(fact(5))

print('#' * 52 + '  And memoizing it:')


@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)


print(fact(6))
print(fact(6))

print('#' * 52 + '  Memoization is such a common thing to do that Python actually has a memoization decorator'
                 '  built for us!')
print('#' * 52 + '  Its in the, you guessed it, **functools** module, and is called **lru_cache** and is going'
                 '  to be quite a bit more efficient compared to the rudimentary memoization example we did above.')
print('#' * 52 + '  [LRU Cache = Least Recently Used caching: since the cache is not unlimited,'
                 '  at some point cached entries need to be discarded, '
                 '  and the least recently used entries are discarded first]')


from functools import lru_cache


@lru_cache()
def fact(n):
    print("Calculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)


print(fact(5))
print(fact(4))

print('#' * 52 + '  As you can see, `fact(4)` was returned via a cached entry!')
print('#' * 52 + '  Same thing with our Fibonacci function:')


@lru_cache()
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(6))
print(fib(5))


print('#' * 52 + '  Recall from a few videos back that we timed the calculation for Fibonacci numbers.'
                 '  Calculating fib(35) took several seconds - every time...')


from time import perf_counter


def fib_no_memo(n):
    return 1 if n < 3 else fib_no_memo(n-1) + fib_no_memo(n-2)


start = perf_counter()
result = fib_no_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))


@lru_cache()
def fib_memo(n):
    return 1 if n < 3 else fib_memo(n-1) + fib_memo(n-2)


start = perf_counter()
result = fib_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))

print('#' * 52 + '  And if we make the calls again:')

start = perf_counter()
result = fib_no_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))


start = perf_counter()
result = fib_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))

print('#' * 52 + '  You may have noticed that the `lru_cache` decorator was implemented using `()`'
                 ' - well see more on this later, but thats because decorators can themselves '
                 ' have parameters (beyond the function being decorated).')

print('#' * 52 + '  One of the arguments to the `lru_cache` decorator is the size of the cache'
                 '  - it defaults to 128 items, but we can easily change this - for performance'
                 '  reasons use powers of 2 for the cache size (or None for unbounded cache):')


@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(20))
print(fib(10))

