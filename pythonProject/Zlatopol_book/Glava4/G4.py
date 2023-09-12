import random


def zadanie4_1():  # 14-04-2023
    num1 = random.uniform(0.01, 9.99)
    num2 = random.uniform(0.01, 9.99)
    print(f'Число1-->{num1} Число2-->{num2}')
    if num1>num2:
        print(f'Число 1 больше --- {num1}')
        print(f'Число 2 меньше --- {num2}')
    if num2>num1:
        print(f'Число 2 больше --- {num2}')
        print(f'Число 1 меньше --- {num1}')


def zadanie4_11():
    speed1 = random.uniform(0.1, 100.0)
    speed2 = random.uniform(0.1, 100.0)
    print()



def zadanie4_60():  # 02-05-2023
    man1 = random.uniform(1.00, 2.00)
    man2 = random.uniform(1.00, 2.00)
    man3 = random.uniform(1.00, 2.00)
    print(f'Человек № 1 с ростом {man1}см')
    print(f'Человек № 2 с ростом {man2}см')
    print(f'Человек № 3 с ростом {man3}см')
    if man1 > man2:
        print('Человек № 1 выше человека № 2')
    if man2 > man1:
        print('Человек № 2 выше человека № 1')
    if man1 > man3:
        print('Человек № 1 выше человека № 3')
    if man1 < man3:
        print('Человек № 3 выше человека № 1')
    if man2 > man3:
        print('Человек № 2 выше человека № 3')
    if man2 < man3:
        print('Человек № 3 выше человека № 2')