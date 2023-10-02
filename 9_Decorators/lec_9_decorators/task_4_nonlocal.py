from typing import Callable

def add_one_str(a: str) -> Callable[[str], str]:
    text = '' # неизменяемый тип данных (nonlocal)

    def add_two_str(b: str) -> str:
        nonlocal text # для неизменяемых нужно указывать nonlocal чтобы замкнуть тоже
                    # (сохранить предыдущие изменения)
                    # если есть сомнения, лучше указать, хуже не будет
        text += ', ' + b
        return a + text
    
    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
