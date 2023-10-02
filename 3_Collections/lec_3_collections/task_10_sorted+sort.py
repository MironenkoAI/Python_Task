# только для однотипных значений

# функция sorted сортирует в новый объект
# для любых последовательностей
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)  # отсортирует по возрастанию в новый объект
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True) # отсортирует по убыванию в новый объект
print(my_list, rev_list, sep='\n')

# метод sort сортирует текущий объект
# только для списков
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort() # отсортирует по возрастанию
print(my_list)
my_list.sort(reverse=True)  # отсортирует по убыванию
print(my_list)