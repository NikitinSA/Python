'''Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.'''

def multiplicity(num):
    return [i for i in range(20, num) if i % 20 == 0 or i % 21 == 0]

print(multiplicity(int(input('Введите число до которого будет считаться кратность: '))))