'''Вычислить число c заданной точностью d'''

from decimal import Decimal

userNum = float(input('Введите число: '))
accuracy = float(input('Введите точность числа (пример:0.001): '))

def accuracyNumber (userNum, accuracy):
    number = Decimal(f'{userNum}')
    return number.quantize(Decimal(f'{accuracy}'))

print(accuracyNumber(userNum, accuracy))