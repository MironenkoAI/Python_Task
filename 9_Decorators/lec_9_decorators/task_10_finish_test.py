import random
from typing import Callable

def count(num: int = 1):   # 3. num примет число 10 от @count(10)
    def deco(func: Callable):
        counter = []  # 4. создаст пустой список / 8. вернется список со значениями и замкнется
        def wrapper(*args, **kwargs):
            for _ in range(num):  # 5. функция отработает 10 раз
                result = func(*args, **kwargs)
                counter.append(result) # 6. добавит 10 рандомных чисел от 1 до 10
            return counter # 7. из нестандартного: возвращаем иное, вместо result

        return wrapper

    return deco


@count(10) # 2. передаст число 10 в первую функцию count
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')   # 1. выберет рандомное число от 1 до 10
print(f'{rnd(1, 100) = }') # далее все отработает в том же порядке, только добавлять значения будет уже 
                           # к замкнутому списку, т.е. получим список из 20 элементов, где вторые 10 рандомные от 1 до 100
print(f'{rnd(1, 1000) = }') # на выходе список из 30 элементов, где последние от 1 до 1000