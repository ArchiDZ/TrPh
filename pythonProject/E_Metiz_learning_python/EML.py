#05-04-2023 Задания из самоучителя по  Python
def upr_4_3():
    num =0
    simple_list = []
    for num in range(1, 21):
        simple_list.append(num)
    print(simple_list)

def upr_4_4():
    number = 0
    for number in range (1,1000000):
        number+=1
        print(number)

def upr_4_5():
    i = 0
    list_num = []
    for i in range (1,1000000):
        list_num.append(i)
    print(list_num)
    print('Отдельные методы')
    print(min(list_num))
    print(max(list_num))
    print(sum(list_num))
def upr_4_6():
    list1 = []
    list2 = []
    for i in range (1,21):
        if i%2!=0:
            list1.append(i)
        else:
            list2.append(i)
    print(f'Нечетные числа {list1}')
    print(f'Четные числа {list2}')

def upr_4_7():
    nums = list(range(3,33,3))
    print(nums)

def upr_4_8():
    cube_list = [num**3 for num in range (1,30)]
    print(cube_list)