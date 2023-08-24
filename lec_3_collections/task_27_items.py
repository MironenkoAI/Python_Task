# метод items возвращает объект-итератор dict_items
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items()) # возвращает ключи и значения в виде словаря (списка с кортежами)

for tuple_data in my_dict.items(): # плохо 
    print(tuple_data)
    print(f'{tuple_data[0] = } value before 100 - {100 - tuple_data[1]}')

for key, value in my_dict.items(): # хорошо, одновременное обращение к ключу и значению
    print(f'{key = } value before 100 - {100 - value}')