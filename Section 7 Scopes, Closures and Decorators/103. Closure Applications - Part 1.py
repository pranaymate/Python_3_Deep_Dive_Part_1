print('#' * 52 + '  In this example we are going to build an averager function that can average multiple values.')
print('#' * 52 + '  The twist is that we want to simply be able to feed numbers to that function and get a running'
                 '  average over time, not average a list which requires performing the same calculations'
                 '  (sum and count) over and over again.')


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()

print(a.add(10))
print(a.add(20))
print(a.add(30))

print('#' * 52 + '  We can do this using a closure as follows:')


def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


a = averager()

print(a(10))
print(a(20))
print(a(30))

print('#' * 52 + '  ')


class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0

    def add(self, value):
        self._total += value
        self._count += 1
        return self._total / self._count


a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))

print('#' * 52 + '  Now, lets see how we might use a closure to achieve the same thing.')


def averager():
    total = 0
    count = 0

    def add(value):
        nonlocal total, count
        total += value
        count += 1
        return 0 if count == 0 else total / count

    return add


a = averager()

print(a(10))
print(a(20))
print(a(30))

print('#' * 52 + '  Suppose we want something that can keep track of the running elapsed time in seconds.')

from time import perf_counter


class Timer:
    def __init__(self):
        self._start = perf_counter()

    def __call__(self):
        return (perf_counter() - self._start)


a = Timer()
print(a())
print('#' * 52 + '  Lets start another "timer":')

b = Timer()

print(a())
print(b())

print('#' * 52 + '  Now lets rewrite this using a closure instead:')


def timer():
    start = perf_counter()

    def elapsed():
        # we don't even need to make start nonlocal
        # since we are only reading it
        return perf_counter() - start

    return elapsed


x = timer()
print(x)
print(x())

y = timer()
print(y)
print(y())

print(a())
print(b())
print(x())
print(y())
