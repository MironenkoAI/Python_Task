import csv

# чтобы извлекать числа необходим файл с табуляцией (вместо запятых)
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
            # dialect -  указали диалект с табуляцией в качестве разделителя
            # quoting — передали встроенную константу, указывающую что числа без кавычек 
                # необходимо преобразовать к типу float.

    for line in csv_file:
        print(line)
    print(type(line))