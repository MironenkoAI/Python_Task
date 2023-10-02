# в случае с matrix (список списков) copy работает поверхностно,
# не проникая во вложенную структуру и внесет изменения в оба списка
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = matrix.copy()
print(matrix, new_matrix, sep='\n')
matrix[0][1] = 555
print(matrix, new_matrix, sep='\n')

# если нужно создать независимую копию списка matrix,
# импортируй метод copy и используй функцию .deepcopy
import copy
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = copy.deepcopy(matrix)
print(matrix, new_matrix, sep='\n')
matrix[0][1] = 555
print(matrix, new_matrix, sep='\n')