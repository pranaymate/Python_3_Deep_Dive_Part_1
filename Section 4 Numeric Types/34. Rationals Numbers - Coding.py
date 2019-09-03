from fractions import Fraction

print('#' * 52 + '  We can create Fraction objects in a variety of ways:')

print(Fraction(1))
print(Fraction(1, 3))

print('#' * 52 + '  Using rational numbers:')

x = Fraction(2, 3)
y = Fraction(3, 4)
# 2/3 / 3/4 --> 2/3 * 4/3 --> 8/9
print(Fraction(x, y))

print('#' * 52 + '  Using floats:')
print(Fraction(0.125))
print(Fraction(0.5))

print('#' * 52 + '  Using strings:')

print(Fraction('10.5'))
print(Fraction('22/7'))

print('#' * 52 + '  Fractions are automatically reduced:')
print(Fraction(8, 16))

print('#' * 52 + '  Negative sign is attached to the numerator:')
print(Fraction(1, -4))

print('#' * 52 + '  Standard arithmetic operators are supported:')
print(Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3))
print(Fraction(1, 2) * Fraction(1, 4))
print(Fraction(1, 2) / Fraction(1, 3))

print('#' * 52 + '  We can recover the numerator and denominator (integers):')

x = Fraction(22, 7)
print(x.numerator)
print(x.denominator)

print('#' * 52 + '  Since floats have finite precision, any float can be converted to a rational number:')
import math
x = Fraction(math.pi)
print(x)
print(float(x))

x = Fraction(math.sqrt(2))
print(x)

print('#' * 52 + '  Note that these rational values are approximations to the irrational numbers π and 2⎯⎯√')
print('#' * 52 + '  The number 0.125 (1/8) has an exact representation:')
print(Fraction(0.125))

print('#' * 52 + '  and so we see the expected equivalent fraction.')
print('#' * 52 + '  But, 0.3 (3/10) does not have an exact representation:')

print(Fraction(3, 10))

print('#' * 52 + '  but')

print(Fraction(0.3))

x = 0.3
print(x)

print('#' * 52 + '  Everything looks ok here - why am I saying 0.3 (float) is just an approximation?')
print('#' * 52 + '  Python is trying to format the displayed value for readability - '
                 '  so it rounds the number for a better display format!')
print('#' * 52 + '  We can instead choose to display the value using a certain number of digits:')

print(format(x, '.5f'))

print('#' * 52 + '  At 5 digits after the decimal, we might still think 0.3 is an exact representation.')
print('#' * 52 + '  But lets display a few more digits:')

print(format(x, '.15f'))

print('#' * 52 + '  Hmm... 15 digits and still looking good!')
print('#' * 52 + '  How about 25 digits...')

print(format(x, '.25f'))

print('#' * 52 + '  Now we see that x is not quite 0.3...')

print('#' * 52 + '  In fact, we can quantify the delta this way:')

delta = Fraction(0.3) - Fraction(3, 10)

print('#' * 52 + '  Theoretically, delta should be 0, but its not:')

print(delta == 0)
print(delta)

print('#' * 52 + '  delta is a very small number, the above fraction...')
print('#' * 52 + '  As a float:')
print(float(delta))
print('#' * 52 + '  Constraining the denominator')
x = Fraction(math.pi)
print(x)
print(format(float(x), '.25f'))

y = x.limit_denominator(10)
print(y)
print(format(float(y), '.25f'))

y = x.limit_denominator(500)
print(y)
print(format(float(y), '.25f'))

