'''1. Написать функцию, которая будет принимать целое положительное число и возвращать True,
если это число простое, иначе - False.'''
from math import sqrt
import string

def simple(el):
    i = 3
    while i <= sqrt(el):
        if el % i == 0:
            return False
        i += 2
    return True
print(simple(13))


'''2. На вход функции передается строка вида: "1 9 3 4 -5 "
необходимо вернуть максимальное и минимальное число из этой последовательности.'''


def element(numbers):
    lst = numbers.split()
    lst_numbers = list(map(int, lst))
    return max(lst_numbers), min(lst_numbers)


print(element("1 9 3 4 -5"))


'''3. Написать функцию, принимающую строку вида: "The sunset sets at twelve o' clock." и возвращающую строку:
"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
где каждое число это порядковый номер буквы в алфавите.
Например при передаче строки: "abc" должно вернуться "1 2 3". *Без учета регистра.'''


def get_digit(st):
    lower = (''.join(c for c in st if c in string.ascii_letters)).lower()
    res = ""
    for i in lower:
        res += str(ord(i) - 96) + " "
    return res


print(get_digit("The sunset sets at twelve o' clock."))