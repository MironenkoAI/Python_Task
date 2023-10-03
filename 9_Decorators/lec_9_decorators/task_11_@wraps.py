import time
from typing import Callable
from functools import wraps # ДОБАВИЛИ 

def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)   # ДОБАВИЛИ: позволяет сохранить данные той функции, 
                       # что мы декорируем, а не обертки
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        
        return wrapper
    
    return deco


@count(10)
def factorial(n: int) -> int:
    """Returns the factorial of the number n.""" # добавили строку документации
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(5) = }')
print(f'{factorial.__name__ = }') # укажет что работала обертка wrapper 
help(factorial) # при попытке вызвать документацию также выдаст документацию обертки wrapper 

# ПОСЛЕ ДОБАВЛЕНИЯ @wraps: покажет имя настоящей функции - factorial
            # а help покажет справку по пункции factorial и строку документации 