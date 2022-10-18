import random
import csv
import logger as lg


file = open('employees_base.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,email,Salary,Position\n"
file.writelines(newrecord)

ls_name = ['Lana', 'Dima', 'Anna', 'Natasha', 'Pasha', 'Denis', 'Kate', 'Sonya', 'Roma', 'Igor', 'Lina']
ls_surname = ['Petrenko', 'Ivanov', 'Nebozenko', 'Kaleeva', 'Zinchenko', 'Kushnir', 'Krasota', 'Usenko', 'Morozov', 'Fomenko', 'Vitek']
ls_e_mail = ['11111@gmail.com', '2222222@yandex.ru', '333333@mail.ru', '44444444@gmail.com', '5555555@gmail.com', '666666666@mail.ru', '77777777@mail.ru', '88888888@mail.ru', '99999999@yandex.ru']
ls_position = ['teacher of math', 'teacher of history', 'English teacher', 'Spanish teacher', 'German teacher', 'Methodist']


def list_of_numbers():
    randomListPhone = random.randint(79000000000, 80000000000)
    return str(randomListPhone)

def salary():
    randomListSalary = random.randrange(60000, 150000, 10000)
    return str(randomListSalary)

def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + list_of_numbers() + ',' + random.choice(ls_e_mail) + ',' + salary() + ',' + random.choice(ls_position)
    return s


def start():
    for i in range(25):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()