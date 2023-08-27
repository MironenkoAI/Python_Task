# ОДНОСТРОЧНИКИ 
a = 42
b = 73
a, b = b, a # поменять местами значения
print(f'{a = }\t{b = }')

a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}') # присвоить одновременно несколько значений

a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}') # присвоить одновременно несколько значений

# a, b, c = {"один", "два", "три", "четыре", "пять"}
# print(f'{a=} {b=} {c=}') # Ошибка: кол-во должно совпадать

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}') # * заберет в себя лишнее и ошибки не будет
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}') # a='один' b='два' c=['три', 'четыре', 'пять', 'шесть'] d='семь'
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}') # a='один' b=['два', 'три', 'четыре', 'пять'] c='шесть' d='семь'
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}') # a=['один', 'два', 'три', 'четыре'] b='пять' c='шесть' d='семь'


link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/') # *_ запакует лишнее, чтобы его не использовать (как корзина)
print(prefix) # https:
print(*_) # docs.python.org 3 faq
print(suffix) # programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another


data = [2, 4, 6, 8, 10, ]
for item in data:       # код
    print(item, end='\t')
print()
data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t') # сокращенная запись

