""" Напишите функцию для транспонирования матрицы """

my_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [10, 20, 30, 40, 50, 60, 70, 80, 90],
           [10, 40, 90, 160, 250, 360, 490, 640, 810]]


def transpos_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        


for row in transpos_matrix(my_matrix):
    print(row)
