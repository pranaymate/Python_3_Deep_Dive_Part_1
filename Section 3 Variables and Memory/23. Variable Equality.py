a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))

print('#' * 52 + '  When we use the **is** operator, we are comparing the memory address **references**: ')
print("a is b: ", a is b)

print('#' * 52 + '  print("a is b: ", a is b) ')
print("a == b:", a == b)


print('#' * 52 + '   The following however, do not have a shared reference:')
a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))
print(hex(id(b)))

print('#' * 52 + '   Although they are not the same objects, they do contain the same "values')
print("a is b: ", a is b)
print("a == b", a == b)

print('#' * 52 + '  Python will attempt to compare values as best as possible, for example: ')
a = 10
b = 10.0
print(type(a))
print(type(b))
print(hex(id(a)))
print(hex(id(b)))
print('a is b:', a is b)
print('a == b:', a == b)

print('#' * 52 + '  In fact, this will also have the same behavior: ')
c = 10 + 0j
print(type(c))
print('a is c:', a is c)
print('a == c:', a == c)

print('#' * 52 + '  The None Object ')
print(None)
hex(id(None))
type(None)
a = None
print(type(a))
print(hex(id(a)))
print(a is None)
print(a == None)
b = None
hex(id(b))
print(a is b)
print(a == b)
l = []
print(type(l))
print(l is None)
print(l == None)


