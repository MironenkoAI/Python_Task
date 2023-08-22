my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4) # выдаст первое вхождение элемента (по значению) в список
print(spam)  # 1 (у первой четверки индекс 1)
eggs = my_list.index(4, spam + 1, 90) # доп.параметры start, stop (откуда и докуда искать)
print(eggs)  # 8
err = my_list.index(3)  # ValueError: 3 is not in list