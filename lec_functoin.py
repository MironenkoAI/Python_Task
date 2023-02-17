""" Функция суммирования элементов строки"""
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# sum_numbers(5)   # 1+2+3+4+5   15

""" Функция, возвращающая значение"""
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))
#     # или
# a = sum_numbers(5)
# print(a)

""" Сколько аргументов передаем, столько возвращается - это правило!
    Но можно добавить постоянный аргумент сразу в функцию """
# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))   # Hello  15
#    # или (если передадим аргумент, он заменит постоянный)
# print(sum_numbers(5, 'Привет'))   # Привет  15

""" Если кол-во аргументов не известно - ДЛЯ ТЕКСТОВЫХ АРГУМЕНОВ"""
# def sum_str(*args):
#     res = ''  # создали строку 
#     for i in args:
#         res += i
#     return res

# print(sum_str('H', 'e', 'l'))
# print(sum_str('H', 'e', 'l', 'l', 'o'))
# print(sum_str('1', '2', '3'))  
# print(sum_str(1, 2, 3))   # БУДЕТ ОШИБКА

""" Если кол-во аргументов не известно - ДЛЯ ЧИСЕЛ"""

#  ???


""" Рекурсия - Функция Фибонначи"""
# def Fib(n):
#     if n in [1, 2]:
#         return 1
#     return Fib(n-1) + Fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(Fib(i))
# print(list_1)

""" Быстрая сортировка - алгоритм деления большого на части """
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0] # сохраняем в переменную первый элемент
    less = [i for i in array[1:] if i <= pivot]  # находим значения меньше первого элемента
    greater = [i for i in array[1:] if i > pivot]  # находим значения больше первого элемента
    return quick_sort(less) + [pivot] + quick_sort(greater)  # возвращаем отсортированные списки по возрастанию

print(quick_sort([15, 4, 2013, 9, 3, 140, 26, 8, 1000000, 0, -7, 1.25]))

""" Сортировка слияние - алгоритм деления на пары, а потом возвращение отсортированных пар """
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2      # делим список на двое, пока не 
#         left = nums[:mid]         # останется по одному элементу
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right): # начинаем это упорядочеать
#             if left[i] < right[j]:        # сравниваем по два значения и
#                 nums[k] = left[i]         # добавляем их в новый список nums
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             nums[k] = left[i]    # если в одном из списков еще остались значения, 
#             i += 1               # а в другом больше нет, то
#             k += 1               # продолжаем его добавлять в конец списка

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list_1 = [15, 4, 2013, 9, 3, 140, 26, 8, 1000000, 0, -7, 1.25]  # передаем значения
# merge_sort(list_1)                        # обращаемся к рекурсии
# print(list_1)                             # выводим результат
        