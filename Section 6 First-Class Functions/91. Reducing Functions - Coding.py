print('#' * 52 + '  #### Maximum and Minimum')

l = [5, 8, 6, 10, 9]

print('#' * 52 + '  We can solve this problem using a **for** loop.')
print('#' * 52 + '  First we define a function that returns the maximum of two arguments:')

_max = lambda a, b: a if a > b else b


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))

print('#' * 52 + '  To calculate the minimum, all we need to do is to change the function that is repeatedly applied:')

_min = lambda a, b: a if a < b else b


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(l)
print(min_sequence(l))

print('#' * 52 + '  In general we could write it like this:')


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l))
print(_reduce(_min, l))


print('#' * 52 + '  We could even just use a lambda directly in the call to **\_reduce**:')

print(_reduce(lambda a, b: a if a > b else b, l))
print(_reduce(lambda a, b: a if a < b else b, l))

print('#' * 52 + '  Using the same approach, we could even add all the elements of a sequence together:')

print(l)
print(_reduce(lambda a, b: a + b, l))

print('#' * 52 + '  Python actually implements a reduce function, which is found in the **functools** module.')
print('#' * 52 + '  Unlike our **\_reduce** function, it can handle any iterable, not just sequences.')

from functools import reduce

print(l)
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a + b, l))

print('#' * 52 + '  Finding the max and min of an iterable is such a common thing that Python provides '
                 ' a built-in function to do just that:')

print(max(l), min(l))

print('#' * 52 + '  Finding the sum of all the elements in an iterable is also common enough that'
                 '  Python implements the **sum** function:')
print(sum(l))

print('#' * 52 + '  #### The **any** and **all** built-ins')

l = [0, 1, 2]
print(any(l))

l = [0, 0, 0]
print(any(l))

print('#' * 52 + '  On the other hand, **all** will return True if **every** element of the iterable is truthy:')

l = [0, 1, 2]
print(all(l))

l = [1, 2, 3]
print(all(l))

print('#' * 52 + '  We can implement these functions ourselves using **reduce**')
print('#' * 52 + '  any')

l = [0, 1, 2]
print(reduce(lambda a, b: bool(a or b), l))

print('#' * 52 + '  all')

l = [0, 1, 2]
print(reduce(lambda a, b: bool(a and b), l))

l = [1, 2, 3]
print(reduce(lambda a, b: bool(a and b), l))

print('#' * 52 + '  Sometimes we may want to find the product of every element of an iterable.')
print('#' * 52 + '  Python does not provide us a built-in method to do this, so we have to either'
                 '  use a procedural approach, or we can use the **reduce** function.')


def mult(a, b):
    return a * b


l = [2, 3, 4]
print(reduce(mult, l))
print(reduce(lambda a, b: a * b, l))

print('#' * 52 + '  #### Factorials')


def fact(n):
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result


print(fact(1), fact(2), fact(3), fact(4), fact(5))

print('#' * 52 + '  We could also write this using a recursive function:')


def fact(n):
    if n <=1:
        return 1
    else:
        return n * fact(n-1)


print(fact(1), fact(2), fact(3), fact(4), fact(5))

print('#' * 52 + '  Finally we can also write this using **reduce** as follows:')

n = 5
print(reduce(lambda a, b: a * b, range(1, n+1)))

print('#' * 52 + '  #### **reduce** initializer')

l = [1, 2, 3]
print(reduce(lambda x, y: x*y, l))

print('#' * 52 + '  but if l is empty:')

l = []
# reduce(lambda x, y: x*y, l) # TypeError: reduce() of empty sequence with no initial value

print('#' * 52 + '  To fix this, we can provide an initializer.')

l = []
print(reduce(lambda x, y: x*y, l, 1))
