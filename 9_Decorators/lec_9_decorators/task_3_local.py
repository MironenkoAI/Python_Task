from typing import Callable

def add_one_str(a: str) -> Callable[[str], str]:
    names = [] # изменяемый тип переменной (local)

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    
    return add_two_str


hello = add_one_str('Hello') # замкнули Hello
bye = add_one_str('Good bye') # замкнули Good bye

print(hello('Alex')) # добавит Alex
print(hello('Karina')) # добавит Karina после Alex и т.д.
print(bye('Alina'))
print(hello('John')) 
print(bye('Neo'))