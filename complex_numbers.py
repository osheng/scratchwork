class ComplexNumber:
    def __init__(self, r: float, i: float):
        self.r = r
        self.i = i

    def __str__(self):
        if self.i >= 0:
            return "{} + i{}".format(self.r, self.i)
        else:
            return "{} - i{}".format(self.r, -self.i)

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return ComplexNumber(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __pow__(self, power, modulo=None):
        if power == 0:
            return ComplexNumber(1, 0)
        elif power % 1 == 0 and power > 0:
            return self * self ** (power - 1)
        else:
            return "you're asking for functionality which hasn't been implemented yet"


if __name__ == '__main__':
    a = ComplexNumber(2, -3)
    print(a ** 2.0)  # which should give you -5 - i12
