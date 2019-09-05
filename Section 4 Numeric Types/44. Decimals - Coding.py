import decimal

from decimal import Decimal

print('#' * 52 + '  Decimals have context, that can be used to specify rounding and precision (amongst other things)')
print('#' * 52 + '  Contexts can be local (temporary contexts) or global (default)')

g_ctx = decimal.getcontext()
print(g_ctx.prec)

print(g_ctx.rounding)
print(dir(decimal))

print('#' * 52 + '  We can change settings in the global context:')

g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP

print('#' * 52 + '  And if we read this back directly from the global context:')

print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)

print('#' * 52 + '  we see that the global context was indeed changed.')
print('#' * 52 + '  ')
print('#' * 52 + '  Local Context')
print('#' * 52 + '  ')

print('#' * 52 + '  The localcontext() function will return a context manager that we can use with a with statement:')

with decimal.localcontext() as ctx:
    print(ctx.prec)
    print(ctx.rounding)

print('#' * 52 + '  Since no argument was specified in the localcontext() call, '
                 '  it provides us a context manager that uses a copy of the global context.')
print('#' * 52 + '  Modifying the local context has no effect on the global context')

with decimal.localcontext() as ctx:
    ctx.prec = 10
    print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))
print('')
print('#' * 52 + '  Rounding')
print('')

print(decimal.getcontext().rounding)

print('#' * 52 + '  The rounding mechanism is ROUND_HALF_UP because we set the global context '
                 '  to that earlier in this notebook. Note that normally the default is ROUND_HALF_EVEN.')
print('#' * 52 + '  So we first reset our global context rounding to that:')

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

x = Decimal('1.26')
y = Decimal('1.36')
print(round(x, 1))
print(round(y, 1))

print('#' * 52 + '  Lets change the rounding mechanism in the global context to ROUND_HALF_UP:')

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

'''
As you may have realized, changing the global context is a pain if you need to constantly switch between different precisions and rounding algorithms. Also, it could introduce bugs if you forget that you changed the global context somewhere further up in your module.

For this reason, it is usually better to use a local context manager instead:

First we reset our global context rounding to the default:

'''

print('#' * 52 + '  First we reset our global context rounding to the default:')

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))