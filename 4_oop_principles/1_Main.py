from ftplib import print_line

from Inheritance import Animal as iAnimal
from Inheritance import Cat as iCat
from Inheritance import Dog as iDog
from Polymorphism import Animal as pAnimal
from Polymorphism import Cat as pCat
from Polymorphism import Dog as pDog
from Abstraction import Animal as aAnimal
from Abstraction import Cat as aCat
from Abstraction import Dog as aDog

#Inheritance: Inheriting attributes & behaviours
print_line("Inheritance:")
animal = iAnimal("Animal", 0)
dog = iDog("Hund1", 3)
cat = iCat("Cat15", 15)

animal.speak()
dog.speak()
cat.speak()

#Polymorphism: same method, different behaviour
print_line("Polymorphism:")
animal = pAnimal("Animal", 0)
dog = pDog("Hund1", 3)
cat = pCat("Cat15", 15)

animal.speak()
dog.speak()
cat.speak()

#Abstraction: hides implementation features (& forces implementation logic)
print_line("Abstraction:")
#animal = aAnimal("Animal", 0) this will fail cause it's an abstract class
dog = aDog("Hund1", 3)
cat = aCat("Cat15", 15)

dog.speak()
cat.speak()

#Encapsulation: Combining attributes in eg a class
