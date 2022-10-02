"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4
out
[2, 5, 8, 10]
[20, 40]
in
5
out
[2, 2, 4, 8, 8]
[16, 16, 4]"""

from random import sample

size = int(input("Введите размерность списка: "))

def multiplicationDigits(size):
    arr = sample(range(1, 20), size)
    print(arr)
    mult = 0
    count = 1
    numList = []
    if size % 2 == 0:
        for i in range(0, size // 2):
            mult = arr[i] * arr[-count]
            count += 1
            numList.append(mult)        
    else:
        for i in range(0, int(size / 2) + 1):
            mult = arr[i] * arr[-count]
            count += 1
            numList.append(mult)
    print(numList)
    
multiplicationDigits(size)