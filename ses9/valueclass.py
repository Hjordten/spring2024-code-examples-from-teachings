class Value:

    def __init__(self, data, op='', parrents=(), label=''):
        self.data = data
        self.label = label
        self.op = op
        self.parrents = parrents


    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Værdien af data er: {self.data}'


    def __add__(self, other):
        return Value(self.data + other.data, '+', (self, other) )

