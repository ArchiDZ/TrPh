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
