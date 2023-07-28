
def kindergarden():
    name = input()
    number = int(input())

    num1 = int(number/100)
    num2 = int((number/10)%10)
    num3 = int(number%10)

    print(f'Группа №{num1}.')
    print(f'{num3}. {name}')
    print(f'Шкафчик: {number}.')
    print(f'Кроватка: {num2}.')

def auto_game():
    number = int(input())
    num1 = int(number / 1000)
    num2 = int((number / 100) % 10)
    num3 = int((number % 100) / 10)
    num4 = int(number % 10)
    new_num = (num2*1000)+(num1*100)+(num4*10)+num3
    print(f'{new_num}')