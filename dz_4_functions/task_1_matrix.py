""" Напишите функцию для транспонирования матрицы """

mults_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mults_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
resalts = [10, 40, 90, 160, 250, 360, 490, 640, 810]


def transpos_matrix(str_1, str_2, str_3):
    for el_1, el_2, el_3 in zip(str_1, str_2, str_3): 
        print(f'{el_1}\t{el_2}\t{el_3}')


transpos_matrix(mults_1, mults_2, resalts)
