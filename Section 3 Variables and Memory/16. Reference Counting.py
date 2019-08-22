import ctypes

print('#' * 52 + '  Method that returns the reference count for a given variables memory address:')


def ref_count(address):
    return ctypes.c_long.from_address(address).value


print('#' * 52 + '  Lets make a variable, and check its reference count:')

my_var = [1, 2, 3, 4]
print(ref_count(id(my_var)))

print('#' * 52 + ' There is another built-in function we can use to obtain the reference count:')

import sys
print(sys.getrefcount(my_var))

print('#' * 52 + '  But why is this returning 2, instead of the expected 1 we obtained with the previous function?')
print('#' * 52 + '  Answer: The sys.getrefcount() function takes my_var as an argument, '
                 '  this means it receives (and stores) a reference to my_vars memory address also - '
                 '  hence the count is off by 1. So we will use from_address() instead.')
print('#' * 52 + '  We make another reference to the same reference as my_var:')

other_var = my_var

print('#' * 52 + '  Lets look at the memory address of those two variables and the reference counts:')
print(hex(id(my_var)), hex(id(other_var)))
print(ref_count(id(my_var)))


print('#' * 52 + ' Force one reference to go away:')
other_var = None

print('#' * 52 + '  And we look at the reference count again:')

print(ref_count(id(my_var)))

print('#' * 52 + '  We see that the reference count has gone back to 1.')
print('#' * 52 + '  You will probably never need to do anything like this in Python. '
                 '  Memory management is completely transparent - this is just to illustrate some of what is going'
                 '  behind the scenes as it helps to understand upcoming concepts.')


