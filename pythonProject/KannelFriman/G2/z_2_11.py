

name = input('Enter your name...')
t_number = input('Enter your Phone number...')
l1 = len(name)+2
l2 = len(t_number)+2
if l1 > l2:
    print('*'*l1)
    print(f'* {name}')
    print(f'* {t_number}')
    print('*' * l1)
else:
    print('*' * l2)
    print(f'* {name}')
    print(f'* {t_number}')
    print('*' * l2)

