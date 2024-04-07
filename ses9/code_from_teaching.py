class Value:

    def __init__(self, data, op='', parrents=(), label=''):
        self.data = data
        self.label = label
        self.op = op
        self.parrents = parrents

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'værdien af data er: {self.data}'
    
    def __add__(self, other): # adds to objects of the same data type
        return Value(self.data + other.data, '+', (self, other) )

#a = Value(1)
#b = Value(2)

#print(b) 
