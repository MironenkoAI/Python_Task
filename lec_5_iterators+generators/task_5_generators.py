# функции-генераторы генерируют значения по мере необходимости и не хранят их
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# Генераторные выражения Python позволяют создать собственный генератор,
# перебирающий значения
my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)

# пример сложнее:
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')
