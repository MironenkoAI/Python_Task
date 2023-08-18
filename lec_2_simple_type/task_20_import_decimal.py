import decimal 
# более точные вычисления по сравнению с float 
# точность до 28 знаков

print(0.1 + 0.2)  # 0.30000000000000004

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643')
print(pi)   # 3.141592653589793238462643

num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)   # 0.3333333333333333333333333333

decimal.getcontext().prec = 120   # задаем точность вручную
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)
