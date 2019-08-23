a = 10
print(hex(id(a)))

a = 15
print(hex(id(a)))

a = 5
print(hex(id(a)))

a = a + 1
print(hex(id(a)))

print('#' * 52 + ' However, look at this:')

a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

# The memory addresses of both **a** and **b** are the same!!