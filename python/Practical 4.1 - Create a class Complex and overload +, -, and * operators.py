# Practical 4.1
# Title: Practical 4.1 - Create a class Complex and overload +, -, and * operators

class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def display(self):
        if self.j >= 0:
            print(f"{self.i}+{self.j}i")
        else:
            print(f"{self.i}{self.j}i")

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Complex(self.i - other.i, self.j - other.j)

    def __mul__(self, other):
        real = self.i * other.i - self.j * other.j
        imag = self.i * other.j + self.j * other.i
        return Complex(real, imag)

# Creating objects
c1 = Complex(4, -3)
c2 = Complex(2, 5)

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Addition:")
c3 = c1 + c2
c3.display()

print("Subtraction:")
c4 = c1 - c2
c4.display()

print("Multiplication:")
c5 = c1 * c2
c5.display()
