"""
Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

lst_numbers = []
lst = [2, 2, 2, 3, 3, 5]
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        lst_numbers.append(i + 1)
print(lst_numbers)
