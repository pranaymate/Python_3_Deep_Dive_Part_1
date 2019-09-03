# Help on built-in function round in module builtins:
#
# round(...)
#     round(number[, ndigits]) -> number
#
#     Round a number to a given precision in decimal digits (default 0 digits).
#     This returns an int when called with one argument, otherwise the
#     same type as the number. ndigits may be negative.

a = round(1.5)
print(a, type(a))

print('#' * 52 + '  n > 0')
print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0))

print('#' * 52 + '  n < 0')

print(round(888.88, 1), round(888.88, 0),
      round(888.88, -1), round(888.88, -2),
      round(888.88, -3))

print('#' * 52 + '  Ties')
print(round(1.25, 1))
print(round(1.35, 1))

print('#' * 52 + '  This is rounding to nearest, with ties to nearest number with even least significant digit, '
                 '  aka Bankers Rounding.')
print('#' * 52 + '  Works similarly with n negative.')

print(round(15, -1))
print(round(25, -1))

print('#' * 52 + '  Rounding to closest, ties away from zero')
print('#' * 52 + '  This is traditionally the type of rounding taught in school, which is different from '
                 '  the Bankers Rounding implemented in Python (and in many other programming languages)')
# 1.5 --> 2
# 2.5 --> 3
#
# -1.5 --> -2
# -2.5 --> -3
#
# To do this type of rounding (to nearest 1) we can add (for positive numbers) or subtract (for negative numbers) 0.5
# and then truncate the resulting number.


def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))


print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))
