""" ЗАДАЧА 2: Напишите программу, которая получает целое число 
и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

x = input('Введите целое число: ')
if x.isnumeric() == False:
    print('Вы ввели не целое число. Попробуйте снова')
    
else:
    x = int(x)
    print('Шестнадцатеричное число: ', hex(x))

    hexadecimal_digits = '0123456789abcdef'
    hexadecimal_number = ''
    while x > 0:
        remainder = x % 16
        hexadecimal_digit = hexadecimal_digits[remainder]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        x //= 16
    print("Шестнадцатеричное число:", hexadecimal_number)