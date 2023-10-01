import csv

                            # рекомендуемый параметр
with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f) # чтение csv-файла 
    for line in csv_file:
        print(line) # по умолчанию все данные распознаются как текст
    print(type(line))