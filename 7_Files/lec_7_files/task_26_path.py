import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list: # строки 
    print(f'{os.path.isdir(obj) = }', end='\t') # проверка на директорию
    print(f'{os.path.isfile(obj) = }', end='\t') # проверка на файл
    print(f'{os.path.islink(obj) = }', end='\t') # проверка на ссылку
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir(): # объекты 
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')