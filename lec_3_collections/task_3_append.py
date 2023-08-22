a = 42
b = 'Hello world'
c = [1, 3, 5, 7]

my_list = [None]
my_list.append(a) # добавляет элемент в конец списка
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list) # [None, 42, 'Hello world', [1, 3, 5, 7]]

my_list.append(my_list) # циклическая ссылка - список вложен сам в себя
print(my_list)          # НЕ ИСПОЛЬЗОВАТЬ!