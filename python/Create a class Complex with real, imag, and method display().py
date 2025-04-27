# Practical 1.5
# Title: Create a class Complex with real and imag, with display() method

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        if self.imag >= 0:
            print(f"{self.real}+{self.imag}i")
        else:
            print(f"{self.real}{self.imag}i")

# Creating two objects
c1 = Complex(4, -3)
c2 = Complex(-30, 2)

# Testing methods
c1.display()
c2.display()
