import csv

with (
    open('biostats_tab.csv', 'r', newline='') as f_read, # читаем существующий файл
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write # записываем в новый
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                # записываем как excel (разделитель запятая); заменит запятую на пробел между объектами; если есть 
                # пробел в самой записи, то оборачиваем текст в |; используем | только при необходимости.
    all_data = [] # создали список
    for i, line in enumerate(csv_read): # проходим построчно
        if i == 0: # заголовок (первую строку)
            csv_write.writerow(line) # записываем в новый файл
        else:
            line[2] += 1 # далее проходим по всем данным
            for j in range(2, 4 + 1):
                line[j] = int(line[j]) # числа приводим к int 
            all_data.append(line)
    csv_write.writerows(all_data) # записываем все данные в файл
