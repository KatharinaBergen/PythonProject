class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Miau or Woof, idk cause I'm an animal!")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)