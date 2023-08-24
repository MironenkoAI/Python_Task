my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9) # добавит 9 в конец
print(my_set)
my_set.add(7) # не добавит, т.к. элементы должны быть уникальны
print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10)) # добавит как кортеж, а не отдельные элементы
print(my_set)