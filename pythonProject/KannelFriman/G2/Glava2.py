import random


def z_2_1():
    print('Hello,World!')


def z_2_2():
    print('H-e-l-l-o-,-F-r-i-e-n-d')


def z_2_3():
    str1 = '+'
    str2 = '!'
    str3 = '?'
    print(str1*3)
    print(str2*4)
    print(str3*2)


def z_2_4():
    str1 = '+'
    str2 = '!'
    str3 = '?'
    print(str1*3, (str2*4), (str3*2))


def z_2_8():
    x = 6
    print(x)
    print(x**2)
    print(x**3)


def z_2_9():
    x = 9
    print(f'Значение переменной х = {x}')
    print(f'Значение переменной х^2 = {x**2}')


def z_2_10():
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    print(f'Значение х={x} Значение у={y}')
    print(f'Произведение х*у={x * y}')
    print(f'Сумма х+у={x + y}')