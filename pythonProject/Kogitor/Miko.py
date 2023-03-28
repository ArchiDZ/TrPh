from datetime import datetime
from array import *

def greeting():
    message = 'Привет, Я мико твой виртуальный ' \
              'помошник. Чем я могу тебе помочь?'
    print(message)
def which_month():
    w_month =array(['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь'])
    print(w_month)

def Run_miko():
    greeting()
    question = input('>>>')
    if question == 'дата':
        current_datetime = datetime.now()

        print(current_datetime.day)