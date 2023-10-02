#range - функция для перебора значений от.. до .. с шагом
num = int(input('Введите число: '))
for i in range(0, num, 2): #(start, stop(не включается), step)
    print(i)               #range может иметь только stop