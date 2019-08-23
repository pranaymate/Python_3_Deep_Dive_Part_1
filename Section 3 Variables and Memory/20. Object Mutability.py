my_list = [1, 2, 3]
print(my_list)
print(hex(id(my_list)))

my_list.append(4)
print(my_list)
print(hex(id(my_list)))

# As you can see, the memory address of *my_list* has **not** changed.
# But, the **contents** of *my_list* has changed from *[1, 2, 3]* to *[1, 2, 3, 4]*.

my_list_1 = [1, 2, 3]
print(my_list_1)
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]
print(my_list_1)
print(hex(id(my_list_1)))

# Notice here that the memory address of *my_list_1* **did** change.

# This is because concatenating two lists objects *my_list_1* and *[4]*
# did not modify the contents of *my_list_1* - instead it created a new
# list object and re-assigned *my_list_1* to reference this new object.

print('#' * 52 + ' Similarly with **dictionary** objects that are also **mutable** types.')

my_dict = dict(key1='value 1')
print(my_dict)
print(hex(id(my_dict)))

my_dict['key1'] = 'modified value 1'
print(my_dict)
print(hex(id(my_dict)))

my_dict['key2'] = 'value 2'
print(my_dict)
print(hex(id(my_dict)))

print('#' * 52 + ' tuple')

t = (1, 2, 3)

a = [1, 2]
b = [3, 4]
t = (a, b)

a.append(3)
b.append(5)
print(t)
