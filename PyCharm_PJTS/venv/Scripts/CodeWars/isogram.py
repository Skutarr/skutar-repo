# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
{'first_name': 'Вася'},
{'first_name': 'Петя'},
{'first_name': 'Маша'},
{'first_name': 'Маша'},
{'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

# print(students['first_name'])
# a=students[1]
def fun (x):
    """ Конский ХУЙ """
    counterVas = 0
    counterPet = 0
    counterMash = 0
    for i in range(len(students)):
        if (students[i])['first_name']=='Вася':
                counterVas=counterVas+1
        elif (students[i])['first_name']=='Петя':
                counterPet=counterPet+1
        elif (students[i])['first_name'] == 'Маша':
                counterMash = counterMash + 1
    print("Вася: Конский ХУЙ! Отпаравить в приемную Когогина")
    print("Петя: " + str(counterPet))
    print("Маша: " + str(counterMash))

    return counterVas,counterPet,counterMash

fun(students)