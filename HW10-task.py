# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Gaf gaf!"

class Cat(Animal):
    def sound(self):
        return "Meow meow!"

class Cow(Animal):
    def sound(self):
        return "Muuu!"


class AnimalFactory:
    # Класс-фабрика
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "dog":
            return Dog(**kwargs)
        elif animal_type == "cat":
            return Cat(**kwargs)
        elif animal_type == "cow":
            return Cow(**kwargs)
        else:
            print('Нет такого животного!')






my_dog = AnimalFactory.create_animal("dog", name="Sharik", age=5)
my_cat = AnimalFactory.create_animal("cat", name="Barsik", age=4)
my_cow = AnimalFactory.create_animal("cow", name="Burjenka", age=3)

print(my_dog.name, 'is', my_dog.age, 'years old')
print(my_dog.sound())

print(my_cat.name, 'is', my_cat.age, 'years old')
print(my_cat.sound())

print(my_cow.name, 'is', my_cow.age, 'years old')
print(my_cow.sound())