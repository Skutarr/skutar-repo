# применяются для анализа/обработки текста
# поиск по важным символам , наборам символов
import re
# ---------------------------- First lesson ---------------------
mytext= "rergerg,trwv,name,date,name,123,456789,matrix,sel,"
textlookfor =r"name" # регулярное выражение
# описание литераллов
"""
/d- поиск любой цифры 0-9
/D - любой нецифровой символ 
/w - любой алфавитный символ [A-Z a-z]
/W - любой не алфавитный символ 
/s - поиск пробел
/S - любой элемент , но не пробел

/d/d/d/     - поиск любых стоящих 3 цифры   -----> 123,456,789
[0-9][3]    - поиск любых стоящих 3 цифры  -----> 123,456,789

[A-Z][a-z]  - ищем первй символ большой , второй маленький 
[A-Z][a-z]+ - неважно сколько символов после  ----> вывод всех имен , которые начинаются с большой буквы 
\w+\.\w+    - вывод мейлов yandex.ru
@\w+\.\w+   -@yandex.ru
"""
#                     patern - то что ищем
allresults= re.findall(textlookfor, mytext)  # поиск слова, также есть найти и заменить
#                                    ^string - где ищем
#
# примеры комбинаций для регулярных выражений есть на сайте regex101
print(allresults)
# ----------------------------  Second lesson ---------------------

input_filename= "../dumpfile.txt" # ../ директорией выше
result_filename= "../results.txt"

inputfile= open(input_filename, mode='r', encoding='Latin-1')
resultfile= open(result_filename, mode='w',encoding='Latin-1')
mytext= inputfile.read()

lookfor= r'' # любое регулярное выражение
results= re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item)

print("Total: " + str(len(results)))
