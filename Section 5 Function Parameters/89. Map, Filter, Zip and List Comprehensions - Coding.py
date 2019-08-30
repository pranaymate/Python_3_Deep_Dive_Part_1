help(map)


def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))
print(fact(4))

print(map(fact, [1, 2, 3, 4, 5]))

print('#' * 52 + '  The **map** function returns a **map** object, which is an **iterable** -'
                 '  we can either convert that to a list or enumerate it:')

l = list(map(fact, [1, 2, 3, 4, 5]))
print(l)

print('#' * 52 + '  We can also use it this way:')

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x+y

m = map(f, l1, l2)
print(list(m))

print('#' * 52 + '  ')
print('#' * 52 + '  #### Filter')
print('#' * 52 + '  ')

help(filter)

l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l):
    print(e)

print('#' * 52 + '  Notice how **0** was eliminated from the list, since **0** is **falsy**.')
print('#' * 52 + '  We can use a function for this filtering.')
print('#' * 52 + '  Suppose we want to filter out all odd values, only retaining even values:')
print('#' * 52 + '  We could first define a function to return True if the value is even, and False otherwise:')


def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))

print('#' * 52 + '  Of course, we could just use a lambda expression instead:')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))

print('#' * 52 + '  #### Alternatives to **map** and **filter** using Comprehensions')

print('#' * 52 + '  ##### Map using a list comprehension:')

l = [1, 2, 3, 4, 5]
result = [fact(i) for i in l]
print(result)

print('#' * 52 + '  * two iterables example')

l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
print(list(zip(l1, l2)))

print('#' * 52 + '  ')

l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
print(list(zip(l1, l2, l3)))

print('#' * 52 + '  ')

l1 = [1, 2, 3]
l2 = (10, 20, 30)
l3 = 'abc'
print(list(zip(l1, l2, l3)))

print('#' * 52 + '  ')

l1 = range(100)
l2 = 'python'
print(list(zip(l1, l2)))

print('#' * 52 + '  Using the **zip** function we can now add our two lists element by element as follows:7')

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i,j in zip(l1,l2)]
print(result)

print('#' * 52 + '  ##### Filtering using a comprehension')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in l if i % 2 == 0]
print(result)

print('#' * 52 + '  As you can see, we did not even need a lambda expression!')

print('#' * 52 + '  #### Combining **map** and **filter**')

print(list(filter(lambda y: y < 25, map(lambda x: x**2, range(10)))))

print('#' * 52 + '  Alternatively, we can use a list comprehension to do the same thing:')
