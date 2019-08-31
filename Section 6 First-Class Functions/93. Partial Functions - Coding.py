from functools import partial


def my_func(a, b, c):
    print(a, b, c)


f = partial(my_func, 10)

f(20, 30)

print('#' * 52 + '  We could have done this using another function (or a lambda) as well:')


def partial_func(b, c):
    return my_func(10, b, c)


partial_func(20, 30)

print('#' * 52 + ' or, using a lambda: ')

fn = lambda b, c: my_func(10, b, c)

fn(20, 30)

print('#' * 52 + '  Any of these ways is fine, but sometimes partial is just a cleaner more consise way to do it.')


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


f = partial(my_func, 10, k1='a')
f(20, 30, 40, k2='b', k3='c')

print('#' * 52 + '  We can of course do the same thing using a regular function too:')


def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)


f(20, 30, 40, k2='b', k3='c')

print('#' * 52 + '  As you can see in this case, using **partial** seems a lot simpler.')
print('#' * 52 + '  Also, you are not stuck having to specify the first argument in your partial:')


def power(base, exponent):
    return base ** exponent


print(power(2, 3))

square = partial(power, exponent=2)

print(square(4))

cube = partial(power, exponent=3)

print(cube(2))

print('#' * 52 + '  You can even call it this way:')

print(cube(base=3))

print('#' * 52 + '  #### Caveat')


def my_func(a, b, c):
    print(a, b, c)


a = 10
f = partial(my_func, a)
f(20, 30)

print('#' * 52 + '  Now lets change the value of the variable **a** and see what happens:')

a = 100

f(20, 30)

print('#' * 52 + '  As you can see, the value for **a** is fixed once the partial has been created.')
print('#' * 52 + '  In fact, the memory address of **a** is baked in to the partial, and **a** is immutable.')
print('#' * 52 + '  If we use a mutable object, things are different:')

a = [10, 20]
f = partial(my_func, a)

f(100, 200)

a.append(30)

f(100, 200)

print('#' * 52 + '  #### Use Cases')
print('#' * 52 + '  We tend to use partials in situation where we need to call a function that actually'
                 '  requires more parameters than we can supply.')
print('#' * 52 + '  Often this is because we are working with exiting libraries or code, and we have a special case.')
print('#' * 52 + '  For example, suppose we have points (represented as tuples), and we want to sort them based on'
                 '  the distance of the point from some other fixed point:')

origin = (0, 0)

l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]
dist2 = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
print(dist2((0, 0), (1, 1)))
print(sorted(l, key=lambda x: dist2((0, 0), x)))
print(sorted(l, key=partial(dist2, (0, 0))))

print('#' * 52 + '  Often we can also use partial functions to make our life a bit easier.')
print('#' * 52 + '  Consider a situation where we have some generic `email()` function that can be used to notify '
                 ' someone when various things happen in our application.')
print('#' * 52 + '  But depending on what is happening we may want to notify different people.')


def sendmail(to, subject, body):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}'.format(to, subject, body))


email_admin = 'palin@python.edu'
email_devteam = 'idle@python.edu;cleese@python.edu'

sendmail(email_admin, 'My App Notification', 'the parrot is dead.')
sendmail(';'.join((email_admin, email_devteam)), 'My App Notification', 'the ministry is closed until further notice.')

print('#' * 52 + '  We could simply our life a little using partials this way:')

send_admin = partial(sendmail, email_admin, 'For you eyes only')
send_dev = partial(sendmail, email_devteam, 'Dear IT:')
send_all = partial(sendmail, ';'.join((email_admin, email_devteam)), 'Loyal Subjects')

send_admin('the parrot is dead.')
send_all('the ministry is closed until further notice.')

print('#' * 52 + '  Finally, lets make this a little more complex,'
                 '  with a mixture of positional and keyword-only arguments:')


def sendmail(to, subject, body, *, cc=None, bcc=email_devteam):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}, CC:{3}, BCC:{4}'.format(to,
                                                                  subject,
                                                                  body,
                                                                  cc,
                                                                  bcc))


send_admin = partial(sendmail, email_admin, 'General Admin')
send_admin_secret = partial(sendmail, email_admin, 'For your eyes only', cc=None, bcc=None)

send_admin('and now for something completely different')

send_admin_secret('the parrot is dead!')

send_admin_secret('the parrot is no more!', bcc=email_devteam)

print('#' * 52 + '  ')


def pow(base, exponent):
    return base ** exponent


cube = partial(pow, exponent=3)

print(cube(2))

# cube(2, 4) #  TypeError: pow() got multiple values for argument 'exponent'

print(cube(2, exponent=4))