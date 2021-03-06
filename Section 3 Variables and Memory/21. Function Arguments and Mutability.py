print('#' * 52 + '  Consider a function that receives a string argument, and changes the argument in some way:')


def process(s):
    print('initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('s after change # = {0}'.format(hex(id(s))))


my_var = 'hello'
print('my_var # = {0}'.format(hex(id(my_var))))

print('#' * 52 + '  Note that when s* is received, it is referencing the same object as *my_var.')
print('#' * 52 + '  After we "modify" s*, *s is pointing to a new memory address:')

process(my_var)

# And our own variable *my_var* is still pointing to the original memory address:

print('#' * 52 + ' And our own variable *my_var* is still pointing to the original memory address: ')
print('my_var # = {0}'.format(hex(id(my_var))))

print('#' * 52 + ' Lets see how this works with mutable objects: ')


def modify_list(items):
    print('initial items # = {0}'.format(hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2
    items.pop()
    items.append(5)
    print('final items # = {0}'.format(hex(id(items))))


my_list = [2, 3, 4]
print('my_list # = {0}'.format(hex(id(my_list))))

modify_list(my_list)
print(my_list)
print('my_list # = {0}'.format(hex(id(my_list))))

# Now, even with immutable container objects we have to be careful, e.g. a tuple containing a list (the tuple is
# immutable, but the list element inside the tuple **is** mutable)

print('#' * 52 + ' the tuple is immutable, but the list element inside the tuple **is** mutable ')


def modify_tuple(t):
    print('initial t # = {0}'.format(hex(id(t))))
    t[0].append(100)
    print('final t # = {0}'.format(hex(id(t))))


my_tuple = ([1, 2], 'a')

print(hex(id(my_tuple)))
modify_tuple(my_tuple)
print(my_tuple)
