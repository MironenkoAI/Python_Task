# в данном случае новый список является ссылкой на старый
# и изменения произойдут в обоих списках
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16]
new_list = my_list
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')

# copy позволяет создать новый независимый список 
# и вносить изменения отдельно в каждый из них
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
