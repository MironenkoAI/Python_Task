""" Функция globals()
Функция возвращает словарь переменных из глобальной области видимости, т.е. из
пространства модуля. """
SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals()) # один ответ, где бы не находился запрос
    z = x + c
    return z


print(globals())
print(f'{func(1, 2, 3) = }')

# изменяем словарь globals()
x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(f'{x = }')