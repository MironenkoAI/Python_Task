import os # старый способ
from pathlib import Path # новый аналог

print(os.getcwd()) # покажет путь текущей папки
print(Path.cwd())
