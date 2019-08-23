print('#' * 52 + ' Earlier, we saw shared references being created automatically by Python: ')
a = 10
b = 10
print(id(a))
print(id(b))

print('#' * 52 + ' But consider the following example: ')
a = 500
b = 500
print(id(a))
print(id(b))

print('#' * 52 + '  As you can see, the variables `a` and `b` do **not** point to the same object! ')
print('#' * 52 + '  This is because Python pre-caches integer objects in the range [-5, 256] ')
a = 256
b = 256
print(id(a))
print(id(b))

print('#' * 52 + '  and ')
a = -5
b = -5
print(id(a))
print(id(b))

print('#' * 52 + ' The integers in the range [-5, 256] are essentially **singleton** objects.  ')
a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
print(a, b, c, d)

print(a is b)
print(a is c)
print(a is d)
