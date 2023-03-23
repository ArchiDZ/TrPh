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