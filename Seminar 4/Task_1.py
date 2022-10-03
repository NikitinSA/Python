'''Задайте строку из набора чисел. Напишите программу, 
которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел.'''

def check(line):
    arr = line.split()
    for i in arr:
        if not i.strip("-").isdigit():
            return []
    return arr

def minMax(array):
    if array:
        return min(array, key=int), max(array, key=int)
    else:
        return []


f = check("2 3 4 5 6 7")
print(minMax(f))