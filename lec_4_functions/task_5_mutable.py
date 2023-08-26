# ИЗМЕНЯЕМАЯ ФУНКЦИЯ: изменит изменяемые объекты
# при передаче в функцию изменяемого объекта, он изменится и во внешнем коде

def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In_func {data = }') # для демострации
    return data

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')