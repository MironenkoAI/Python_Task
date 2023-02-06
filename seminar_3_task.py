""" Дан список чисел. Опредлите, сколько в нем 
встречается различных чисел.
[1, 1, 2, 0, -1, 3, 4, 4] """

# решение 1:
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_1)))

# решение 2:
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# result_list = list()
# for i in list_1:
#     if i not in result_list:
#         result_list.append(i)
# print(result_list)
# print(len(result_list))

""" Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательноть (сдвиг - 
циклический) на К элементов вправо, К - положительное число.
[1, 2, 3, 4, 5] k = 2
[4, 5, 1, 2, 3] """

# решение 1:
# list_1 = [5, 4, 6, 7, 8, -10]
# k = int(input('Введите коэффициент смещения: '))
# k = k % len(list_1)
# list_result = list()

# for i in range(k):
#     list_result.append(list_1[len(list_1) - k + i])

# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)

# решение 2:
# list = [1, 2, 3, 4, 5]
# k = int(input('Введите коэффициент смещения: '))
# k %= len(list) #ЗАЩИТА ОТ БОЛЬШИХ ЧИСЕЛ, чтобы не было лишних циклов

# for i in range(k):
#     list.insert(0, list.pop(-1))
# print(list)

""" Напишите программу для печати всех уникальных значений
в словаре. 
[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}] """

# решение 1:
# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print('Оригинальный список: ', list)
# u_value = set(val for dic in list for val in dic.values())
# print('Уникалиные значения: ', u_value)

# решение 2 (через множества):
# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print(list)
# set_1 = set()
# for i in list:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)

# решение 3 (через списки):
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print(list_1)
# list_2 = list()
# for i in list_1:
#     for j in i:
#         list_2.append(i[j])
# list_result = list()
# for i in list_2:
#     if i not in list_result:
#         list_result.append(i)
# print(list_result)

""" Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3) """

# решение 1:
# n = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(n)):
#     if n[i] > n[i - 1]:
#         count += 1
# print(count)

# решение 2: аналогичное, только счет в др сторону
n = [0, -1, 5, 2, 3]
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        count += 1
print(count)
