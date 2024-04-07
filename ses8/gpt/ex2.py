"""
Define a Simple Class: Create a class named Animal. Add two instance attributes: name and species, and initialize them through the constructor (__init__ method).

"""

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} ... {self.age}'

    def get_sound(self):
        return self.sound


dog = Animal('Fido', 112)
dog2 = Animal('Anna', '23', 'Female')
    



