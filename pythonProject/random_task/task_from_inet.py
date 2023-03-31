import datetime
import random
from sys import getsizeof


#28-03-2023 Задача1 smartiqa.ru/python-workbook
def what_result():
    result = 11*2**2-13/4+7
    print(result)
#28-03-2023 Задача2 smartiqa.ru/python-workbook
def mb_in_memory():
   y = getsizeof(3**9090001)/1024*1024
   print(y)
#28-03-2022 Задача2 smartiqa.ru/python-workbook
def bigest_number():
    x = 4**4**4
    print(x)

#28-03-2023 Задача5 smartiqa.ru/python-workbook
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

#29-03-2023 Задача5 smartiqa.ru/python-workbook
def num_sum(a):
    """ Задача 7
        Напишите функцию num_sum(a), принимающее любое значение, если
        это целое число , то возвратить сумму его чисел. В противном случае вернуть
        фразу "это не целое число"
    """
#30-03-2023
def game_cheharda():
    """Игра чехарда, Фраза: Я путешествовал через ... и встретил ... .... """
    first_word = ['Лес','город','поле','улицу','чащу','деревню','кусты','рынок','болото','джунгли']
    second_word = ['кровавого','пошлого','сильного','огромного','вонючего','хитрого','бешеного','грустного','великого','жестокого','косого',
                   'озабоченого','грязного','ароматного','красивого']
    third_word = ['орка','человека','эльфа','улитку','гнома','волка','ёжика','котика','гриб','плесень','старика']
    choser1 = random.randint(0,9)
    choser2 = random.randint(0,14)
    choser3 = random.randint(0,10)
    print(f'Я шел через {first_word[choser1]} и встретил {second_word[choser2]} {third_word[choser3]}')

#30-03-2023
def eght_ball():
    input('>>>')
    answer = ['Бесспорно','Предрешено','Никаких сомнений','Определённо да','Можешь быть уверен в этом',
              'Мне кажется — «да»','Вероятнее всего','Хорошие перспективы','Знаки говорят — «да»','Да',
              'Пока не ясно, попробуй снова','Спроси позже','Лучше не рассказывать','Сейчас нельзя предсказать','Сконцентрируйся и спроси опять',
              'Даже не думай','Мой ответ — «нет»','По моим данным — «нет»','Перспективы не очень хорошие','Весьма сомнительно']
    number = random.randint(0,19)
    print(answer[number])
#30-03-2023 кусок кода из Вконтакте
def outer(func):
    def inner(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args)
        ennd_time = datetime.now()
        time_result = ennd_time-start_time
        print(time_result)
    return inner()
