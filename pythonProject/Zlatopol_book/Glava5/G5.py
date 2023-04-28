def zadanie5_1():  # 04-04-2023
    for i in range(1, 21):
        print(f'{i}){20} ')


def zadanie5_2():  # 04-04-2023
    for i in range(1, 11):
        print(f'Learning Python {i}')


def zadanie5_3():  # 04-04-2023
    x = 19
    for i in range(1, 17):
        x += 1
        print(x)
    squares = [num**2 for num in range(1, 11)]
    print(squares)


def zadanie5_7():  # 18-04-2023
    price = 20.4
    num = 0
    for x in range(1, 20):
        num += 1
        x = x*price
        print(f'{num} товар стоит {round(x,2)}p')


def zadanie5_8():  # 18-04-2023
    kg = 0.453
    num = 0
    print('Фунт \tКГ')
    for funt in range(1, 20):
        num += 1
        funt = funt*kg
        print(f'{num}   \t{round(funt, 4)}')


def zadanie5_9():  # 18-04-2023
    ich = 2.54
    num = 0
    print('Дюйм   \tсм')
    for x in range(1, 20):
        num += 1
        x = x*ich
        print(f'{num}    \t{round(x, 2)}')


def zadanie5_13():  # 20-04-2023
    num = 7
    for x in range(0, 11):
        result = x * num
        print(f'{num}*{x}={result}')


def zadanie5_14():  # 20-04-2023
    num = 9
    for x in range(0, 11):
        result = x * num
        print(f'{num}*{x}={result}')


def zadanie5_15():  # 20-04-2023
    num = int(input('>>>'))
    if num > 10:
        print('Error, num cant be more then 9')
    else:
        for x in range(1, 11):
            result = x * num
            print(f'{num}*{x}={result}')
