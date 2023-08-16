""" ЗАДАЧА 3. Напишите код, который запрашивает число и сообщает 
является ли оно простым или составным. Используйте правило для проверки: 
“Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

num = int(input("Введите целое число от 0 до 100 000: "))

if 0 > num or num > 100000:
    print('Вы ввели число вне диапазона. Начните сначала ;)')
elif num <= 1:
    print(f"Число {num} является исключением")
else:
    for i in range(2, num):
        if num % i == 0:
            print('Число является составным')
            break
    else:
        print('Число является простым')
