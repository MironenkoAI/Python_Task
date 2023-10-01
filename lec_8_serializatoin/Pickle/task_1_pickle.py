import pickle # модуль позволяет преобразовать объект Python в набор байт и обратно
import os

# нужно относиться очень осторожно к левым файлам
res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }') # преобразуем байты в объект Python

os.system('echo Hello world!')

