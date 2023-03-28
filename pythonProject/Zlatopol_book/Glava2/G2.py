import math
import random


#22-03-2023

def zadanie2_1_variantA():
    x = int(input("Введите число..."))
    y = (17*(x**2))-((6*x)+13)
    print(y)
def zadanie2_1_variantB():
    x = int(input("Введите число..."))
    y = (3 * (x ** 2)) + ((5 * x) - 21)
    print(y)
def zadanie2_2():
    number = int(input("Введите число..."))
    chis = (number**2)+10
    znam = math.sqrt(number**2+1)
    result = chis/znam
    print(result)
def zadanie2_3_variantA():
    number = int(input("Введите число..."))
    chisl = 2*number+math.sin(3*number)
    znam = 3.56
    result = math.sqrt(chisl/znam)
    print(result)
def zadanie2_3_variantB():
    number = int(input("Введите число..."))
    chisl = 3.2+math.sqrt(1+number)
    znam = 5*number
    result = math.sin(chisl/znam)
    print(znam)
def zadanie2_4():
    number = int(input("Введите сторону квадрата"))
    p = number*4
    print(f"Периметр квадрата со стороной {number} равен {p}")
def zadanie2_5():
    number = int(input("Введите радиус окружности..."))
    pi = 3.14
    p = 2*pi*number
    print(f"Периметр окружности равен {p} при радиусе {number}")
def zadanie2_6():
    x = int(input("Введите значение высоты в км..."))
    formula = math.sqrt(x*(2*6350+x))
    print(f"Расстояние до горизонта  {formula} км")
def zadanie2_7():
    rebro = int(input("Введите длинну ребра куба..."))
    P = rebro*4
    S = rebro*rebro*rebro
    print(f"Дан куб с ребром {rebro} его обьем состовляет {S}")

def zadanie2_8():
    r = int(input("Введите радиус окружности..."))
    pi = 3.14
    dlina_okr = 2*pi*r
    S_okr = ((pi*r)**2)
    print(f"Окружность с радиусом {r} имеет длинну {dlina_okr} и площадь окружности {S_okr}")

def zadanie2_9_variant_A():
    x = random.randint(1,100)# Случайное число от 1 до 100
    y = random.randint(1, 100)
    formula = 2*(x**3)-3.44*x*y+2.3*(x**2)-7.1*y+2
    print(f"x={x}  y={y}")
    print(f"Результат вычислений-->{formula}")
def zadanie2_9_variant_B():
    x = random.randint(1, 100)  # Случайное число от 1 до 100
    y = random.randint(1, 100)
    formula = 3.14*((x+y)**3)+2.75*(y**2)-12.7*x-4.1
    print(f"x={x}  y={y}")
    print(f"Результат вычислений-->{formula}")

def zadanie2_10():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    avg = (number1+number2)/2
    geo = math.sqrt(number1*number2)
    print(f"Даны два числа {number1} и {number2}")
    print(f"Среднее арифмитическое равно {avg} а средне геометрическое равно {geo}")
def zadanie2_11():
    objom = random.randint(1,100)
    ves = random.randint (1,100)
    plotnostj = ves/objom
    print(f"Обьем гипотетического тела... {objom}")
    print(f" Вес гипотетического тела... {ves}")
    print(f"Плотность данного тела состовляет ... {plotnostj}")
def zadanie2_12():
    zhiteli = random.randint(1,1000000)
    ploshad_gos = random.randint(1000,100000)
    plotnost_naselenia = zhiteli/ploshad_gos
    print(f"Гипотетическое государство с площадью {ploshad_gos} км на которой проживают {zhiteli} человек")
    print(f"Плотность населения состовляет {plotnost_naselenia}")

#===========
#23-03-2023|
#===========

def zadanie2_13():
    a = random.randint(1,100)
    b = random.randint(1,100)
    print(f"{a}X+{b}=0")
    x = -b/a
    print(f"X={round(x,2)}")
def zadanie2_14():
    katet1 = random.randint(1,25)
    katet2 = random.randint(1,25)
    gipotenuza = (katet1**2)+(katet2**2)
    result = math.sqrt(gipotenuza)
    print(f"Катет 1={katet1}  Катет 2={katet2}   Гипотенуза={round(result,2)}")
def zadanie2_15():
    vneshniy_r = random.randint(1,100)
    max_vnR = vneshniy_r
    vnutrenniy_r = random.randint(1,max_vnR-1)
    pi = 3.14
    S1 = 2*pi*(vneshniy_r**2)
    S2 = 2 * pi * (vnutrenniy_r ** 2)
    print(f"Площадь кольца по внешнему радиусу равна {vneshniy_r}")
    print(f"Площадь кольца по внутриннему радиусу радиусу равна {vnutrenniy_r}")
def zadanie2_16():
    katet1 = random.randint(1,100)
    katet2 = random.randint(1,100)
    gipotenuza = math.sqrt((katet1**2)+(katet2**2))
    p_treugolnika = katet1+katet2+round(gipotenuza,1)
    print(f"Катет1={katet1}")
    print(f"Катет2={katet2}")
    print(f"Гипотенуза={gipotenuza}")
    print(f"Периметр треугольника={p_treugolnika}")
#26--3-2023
def zadanie2_17():
    osnovanie = random.randint(1,25)
    visota = random.randint(1,30)
    print(f"Равнобедренная трапеция. Основание--{osnovanie} высота--{visota}")
# я хз какая тут формула нахождкния боковой стороны
def zadanie2_18():
    x = random.randint(1,15)
    y = random.randint(1,10)
    formula1 = x+(2+y)/(x**2)
    formula2 = y+1/(math.sqrt((x**2)+10))
    result = formula1/formula2
    print(f"Число Х {x} Число У {y} Результат вычисления формулы {result}")
def zadanie2_19():
    print()
    #Later
def zadanie2_20():
    print()
    #Later
def zadanie2_21():
    print()
    #Later
def zadanie2_22():
    print()
    #Later
#26-03-2022
def zadanie2_23():
    storona1 = random.randint(1,50)
    storona2 = random.randint(1,25)
    p = (storona1+storona2)*2
    print(f"Сторона1={storona1} Сторона2={storona2}")
    print(f"Периметр прямоугольника равен {p}")
def zadanie2_24():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    summa = number1+number2
    if number1>number2:
        raznost = number1-number2
    if number2>number1:
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
