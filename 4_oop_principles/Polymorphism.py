class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Miau, cause I'm a cat!")

class Dog(Animal):
    def speak(self):
        print("Wuff, cause I'm a dog!")