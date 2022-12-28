import sys

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
