""" Функция, возвращающая квадрат числа """
# def f(x):
#     return x*x
# print(f(5)) # выдаст ответ
# print(type(f)) # выдаст тип function

# a = f # переменная а будет хранить в себе ссылк на функцию f
# print(type(a)) # тоже выдаст тип function
# print(a(5)) # выдаст ответ

""" Функция - КАЛЬКУЛЯТОР """
# ВАРИАНТ с одним числом
# def calk1(a):
#     return a + a
# def calk2(a):
#     return a * a
# def math(op, x):
#     print(op(x))

# math(calk2, 5)

# ВАРИАНТ с двумя числами
# def calk1(a, b):
#     return a + b
# def calk2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 4)

""" ЛЯМБДА Функции - для сокращения кода """
# def calk2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b   # лямбда функция
# math(calk1, 5, 4)

# math(lambda a, b: a + b, 5, 4)  # можно сразу передавать функцию, не создавая ее отдельно

""" ЗАДАЧА 1: в списке хранятся числа. Нужно выбрать только четные числа и составить список 
пар (число; квадрат числа) """
# РЕШЕНИЕ 1:
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# РЕШЕНИЕ 2:
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# РЕШЕНИЕ 3: с учетом новых функций
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)  # перевели список в числа
# res = filter(lambda x: x % 2 == 0, res) # отфильтровали четные
# res = list(map(lambda x: (x, x**2), res))  # вывели кортежи с числом и его квадратом
# print(res)

""" ФУНКЦИЯ map """
# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

""" ЗАДАЧА 2: С клавиатуры вводится некоторый набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как превратить 
list строк в list чисел? """
# data = '15 156 96 3 5 8 52 5'
# print(data)
# # data = data.split() # преобразовали строку в список
# # print(data) # и далее for i in...
# #   # вместо этого можно сократить:
# data = list(map(int, data.split()))
# print(data)

""" ФУНКЦИЯ filter """
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

""" ФУНКЦИЯ zip """
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333] # выдаст результат по наименьшему списку

# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

""" ФУНКЦИЯ enumerate """
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
#             # пронумерует список: индекс + значение





