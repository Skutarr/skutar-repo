# import Module
from Module import aaa as aa
def create_record(first_item,second_item,third_item):
    record={
        'first_item'    : first_item,
        'second_item'   : second_item,
        'third_item'    :  third_item
    }
    return record

# print(create_record(1,2,3))
# Module.aaa()
# Module.ccc()
aa()


# если функция ничего не возвращает
# используется оператор "pass"
# результат такой функции вернется "NONE"
