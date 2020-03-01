# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
{'first_name': 'Вася'},
{'first_name': 'Петя'},
{'first_name': 'Маша'},
{'first_name': 'Маша'},
{'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

def fun (x):
    counterVas = 0
    counterPet = 0
    counterMash = 0
    counterOl = 0

    for i in range(len(students)):
        if (students[i])['first_name']=='Вася':
                counterVas=counterVas+1
        elif (students[i])['first_name']=='Петя':
                counterPet=counterPet+1
        elif (students[i])['first_name'] == 'Маша':
                counterMash = counterMash + 1
        elif (students[i])['first_name'] == 'Оля':
            counterOl = counterOl + 1

    newList=[
        {'first_name': 'Вася','qty_rep': counterVas},
        {'first_name': 'Петя', 'qty_rep': counterPet},
        {'first_name': 'Маша', 'qty_rep': counterMash},
        {'first_name': 'Оля', 'qty_rep': counterOl}
    ]
    print("Вася: " + str(counterVas))
    print("Петя: " + str(counterPet))
    print("Маша: " + str(counterMash))
    print("Оля: " + str(counterOl))

    if counterVas>counterPet and counterVas>counterMash and counterVas>counterOl:
        print("Самое частое имя среди учеников: Вася")
    elif counterVas < counterPet and counterPet > counterMash and counterPet > counterOl:
        print("Самое частое имя среди учеников: Петя")
    elif counterMash > counterPet and counterMash > counterPet and counterMash > counterOl:
        print("Самое частое имя среди учеников: Маша")
    elif counterOl > counterVas and counterOl > counterPet and counterOl > counterMash:
        print("Самое частое имя среди учеников: Оля")

    return counterVas,counterPet,counterMash

fun(students)