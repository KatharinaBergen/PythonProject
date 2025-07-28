from mongoengine import Document, StringField, IntField

#Define a model
class Animal(Document):
    name = StringField(required=True)
    species = StringField(required=True)
    age = IntField()
    habitat = StringField()