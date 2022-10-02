"""Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5
out
[10, 2, 3, 8, 9]
22

in
4
out
[4, 2, 4, 9]
8"""

from random import sample

size = int(input("Введите размерность списка: "))

def sumDigits(size):
    arr = sample(range(0, 100), size)
    print(arr)
    summ = 0
    for i in range(0, size, 2):
        summ += arr[i]
    print(f"Сумма элементов списка, стоящих на нечётных позициях = {summ}")

sumDigits(size)