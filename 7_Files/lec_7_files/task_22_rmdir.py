import os
from pathlib import Path

# os.rmdir('dir') # не может удалить, если в папке есть информация
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()