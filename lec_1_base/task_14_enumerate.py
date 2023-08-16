#enumerate - позволяет пройтись по коллекции 
#и вывести по порядку элементы с возможностью их пронумеровать
#c заданного числа start. Если не задать - будет с нуля
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)