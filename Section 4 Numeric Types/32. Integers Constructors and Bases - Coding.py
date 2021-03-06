print('#' * 52 + '  Constructors')
print('#' * 52 + '  The int class has two constructors')

print(int(10))
print(int(10.9))
print(int(-10.9))

from fractions import Fraction

a = Fraction(22, 7)

print(a)
print(int(a))

print('#' * 52 + '  We can use the second constructor to generate integers (base 10) from strings in any base.')

print(int("10"))
print(int("101"))
print(int("101", 2))
print(int("101", base=2))

print('#' * 52 + '  Python uses a-z for bases from 11 to 36.')

print(int("F1A", base=16))
print(int("f1a", base=16))

print('#' * 52 + '  Of course, the string must be a valid number in whatever base you specify.')

# print(int('B1A', base=11))  # ValueError: invalid literal for int() with base 11: 'B1A'

print(int('B1A', 12))

print('#' * 52 + '  #### Base Representations')
print(bin(10))
print(oct(10))
print(hex(10))

print('#' * 52 + '  You can use these in your own strings as well, and they correspond to '
                 ' prefixes used in integer literals as well.')

a = int('1010', 2)
b = int('0b1010', 2)
c = 0b1010

print(a, b, c)
print('#' * 52 + '  ')
a = int('f1a', 16)
b = int('0xf1a', 16)
c = 0xf1a

print(a, b, c)

print('#' * 52 + '  For literals, the a-z characters are not case-sensitive either')

a = 0xf1a
b = 0xF1a
c = 0xF1A

print(a, b, c)

print('#' * 52 + '  Custom Rebasing')
print('#' * 52 + '  Python only provides built-in function to rebase to base 2, 8 and 16.')
print('#' * 52 + '  For other bases, you have to provide your own algorithm '
                 ' (or leverage some 3rd party library of your choice)')

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


print(from_base10(10, 2))
print(from_base10(255, 16))

print('#' * 52 + '  Next we may want to encode the digits into strings using different characters '
                 '  for each digit in the base')


def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    # we'll see this later, but the following would be better:
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding


print(encode([1, 0, 1], "FT"))
print(encode([1, 10, 11], '0123456789AB'))

print('#' * 52 + '  And we can combine both functions into a single one for easier use:')


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


e = rebase_from10(10, 2)
print(e)
print(int(e, 2))

print('')

e = rebase_from10(-10, 2)
print(e)
print(int(e, 2))

print('')

print(rebase_from10(131, 11))
print(rebase_from10(4095, 16))
print(rebase_from10(-4095, 16))

