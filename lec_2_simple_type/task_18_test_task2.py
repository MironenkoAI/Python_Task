x = 5
print(type(x))
if isinstance(x, int):
    print(bin(x), oct(x), hex(x), sep='\n')
else:
    print(str.isascii(x))