userNum = int(input('Введите число: '))

if (userNum % 5 == 0 and userNum % 10 == 0 or userNum % 15 == 0) and (userNum % 30 != 0):
    print('true')
else:
    print('false')