from functools import cache


@cache # позволяет кэшировать данные
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }') # вычислит 
print(f'{factorial(15) = }') # вычислит 
print(f'{factorial(10) = }') # отдаст ответ из памяти (кэш)
print(f'{factorial(20) = }') # вычислит 
print(f'{factorial(10) = }') # отдаст ответ из памяти (кэш)
print(f'{factorial(20) = }') # отдаст ответ из памяти (кэш)