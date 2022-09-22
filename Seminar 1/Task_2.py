max = 0
print('Введите 5 чисел')
for i in range(5):
    print('Введите число')
    userNum = int(input())
    if userNum > max:
        max = userNum
print(f'Максимальное число {max}')