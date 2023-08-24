# метод union и | для объединения множеств
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set) # объединит два множества, исключит повторяющиеся элементы
print(f'{my_set = }\n{other_set = }\n{new_set = }')

new_set_2 = my_set | other_set  # новый способ
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')