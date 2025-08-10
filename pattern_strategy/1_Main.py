from ftplib import print_line

from Abstraction import DogSpeak as aDogSpeaks
from Abstraction import CatSpeak as aCatSpeaks
from Abstraction import Animal as aAnimal

from DuckTyping import Animal as dAnimal
from DuckTyping import dog_speak
from DuckTyping import cat_speak


from Protocol import Dog as pDog
from Protocol import Cat as pCat
from Protocol import Tree as pTree
from Protocol import do_speak

# Strategy Pattern using Abstraction:
# pro - pretty safe, enforces interface at design time,
# con - requires inheritance and explicit strategy objects
print_line("Abstraction:")
dog = aAnimal(aDogSpeaks())
cat = aAnimal(aCatSpeaks())

dog.speak()
cat.speak()

# Strategy Pattern using DuckTyping:
# pro - no need for inheritance or classes, just method presence is enough
# con - no static type checking, runtime errors possible if interface not followed
print_line("DuckTyping:")
dog = dAnimal(dog_speak)
cat = dAnimal(cat_speak)
# tree = dAnimal(42)  # Would fail at runtime: 'int' has no 'speak' method

dog.speak()
cat.speak()
# tree.speak()  # Would raise AttributeError at runtime

# Strategy Pattern using Protocol:
# pro - static type checking support, no inheritance needed to conform
# con - requires classes (not just plain functions), no runtime enforcement
print_line("Protocol:")
dog = pDog()
cat = pCat()
tree = pTree() # runs just fine at runtime

do_speak(dog)
do_speak(cat)
# do_speak(tree)  # Static checker warns (yellow underline),
# at runtime will raise AttributeError if 'speak' is called but not implemented properly
