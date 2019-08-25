print('#' * 52 + ' tuple ')
a = (1, 2, 3)

print(type(a))

a = 1, 2, 3

print(type(a))

a = (1)

print(type(a))

a = (1,)

print(type(a))

a = 1,

print(type(a))

a = ()

print(type(a))

a = tuple()

print(type(a))


print('#' * 52 + ' Unpacking')

l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)
a, b, c = 'XYZ'
print(a, b, c)

print('#' * 52 + ' Swapping Two Variables')

a = 10
b = 20
print("a={0}, b={1}".format(a, b))

tmp = a
a = b
b = tmp
print("a={0}, b={1}".format(a, b))

a = 10
b = 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))

a, b = 10, 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))

print('#' * 52 + ' dict')
dict1 = {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
print(dict1)

for c in dict1:
    print(c)

a, b, c, d, e, f = dict1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print('#' * 52 + ' Set')
s = {'p', 'y', 't', 'h', 'o', 'n'}
print(type(s))
print(s)

for c in s:
    print(c)

a, b, c, d, e, f = s
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)