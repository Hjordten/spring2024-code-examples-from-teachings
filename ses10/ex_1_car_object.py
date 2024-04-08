class Car:
    def __init__(self, make, model, bhp, mph):
            self.make = make
            self.model = model
            self.bhp = bhp
            self.mph = mph

    @property
    def make(self):
          return self._make

    @make.setter
    def make(self, make):
          self._make = make     

    @property
    def model(self):
          return self._model

    @model.setter
    def model(self, model):
          self._model = model

    @property
    def bhp(self):
          return self._bhp

    @bhp.setter
    def bhp(self, bhp):
          self._bhp = bhp      

    @property
    def mph(self):
          return self._mph

    @mph.setter
    def mph(self, mph):
          self._mph = mph        
    
    def print_information(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"BHP: {self.bhp}")
        print(f"MPH: {self.mph}")
