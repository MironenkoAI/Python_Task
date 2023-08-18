""" isinstance(что, с чем) - функция позволяет проверить входит ли
заданная переменная в определенный тип или в один из типов(пример 3).
Используем, когда нужно убедиться является ли какой-то объект - 
объектом нужного нам типа"""

data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))