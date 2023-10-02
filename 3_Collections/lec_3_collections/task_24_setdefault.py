# Метод setdefault возвращает значение и добавляет ключ в словарь 
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

spam = my_dict.setdefault('five') # создаст новый ключ в словаре со значением None 
print(f'{spam = }\t{my_dict = }')

eggs = my_dict.setdefault('six', 6) # создаст новый ключ в словаре со значением 6
print(f'{eggs = }\t{my_dict = }')

new_spam = my_dict.setdefault('two') # выдаст значение по найденному ключу
print(f'{new_spam = }\t{my_dict = }')

new_eggs = my_dict.setdefault('one', 1_000) # выдаст значение по найденному ключу, 
print(f'{new_eggs = }\t{my_dict = }')       # 1_000 добавится если ключ не найден