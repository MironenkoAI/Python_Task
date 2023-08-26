# Локальные переменные:
def func(y: int) -> int:
    x = 100
    # x += 100 # ошибка 
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

# Глобальные переменные:
def func(y: int) -> int:
    global x # позволяет "выглянуть" за пределы функции и взять значение x из основного кода
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

# Не локальные переменные:
def main(a):
    x = 1
    
    def func(y):
        nonlocal x # позволяет "выглянуть" за пределы вложенной функции во внешнюю функцию
        x += 100
        print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1
    
    return x + func(a)


x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')