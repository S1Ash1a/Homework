import sys
import functools
#Генератор функции Факториала
def factorial(n):
    res = 1
    while n != 0:
        res *= n
        n -= 1
    yield res

print(factorial(5))

def f(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(lambda x, y: x * y, range(1, n+1))

print(f(5))
print(sys.getsizeof(factorial(5)))
print(sys.getsizeof(f(5)))
