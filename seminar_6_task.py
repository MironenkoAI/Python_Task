""" обсуждение сортировки: множества не всегда сортируются при изменениях. 
Лучше перевести в лист (список)

setn = set([random.randint(1,21) for i in range(int(input('Введите кол-во элементов первого множества: ')))])
print(sorted(list(set_name))) """

""" ЗАДАЧА 1: Дан массив, состоящий из целых чисел. Напишите программу, которая в данном 
массиве определит количество элементов, у которых два соседних и, при этом, оба соседних 
элемента меньше данного. Сначала вводится число N — количество элементов в массиве. 
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. """

# РЕШЕНИЕ 1:
# n = int(input("Введите количество: "))
# list_first = list()
# for i in range(n):
#     x = int(input("Введите число: "))
#     list_first.append(x)
# count = 0
# for i in range(1, n - 1):
#     if list_first[i - 1] < list_first[i] > list_first[i + 1]:
#         count += 1
# print(f'Ответ: {count}')

# РЕШЕНИЕ 2:
# numbers = [5, 1, 5, 3, 6, 3, 4]
# count = 0
# for i in range(1, len(numbers)-1):
#     if numbers[i - 1] < numbers[i] > numbers[i+1]:
#         count += 1
# print(count)


""" ЗАДАЧА 2: Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, равные друг другу образуют 
одну пару, которую необходимо посчитать.
Вводится список чисел. """

# РЕШЕНИЕ 1:
# import random
# from collections import Counter
# N = int(input('Введите длину списка: '))
# list1 = []
# for i in range(N):
#     list1.append(random.randrange(1, 2))
# print(list1)

# dictionary = Counter(list1)
# for key, values in dictionary.items():
#     if int(values) // 2:
#         print(f'{key}, количество пар {int(values) // 2}')
    

""" ЗАДАЧА 3: Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k > 300.
Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). """

# РЕШЕНИЕ 1:
# def div_list(num):
#     summa = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             summa += i
#     return summa

# number = int(input('Введите число: '))
# for i in range(1, number):
#     for j in range(i + 1, number):
#         if i == div_list(j) and j == div_list(i) and i != j:
#             print(i, j)

# РЕШЕНИЕ 2: оптимизированное
def div_list(number: int) -> dict:
    div_dict = {}
    for j in range(1, number):
        summa_div = 0
        for i in range(1, j):
            if j % i == 0:
                summa_div += i
        div_dict[j] = summa_div
    return div_dict

number = int(input('Введите предел: '))

div_dict = div_list(number)

for i in range(1, number):
    for j in range(i, number):
        if i == div_dict.get(j) and j == div_dict.get(i) and i != j:
            print(i, j)


# Стоун Семнадцатый: https://t.me/+bEMRhfWNrJw1NDNi
# Стоун Семнадцатый: https://t.me/STONECx3
