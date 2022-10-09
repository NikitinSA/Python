'''Задайте последовательность чисел. Напишите программу, которая 
выведет список неповторяющихся элементов исходной 
последовательности в том же порядке.
in 7 out [4, 5, 3, 3, 4, 1, 2] [5, 1, 2]'''

from random import randrange, sample

size = int(input("Введите размерность списка: "))

def fillArray(size):
    randNums = []
    for i in range(size):
        randNums.append(randrange(size))
    return randNums

def searchForDuplicateNumbers(randNums: list):
    result = []
    my_dict = {}.fromkeys(randNums, 0)

    for i in randNums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)
    return result

allList = fillArray(size)
print(allList)
print(searchForDuplicateNumbers(allList))