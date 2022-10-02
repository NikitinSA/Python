'''Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13'''

userNum = int(input("Введите число: "))
sumDigits = 0
userList = []

for i in range (1, userNum + 1):
    res = round((1+1/i)**i)
    userList.append(res)
    sumDigits += res
print(f"{userList} => сумма числе в списке = {sumDigits}")