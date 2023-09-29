"""
Задача №1
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


(Задание №5 из СЕМИНАРА
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

Задание №6 из СЕМИНАРА
Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.)
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Factory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == 'dog':
            return Dog(name)
        elif animal_type == 'cat':
            return Cat(name)
        elif animal_type == 'bear':
            return Bear(name)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав-гав!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу-мяу!"


class Bear(Animal):
    def speak(self):
        return f"{self.name} говорит: Ррррр!"


my_dog = Factory.create_animal('dog', 'Шарик')
print(my_dog.speak())

my_cat = Factory.create_animal('cat', 'Васька')
print(my_cat.speak())

my_bear = Factory.create_animal('bear', 'Мишка')
print(my_bear.speak())