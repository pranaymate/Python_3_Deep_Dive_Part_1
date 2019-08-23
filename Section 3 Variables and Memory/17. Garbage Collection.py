import ctypes
import gc

# gc — Garbage Collector interface
# This module provides an interface to the optional garbage collector.
# It provides the ability to disable the collector, tune the collection frequency
# and set debugging options. It also provides access to unreachable objects
# that the collector found but cannot free. Since the collector supplements
# the reference counting already used in Python, you can disable the collector
# if you are sure your program does not create reference cycles. Automatic
# collection can be disabled by calling gc.disable(). To debug a leaking
# program call gc.set_debug(gc.DEBUG_LEAK). Notice that this includes
# gc.DEBUG_SAVEALL, causing garbage-collected objects to be saved in gc.garbage
# for inspection.


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

# We turn off the GC so we can see how reference counts are affected when the GC does not run and when it does
# (by running it manually).


gc.disable()

# Now we create an instance of A, which will, in turn, create an instance of B which will store a reference
# to the calling A instance.

print('#' * 52 + '  Now we create an instance of A, which will, in turn, '
                 '  create an instance of B which will store a reference to the calling A instance.')

my_var = A()

# Now we create an instance of A, which will, in turn, create an instance of B which will store a reference to the
# calling A instance.

print('#' * 52 + '  As we can see A and Bs constructors ran, and we also see from the memory addresses that'
                 '  we have a circular reference.')
print('#' * 52 + '  In fact my_var is also a reference to the same A instance:')

print(hex(id(my_var)))

print('#' * 52 + ' Another way to see this:')

print('a: \t{0}'.format(hex(id(my_var))))
print('a.b: \t{0}'.format(hex(id(my_var.b))))
print('b.a: \t{0}'.format(hex(id(my_var.b.a))))

a_id = id(my_var)
b_id = id(my_var.b)

print('#' * 52 + ' We can see how many references we have for `a` and `b`:')

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# Now, let's remove the reference to the A instance that is being held by `my_var`:

my_var = None

print('#' * 52 + ' Now, lets remove the reference to the A instance that is being held by `my_var`:')

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# Let's run the GC manually and re-check whether the objects still exist:
print('#' * 52 + ' We can see how many references we have for `a` and `b`:')

gc.collect()
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
