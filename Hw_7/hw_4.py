 # Напишите функцию, которая принимает два числа в кач-ве аргументов
# и считает наименьшее общее кратное для этих чисел.
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

def conter(a: int, b: int) -> int:
    while (b > 0):
        a, b = b, a % b
    return a

def nod(x: int, y: int) -> float:
    return (x * y) // conter(x, y)


print(nod(a, b))


  #Напишите функцию sum_range(start, end), которая суммирует все целые чиckf
#от значения «start» до величины «end» включительно.Если пользователь задаст первое число большее чем второе,
  # просто поменяйте их местами.

def sum_range(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))
print(sum_range(start=1, end=18))

 #Написать программу, которая посчитает кол-во одинаковых элементов в списке.
#Список будет заполняться рандомными целыми числами.
# Рекомендую использовать несколько функций
 #(для заполнения списка целыми числами, для подсчета количества)


from random import randint
def random_list(start: int, end: int, count: int) -> list:
    random_list = []
    for i in range(1, count + 1):
        random_list.append(randint(start, end))
    return random_list

def count_same(n: list ) -> int:
    counter = 0
    for num in set(n):
        if n.count(num) > 1:
            counter += 1
    return counter
print(random_list(start=1, end=10, count=7))
print(count_same(random_list(start=1, end=10, count=7)))


#Напишите функцию, которая выводит первые n чисел последовательности фибоначчи.
 # n - аргумент, который передается в функцию.
def fib(n: int):
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=' ')
    for _ in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')
fib(5)
