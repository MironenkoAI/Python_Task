import sys

# getsizeof - показывает сколько байт занимает объект
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP