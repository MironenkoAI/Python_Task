# метод update расширяет исходный словарь новыми парами
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6)) # добавит новую пару в словарь
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)])) # добавит новую пару в конец
                         # и заменит значение у ранее созданного ключа
print(my_dict)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6) # новый способ
print(new_dict) # объединит словари, новые ключи добавит в конец
                # из повторяющиеся ключей выберет значение, которое встретилось последним