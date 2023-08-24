# метод keys возвращает объект-итератор dict_keys
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys()) # выведет все ключи в виде списка

for key in my_dict.keys(): # если не писать метод keys, выдаст то же самое автоматически
    print(key) # выдает ключи как значения