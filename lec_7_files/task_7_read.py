with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}') # повторный вызов метода не работает


SIZE = 100 # можно читать файл частями (по 100 символов)
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)
