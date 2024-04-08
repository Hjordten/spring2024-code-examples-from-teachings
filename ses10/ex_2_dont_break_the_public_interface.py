class Square:
    def __init__(self, height, width):
        if height < 0 or width < 0: 
            raise ValueError("Height and width must be non-negative.")
        else:
            self._height = height   
            self._width = width


  
               