import random


def upr_2_1():  # 17-04-2023
    f = 'Hello'
    print(f)


def upr_2_2():  # 17-04-2023
    message1 = 'Hello world'
    print(message1)
    message1 = 'World hello'
    print(message1)


def upr_2_3():  # 17-04-2023
    name = 'Bob'
    print(f'Hello {name}, Lets Play the Game')


def upr_2_4():  # 17-04-2023
    name = 'terminator'
    print(name.title())
    print(name.lower())
    print(name.upper())


def upr_2_5():  # 17-04-2023
    name = 'terminator T-1000'
    frase = 'I will be back'
    print(f'{name} once said "{frase}"')


def upr_2_6():  # 17-04-2023
    """Аналогичное задание 2.5"""


def upr_2_7():  # 17-04-2023
    message = "Albert Einstein once \tsaid, \nperson who never made " \
              "a mistake never tried anything new"
    print(message)
    print(message.lstrip())
    print(message.rstrip())
    print(message.strip())


def upr_2_8():  # 17-04-2023
    num1 = 4+4
    num2 = 12-4
    num3 = 4*2
    num4 = 16/2
    print(f'{num1} \t{num2} \t{num3} \t{num4}')


def upr_2_9():  # 17-04-2023
    favorite_num = 14
    print(f'My favorite number is {favorite_num}')


def upr_2_10():  # 17-04-2023
    # Однострочный коментарий
    """Многострочный коментарий"""

def upr_3_1(): # 17-04-2023
    friend_name = ['Геральт', 'Мики Маус', 'Тони Монтана']
    print(friend_name[0])
    print(friend_name[1])
    print(friend_name[2])


def upr_3_2():  # 17-04-2023
    friend_name = ['Геральт', 'Мики Маус', 'Тони Монтана']
    print(f'Привет, {friend_name[0]}!')
    print(f'Привет, {friend_name[1]}!')
    print(f'Привет, {friend_name[2]}!')


def upr_3_3():  # 17-04-2023
    cars = ['NIVA', 'MiniCooper', 'Audi']
    for car in cars:
        print(f'I like, {car}')


def upr_3_4():  # 17_04_2023
    persons = ['Грей', 'Алиса ВандерХиден', 'Т1000', 'МикиМаус', 'Гуфи']
    for person in persons:
        print(f'{person}, Приглашаю на обед в английский ПАБ')
        if person == 'Гуфи':
            print(f'{person} Не сможет прийти.')
    persons = ['Грей', 'Алиса ВандерХиден', 'Т1000', 'МикиМаус']
    persons.append('Дональд Дак')
    for person in persons:
        print(f'{person}, Приглашаю на обед в английский ПАБ')

def upr_3_5():  # 18-04-2023
    persons = ['Грей', 'Алиса ВандерХиден', 'Т1000', 'МикиМаус', 'Гуфи']
    for person in persons:
        print(f'{person}, Приглашаю на обед в английский ПАБ')


def upr_4_1():  # 06-04-2023
    pizza_list = ['cheese', 'hunter', 'hawaii', 'pepperoni']
    for pizza in pizza_list:
        print(f'I like {pizza} pizza')
    print('I really like pizza')


def upr_4_2():  # 06-04-2023
    animals = ['cat', 'dog', 'cow', 'elephant', 'monkey', 'tiger']
    for animal in animals:
        print(animal.title())
        print(f'A {animal} would make a great pet')
    print('Any of these animals would make a great pet')


def upr_4_3():  # 05-04-2023 Задания из самоучителя по  Python
    simple_list = []
    for num in range(1, 21):
        simple_list.append(num)
    print(simple_list)


def upr_4_4():  # 05-04-2023 Задания из самоучителя по  Python
    for number in range(1, 1000000):
        number += 1
        print(number)


def upr_4_5():  # 05-04-2023 Задания из самоучителя по  Python
    list_num = []
    for i in range(1, 1000000):
        list_num.append(i)
    print(list_num)
    print('Отдельные методы')
    print(min(list_num))
    print(max(list_num))
    print(sum(list_num))


def upr_4_6():  # 05-04-2023 Задания из самоучителя по  Python
    list1 = []
    list2 = []
    for i in range(1, 21):
        if i % 2 != 0:
            list1.append(i)
        else:
            list2.append(i)
    print(f'Нечетные числа {list1}')
    print(f'Четные числа {list2}')


def upr_4_7():  # 05-04-2023 Задания из самоучителя по  Python
    nums = list(range(3, 33, 3))
    print(nums)


def upr_4_8():  # 05-04-2023 Задания из самоучителя по  Python
    cube_list = []
    for i in range(1, 11):
        cube_list.append(i**3)
    print(cube_list)


def upr_4_9():  # 06-04-2023
    cube_list = [num ** 3 for num in range(1, 30)]
    print(cube_list)


def upr_4_10():  # 06-04-2023
    car_list = ['BMW', 'AUDI', 'SAAB', 'VOLVO', 'MERCEDES', 'LIFFAN', 'RENO',
                'LADA', 'FORD', 'SUBARU', 'TAYOTA', 'HYUNDAI', 'ISUZU', 'MAZDA']
    for ls1 in car_list[:3]:
        print(f'First items in list are {ls1}')
    print('--------------------------------#')
    for ls2 in car_list[3:11]:
        print(f'Midlle items in list are {ls2}')
    print('--------------------------------#')
    for ls3 in car_list[-3:]:
        print(f'The last item in list are {ls3}')


def upr_4_11():  # 07-04-2023
    stuff_list = ['apple', 'heal potion', 'sword']
    copy_stuff_list = stuff_list[:]
    copy_stuff_list.append('shield')
    copy_stuff_list.append('helmet')
    print('Original list')
    print(stuff_list)
    print('This is copy of stuff list with few new items')
    print(copy_stuff_list)


def upr_4_12():  # 07-04-2023
    stuff_list = ['apple', 'heal potion', 'sword']
    copy_stuff_list = stuff_list[:]
    copy_stuff_list.append('shield')
    copy_stuff_list.append('helmet')
    for stuf1 in stuff_list:
        print(f'In my bag : {stuf1}')
    for stuf2 in copy_stuff_list:
        print(f'In my new bag : {stuf2}')


def upr_4_13():  # 07-04-2023
    swed_table = ('фасоль', 'суп', 'картофель', 'свинина', 'жёлуди')
    print('Сегодня на обед предлогаются: ')
    for food in swed_table:
        print(f'-{food}')

    swed_table = ('фасоль', 'суп', 'картофель', 'рыба озерная', 'каштаны')
    print('Завтра ресторан предлогает попробовать: ')
    for fod in swed_table:
        print(f'-{fod}')


def upr_5_3():  # 20-04-2023
    color_list = ['yellow', 'green', 'red', 'white']
    rnd_num = random.randint(0, 3)
    ship = color_list[rnd_num]
    print(ship)
    if ship == 'yellow':
        print(f'{ship} alien ship FALL!\t+10 score')
    if ship == 'green':
        print(f'{ship} alien ship FALL!\t+15 score')
    if ship == 'red':
        print(f'{ship} alien ship FALL!\t+25 score')
    if ship == 'white':
        print(f'{ship} alien ship FALL!\t+5 score')


def upr_5_4():  # 20-04-2023
    color_list = ['green', 'red']
    green = 0
    red = 0
    for x in range(1, 21):
        rnd_num = random.randint(0, 1)
        result = color_list[rnd_num]
        if result == 'green':
            print(f'{result} +5')
            green += 5
        else:
            print(f'{result} +10')
            red += 10
    print(f'Scores: green->{green} \tred->{red}')


def upr_5_5():  # 21-04-2023
    color_list = ['green', 'red', 'black']
    green = 0
    red = 0
    black = 0
    for x in range(1, 21):
        rnd_num = random.randint(0, 2)
        result = color_list[rnd_num]
        if result == 'green':
            print(f'{result} +5')
            green += 5
        elif result == 'red':
            print(f'{result} +10')
            red += 10
        else:
            print(f'{result} +15')
            black += 15
    print(f'Scores: green->{green} \tred->{red} \tblack->{black}')


def upr_5_6():  # 21-04-2023
    age = random.randint(1, 100)
    if age < 2:
        print('Младенец')
    elif 2 <= age < 4:
        print('Малыш')
    elif 4 <= age < 13:
        print('Ребенок')
    elif 13 <= age < 20:
        print('Подросток')
    elif 20 <= age < 65:
        print('Взрослый')
    else:
        print('Пожилой')


def upr_5_7():  # 25-04-2023
    favorite_fruit = ['apple', 'banana', 'pineapple']
    if 'orange' in favorite_fruit:
        print('Dismatch')

    if 'banana' in favorite_fruit:
        print('Match')
