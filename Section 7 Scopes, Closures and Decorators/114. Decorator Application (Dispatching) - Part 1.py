from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), html_escape(v))
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(html_str("""this is 
a multi line string
with special characters: 10 < 100"""))

print(html_int(255))
print(html_escape(3 + 10j))

print('#' * 52 + '  Ideally we would want to just have to call a single function,'
                 '  maybe `htmlize` that would figure out which particular flavor of the `html_xxx` function'
                 '  to call depending on the argument type.')

from decimal import Decimal


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


print('#' * 52 + '  Now we can essentially use the same function call to handle different types'
                 ' - the `htmlize` function is a dispatcher - it dispatches the request to a different function'
                 '  based on the argument type. ')

print(htmlize([1, 2, 3]))
print(htmlize(dict(key1=1, key2=2)))
print(htmlize(255))

print('#' * 52 + '  But there are a number of shortcomings here:')

print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

print('#' * 52 + '  As you can see, the multi-line string did not get the newline characters replaced,'
                 '  the tuple was not rendered as an html list, and the integers do not have their hex representation.')
print(
    '#' * 52 + '  So we just need to redefine the `html_list` and `html_dict` functions to use the `htmlize` function:')


def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

print('#' * 52 + '  In order to define `html_list` and `html_dict` we needed to call `htmlize`,'
                 '  but in order to define `htmlize` we needed to call `html_list` and `html_dict`.')

print('#' * 52 + '  The `htmlize` function body makes calls to other functions such as `html_escape`,'
                 '  `html_int`, etc that have not actually been defined yet')

from html import escape
from decimal import Decimal


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


print('#' * 52 + '  Now we define all the functions that `htmlize` uses'
                 '  before we actually call `htmlize` and all is good:')


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

print('#' * 52 + '  First, we are going to create a decorator that will do something that may seem kind of silly'
                 ' - it is going to take the decorated function and store it in a dictionary,'
                 '  using a key consisting of the **type** `object`.')

print('#' * 52 + '  Then when the returned closure is called,'
                 '  the closure will call the function stored in that dictionary.')


def singledispatch(fn):
    registry = dict()
    registry[object] = fn

    def inner(arg):
        return registry[object](arg)

    return inner


@singledispatch
def htmlizer(arg):
    return escape(str(arg))


print(htmlizer('a < 10'))

print('#' * 52 + '  Next, we are going to add some functions to that `registry` dictionary,'
                 '  and modify our inner function to choose the correct function from the registry,'
                 '  or pick a default based on the type of the argument:')


def singledispatch(fn):
    registry = dict()

    registry[object] = fn
    registry[int] = lambda arg: '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))

    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    return inner


@singledispatch
def htmlize(a):
    return escape(str(a))


print(htmlize(10))
print(htmlize(3.1415))

print('#' * 52 + '  Now, we want a way to add the specialized functions to the `registry` dictionary from **outside**'
                 '  the `singledispatch` function - to do so we will create a parametrized decorator that will'
                 ' (1) take the type as a parameter,'
                 '  and (2) return a closure that will decorate the function associated with the type:')


def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn

        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    return decorator


print('#' * 52 + '  But of course this is not good enough - how do we get a hold of the `register` function'
                 '  from outside `singledispatch`? Remember, `singledispatch` is a decorator that returns'
                 '  the `decorated` closure, not the `register` closure.')


def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!

        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator


@singledispatch
def htmlize(arg):
    return escape(str(arg))


print(htmlize.register)

print('#' * 52 + '  as well as that `registry` attribute that we put in just we could see'
                 '  what keys are in the `registry` dictionary:')

print(htmlize.registry)

print('#' * 52 + '  We can also ask it what function it is going to use for any specific type'
                 '  (currently we only have one registered, the default, for the most general `object` type):')

print(htmlize.dispatch(str))

print('#' * 52 + '  And youll note that the extended scope of `register` and `dispatch` '
                 '  is the same as the extended scope of `htmlize`.')


@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize.registry)

print('#' * 52 + '  and we can ask the decorated `htmlize` function what function it is going to use '
                 '  for the `int` type:')

print(htmlize.dispatch(int))

print('#' * 52 + '  and we can actually call it as well:')

print(htmlize(100))

print('#' * 52 + '  The huge advantage now is that we can keep registering new handlers from anywhere in our module,'
                 '  or even from outside our module!')


@htmlize.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')


@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(dict)
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(htmlize(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize.registry)
print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))
print(htmlize("""this
is a multi line string with
a < 10"""))

print('#' * 52 + '  Our single dispatch decorator works quite well - but it has some limitations.')
print('#' * 52 + '  For example it cannot handle functions that take in more than one argument'
                 '  (in which case dispatching would be based on the type of the **first** argument),'
                 '  and we also are not allowing for types based on parent classes - for example,'
                 '  integers and booleans are both integral numbers -'
                 '  i.e. they both inherit from the Integral base class.')
print('#' * 52 + '  Similarly lists and tuples are both more generic Sequence types.')
print('#' * 52 + '   Well see this in more detail when we get to the topic of abstract base classes')

from numbers import Integral

print(isinstance(100, Integral))
print(isinstance(True, Integral))
print(isinstance(100.5, Integral))
print(type(100) is Integral)
print(type(True) is Integral)
print((100).__class__)
print((True).__class__)

print('#' * 52 + '  The way we have implement our decorator, if we register an Integral generic function,'
                 '  it wont pick up either integers or Booleans.')


from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence


@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize.dispatch(int))
print(htmlize.dispatch(bool))
print(htmlize(100))
print(htmlize(True))


@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize.dispatch(list))
print(htmlize.dispatch(tuple))
print(htmlize.dispatch(str))

print('#' * 52 + '  Instead, we are going to register a string handler specifically -'
                 '  that way we will avoid that problem entirely:')


@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')


print(htmlize.dispatch(str))

print('#' * 52 + '  This means, we have something for generic sequences,'
                 '  but something specific for more specialized strings.')

print(htmlize('abc'))

print('#' * 52 + '  We can do the same thing with sequences - right now `html_sequence` will be used for both'
                 '  lists and tuples. ')
print('#' * 52 + '  But suppose we want slightly different handling of tuples:')


@htmlize.register(tuple)
def html_tuple(t):
    items = [escape(str(item)) for item in t]
    return '({0})'.format(', '.join(items))


print(htmlize.dispatch(list))
print(htmlize.dispatch(tuple))
print(htmlize(['a', 100, 3.14]))
print(htmlize(('a', 100, 3.14)))

print('#' * 52 + '  This means that any object type not specifically handled by our dispatcher will fall back on that'
                 ' `object` key - hence you can think of it as the default for the dispatcher.')

print(type(None))
print(htmlize.dispatch(type(None)))
print(type(1+1j))
print(htmlize.dispatch(complex))
print(type(3))

print(htmlize.dispatch(int))

print('#' * 52 + '  Lastly, because the name of the individual specialized functions does not'
                 '  really matter to us (the dispatcher will pick the appropriate function),')
print('#' * 52 + '  it is quite common for an underscore character ( \_ ) to be used for the function name'
                 ' - the memory address of each specialized function will be stored in the `registry` dictionary,'
                 '  and the function name does not matter - in fact we can even add lambdas to the registry.')


@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(int)
def _(a):
    return '{0}({1})'.format(a, str(hex(a)))


@htmlize.register(str)
def _(s):
    return escape(s).replace('\n', '<br/>\n')


print(htmlize.register(float)(lambda f: '{0:.2f}'.format(f)))
print(htmlize.registry)

print('#' * 52 + '  But note that the `__main__._` function for `int` and `str` are not the same functions '
                 '  (even tough they have the same name):')

print(id(htmlize.registry[str]))
print(id(htmlize.registry[int]))

print('#' * 52 + '  And everything works as expected:')

print(htmlize(100))
print(htmlize(3.1415))
print(htmlize("""this
is a multi-line string
a < 10"""))

print('#' * 52 + '  If this same name but different function thing has you confused, look at it this way:')


def my_func():
    print('my_func initial')


print(id(my_func))

f = my_func

print(id(f))

print('#' * 52 + '  So, `f` and `my_func` point to the same function in memory.')
print('#' * 52 + '  Lets go ahead and "redefine" the function `my_func`:')


def my_func():
    print('second my_func')


print('#' * 52 + '  In fact, we did not "redefine" the previous `my_func`,'
                 '  it still exists in memory (and `f` still points to it).')

print(id(my_func))

print('#' * 52 + '  But the original `my_func` is still around, and 'f' still has a reference to it:')

print(id(f))

print('#' * 52 + '  So, we can call each one:')

f()

my_func()

print('#' * 52 + '  But the function `__name__` have the same value:')

print(f.__name__)
print(my_func.__name__)


