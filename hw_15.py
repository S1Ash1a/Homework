import sys

#Генератор функции Факториала
def factorial(n):
    res = 1
    while n != 0:
        res *= n
        n -= 1
    yield res
for x in factorial(5):
    print(x)
print(factorial(5))

#Напишите функцию, которая выводит последовательность (из первых 100 значений)
# Фибоначчи с помощью генератора

def fib(n):
    fib_1, fib_2 = 1, 1
    for _ in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


print(fib(100))
print(sys.getsizeof(fib(100)))
print(sys.getsizeof(list(fib(100))))