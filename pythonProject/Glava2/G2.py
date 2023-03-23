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
    print("")