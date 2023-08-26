""" функция max(iterable, *[, key, default]) или max(arg1, arg2, *args[, key])
Функция принимает на вход итерируемую последовательность или несколько
позиционных элементов и ищет максимальное из них. Ключевой параметр key
указывает на то, какие элементы необходимо сравнить, если объект является
сложной структурой. Отдельно параметр default используется для возврата
значения, если на вход передана пустой итератор.
"""
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty')) # вернет empty, если передать ничего
print(max(*lst_2)) # * распакует последовательность lst
print(max(lst_3, key=lambda x: x[1])) # найдет max среди значений, вернет пару