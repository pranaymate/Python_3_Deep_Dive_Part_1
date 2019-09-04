from random import randint, random

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

print(random_color())

print('#' * 52 + '  So of course, we could call the function this and unpack the results at the same time: ')
red, green, blue, alpha = random_color()
print(f'red={red}, green={green}, blue={blue}, alpha={alpha}')

print('#' * 52 + '  But it might be nicer to use a named tuple: ')

from collections import namedtuple

Color = namedtuple('Color', 'red green blue alpha')

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()

print(color.red)
print(color)