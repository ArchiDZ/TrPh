import random
from datetime import datetime


def greeting():
    message = 'Привет, Я мико твой виртуальный ' \
              'помошник. Чем я могу тебе помочь?'
    print(message)


def excercise_chooser():
    book_list = ['Златопольский', 'Каннель-Фриман', 'Задачник']
    book_chooser = random.randint(0, 2)
    chapter_chooser = random.randint(1, 13)
    exer_chooser = random.randint(1, 100)
    print(f'Попробуй решить из книги {book_list[book_chooser]} Глава {chapter_chooser} Задача {exer_chooser}')


def run_miko():
    greeting()
    excercise_chooser()
    question = input('>>>')
