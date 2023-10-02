from sys import builtin_module_names, path
            # импортировать частично модули (переменные)
print(builtin_module_names)
print(*path, sep='\n')