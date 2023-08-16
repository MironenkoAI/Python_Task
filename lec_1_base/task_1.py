name = 'Alex'
age = None

a = 42
print(id(a))
# a = 'Hello world'
# print(id(a))

print(name, age, a, 456, 'text', sep=' * ', end='\n')
print('tot текст', end='\n')
print('еще текст', end='\n')

# res = input('Print your text: ')
# print('Ты написал: ', res)

age = int(input('Сколько тебе лет? '))
print(age * 2)