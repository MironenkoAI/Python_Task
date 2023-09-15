# 'w' — открыть для записи, предварительно очистив файл
# 'b' — двоичный режим

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()