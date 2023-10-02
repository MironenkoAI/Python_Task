""" Функция iter
Функция iter имеет формат iter(object[, sentinel]). object является обязательным
аргументом. Если объект не реализует интерфейс итерации через методы __iter__
или __getitem__, получим ошибку TypeError."""

# a = 42
# iter(a) # TypeError: 'int' object is not iterable
          # нельзя итерироваться по целому числу

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter) # выдаст объект
print(*list_iter) # распакует объект
print(*list_iter) # при повторном запросе ничего не выдаст

# ПРИМЕНЕНИЕ аргумента sentinel
data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools

f = open('mydata.bin', 'rb') # должен быть сторонний файл mydata.bin
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
