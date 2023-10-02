""" ЗАДАЧА 2: Напишите программу, которая получает целое число 
и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

x = input('Введите целое число: ')
if x.isnumeric() == False:
    print('Вы ввели не целое число. Попробуйте снова')
    
else:
    x = int(x)
    print('Шестнадцатеричное число: ', hex(x))

    hex_digits = '0123456789abcdef'
    hex_number = ''
    while x > 0:
        remainder = x % 16
        hex_digit = hex_digits[remainder]
        hex_number = hex_digit + hex_number
        x //= 16
    print("Шестнадцатеричное число:", hex_number)