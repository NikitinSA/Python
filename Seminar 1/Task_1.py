print('Введи первое число:')
num1 = int(input())
print('Введи вротое число:')
num2 = int(input())

if num1**2 == num2 or num2**2 == num1:
    print(f'одно из чисел является квадратом второго')

else:
    print(f'не являются квадратом')