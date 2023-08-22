my_list = [2, 4, 6, 8, 10, 12]

print(my_list[0]) # индексация начинается с 0
#print(my_list[6]) # IndexError: list index out of range

print(my_list[-1]) # можно обратиться к индексам с конца, добавив минус
                   # индексация тогда будет с 1
print(my_list[-10]) # IndexError: list index out of range