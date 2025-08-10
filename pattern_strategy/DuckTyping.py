from abc import abstractmethod, ABC

from abc import ABC, abstractmethod

# you can do this only defining the methods. you can also if you want pack them in classes
def dog_speak():
    print("Woof!")

def cat_speak():
    print("Meow!")

# Strategy pattern: behavior delegated to strategy object at runtime
class Animal:
    def __init__(self, speak_strategy): self.speak_strategy = speak_strategy
    def speak(self): self.speak_strategy()