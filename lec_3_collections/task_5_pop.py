# pop - Удаление по индексу!
my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop() # без пердачи значения удалит последний элемент из списка
                     # и сохранит его в переменную spam
print(spam, my_list)   # 12 [2, 4, 6, 8, 10]

eggs = my_list.pop(1) # удалит заданный элемент и также сохранит в переменную
print(eggs, my_list)  # 4 [2, 6, 8, 10]
err = my_list.pop(10) # IndexError: pop index out of range