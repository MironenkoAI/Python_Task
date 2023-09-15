import os
from pathlib import Path

os.mkdir('new_os_dir') # создает новую директорию (папку) в текущей папке
Path('new_path_dir').mkdir()
# если указать абсолютный путь, создаст там, где указали
