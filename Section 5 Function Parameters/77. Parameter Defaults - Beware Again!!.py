print('#' * 52 + ' To make sure the data is consistent, '
                 ' we want to use a function that we can call to add the item to our list.  ')
print('#' * 52 + ' So we will need to provide it our current grocery list as well as the item information to be added:')


def add_item(name, quantity, unit, grocery_list):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = []
store_2 = []

print(add_item('bananas', 2, 'units', store_1))
print(add_item('grapes', 1, 'bunch', store_1))
print(add_item('python', 1, 'medium-rare', store_2))


print('#' * 52 + ' print store_1  ')
print(store_1)

print('#' * 52 + '  ')
print(store_2)

print('#' * 52 + '  But lets make the function a little easier to use ')
print('#' * 52 + '  if the user does not supply an existing grocery list to append the item to, ')
print('#' * 52 + '  lets just go ahead and default our grocery_list to an empty list hence starting a new shopping list')


def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)

print(store_1)

print('#' * 52 + ' Lets start our second list: ')
store_2 = add_item('milk', 1, 'gallon')
print(store_2)

print('#' * 52 + ' When we started out first list, we were adding item to that default list.  ')
print('#' * 52 + ' When we started our second list, '
                 ' we were adding items to the same default list (since it is the same object). ')
print('#' * 52 + ' We can avoid this problem using the same pattern as in the previous example '
                 ' we had with the default date time value. ')
print('#' * 52 + ' We use None as a default value instead, and generate a new empty list'
                 ' (hence starting a new list) if none was provided.')


def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
print(add_item('grapes', 1, 'bunch', store_1))
store_2 = add_item('milk', 1, 'gallon')
print(store_2)

print('#' * 52 + ' Lets say we have a factorial function, that can be defined recursively as:  ')


def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)


print(factorial(3))
print(factorial(3))

print('#' * 52 + ' As you can see we had to recalculate all those factorials the second time around. ')
print('#' * 52 + ' Lets cache the results leveraging what we saw in the previous example: ')


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result


print(factorial(3))
print(factorial(3))


print('#' * 52 + ' Now as you can see, the second time around we did not have to recalculate all the factorials  ')
print('#' * 52 + '  In fact, to calculate higher factorials, you will notice'
                 '  that we dont need to re-run all the recursive calls: ')
print(factorial(5))
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')