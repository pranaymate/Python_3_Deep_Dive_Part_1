print('#' * 52 + '  Addition, subtraction, multiplication and exponentiation of integers always result in an integer.')

print(type(2 + 3))
print(type(3 - 10))
print(type(3 * 5))
print(type(3 ** 4))

print('#' * 52 + '  But the standard division operator / always results in a float value.')

print(type(2 / 3))
print(type(10 / 2))

import math

print('#' * 52 + '  For non-negative values (>= 0), the floor of the value is the same as the integer portion '
                 ' of the value (truncation)')

print(math.floor(3.15))
print(math.floor(3.9999999))

print('#' * 52 + '  However, this is not the case for negative values:')

print(math.floor(-3.15))
print(math.floor(-3.0000001))

print('#' * 52 + '  The Floor Division Operator')
print('#' * 52 + '  The floor division operator a//b is the floor of a / b')
print('#' * 52 + '  i.e. a // b = math.floor(a / b)')
print('#' * 52 + '  This is true whether a and b are positive or negative.')

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

print('#' * 52 + '  For positive numbers, a//b is basically the same as truncating'
                 ' (taking the integer portion) of a / b.')
print('#' * 52 + '  But this is not the case for negative numbers.')

a = -33
b = 16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))

print('')

print(math.trunc(a/b))

print('')

a = 33
b = -16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))

print('#' * 52 + '  The Modulo Operator')
print('#' * 52 + '  The modulo operator and the floor division operator will always satisfy the following equation:')

a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)

a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)

a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)

a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)

