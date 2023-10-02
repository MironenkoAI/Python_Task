def mean(args): # для одной позиционной переменной
    return sum(args) / len(args)


print(mean([1, 2, 3])) # распознает список, как одну переменную
# print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

# ---------------------------
def mean(*args): # для нескольких позиционных переменных
    return sum(args) / len(args)


print(mean(*[1, 2, 3])) # распакует список и превратит в кортеж
print(mean(1, 2, 3))