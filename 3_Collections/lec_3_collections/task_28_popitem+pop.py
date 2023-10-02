# метод popitem удаляет последнюю пару ключ-значение
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem() # сохраняет удаленную пару как кортеж в переменную
                         # и удаляет ее из словаря
print(f'{spam = }\t{my_dict = }')

eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict = }')

# метод pop удаляет пару ключ-значение по ключу
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two') # сохраняет удаленную пару как кортеж в переменную
                          # и удаляет ее из словаря
print(f'{spam = }\t{my_dict = }')

err = my_dict.pop('six') # ошибка, если ключ не найден
err = my_dict.pop() # ошибка, если ключ не указан