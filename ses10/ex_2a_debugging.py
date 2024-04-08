class C:
         def __init__(self, value):
             self._x = value

         @property
         def x(self):
             return self._x

         @x.setter
         def x(self, value):
             if value <= 100 and value >= 0:
                 self._x = value
             else:
                 raise ValueError('value should be between 0 and 100')