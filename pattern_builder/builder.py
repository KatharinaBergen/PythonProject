from dataclasses import dataclass

#@dataclass -> With Python 3.7+, you can simplify the Person with @dataclass
class Person:
    def __init__(self, name: str = "", age: int = 0, city: str = "") -> None:
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"


class PersonBuilder:
    def __init__(self) -> None:
        self._person = Person()

    def set_name(self, name: str):
        self._person.name = name
        return self

    def set_age(self, age: int):
        self._person.age = age
        return self

    def set_city(self, city: str):
        self._person.city = city
        return self

    def build(self) -> Person:
        return self._person
