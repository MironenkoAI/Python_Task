my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555) # вставит 555 на индекс 2, тем самым увеличив список на 1 элемент
print(my_list)  # [2, 4, 555, 6, 8, 10, 12]
my_list.insert(-2, 13) # вставит 13 после 2х элементов с конца, т.е. на третье место с конца
print(my_list)  # [2, 4, 555, 6, 8, 13, 10, 12]
my_list.insert(42, 73) # вставит в конце, = my_list.append(73) в данном случае
print(my_list)  # [2, 4, 555, 6, 8, 13, 10, 12, 73]