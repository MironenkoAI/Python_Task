link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/') # разделит текст на элементы по заданному символу
print(urls)            # ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts', '']

a, b, с = input('Введите 3 числа через пробел: ').split()
print(с, b, a) # выдаст ошибку, если чисел окажется более 3

a, b, с, *_ = input('Введите не менее 3х чисел через пробел: ').split()
print(с, b, a, *_) # запакует лишние числа в переменную _ и не выдаст ошибку