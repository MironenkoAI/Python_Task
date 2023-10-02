""" Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента, 
а значение — имя аргумента. Если ключ не хешируем, используйте его 
строковое представление."""


def reverse_dict(**kwargs):
    return {value if isinstance(value, (int, float, str, tuple)) 
            else str(value): key for key, value in kwargs.items()}


print(reverse_dict(a=5, b=[2,3], c='Hello', d=(4,5)))