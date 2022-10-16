'''Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента. Use comprehension.'''

'''from random import sample

size = int(input("Введите размерность списка: "))

def outputOfElementsLargerThanThePreviousOnes(size):
    userList = sample(range(1, 20), size)
    print(userList)
    resultList = []
    for i in range(1, len(userList)):
        if userList[i] > userList[i-1]:
            (resultList.append(userList[i]))
    print(resultList)

outputOfElementsLargerThanThePreviousOnes(size)''' # Вариант без List comprehension.

from random import randint

def outputOfElementsLargerThanThePreviousOnes(num):
    
    userList = [randint(0,10) for _ in range(num)]
    print(userList)
    return [num for i, num in enumerate(userList[1:]) if num > userList[i]]

print(outputOfElementsLargerThanThePreviousOnes(int(input('Введите размерность списка: ')))) # Вариант c List comprehension.