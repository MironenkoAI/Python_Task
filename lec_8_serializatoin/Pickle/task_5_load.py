import pickle

def func(a, b, c): # при десерализации одноименная функция заменится
                    # а не прописанная заново выдаст ошибку, нужно переносить такие объекты
    return a * b * c


with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f) # преобразует бинарный файл в объект Python
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')
