""" Функция next
Функция next имеет формат next(iterator[, default]). На вход функция принимает
итератор, который вернула функция iter. Каждый вызов функции возвращает
очередной элемент итератора."""
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter)) # StopIteration

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42)) # когда закончится последовательность, 
print(next(list_iter, 42)) # будет возвращать 42
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))

data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x) # вернет <dict_itemiterator object at 0x00000284CC1909A0>
y = next(x)
print(y) # вернет ('один', 1)
z = next(iter(y))
print(z) # вернет один
