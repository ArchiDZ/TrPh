import random
import math
#23-03-2023
def zadanie3_1():
    cm = int(input("Введите значение в сантиметрах..."))
    m = cm/100
    print(f"{cm}см это {m}м")
def zadanie3_2():
    kg = int(input("Введите значение в кг..."))
    cent = kg/100
    print(f"{kg}кг ровняется {cent} центнеров")
def zadanie3_3():
    days = 234
    week = days/7
    print(round(week))
def zadanie3_4():
    children = random.randint(1,30)
    apple = random.randint(1,200)
    print(f"В классе учатся {children} детей")
    print(f"В корзине лежит {apple} яблок")
    x = apple/children
    y = apple%children
    print(f"Каждый школьник получит по {int(x)} яблок")
    print(f"В корзине останется лежать {y} яблок")
def zadanie3_5():
    storona1 = 543
    x = int(storona1/130)
    x_ost = int(storona1%130)
    print(f"Из прямоугольника может получиться {x} квадрата со стороной 130 и останется прямоугольник {x_ost} на 130")
def zadanie3_6():
    i=0
    mesto = 0
    for i in range (1,10):
      #  print(f"Купе №{i}")
        for x in range(0,4):
            mesto+=1
            print(f"Купе №{i} Место №{mesto}")
            #print(f"Место {mesto}")
def zadanie3_7():
    nomer_kvartiri = 0
    for i in range (1,6):
        print(f"Этаж-->{i}")
        for x in range(0,3):
            nomer_kvartiri+=1
            print(f"КВ_{nomer_kvartiri}")

def zadanie3_8():
    kod_bileta = 1643
    