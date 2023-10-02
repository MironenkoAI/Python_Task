LIMIT = 1_000 # можно обращаться к внешним константам из функции


def func(x, y):
    result = x ** y % LIMIT
    return result


print(func(42, 73))
