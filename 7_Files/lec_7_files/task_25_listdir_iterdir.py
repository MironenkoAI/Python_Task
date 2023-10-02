import os
from pathlib import Path

print(os.listdir()) # покажет все папки в текущей папке массивом

p = Path(Path().cwd()) # покажет все папки столбиком с путем
for obj in p.iterdir():
    print(obj)