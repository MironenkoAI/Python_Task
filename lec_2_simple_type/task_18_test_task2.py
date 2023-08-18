x = input('Введите текст: ')

if isinstance(x, int) == True:
    b = bin(x)
    o = oct(x)
    h = hex(x)
    print(b, o, h, sep='\n')
else:
    print(str.isascii(x))

    # НЕ РАБОТАЕТ!!!