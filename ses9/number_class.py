class Number:
    def __init__(self, num, obj_name):
        self.num = num
        self.obj_name = obj_name

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.num + other.num, self.obj_name)
        elif isinstance(other, int):
            return Number(self.num + other, self.obj_name)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.num - other.num, self.obj_name)
        elif isinstance(other, int):
            return Number(self.num - other, self.obj_name)
        else:
            raise ValueError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num, self.obj_name)
        elif isinstance(other, int):
            return Number(self.num * other, self.obj_name)
        else:
            raise ValueError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.num / other.num, self.obj_name)
        elif isinstance(other, int):
            return Number(self.num / other, self.obj_name)
        else:
            raise ValueError("Unsupported operand type for /")

    def __str__(self):
        return f'{self.obj_name}: {self.num}'

# Example usage
a = Number(5, 'a')
b = Number(-4, 'b')

print(a + b)  # Output: a: 1
print(a - b)  # Output: a: 9
print(a * b)  # Output: a: -20
print(a / b)  # Output: a: -1.25
