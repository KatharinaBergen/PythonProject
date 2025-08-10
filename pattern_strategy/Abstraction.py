from abc import abstractmethod, ABC

from abc import ABC, abstractmethod

class SpeakStrategy(ABC):
    @abstractmethod
    def speak(self):
        pass

class DogSpeak(SpeakStrategy):
    def speak(self):
        print("Woof!")

class CatSpeak(SpeakStrategy):
    def speak(self):
        print("Meow!")


# Strategy pattern: behavior delegated to strategy object at runtime
class Animal:
    def __init__(self, speak_strategy): self.speak_strategy = speak_strategy
    def speak(self): self.speak_strategy.speak()