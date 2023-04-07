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
    car_list = ['BMW', 'AUDI', 'SAAB', 'VOLVO', 'MERCEDES', 'LIFFAN', 'RENO', 'LADA', 'FORD',
                'SUBARU', 'TAYOTA', 'HYUNDAI', 'ISUZU', 'MAZDA']
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
