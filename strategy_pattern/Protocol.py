from typing import Protocol

class SpeakStrategy(Protocol):
    def speak(self):
        pass

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")


class Tree:
        pass

def do_speak(speaker: SpeakStrategy) -> None:
    speaker.speak()
