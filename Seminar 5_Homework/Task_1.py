'''Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
in
Number of words: 10
out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба'''

from random import choices

size = int(input('Number of words: '))

def word(size, lst):
    listWord = []
    for i in range(size):
        selection = choices(lst, k=3)
        listWord.append("".join(selection))
    return listWord
    
def deleteWords(myList):
    myList = list(filter(lambda x: 'абв' not in x, myList.split()))
    return " ".join(myList)

myList = (" ".join(map(str, word(size,'абв'))))

print(myList)
print(deleteWords(myList))