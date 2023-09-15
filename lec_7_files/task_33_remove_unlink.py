import os
from pathlib import Path

os.remove('lec_7_files/one.txt')
Path('lec_7_files/one_more.txt').unlink()
 # удалит файлы