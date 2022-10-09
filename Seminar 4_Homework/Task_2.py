'''Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
in 54 out [2, 3, 3, 3]'''
userNum = int(input('Введите число: '))

def primeFactorization(userNum):
    primeFact = []
    di = 2
    while userNum > 1:
        if userNum % di == 0:
            primeFact.append(di)
            userNum //= di
        else:
            di += 1
    return primeFact

print(primeFactorization(userNum))