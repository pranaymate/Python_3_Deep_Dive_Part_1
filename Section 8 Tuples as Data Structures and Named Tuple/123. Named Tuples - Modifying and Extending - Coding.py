from collections import namedtuple


Point2D = namedtuple('Point2D', 'x y')

origin = Point2D(10,0)
# origin.x = 0 # AttributeError: can't set attribute

print('#' * 52 + ' However, we may want to "change" the value of one of the coordinates of our origin variable. ')
origin = Point2D(0, origin.y)
print(origin)

print('#' * 52 + ' Of course this could become quite unwieldy when we have a larger number of properties and we only'
                 ' need to change a single item: ')

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia = Stock(djia.symbol, djia.year, djia.month, djia.day,
                  djia.open, djia.high, djia.low, 26_394)
*values, _ = djia
print(values)
djia = Stock(*values, 26_393)
print(djia)

print('#' * 52 + ' We could try **slicing**: ')

print(djia[:3])
print(djia[:3] + (26,) + djia[4:])

print('#' * 52 + ' So now we could use this to create a new StockPrice instance: ')

djia2 = Stock(*(djia[:3] + (26,) + djia[4:]))
print(djia2)
print(djia)
values = djia[0:1] + (2019,) + djia[2:3] + (26,) + djia[4:]

print(values)
djia3 = Stock(*values)
print(djia3)

print('#' * 52 + ' Or, if you want to avoid unpacking the `values` into the multiple positional arguments required'
                 ' by the `Stock` constructor, we can make us of the `_make` class method that can use an iterable: ')

djia4 = Stock._make(values)
print(djia4)

print('#' * 52 + ' The namedtuple implementation also provides another instance method called `_replace` which takes'
                 ' keyword-only arguments. That method will make a copy of the current tuple and substitute property'
                 ' values based on the keyword-only arguments passed in. ')

print(djia)
print(id(djia))

djia5 = djia._replace(year=2019, day=26)
print(djia5)
print(djia)
print(djia5)

print('#' * 52 + ' #### Extending Named Tuples ')

Point2D = namedtuple('Point2D', 'x y')

print('#' * 52 + ' We could easily create a 3D point class as follows: ')
Point3D = namedtuple('Point3D', 'x y z')

print('#' * 52 + ' But if our named tuple has many fields, such as our `Stock` named tuple thats a little more '
                 'difficult: ')

print(djia)

print('#' * 52 + ' Suppose we want to create a new class, say `StockExt`, it would take some effort: ')

StockExt = namedtuple('StockExt',
                      '''symbol year month day open high low 
                      close previous_close''')

print(Stock._fields)

print('#' * 52 + ' Remember that the `namedtuple` initializer can handle a list or tuple containing the field names.'
                 ' For example, the one we just retrieved from `_fields`. ')

print('#' * 52 + ' Now all we need to do is create a new tuple that contains those fields along with whatever extras'
                 ' we want: ')

new_fields = Stock._fields + ('previous_close',)
print(new_fields)

print('#' * 52 + ' And now we can create our new named tuple this way: ')

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
print(StockExt._fields)

print('#' * 52 + ' If you did not want to use tuple concatenation for some reason, you could also do it using strings: ')

print(' '.join(Stock._fields) + ' previous_close')
StockExt = namedtuple('StockExt',
                      ' '.join(Stock._fields) + ' previous_close')

print(StockExt._fields)

print('#' * 52 + ' Now, with this newly extended class, we may want to take one of the "old" named tuple instance'
                 ' (`djia`) and create the extended version of it using the `StockExt` class. ')
print('#' * 52 + ' This is also quite simple to do, since named tuples are tuples, and can therefore be unpacked in'
                 ' the arguments of a function call. ')

print(djia)
djia_ext = StockExt(*djia, 25_000)
print(djia_ext)

print('#' * 52 + ' or, we can use the `_make` method: ')

djia_ext = StockExt._make(djia + (25_000, ))
print(djia_ext)



