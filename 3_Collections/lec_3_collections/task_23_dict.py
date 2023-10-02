# dict - словарь. Все записи равнозначные
a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!') # не следует использовать, если 
                                               # ключи совпадают с зарезервированными словами
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')]) # словарь с кортежами
print(a == b == c)

# добавление ключа
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x # добавит новый ключ в конец
print(my_dict)

# обращение к ключам
TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two']) # выведет значение по ключу
print(my_dict[TEN]) # ищет ключ по заданной переменной, если найдет отдает значение по ключу
# print(my_dict[1]) # KeyError: 1

print(my_dict.get('two')) # выведет значение по ключу
print(my_dict.get('five')) # ошибки не будет, отдаст None 
print(my_dict.get('five', 5)) # если не найдет ключ, то вернет 5 по умолчанию
print(my_dict.get('ten', 5))