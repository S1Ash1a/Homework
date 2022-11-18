"""Написать программу,которая проверяет являеться ли число четным"""

number = int(input("Введите число: "))
if number % 2 == 0:
    print(f"{number} четное ")

"""Есть две переменных x, y. Поменяйте значения переменных местами."""
import os

os.system("cls")

x = 3; y = 5
print("x = ", x, "; y = ", y, sep ="" )

x, y = y, x
print("x = ", x, "; y = ", y, sep ="" )

"""Написать программу, которая удаляет первый и последний символы строки."""

strng = input("Enter a string: ")
if len(strng) <= 2:
    print("Error")
else:
    strng = strng[1:-1]
    print(strng)



"""Вы вводите с клавиатуры последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами."""
string_numbers = input("Enter numbers: ")

list_numbers = string_numbers.split(',')
tuple_numbers = string_numbers.split(',')


print(list_numbers, type(string_numbers))
print(tuple_numbers, type(string_numbers))

