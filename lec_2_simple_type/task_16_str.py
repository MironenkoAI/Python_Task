txt = 'Книга называется "Война и мир".'
print(txt)  #использовать разные кавычки

text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text) # текст склеится - не использовать

long_text = 'Тэд — неотразимый красавец, устоять перед таким невозможно. \
    Очаровательная Лиз и не устояла. Свидание на одну ночь переросло в долгие \
    замечательные отношения, о которых большинство девушек только и мечтает. \
    Внезапно Тэда арестовали, предъявив ему чудовищные обвинения. Но как можно \
    поверить, что этот нежный умный элегантный мужчина мог насиловать, убивать и \
    расчленять несчастных женщин?! Ее родной и милый Тэд. Тэд Банди'
print(long_text)   # \ - позволяет разделять текст визуально

LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твое имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
    ' до 100 лет, но длина строки не должна превышать ' +\
    str(LIMIT) + ' символов.'
print(text)    # + соединяет строки (числа надо обернуть в строку)
               # НЕ ЗЛОУПОТРЕБЛЯТЬ!