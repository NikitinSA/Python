from unittest import result


userNum = int(input("Введите число: "))
result = 1
for i in range (userNum):
    print(result, end = " ")
    result *= -3