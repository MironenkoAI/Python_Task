# особенности float: не подходит для точных вычислений
#    1. добавляет "хвостик"
#    2. отсекает более 15 символов после запятой

print(0.1 + 0.2) # 0.30000000000000004
pi = 3.141_592_653_589_793_238_462_643
print(pi)   # 3.141592653589793