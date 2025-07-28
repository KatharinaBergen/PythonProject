from Animal import Animal
from DatabaseConnectionService import connect


# Save Objects
koala = Animal(
    name="Koala",
    species="Phascolarctos cinereus",
    age=4,
    habitat="Eucalyptus forest"
)
koala.save()

# Set age=3 for all animals with species="Cat"
Animal.objects(name="Koala").update(set__age=3)

#Delete one
#animal = Animal.objects(name="Luna").first()
#if animal:
#    animal.delete()

# Delete many
#Animal.objects(age__gt=10).delete()

#Fetch
for animal in Animal.objects:
    print(animal.to_json())