# Замыкание (англ. closure) в программировании — функция первого класса,
# в теле которой присутствуют ссылки на переменные, объявленные вне тела
# этой функции в окружающем коде и не являющиеся её параметрами.

def func(a):  # обычная функция
    x = 1 # будет использовано значение переменной внутри функции
    res = x + a
    return res


x = 100
print(func(5)) # ответ 6

# ---------------------------------
def add_str(a: str, b: str) -> str: # обычная функция
    return a + ' ' + b


print(add_str('Hello', 'world!')) # ответ Hello world!

# ----------------------------------
from typing import Callable

def add_one_str(a: str) -> Callable[[str], str]: # в первую функцию попадет значение 'Hello'
                                                # и она сохранит его (замкнет)
    def add_two_str(b: str) -> str: # во вторую попадет 'world!' 
        return a + ' ' + b # здесь применятся оба значения
    return add_two_str

print(add_one_str('Hello')('world!')) # ответ Hello world!