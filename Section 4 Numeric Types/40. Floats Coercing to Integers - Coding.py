from math import trunc

print(trunc(10.3), trunc(10.5), trunc(10.6))
print(trunc(-10.6), trunc(-10.5), trunc(-10.3))
print(trunc(-10.6), trunc(-10.5), trunc(-10.3))

print('#' * 52 + '  The int constructor uses truncation when a float is passed in:')

print(int(10.3), int(10.5), int(10.6))
print(int(-10.5), int(-10.5), int(-10.4))

print('#' * 52 + '  Floor')

from math import floor
print(floor(10.4), floor(10.5), floor(10.6))
print(floor(-10.4), floor(-10.5), floor(-10.6))

print('#' * 52 + '  Ceiling')

from math import ceil
print(ceil(10.4), ceil(10.5), ceil(10.6))
print(ceil(-10.4), ceil(-10.5), ceil(-10.6))