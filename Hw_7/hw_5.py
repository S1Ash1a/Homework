# [1,2,'a','b'] == [1, 2, 3]    -> 1 + 4 + 9 = 14
from typing import Tuple, List, Any


def filter_list(l: list) -> list:
    list_nums = [num for num in l if type(num) == int]
    return list_nums
print(filter_list([1,2,3, 'a','b']))


def bar(n: list) -> tuple[list[Any], int]:
    result = []
    sum = 0
    for i in n:
        tmp = i**2
        result.append(tmp)
        sum += tmp
    return result, sum


print(bar(filter_list([1, 2, 3, 'a', 'b'])))

'''Дана строка, состоящая из слов, вернуть длину кратчайшего слова(слов).
Проверьте, если строка имеет одинаковое количество " х " и "о". Метод должен возвращать логическое True/False если количесвто разное. Без учета регистра.
Примеры строк:
XO("ooxx") => true '''

'''def get_shortest(array: str) -> int:
    return len(min(array.split(), key=len))
print(get_shortest("Hello, world I'm python!"))'''

def get_equal(array: str) -> bool:
    if array.lower().count("x") == array.lower().count("o"):
        return True
    else:
        return False

print(get_equal("ooxXm"))

def is_isogram(array: str):
    if len(array.lower()) == len("".join(set(array.lower()))):
        return True
    else:
        return False

print(is_isogram("AAAbbbss"))
