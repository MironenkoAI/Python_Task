import sys
import random

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

print(random.randint(1, 6))