# remove - Удаление по значению!
my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6) # удалит первый встретившийся элемент со значением 6
print(my_list)    # [2, 4, 8, 10, 12, 6]
my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)