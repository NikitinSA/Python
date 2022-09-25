"""Напишите программу, которая принимает на вход координаты двух точек и 
находит расстояние между ними в 2D пространстве.
in
- 3
- 6
- 2
- 1
out
5.099"""
import math

numA1 = float(input('Введите координату А1: '))
numA2 = float(input('Введите координату А2: '))
numB1 = float(input('Введите координату B1: '))
numB2 = float(input('Введите координату B2: '))

result = math.sqrt((numB1 - numA1)**2 + (numB2 - numA2)**2)

print (f"A({numA1},{numA2}); B({numB1},{numB2}) -> {round(result,3)}")