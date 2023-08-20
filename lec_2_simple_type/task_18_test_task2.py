
x = input('Введите текст: ')
if x.isnumeric() == True:
    x = int(x)
    print(bin(x), oct(x), hex(x), sep='\n')
else:
    print(str.isascii(x))