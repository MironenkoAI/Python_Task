""" СЛОВАРИ """
# dict1 = {"first": 1, "second": 2, "third": 3}   # словарь

#    # пройтись по всем элементам - это for
# for i, j in dict1.items():
#     print(i, j)  # first 1
#                  # second 2
#                  # third 3
# print(dict1.items())   # dict_items([('first', 1), ('second', 2), ('third', 3)])
#                        # это список из кортежей
#         # в строке for i, j in dict1.items():
#             # i, j алалогичны key, value
#             # если только i - выведет в столбик кортежи: ('first', 1)  ('second', 2)  ('third', 3)
# print(dict1)  # выведет словарь: {'first': 1, 'second': 2, 'third': 3}
# print(dict1["first"])   # выведет значение элемента:  1. Если такого элемента нет - выдаст ошибку
# print(dict1.get("second"))   # выведет значение элемента: 2. Если такого элемента нет - 
#                              # выдаст None. 
# print(dict1.get("four", 0))  # Также можно указать что выводить, если нет эл-та: выведет 0, если нет four
# print(dict1.keys())  # вывести список всех ключей: dict_keys(['first', 'second', 'third'])
# print(dict1.values())  # вывести список всех значения: dict_values([1, 2, 3])

# dict1["four"] = 4  # ДОБАВИТЬ элемент в словарь
# dict1.update({"four": 4, "five": 5})  # ДОБАВИТЬ несколько элементов в словарь

# dict1.pop("second") # УДАЛИТЬ элемент по ключу

""" ЛОЖНЫЙ СЛОВАРЬ """
# dict1 = {'Tom': {'English': 5, 'Math': 5}, 'Red': {'English': 4, 'Math': 4}}
# # print(dict1) # выведет все как есть
# # print(dict1['Tom']) # выведет словарь Тома {'English': 5, 'Math': 5}
# for i in dict1['Tom'].items():
#     print(*i)  # выведет в столбик: English 5 Math 5
# print(dict1['Red']['Math'])  # выведет только значение из второго словаря: 4

# dict1.update({"Wer": {'English': 3, 'Math': 3}})  # добавить нового ученика в словарь
# dict1['Tom'].update({'Trud': 6}) # добавить новый предмет во внутренний словарь

# dict1['Red']['Math'] = 5  # изменить значение

""" Последовательность Фибоначчи"""
# def Fib(n):
#     if n == 0 or n == 1:
#         return n
#     return Fib(n-1) + Fib(n-2)

# list_1 = []
# for i in range(0, 10):
#     list_1.append(Fib(i))
# print(list_1)

# print(f'Равен: {Fib(int(input("Элемент: ")))}')

""" Поиск и замена MIN на MAX """ 
# n = int(input("Введите число: "))
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)
# # аналогично в одну строку: list1 = [int(input()) for i in range(int(input()))]    
# print(list1)

# max_n = max(list1)
# min_n = min(list1)
# for i in range(len(list1)):
#     if list1[i] == max_n:
#         list1[i] = min_n
# print(list1)

""" Функция, которая проверяет простое число """
# def prime(n):
#     i = 2
#     flag = True
#     while i < n and flag:
#   # while i < n // 2 + 1 and flag: можно делить до половины числа для экономии ресурса
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return "yes"
#     return "no"
# print(prime(int(input("Введите число: "))))

""" Перевернуть последовательноть с помощью рекурсии"""
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'
print(f(int(input())))


