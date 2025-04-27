# Practical 4.6
# Title: Practical 4.6 - Create a class Complex and overload == and != operators

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self == other

# Creating objects
c1 = Complex(2, 3)
c2 = Complex(2, 3)
c3 = Complex(4, -1)

print("c1 == c2:", c1 == c2)
print("c1 != c3:", c1 != c3)
