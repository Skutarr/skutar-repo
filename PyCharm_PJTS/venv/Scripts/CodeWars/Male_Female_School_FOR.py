# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
'Маша': False,
'Оля': False,
'Олег': True,
'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

class2A=school[0]
class3C=school[1]

def fun (x) :
    length=len(x)

    for clas in range(length):
        male_qty = 0
        female_qty = 0
        theClass=school[clas]
        # print(theClass)
        for stud in range(len(theClass)-1):
            stud_list=theClass['students']
            # print(stud_list)
            for w in range(len(stud_list)):
                info_stud=stud_list[w]
                # print(info_stud)
                for e in range(len(info_stud)):
                    stud_name=info_stud['first_name']
                    # print(stud_name)
                    if is_male[stud_name] is True:
                        # print ('male')
                        male_qty=male_qty+1
                    else:
                        # print('female')
                        female_qty=female_qty+1

        print('In class ' + str(theClass['class'])+' ' + str(male_qty) + ' boys' +' and ' + str(female_qty) + ' girls')


fun(school)

