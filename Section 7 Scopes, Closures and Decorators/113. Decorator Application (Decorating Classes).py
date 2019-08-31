from fractions import Fraction

Fraction.speak = lambda self: 'This is a late parrot.'

f = Fraction(2, 3)

print(f)

print(f.speak())

print('#' * 52 + '  Yes, this is obviously nonsense, but you get the idea that you can add attributes to classes'
                 '  even if you do not have direct control over the class, or after your class has been defined.')

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(1, 2)
f2 = Fraction(10, 5)

print(f1.is_integral())
print(f2.is_integral())

print('#' * 52 + '  Now, we can make this change to the class by calling a function to do it instead:')


def dec_speak(cls):
    cls.speak = lambda self: 'This is a very late parrot.'
    return cls


Fraction = dec_speak(Fraction)

f = Fraction(10, 2)

print(f.speak())

print('#' * 52 + '  We can use that function to decorate our custom classes too, using the short **@** syntax too.')


@dec_speak
class Parrot:
    def __init__(self):
        self.state = 'late'


polly = Parrot()
print(polly.speak())

print('#' * 52 + '   Decorators  are useful when they are able to be reused in more general ways.')

Fraction.recip = lambda self: Fraction(self.denominator, self.numerator)

f = Fraction(2, 3)
print(f)

print(f.recip())

print('#' * 52 + '  As a first example, lets say you typically like to inspect various properties of an object'
                 '  for debugging purposes, maybe the memory address, its current state (property values),'
                 '  and the time at which the debug info was generated.')

from datetime import datetime, timezone


def debug_info(cls):
    def info(self):
        results = []
        results.append('time: {0}'.format(datetime.now(timezone.utc)))
        results.append('class: {0}'.format(self.__class__.__name__))
        results.append('id: {0}'.format(hex(id(self))))

        if vars(self):
            for k, v in vars(self).items():
                results.append('{0}: {1}'.format(k, v))

        # we have not covered lists, the extend method and generators,
        # but note that a more Pythonic way to do this would be:
        # if vars(self):
        #    results.extend('{0}: {1}'.format(k, v)
        #                   for k, v in vars(self).items())

        return results

    cls.debug = info

    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there!'


p1 = Person('John', 1939)

print(p1.debug())

print('#' * 52 + '  And of course we can decorate other classes this way too, not just a single class:')


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0

    @property
    def speed(self):
        return self.current_speed

    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed


s = Automobile('Ford', 'Model T', 1908, 45)

print(s.debug())

print('#' * 52 + '  ')

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0},{1})'.format(self.x, self.y)


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(abs(p1))
print(p1, p2)
print(p1 == p2)

print('#' * 52 + '  Hmm, we probably would have expected `p1` to be equal to `p2` since it has the same coordinates.'
                 '  But by default Python will compare memory addresses, since our class does not implement'
                 '  the `__eq__` method used for `==` comparisons.')

# print(p2 > p3) # TypeError: '>' not supported between instances of 'Point' and 'Point'


del Point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, self.x, self.y)


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(p1, p2, p1 == p2)
print(p2, p3, p2 == p3)

print('#' * 52 + '  As we can see, `==` now works as expected')

p4 = Point(1, 2)
print(abs(p1), abs(p4), p1 < p4)
print(p1 > p4)


def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls


print('#' * 52 + '  For example, a better way to implement `__ge__` would be as follows:')


def ge_from_lt(self, other):
    # self >= other iff not(other < self)
    result = self.__lt__(other)
    if result is NotImplemented:
        return NotImplemented
    else:
        return not result


print('#' * 52 + '  ')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__, self.x, self.y)


Point = complete_ordering(Point)

p1, p2, p3 = Point(1, 1), Point(3, 4), Point(3, 4)

print(abs(p1), abs(p2), abs(p3))

print(p1 < p2, p1 <= p2, p1 > p2, p1 >= p2, p2 > p2, p2 >= p3)

print('#' * 52 + '  Now the `complete_ordering` decorator can also be directly applied to any class'
                 '  that defines `__eq__` and `__lt__`.')


@complete_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented


g1 = Grade(10, 100)
g2 = Grade(20, 30)
g3 = Grade(5, 50)

print(g1 <= g2, g1 == g3, g2 > g3)

print('#' * 52 + '  Often, given the `==` operator and just **one** of the other comparison operators'
                 '  (`<`, `<=`, `>`, `>=`), then all the rest can be derived.')
print('#' * 52 + '  Our decorator insisted on `==` and `<`. but we could make it better by insisting'
                 '  on `==` and any one of the other operators. ')
print('#' * 52 + '  This will of course make our decorator more complicated,'
                 '  and in fact, Python has this precise functionality built in to the, you guessed it,'
                 ' `functools` module!')
print('#' * 52 + '  It is a decorator called `total_ordering`.')

from functools import total_ordering


@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented


g1, g2 = Grade(80, 100), Grade(60, 100)

print(g1 >= g2, g1 > g2)

print('#' * 52 + '  Or we could also do it this way:')


@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent > other.score_percent
        else:
            return NotImplemented


g1, g2 = Grade(80, 100), Grade(60, 100)
print(g1 >= g2, g1 > g2, g1 <= g2, g1 < g2)

