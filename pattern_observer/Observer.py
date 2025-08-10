from typing import Protocol

# Observer interface using typing.Protocol (better for static typing)
class Observer(Protocol):
    def update(self, message: str) -> None:
        raise NotImplementedError

# Concrete Observers
class Dog(Observer):
    def update(self, message: str) -> None:
        print(f"[Dog Received Food]: {message}")

class Cat(Observer):
    def update(self, message: str) -> None:
        print(f"[Cat Received Food]: {message}")