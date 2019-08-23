print('#' * 52 + '  Python is dynamically typed.')

a = "hello"

print(type(a))

a = 10

print(type(a))

a = lambda x: x**2

a(2)

print(type(a))

# As you can see from the above examples, the type of the variable a changed over time -
# in fact it was simply the type of the object a was referencing at that time.
# No type was ever attached to the variable name itself.
