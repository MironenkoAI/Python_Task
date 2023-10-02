def quadratic_equations(a, b, c=0): # вместо передаваемых переменных можно подставить 
    d = b ** 2 - 4 * a * c          # значения по умолчанию, но только НЕИЗМЕНЯЕМЫЕ типы
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None  # если эту строку убрать, то Python подставит ее сам
                 # НО! В случае с изменяемыми переменными, он тоже вернет None, вместо нужного значения


print(quadratic_equations(2, -3, -9))

# -----------------------
def from_one_to_n(n, data=[]): # при попытке передать изменяемый тип - список,
    for i in range(1, n + 1):  # Python будет дополнять предыдущий список
        data.append(i)
    return data                # ЭТО ПЛОХОЙ ПРИЕМ


new_list = from_one_to_n(5)
print(f'{new_list = }') # new_list = [1, 2, 3, 4, 5]

other_list = from_one_to_n(7)
print(f'{other_list = }') # other_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]

# -----------------------------
def from_one_to_n(n, data=None): # надо использовать None - это неизменяемый
    if data is None:             # в данном случае Python возьмет передаваемый список либо значение None
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data                # ЭТО ХОРОШИЙ ПРИЕМ


new_list = from_one_to_n(5)
print(f'{new_list = }') # new_list = [1, 2, 3, 4, 5]

other_list = from_one_to_n(7)
print(f'{other_list = }') # other_list = [1, 2, 3, 4, 5, 6, 7]