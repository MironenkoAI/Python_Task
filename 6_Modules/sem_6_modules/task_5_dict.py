# Задание 5:
# Добавьте в модуль с загадками функцию, которая хранит словарь 
# списков. Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать 
# ей все свои загадки. 
def func(qws, ans, count):
    print(f'загадка: {qws}')
    print(f'варианты ответов: {ans}')
    i = 0
    while count >= i:
        u_ans = input(f'введите ваш ответ: ')
        if u_ans == ans[0]:
            print(f'Правильно! Угадал за {i + 1}-ю попытку')
            return i + 1
        else:
            print('Не угадал!')
            i += 1
        if i == count:
            return 0
        
def func_2(dct):
    for k, v in dct.items():
        print(func(k, v, 3))


dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
       "Не лает, не кусает, а в дом не пускает": ['замок', 'охранник', 'собака']}


func_2(dct)