print('#' * 52 + '  ### Lambdas and Sorting')

l = ['a', 'B', 'c', 'D']

print(sorted(l))

print('#' * 52 + '  Pythons **sorted** function kas a keyword-only argument that allows us to modify'
                 '  the values that are used to sort the list.')

print(sorted(l, key=str.upper))

print('#' * 52 + '  We could have used a lambda here (but you should not,'
                 '  this is just to illustrate using a lambda in this case):')

print(sorted(l, key=lambda s: s.upper()))

print('#' * 52 + '  Lets look at how we might create a sorted list from a dictionary:')

d = {'def': 300, 'abc': 200, 'ghi': 100}

print(d)

print(sorted(d))

print('#' * 52 + '  Remember that iterating dictionaries actually iterates the keys -'
                 '  so we ended up with tyhe keys sorted alphabetically.')

print(sorted(d, key=lambda k: d[k]))

print('#' * 52 + '  Maybe we want to sort complex numbers based on their distance from the origin:')


def dist(x):
    return (x.real)**2 + (x.imag)**2


l = [3+3j, 1+1j, 0]
# sorted(l) # TypeError: '<' not supported between instances of 'complex' and 'complex'

print('#' * 52 + '  Instead, lets try to specify the key using the distance:')

print(sorted(l, key=dist))

print('#' * 52 + '  Of course, if we are only going to use the **dist** function once,'
                 '  we can just do the same thing this way:')

print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))

print('#' * 52 + '  And here is another example where we want to sort a list of strings'
                 '  based on the **last character** of the string:')

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))
