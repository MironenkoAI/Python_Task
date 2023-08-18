# ОБЯЗАТЕЛЬНАЯ ТИПИЗАЦИЯ (аннотация типов) позволяет задать типы, 
# с которыми будет работать программа.

# ПРИМЕР 1:
a: float = 42.0
b: float = float(input('Введите число: '))
a = a / b
print(a)

# ПРИМЕР 2:
def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res

print(my_func([2, 5.5, 15, 8.0, 13.74]))
