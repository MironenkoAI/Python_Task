""" ЗАДАЧА 3: Напишите программу, которая принимает две строки вида “a/b” - 
дробь с числителем и знаменателем. Программа должна возвращать сумму и 
произведение* дробей. Для проверки своего кода используйте модуль fractions. """
import fractions
import math

fract_1 = input('Введите первую дробь вида a/b: ').split('/')
fract_2 = input('Введите вторую дробь вида a/b: ').split('/')
f1 = list(map(int, fract_1))
f2 = list(map(int, fract_2))

# ВАРИАНТ 1: код
def gcd_function(numerator, denominator):
    gcd_summ = math.gcd(numerator, denominator)
    numerat = numerator // gcd_summ
    denomin = denominator // gcd_summ
    return numerat, denomin

if f1[1] == f2[1]:
    sum_numer = f1[0] + f2[0]
    sum_denom = f1[1]
else:
    sum_numer = f1[0] * f2[1] + f2[0] * f1[1]
    sum_denom = f1[1] * f2[1]
numerat, denomin = gcd_function(sum_numer, sum_denom)
print(f'Сумма дробей = ', numerat, '/', denomin, sep='')

prod_numer = f1[0] * f2[0]
prod_denom = f1[1] * f2[1]
numerat, denomin = gcd_function(prod_numer, prod_denom)
print(f'Произведение дробей = ', numerat, '/', denomin, sep='')


# ВАРИАНТ 2: franctions
if f1[1] == f2[1]:
    sum_numer = f1[0] + f2[0]
    sum_denom = f1[1]
else:
    sum_numer = f1[0] * f2[1] + f2[0] * f1[1]
    sum_denom = f1[1] * f2[1]
print(f'Сумма дробей = ', fractions.Fraction(sum_numer, sum_denom))

prod_numer = f1[0] * f2[0]
prod_denom = f1[1] * f2[1]
print(f'Произведение дробей = ', fractions.Fraction(prod_numer, prod_denom))