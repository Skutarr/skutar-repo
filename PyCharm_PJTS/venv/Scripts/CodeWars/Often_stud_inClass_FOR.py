# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
[ # это – первый класс
{'first_name': 'Вася'},
{'first_name': 'Вася'},
],
[ # это – второй класс
{'first_name': 'Маша'},
{'first_name': 'Маша'},
{'first_name': 'Оля'},
]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


#
# print((classA[1]['first_name']))
# print((classB))

def fun (x):
    classA = x[0]
    classB = x[1]

    counterVas_classA = 0
    counterPet_classA = 0
    counterMash_classA = 0
    counterOl_classA = 0

    counterVas_classB = 0
    counterPet_classB = 0
    counterMash_classB = 0
    counterOl_classB = 0


    # FOR  for classA
    for i in range(len(classA)):
        if (classA[i])['first_name']=='Вася':
                counterVas_classA=counterVas_classA+1
        elif (classA[i])['first_name']=='Петя':
                counterPet_classA=counterPet_classA+1
        elif (classA[i])['first_name'] == 'Маша':
                counterMash_classA = counterMash_classA + 1
        elif (classA[i])['first_name'] == 'Оля':
                counterOl_classA = counterOl_classA + 1

    # FOR  for classA
    for i in range(len(classB)):
        if (classB[i])['first_name'] == 'Вася':
            counterVas_classB = counterVas_classB + 1
        elif (classB[i])['first_name'] == 'Петя':
            counterPet_classB = counterPet_classB + 1
        elif (classB[i])['first_name'] == 'Маша':
            counterMash_classB = counterMash_classB + 1
        elif (classB[i])['first_name'] == 'Оля':
            counterOl_classB = counterOl_classB + 1

    # print("Вася1: " + str(counterVas))
    # print("Петя1: " + str(counterPet))
    # print("Маша1: " + str(counterMash))
    #
    # print("Вася2: " + str(counterVas))
    # print("Петя2: " + str(counterPet))
    # print("Маша2: " + str(counterMash))

    if counterVas_classA > counterPet_classA and counterVas_classA > counterMash_classA and counterVas_classA > counterOl_classA:
        print("Самое частое имя среди учеников класса А: Вася")
    elif counterVas_classA < counterPet_classA and counterPet_classA > counterMash_classA and counterPet_classA > counterOl_classA:
        print("Самое частое имя среди учеников класса А: Петя")
    elif counterMash_classA > counterPet_classA and counterMash_classA > counterPet_classA and counterMash_classA > counterOl_classA:
        print("Самое частое имя среди учеников класса А: Маша")
    elif counterOl_classA > counterVas_classA and counterOl_classA > counterPet_classA and counterOl_classA > counterMash_classA:
        print("Самое частое имя среди учеников класса А: Оля")

    if counterVas_classB > counterPet_classB and counterVas_classB > counterMash_classB and counterVas_classB > counterOl_classB:
        print("Самое частое имя среди учеников класса B: Вася")
    elif counterVas_classB < counterPet_classB and counterPet_classB > counterMash_classB and counterPet_classB > counterOl_classB:
        print("Самое частое имя среди учеников класса B: Петя")
    elif counterMash_classB > counterPet_classB and counterMash_classB > counterPet_classB and counterMash_classB > counterOl_classB:
        print("Самое частое имя среди учеников класса B: Маша")
    elif counterOl_classB > counterVas_classB and counterOl_classB > counterPet_classB and counterOl_classB > counterMash_classB:
        print("Самое частое имя среди учеников  класса B: Оля")


    # return counterVas,counterPet,counterMash

fun(school_students)

# print((a['first_name']))
# print((c))











