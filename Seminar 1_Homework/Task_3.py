"""Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
эта точка (или на какой оси она находится).
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3"""

numX = int(input('Введите X: '))
numY = int(input('Введите Y: '))

if numX == 0 or numY == 0:
    print('Ошибка! X и Y ≠ 0.')
elif numX > 0 and numY > 0:
    print('Точка находится в 1 четверти')
elif numX < 0 and numY > 0:
    print('Точка находится в 2 четверти')
elif numX < 0 and numY < 0:
    print('Точка находится в 3 четверти')
elif numX > 0 and numY < 0:
    print('Точка находится в 4 четверти')