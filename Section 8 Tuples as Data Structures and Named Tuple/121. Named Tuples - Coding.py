class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


print('#' * 52 + '  Creating Named Tuples')

from collections import namedtuple

Point2D = namedtuple('Point2D', ('x', 'y'))
Pt = namedtuple('Point2D', ('x', 'y'))
pt1 = Pt(10, 20)

print(pt1)

Point2D = namedtuple('Point2D', ('x', 'y'))
pt1 = Point2D(10, 20)
print(pt1)

Pt3 = Point3D
pt3 = Pt3(10, 20, 30)
print(pt3)

print(type(Point3D))
print(type(Point2D))

print('#' * 52 + '  However, `Point2D` is a subclass of `tuple`, while `Point3D` is not:')

print(isinstance(pt1, tuple))
print(isinstance(pt3, tuple))

# So, when we create an instance of a class, we are in fact calling the `__new__` method with our initial values.
# It's just a callable that has the **field names** we used to generate our named tuple class as its parameters. ' \
# 'This means we can use keyword arguments when instantiating our named tuples!

pt4 = Point2D(y=20, x=10)
print(pt4)

print('#' * 52 + '  What did we get for free using a named tuple vs our own class?')
print('#' * 52 + '  First using a named tuple for our 2D point: ')

pt2d_1 = Point2D(10, 20)
pt2d_2 = Point2D(10, 20)

print(pt2d_1)
print(pt2d_1 == pt2d_2)

print('#' * 52 + '  Now using our 3D class: ')

pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

print(pt3d_1)
print(pt3d_1 == pt3d_2)

print('#' * 52 + '  And we would also need to implement the __eq__ method! ')


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

print(pt3d_1)

print(pt3d_1 == pt3d_2)

print('#' * 52 + '  How about finding the largest coordinate in the point? ')
print('#' * 52 + '  Thats easy for Point2D since it is a tuple, but not the case for Point3D: ')

print(max(pt2d_1))
# print(max(pt3d_1)) # TypeError: 'Point3D' object is not iterable

print('#' * 52 + '  How about calculating the dot product of two points ')


def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z


print(dot_product_3d(pt3d_1, pt3d_2))

print('#' * 52 + '  But for our 2D point, which, remember is a tuple as well, we can write a generic function that '
                 'would work equally well with a 3D named tuple too: ')


def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))


a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))

print('#' * 52 + '  Note that if we had more dimensions this would work equally well ')

u = (1, 2, 3)
v = (10, 20, 30)
print(list(zip(u, v)))

print('#' * 52 + '  Then we create a comprehension that multiplies the components together: ')

print([e[0] * e[1] for e in zip(a, b)])
print(sum([e[0] * e[1] for e in zip(a, b)]))
print(dot_product(a, b))

print('#' * 52 + '  And if we defined a 4D point named tuple: ')

Point4D = namedtuple('Point4D', ['i', 'j', 'k', 'l'])

pt4d_1 = (1, 1, 1, 10)
pt4d_2 = (2, 2, 2, 10)

print(dot_product(pt4d_1, pt4d_2))

print('#' * 52 + '  Other Ways to Specify Field Names ')

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])

circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x=10, center_y=20, radius=100)

print(circle_1)
print(circle_2)

City = namedtuple('City', 'name country population')
new_york = City('New York', 'USA', 8_500_000)

print(new_york)

Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

print('#' * 52 + '  In fact, since whitespace can be used we can even use a multi-line string! ')

Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

print('#' * 52 + '  #### Accessing Items in a Named Tuple ')

print(pt1)
print(pt1.x)
print(circle_1)
print(circle_1.radius)

print('#' * 52 + '  Now named tuples *are* tuples, so elements can be accessed by index, unpacked, and iterated. ')

circle_1[2]

for item in djia:
    print(item)

print('#' * 52 + '  We can also unpack named tuples just like ordinary tuples: ')

print(pt1)
x, y = pt1
print(x, y)

print('#' * 52 + '  We can also use extended unpacking: ')

print(djia)
symbol, *_, close = djia
print(symbol, close)
print(_)

print('#' * 52 + '  The field names for these named tuples can be any valid variable name **except** that '
                 '  they cannot start with an underscore. ')

# Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn']) # ValueError: Field names cannot start with an underscore: '_age'

print('#' * 52 + '  ')

Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)

eric = Person('Eric', 'Idle', 42, 'unknown')

print(eric)

print('#' * 52 + '  #### Named Tuple Internals ')

print(Point2D._fields)
print(Stock._fields)

print('#' * 52 + '  There is also a property, _source that allows us to see exactly the class that was generated by'
                 '  calling  namedtuple ')

print(Point2D._source)

print('#' * 52 + '  And of course this will be slightly different for another named tuple generated class: ')

print(Person._source)

print('#' * 52 + '  #### Converting Named Tuples to Dictionaries')

print(eric._asdict())
