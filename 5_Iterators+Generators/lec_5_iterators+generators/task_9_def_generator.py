def factorial(n): # обычная функция использует return и возвращает все значения
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')


def factorial(n): # функция-генератор использует yield и возвращает значения по одному
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')


# к функции-генератору можно применять iter() и next()
my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) # StopIteration