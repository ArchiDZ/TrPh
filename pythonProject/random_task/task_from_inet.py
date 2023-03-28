from sys import getsizeof


#28-03-2022 Задача1 smartiqa.ru/python-workbook
def what_result():
    result = 11*2**2-13/4+7
    print(result)
#28-03-2022 Задача2 smartiqa.ru/python-workbook
def mb_in_memory():
   y = getsizeof(3**9090001)/1024*1024
   print(y)
#28-03-2022 Задача2 smartiqa.ru/python-workbook
def bigest_number():
    x = 4**4**4
    print(x)

#28-03-2022 Задача5 smartiqa.ru/python-workbook
def pos_add(a,b):
    """Описание
    Напишите функцию pos_add(a,b) которая возвращает
    положительное значение двух целых чисел
    """
    result = a+b
    if result>0:
        print(result)
    elif result<0:
        print('Не допустимое значение по задаче')
