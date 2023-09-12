import random


def zadanie3_1():  # 23-03-2023
    cm = int(input("Введите значение в сантиметрах..."))
    m = cm / 100
    print(f"{cm}см это {m}м")


def zadanie3_2():
    kg = int(input("Введите значение в кг..."))
    cent = kg / 100
    print(f"{kg}кг ровняется {cent} центнеров")


def zadanie3_3():
    days = 234
    week = days/7
    print(round(week))


def zadanie3_4():
    children = random.randint(1, 30)
    apple = random.randint(1, 200)
    print(f"В классе учатся {children} детей")
    print(f"В корзине лежит {apple} яблок")
    x = apple / children
    y = apple % children
    print(f"Каждый школьник получит по {int(x)} яблок")
    print(f"В корзине останется лежать {y} яблок")


def zadanie3_5():
    storona1 = 543
    x = int(storona1 / 130)
    x_ost = int(storona1 % 130)
    print(f"Из прямоугольника может получиться {x} квадрата со стороной 130 "
          f"и останется прямоугольник {x_ost} на 130")


def zadanie3_6():
    mesto = 0
    for i in range(1, 10):
        for x in range(0, 4):
            mesto += 1
            print(f"Купе №{i} Место №{mesto}")
            # print(f"Место {mesto}")


def zadanie3_7():
    nomer_kvartiri = 0
    for i in range(1, 6):
        print(f"Этаж-->{i}")
        for x in range(0, 3):
            nomer_kvartiri += 1
            print(f"КВ_{nomer_kvartiri}")


def zadanie3_8():  # 28-03-2023
    kod_bileta = 1643
    detail = 'AB'
    for i in range(0, 300):
        i += 1
        real_ticket = kod_bileta+i
        print(f'кресло №{i},билет №[{detail} {real_ticket}]')


def zadanie3_9():  # 04-04-2023
    init_time = random.randint(1, 86400)
    left_hour = int(init_time / 3600)
    leftmin = int(init_time % 3600) / 60
    leftsec = 0  # ХЗ как это выщитать буксую
    print(f'С начала суток прошло {init_time} секунд')
    print(f'С начала суток прошло  {left_hour} полных часов')
    print(f'С начала нового часа прошло {int(leftmin)} минут')
    print(f'С начала новой минуты прошло {leftsec} секунд')


def zadanie3_16():  # 04-04-2023
    number = 97
    num1 = number / 10
    num2 = number % 10
    print(f'десятки -- {int(num1)}  еденицы -- {num2}')


def zadanie3_17():  # 04-04-2023
    number = int(input('>>>'))
    num1 = number / 10
    num2 = number % 10
    summ = num1 + num2
    print(f'десятки -- {int(num1)}  еденицы -- {num2}')
    print(f'Сумма цифр числа {number} = {int(summ)}')


def zadanie3_18():  # 04-04-2023
    number = int(input('>>>'))
    num1 = number / 10
    num2 = number % 10
    result = (int(num2)*10)+int(num1)
    print(f'{result}')


def zadanie3_19():  # 11-04-2023
    print('Введите трех значное число')
    number = int(input('>>>'))
    num1 = int(number/100)
    num2 = int((number/10) % 10)
    num3 = int(number % 10)
    print(f'{num1},{num2},{num3}')


def zadanie3_20():  # 11-04-2023
    print('Введите трех значное число')
    number = int(input('>>>'))
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    multiply = (num1*num2)*num3
    summ = num1+num2+num3
    print(f'Число едениц-->{num3}')
    print(f'Число десятков-->{num2}')
    print(f'Число сотен-->{num1}')
    print(f'Сумма цифр числа-->{summ}')
    print(f'Произведение цифр числа-->{multiply}')


def zadanie3_21():  # 11-04-2023
    print('Введите трех значное число')
    number = int(input('>>>'))
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    new_number = (num3*100)+(num2*10)+num1
    print(f'Зеркальное число-->{new_number}')


def zadanie3_22():  # 12-04-2023
    print('Введите трех значное число')
    number = int(input('>>>'))
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    new_number = (num2 * 100) + (num3 * 10) + num1
    print(f'Преобразованое число --> {new_number}')


def zadanie3_23():  # 12-04-2023
    number = random.randint(100, 1000)
    print(f'Трех значное число {number}')
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    new_number = (num3*100)+(num2*10)+num1
    print(f'Преобразованое число --> {new_number}')


def zadanie3_24():  # 12-04-2023
    number = random.randint(100, 1000)
    print(f'Трех значное число {number}')
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    new_number = (num2*100)+(num1*10)+num3
    print(f'Преобразованое число --> {new_number}')


def zadanie3_25():  # 12-04-2023
    number = random.randint(100, 1000)
    print(f'Трех значное число {number}')
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    new_number = (num1*100)+(num3*10)+num2
    print(f'Преобразованое число --> {new_number}')


def zadanie3_26():  # 12-04-2023
    number = random.randint(100, 1000)
    print(f'Трех значное число {number}')
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    num3 = int(number % 10)
    if num1 != num2 and num2 != num3 and num3 != num1:
        new_number1 = (num1 * 100) + (num3 * 10) + num2
        new_number2 = (num2 * 100) + (num1 * 10) + num3
        new_number3 = (num3 * 100) + (num2 * 10) + num1
        new_number4 = (num2 * 100) + (num3 * 10) + num1
        new_number5 = (num3 * 100) + (num2 * 10) + num1
        print(f'{new_number1},{new_number2},{new_number3},{new_number4},'
              f'{new_number5}')
    else:
        print('В числе есть совпадения, не возможно перестроить число')


def zadanie3_27():  # 12-04-2023
    number = random.randint(1000, 99999)
    print(f'Случайное число {number}')
    if number < 9999:
        print('Четырехзначное число')
        num1 = int(number / 1000)
        num2 = int(number / 100) % 10
        num3 = int(number / 10) % 10
        num4 = int(number % 10)
        summ = num1+num2+num3+num4
        print(f'{num1} {num2} {num3} {num4}')
        print(f'Суммы цифр данного числа -->{summ}')
    else:
        print('Пятизначное число')
        num1 = int(number / 10000)
        num2 = int(number / 1000) % 10
        num3 = int(number / 100) % 10
        num4 = int(number / 10) % 10
        num5 = int(number % 10)
        summ = num1+num2+num3+num4+num5
        print(f'{num1} {num2} {num3} {num4} {num5}')
        print(f'Суммы цифр данного числа -->{summ}')


def zadanie3_28():  # 13-04-2023
    number = random.randint(1000, 9999)
    print(f'Дано число: {number}')
    num1 = int(number / 1000)
    num2 = int(number / 100) % 10
    num3 = int(number / 10) % 10
    num4 = int(number % 10)
    print('Преобразования числа')
    new_number1 = (num4 * 1000) + (num3 * 100) + (num2 * 10) + num4
    print(f'a) {new_number1}')
    new_number2 = (num2 * 1000) + (num1 * 100) + (num4 * 10) + num3
    print(f'b) {new_number2}')
    new_number3 = (num1 * 1000) + (num3 * 100) + (num2 * 10) + num4
    print(f'c) {new_number3}')
    new_number4 = (num4 * 1000) + (num3 * 100) + (num1 * 10) + num2
    print(f'd) {new_number4}')


def zadanie3_29():  # 13-04-2023
    number = random.randint(9, 99)
    num1 = int(number / 10)
    num2 = int(number % 10)
    print(f'Случайное число {number}')
    print(f'Число десятков в числе {num1}')
    print(f'Число едениц в числе {num2}')


def zadanie3_30():
    number = random.randint(99, 999)
    num1 = int(number / 100)
    num2 = int((number / 10) % 10)
    print(f'Случайное число {number}')
    print(f'Число сотен в числе {num1}')
    print(f'Число десятков в числе {num2}')


def zadanie3_31():
    number = random.randint(999, 9999)
    num1 = int(number / 1000)
    num2 = int((number / 100) % 10)
    print(f'Случайное число {number}')
    print(f'Число тысяч в числе {num1}')
    print(f'Число сотен в числе {num2}')


def zadanie3_32():  # 27-07-2023
   number = 237
   num1 = int(number / 100)
   num2 = number - (num1*100)
   num3 = (num2*10)+num1
   print(num3)


def zadanie3_33():  # 08-08-2023
    number = random.randint(99, 1000)
    print(f'Число -- {number}')
    num3 = number % 10
    newNum = int((number-num3)/10)
    print(newNum)
    print(num3*100+newNum)


def zadanie3_34():  # 08-08-2023
    number = 564
    


def zadanie3_51():  # 14-04-2023
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f'a={a} b={b}')
    ab = bool(a/b)
    ba = bool(b/a)
    print(int(ab))
    print(int(ba))