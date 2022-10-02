"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
in
88
out
1011000
in
11
out
1011"""

userNum = int(input("Введите число: "))

def binaryNumber(userNum):
    number = []
    while userNum:
        sep = userNum // 2
        bin = userNum % 2
        userNum //= 2
        number.append(bin)
    number.reverse()
    res = int("".join(map(str, number)))
    print(res)

binaryNumber(userNum)