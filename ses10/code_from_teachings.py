class Person:

    def __init__(self):
        self.name = 'Hjordt' # public instance variabel
        self._age = 12
        self._gender = 'Male' # public variable skift til en property

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, x):
        if x in ['male','female']:
            self._gender = x

    def set_age(self, age):
        if age < 0:
            print('No no no')
        else:    
            self._age = age

    def get_age(self):
        return self._age
    