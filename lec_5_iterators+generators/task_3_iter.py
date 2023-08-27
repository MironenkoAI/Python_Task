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


