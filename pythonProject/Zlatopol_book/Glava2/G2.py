import math
import random


def zadanie2_1_variant_a():  # 22-03-2023
    x = int(input("Введите число..."))
    y = (17 * (x ** 2)) - ((6 * x) + 13)
    print(y)


def zadanie2_1_variant_b():  # 22-03-2023
    x = int(input("Введите число..."))
    y = (3 * (x ** 2)) + ((5 * x) - 21)
    print(y)


def zadanie2_2():  # 22-03-2023
    number = int(input("Введите число..."))
    chis = (number ** 2) + 10
    znam = math.sqrt(number ** 2 + 1)
    result = chis / znam
    print(result)


def zadanie2_3_variant_a():  # 22-03-2023
    number = int(input("Введите число..."))
    chisl = 2 * number + math.sin(3 * number)
    znam = 3.56
    result = math.sqrt(chisl / znam)
    print(result)


def zadanie2_3_variant_b():  # 22-03-2023
    number = int(input("Введите число..."))
    chisl = 3.2 + math.sqrt(1 + number)
    znam = 5 * number
    result = math.sin(chisl / znam)
    print(result)


def zadanie2_4():  # 22-03-2023
    number = int(input("Введите сторону квадрата"))
    p = number * 4
    print(f"Периметр квадрата со стороной {number} равен {p}")


def zadanie2_5():  # 22-03-2023
    number = int(input("Введите радиус окружности..."))
    pi = 3.14
    p = 2 * pi * number
    print(f"Периметр окружности равен {p} при радиусе {number}")


def zadanie2_6():  # 22-03-2023
    x = int(input("Введите значение высоты в км..."))
    formula = math.sqrt(x * (2 * 6350 + x))
    print(f"Расстояние до горизонта  {formula} км")


def zadanie2_7():  # 22-03-2023
    rebro = int(input("Введите длинну ребра куба..."))
    perimtr = rebro * 4
    plshad = rebro * rebro * rebro
    print(f"Дан куб с ребром {rebro} его обьем состовляет {plshad}")
    print(f'Периметр состовляет {perimtr}')


def zadanie2_8():  # 22-03-2023
    r = int(input("Введите радиус окружности..."))
    pi = 3.14
    dlina_okr = 2 * pi * r
    s_okr = ((pi * r) ** 2)
    print(f"Окружность с радиусом {r} имеет длинну {dlina_okr} и площадь окружности {s_okr}")


def zadanie2_9_variant_a():  # 22-03-2023
    x = random.randint(1, 100)  # Случайное число от 1 до 100
    y = random.randint(1, 100)
    formula = 2 * (x ** 3)-3.44 * x * y + 2.3 * (x ** 2)-7.1 * y + 2
    print(f"x={x}  y={y}")
    print(f"Результат вычислений-->{formula}")


def zadanie2_9_variant_b():  # 22-03-2023
    x = random.randint(1, 100)  # Случайное число от 1 до 100
    y = random.randint(1, 100)
    formula = 3.14 * ((x + y) ** 3) + 2.75 * (y ** 2) - 12.7 * x - 4.1
    print(f"x={x}  y={y}")
    print(f"Результат вычислений-->{formula}")


def zadanie2_10():  # 22-03-2023
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    avg = (number1 + number2) / 2
    geo = math.sqrt(number1 * number2)
    print(f"Даны два числа {number1} и {number2}")
    print(f"Среднее арифмитическое равно {avg} а средне геометрическое равно {geo}")


def zadanie2_11():  # 22-03-2023
    objom = random.randint(1, 100)
    ves = random.randint(1, 100)
    plotnostj = ves / objom
    print(f"Обьем гипотетического тела... {objom}")
    print(f" Вес гипотетического тела... {ves}")
    print(f"Плотность данного тела состовляет ... {plotnostj}")


def zadanie2_12():  # 22-03-2023
    zhiteli = random.randint(1, 1000000)
    ploshad_gos = random.randint(1000, 100000)
    plotnost_naselenia = zhiteli/ploshad_gos
    print(f"Гипотетическое государство с площадью {ploshad_gos} км на которой проживают {zhiteli} человек")
    print(f"Плотность населения состовляет {plotnost_naselenia}")


def zadanie2_13():  # 23-03-2023
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"{a}X+{b}=0")
    x = -b/a
    print(f"X={round(x,2)}")


def zadanie2_14():  # 23-03-2023
    katet1 = random.randint(1, 25)
    katet2 = random.randint(1, 25)
    gipotenuza = (katet1**2)+(katet2**2)
    result = math.sqrt(gipotenuza)
    print(f"Катет 1={katet1}  Катет 2={katet2}   Гипотенуза={round(result,2)}")


def zadanie2_15():  # 23-03-2023
    vneshniy_r = random.randint(1, 100)
    max_vnr = vneshniy_r
    vnutrenniy_r = random.randint(1, max_vnr-1)
    pi = 3.14
    s1 = 2*pi*(vneshniy_r**2)
    s2 = 2 * pi * (vnutrenniy_r ** 2)
    print(f"Площадь кольца по внешнему радиусу равна {s1}")
    print(f"Площадь кольца по внутриннему радиусу радиусу равна {s2}")


def zadanie2_16():  # 23-03-2023
    katet1 = random.randint(1, 100)
    katet2 = random.randint(1, 100)
    gipotenuza = math.sqrt((katet1**2)+(katet2**2))
    p_treugolnika = katet1+katet2+round(gipotenuza, 1)
    print(f"Катет1={katet1}")
    print(f"Катет2={katet2}")
    print(f"Гипотенуза={gipotenuza}")
    print(f"Периметр треугольника={p_treugolnika}")


def zadanie2_17():  # 26-3-2023
    osnovanie = random.randint(1, 25)
    visota = random.randint(1, 30)
    print(f"Равнобедренная трапеция. Основание--{osnovanie} высота--{visota}")
    # я хз какая тут формула нахождкния боковой стороны


def zadanie2_18():  # 26-3-2023
    x = random.randint(1, 15)
    y = random.randint(1, 10)
    formula1 = x+(2+y)/(x**2)
    formula2 = y+1/(math.sqrt((x**2)+10))
    result = formula1/formula2
    print(f"Число Х {x} Число У {y} Результат вычисления формулы {result}")


def zadanie2_19():  # 29-03-2023
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    first_part = (2/((a**2)+25))+b
    second_part = math.sqrt(b)+((a+b)/2)
    result = first_part/second_part
    y = (a+(2*math.sin(b)))/5.5*a
    print(f'Значение а={a} Значение b={b}')
    print(f'Числитель={first_part} знаменатель={second_part}')
    print(f'Результат деления {result}')
    print(f'Результат вычисления У={y}')


def zadanie2_20():
    print()
    # Later


def zadanie2_21():
    print()
    # Later


def zadanie2_22():
    print()
    # Later


def zadanie2_23():  # 26-03-2022
    storona1 = random.randint(1, 50)
    storona2 = random.randint(1, 25)
    p = (storona1+storona2)*2
    print(f"Сторона1={storona1} Сторона2={storona2}")
    print(f"Периметр прямоугольника равен {p}")


def zadanie2_24():  # 26-03-2022
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    summa = number1+number2
    raznost = 0
    if number1 > number2:
        raznost = number1-number2
    if number2 > number1:
        raznost = number2-number1
    proizvedenie = number1*number2
    chasnoe1 = number1/number2
    chasnoe2 = number2/number1
    print(f"Число1={number1} Число2={number2}")
    print(f"Сумма чисел {summa}")
    print(f"Роазность чисел {raznost}")
    print(f"Произведение чисел {proizvedenie}")
    print(f"Частное от деления 1 на 2 {chasnoe1}")
    print(f"Частное от деления 2 на 1 {chasnoe2}")


def zadanie2_25():
    """Даны длины сторон прямоугольного параллелипипида,
       Найтти его обьем и площадь боковой поверхности"""


def zadanie2_31():  # 29-03-2023
    apple_price = random.uniform(50.00, 200.00)
    apple_weight = random.randint(1, 10)
    coockie_price = random.uniform(39.00, 450.00)
    coockie_weight = random.randint(1, 10)
    print('Расценки')
    print(f'Яблоки {round(apple_price, 2)}р')
    print(f'Печенье {round(coockie_price, 2)}р')
    print('Покупка')
    print(f'Яблок {apple_weight}кг')
    print(f'Печенье {coockie_weight}кг')
    money_for_apple = apple_weight*apple_price
    money_for_coockie = coockie_weight*coockie_price
    total_money = money_for_coockie+money_for_apple
    print(f'За яблоки {round(money_for_apple,2)}р')
    print(f'За печенье {round(money_for_coockie,2)}р')
    print(f'Общая сумма покупки {round(total_money,2)}')


def zadanie2_32():  # 29-03-2023
    monitor_price = random.uniform(100.00, 2000.00)
    keyboar_price = random.uniform(10.00, 1000.00)
    pc_price = random.uniform(1000.00, 3500.00)
    work_set = monitor_price+keyboar_price+pc_price
    quantity = random.randint(1, 10)
    total_price = work_set*quantity
    print('Расценки')
    print(f'Монитор {round(monitor_price,2)}$')
    print(f'Клавиатура {round(keyboar_price,2)}$')
    print(f'Компьютер {round(pc_price,2)}$')
    print(f'Цена за комплект {round(work_set,2)}')
    print(f'Стоимость {quantity} комплектов {round(total_price,2)}$')


def zadanie2_34():  # 31-03-2023
    car_brend = ['BMW', 'AUDI', 'SAAB', 'VOLVO', 'MERCEDES', 'LIFFAN', 'RENO', 'LADA', 'FORD',
                 'SUBARU', 'TAYOTA', 'HYUNDAI', 'ISUZU', 'MAZDA']
    rnd_num1 = random.randint(0, len(car_brend)-1)
    rnd_num2 = random.randint(0, len(car_brend) - 1)
    speed_car1 = random.randint(1, 220)
    speed_car2 = random.randint(1, 220)
    road = random.randint(1, 1000)
    sum_speed = speed_car1+speed_car2
    result = road/sum_speed
    print(f'Первая машина {car_brend[rnd_num1]}')
    print(f'Едет со скоростью {speed_car1}км/ч')
    print(f'Вторая машина {car_brend[rnd_num2]}')
    print(f'Едет со скоростью {speed_car2}км/ч')
    print(f'Расстояние между автомобилями {road}')
    print(f'Автомобили встретятся через {round(result,2)} часов')


def zadanie2_35():  # 03-04-2023
    car_brend = ['BMW', 'AUDI', 'SAAB', 'VOLVO', 'MERCEDES', 'LIFFAN', 'RENO', 'LADA', 'FORD',
                 'SUBARU', 'TAYOTA', 'HYUNDAI', 'ISUZU', 'MAZDA']
    rnd_num1 = random.randint(0, len(car_brend) - 1)
    rnd_num2 = random.randint(0, len(car_brend) - 1)
    speed_car1 = random.randint(1, 220)
    speed_car2 = random.randint(1, 220)
    print(f'Первая машина {car_brend[rnd_num1]}')
    print(f'Едет со скоростью {speed_car1}км/ч')
    print(f'Вторая машина {car_brend[rnd_num2]}')
    print(f'Едет со скоростью {speed_car2}км/ч')
    s = random.randint(1, 25)
    if speed_car1 > speed_car2:
        print("Машина 1 двигается быстрее")
        result = s+(abs(speed_car1-speed_car2)*0.5)
        print(result)
    if speed_car2 > speed_car1:
        print("Машина 2 двигается быстрее")
        result = s + (abs(speed_car2 - speed_car1) * 0.5)
        print(f'Растояние между автомобилями {result}')
        

def zadanie2_36():  # 31-03-2023
    temperatur_cels = random.randint(-100, 100)
    temperatur_far = (temperatur_cels*1.8)+32
    temperatur_kelvin = temperatur_cels+273.15
    print(f'Температура по цельсию ... {temperatur_cels}')
    print(f'Температура по фаренгейту ... {round(temperatur_far,2)}')
    print(f'Температура по кельвину ... {round(temperatur_kelvin,2)}')


def zadanie2_37():  # 04-04-2023
    t_far = 450
    t_cels = (t_far-32)/1.8
    t_kelvin = t_cels+273.15
    print(f'Исходна температура по Фаренгейту {t_far}')
    print(f'Температура по Кельвину {round(t_kelvin,2)}')
    print(f'Темпратура по Цельсию {round(t_cels,2)}')


def zadanie2_38():  # 04-04-2023
    num1 = int(input('Первое число...'))
    num2 = int(input('Второе число ...'))
    plus = num1+num2
    minus = num1 - num2
    umn = num1*num2
    devin = num1/num2
    formula = plus/2
    print(f'{num1}+{num2}={plus}')
    print(f'{num1}-{num2}={minus}')
    print(f'{num1}*{num2}={umn}')
    print(f'{num1}/{num2}={devin}')
    print(f'({num1}+{num2})/2={formula}')
