a = 10
print(type(a))

print('#' * 52 + '  If **int** is a class, we should be able to declare it using standard class instatiation: ')
b = int(10)
print(b)
print(type(b))

print('#' * 52 + '  As we see from the docs, we can even create an **int** using an overloaded constructor: ')
b = int('10', base=2)
print(b)
print(type(b))

print('#' * 52 + '  Functions are Objects too ')


def square(a):
    return a ** 2


print(type(square))

print('#' * 52 + '  In fact, we can even assign them to a variable: ')
f = square
print(type(f))
print(f is square)
print(f(2))
print(type(f(2)))

print('#' * 52 + '  A function can return a function ')


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))

f = select_function(2)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))

print('#' * 52 + '  We could even call it this way: ')
print(select_function(1)(5))

print('#' * 52 + '  A Function can be passed as an argument to another function ')


def exec_function(fn, n):
    return fn(n)


result = exec_function(cube, 2)
print(result)
