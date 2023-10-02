# Декоратор — структурный шаблон проектирования, предназначенный для
# динамического подключения дополнительного поведения к объекту.
# Т.е. Функция может принимать другую функцию в качестве параметра
# 
# def main(func):
#   def wrapper(*args, **kwargs):
#       ...
#       result = func(*args, **kwargs)
#       ...
#       return result
#  return wrapper

# def my_func(data):
#   ...
#   return wrapper
# 
# deco = main(my_func)

import time
from typing import Callable

def main(func: Callable):

    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    
    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(5) = }')
control = main(factorial)
print(f'{control.__name__ = }')
print(f'{control(5) = }')

#  СИНТАКСИЧЕСКИЙ САХАР: чтобы не создавать переменные, декорируем функцию в @main
# этот метод предпочтительнее
@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(5) = }')