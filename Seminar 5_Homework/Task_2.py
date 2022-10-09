'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

with open('Seminar 5_Homework/file_encode_entrance.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('Seminar 5_Homework/file_encode_entrance.txt', 'r') as data:
    string = data.readline()

def coding(txt):
    encoded_string = ''
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    decoded_string = ''
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open('Seminar 5_Homework/file_encode_entrance.txt', 'r') as file:
    decoded_string = file.read()

with open('Seminar 5_Homework/file_decode_exit.txt', 'w') as file:
    encoded_string = coding(decoded_string)
    file.write(encoded_string)

print(f"Текст после кодировки: {coding(decoded_string)}")
print(f"Текст после дешифровки: {decoding(coding(decoded_string))}")