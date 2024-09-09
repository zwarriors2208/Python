from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof Woof Woof Woof"

class Cat(Animal):
    def sound(self):
        return "Meow Meow"

# the coe below will not work as the clas was abstract
#objAnimal = Animal()

objDog = Dog()
print(objDog.sound())