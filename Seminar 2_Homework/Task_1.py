"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in -> out
- 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27"""

userNum = float(input("Введите число: "))
sumDigits = 0
size = len(str(userNum)) - 2
userNum *= 10 ** size

while userNum:
    sumDigits += userNum % 10
    userNum //= 10
    
print(int(sumDigits))