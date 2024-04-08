class Number:

    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, x):
        if x < self.value:
            raise ValueError('no')    
        self._value = x
        