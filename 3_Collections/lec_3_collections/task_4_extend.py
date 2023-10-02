a = 42
b = 'Hello world'
c = [1, 3, 5, 7]

my_list = [None]
# my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b) # работает только с последовательностями, добавляет поэлементно в конец
print(my_list)
my_list.extend(c)
print(my_list) # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', 1, 3, 5, 7]

my_list.extend(my_list) # циклическая ссылка - список вложен сам в себя. Можно использовать
print(my_list)