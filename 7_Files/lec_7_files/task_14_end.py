text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f) # допишет в файл, добавит *** в конце каждой строки
                                         # и ## в начале каждой строки