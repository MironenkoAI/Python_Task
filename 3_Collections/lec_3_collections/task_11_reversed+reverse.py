# функция reversed 
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)

rev_list = list(reversed(my_list)) # если нужно получить новый список
print(rev_list)

for item in reversed(my_list): # если нужно перебрать список справа налево
    print(item)

# метод reverse, работает с текущим списком
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1] # провести срез списка в обратном порядке
print(my_list, new_list, sep='\n')