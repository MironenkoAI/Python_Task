def school_print(**kwargs): # для передачи несольких ключей
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)