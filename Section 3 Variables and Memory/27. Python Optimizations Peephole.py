print('#' * 52 + ' Lets see how Python reduces constant expressions for optimization purposes: ')


def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5


print(my_func.__code__.co_consts)


print('#' * 52 + ' In membership testing, optimizations are applied as can be seen below: ')


def my_func():
    if e in [1, 2, 3]:
        pass


print(my_func.__code__.co_consts)

print('#' * 52 + ' In the same way, set membership will be converted to frozen set membership: ')


def my_func():
    if e in {1, 2, 3}:
        pass


print(my_func.__code__.co_consts)

print('#' * 52 + ' In general, when you are writing your code, if you can use **set** membership testing, prefer '
                 'that over a list or tuple - it is quite a bit more efficient. ')


import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print()
print(char_tuple)
print()
print(char_set)


def membership_test(n, container):
    for i in range(n):
        if 'p' in container:
            pass


print('#' * 52 + ' char_list ')
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list membership: ', end-start)

print('#' * 52 + ' char_tuple ')
start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple membership: ', end-start)

print('#' * 52 + ' char_set ')
start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set membership: ', end-start)

