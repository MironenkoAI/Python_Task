text_en = 'Hello, world!'
res = text_en.encode('utf-8')
print(res, type(res)) # b'Hello, world!' <class 'bytes'>
                      # b означает байты
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
