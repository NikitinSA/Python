"""Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y)."""

userNum = int(input('Введите номер четверти: '))

if userNum < 1 or userNum > 4:
    print('Ошибка! Такой четверти не существует.')
elif userNum == 1:
    print('X > 0; Y > 0')
elif userNum == 2:
    print('X < 0; Y > 0')
elif userNum == 3:
    print('X < 0; Y < 0')
elif userNum == 4:
    print('X > 0; Y < 0')