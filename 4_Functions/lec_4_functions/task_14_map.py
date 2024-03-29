""" функция map(function, iterable) — принимает на вход функцию и последовательность.
Функция применяется к каждому элементу последовательности и возвращает map
итератор.
"""
texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts) # применит функцию lower ко всем элементам последовательности texts
print(res) # вернет map объект 
print(*res) # распакует map объект на отдельные элементы
