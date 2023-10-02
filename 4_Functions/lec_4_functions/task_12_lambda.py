# lambda как сокращенная запись функции, без использования return
def add_two_def(a, b):  # обычная функция
    return a + b


add_two_lambda = lambda a, b: a + b # анонимная функция: аналогичный код с помощью lambda
                          # НО! Нельзя присваивать анонимную функцию в переменную

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

# lambda использовать в словарях и т.п.
my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1]) # отсортирует по значению
print(f'{s_key = }\n{s_value = }')
