import os
from pathlib import Path

os.replace('newest_file.py', os.path.join(os.getcwd(), 'lec_7_files', 'new_name.py'))

old_file = Path('new_name.py') # перенести и переименовать
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)