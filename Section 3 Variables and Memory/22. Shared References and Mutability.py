my_var_1 = 'hello'
my_var_2 = my_var_1
print(my_var_1)
print(my_var_2)

print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

my_var_2 = my_var_2 + ' world!'

print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

# Be careful if the variable type is mutable!
# Here we create a list (*my_list_1*) and create a variable (*my_list_2*) referencing the same list object:

print('#' * 52 + '  Be careful if the variable type is mutable!')

my_list_1 = [1, 2, 3]
my_list_2 = my_list_1
print(my_list_1)
print(my_list_2)

print('#' * 52 + '  As we can see they have the same memory address (shared reference):')

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

print('#' * 52 + '  Now we modify the list referenced by *my_list_2*: ')
print('#' * 52 + '  *my_list_2* has been modified: ')

my_list_2.append(4)
print(my_list_2)

print('#' * 52 + '  And since my_list_1 references the same list object, it has also changed:')
print(my_list_1)

print('#' * 52 + '  As you can see, both variables still share the same reference: ')
print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

print('#' * 52 + '  Recall from a few lectures back: ')

a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))

print('#' * 52 + '  The only way to change *b*s value is to change its reference, which will never affect *a*. ')

b = 15

print(hex(id(a)))
print(hex(id(b)))

print('#' * 52 + '  for mutable objects, Pythons memory manager does not do this, since that would **not** be safe. ')

my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

