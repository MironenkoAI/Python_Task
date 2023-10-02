# 'a' — открыть для записи в конец файла, если он существует

f = open('text_data.txt', "a", encoding='utf-8')
f.write('Окончание файла\n')
f.close()