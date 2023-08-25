""" ЗАДАЧА 2
Дан список повторяющихся элементов. Вернуть список с 
дублирующимися элементами. В результирующем списке не должно 
быть дубликатов."""

my_list = [1, 2, 2, 3, 4, 4, 4, 5, 'el', 'el']
res_list = []
for el in my_list:
    if my_list.count(el) > 1:
        if el not in res_list:
            res_list.append(el)
print(res_list)

