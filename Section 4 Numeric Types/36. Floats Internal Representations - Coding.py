print('#' * 52 + '  The float class can be used to represent real numbers.')

print(float(10))
print(float(3.14))
print(float('0.1'))

print('#' * 52 + '  However, strings that represent fractions cannot be converted to floats, '
                 '  unlike the Fraction class we saw earlier.')

# float('22/7')  # ValueError: could not convert string to float: '22/7'

print('#' * 52 + '  If you really want to get a float from a string such as 22//7, '
                 '  you could first create a Fraction, then create a float from that:')

from fractions import Fraction

print(float(Fraction('22/7')))


print('#' * 52 + '  Floats do not always have an exact representation:')

print(0.1)

print('#' * 52 + '  Although this looks like 0.1 exactly, we need to reveal more digits after the decimal point '
                 '  to see what iss going on:')

print(format(0.1, '.25f'))

print('#' * 52 + '  However, certain numbers can be represented exactly in a binary fraction expansion:')

print(format(0.125, '.25f'))

