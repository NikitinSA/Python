# Семинар 1
## Задача 1
Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
## Задача 2
Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
## Задача 3
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
## Задача 4
Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
## Задача 5
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
## Задача 6
Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))
# Домашнее задание к семинару 1
## Задача 1
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
- 6 -> да
- 7 -> да
- 1 -> нет
## Задача 2
Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
## Задача 3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
## Задача 4
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

## Задача 5
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
in

- 3
- 6
- 2
- 1

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

out
5.099
# Семинар 2
## Задача 1
Напишите программу, которая принимает на вход число N и выдает последовательность из N чисел.
## Задача 2
Создать список, длины n, значения формируются по формуле 3k+1, где k принимает значения от 1 до n включительно.
## Задача 3
Напишите программу, в которой пользователь будет задавать две строки, программа - определять количество вхождений одной строки в другой.
# Домашнее задание к семинару 2
## Задача 1. 
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in -> out
- 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27
## Задача 2.
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
- 4 -> [1, 2, 6, 24]
- 6 -> [1, 2, 6, 24, 120, 720]
## Задача 3.
Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
## Задача 4.
Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 15
## Задача5.
Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
# Семинар 3
## Задача 1
Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. Напишите программу, которая определит, присутствует ли в заданном списке число, полученное от пользователя.
## Задача 2
Задайте список, состоящий из произвольных слов, количество задаёт пользователь. Напишите программу, которая определит индекс второго вхождения строки в списке либо сообщит, что её нет.