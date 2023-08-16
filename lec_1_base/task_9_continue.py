num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue #перебрасывает к началу цикла, не завершая данный проход 
    print(count)
    