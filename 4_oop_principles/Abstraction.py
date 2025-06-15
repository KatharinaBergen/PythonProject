from abc import abstractmethod, ABC


class Animal(ABC):  # Inherits from ABC, so it’s an abstract class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Miau, cause I'm a cat!")

class Dog(Animal):
    def speak(self):
        print("Wuff, cause I'm a dog!")