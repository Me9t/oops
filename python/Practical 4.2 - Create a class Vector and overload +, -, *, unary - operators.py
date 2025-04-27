# Practical 4.2
# Title: Practical 4.2 - Create a class Vector and overload +, -, *, and unary - operators

import math

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def display(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

    def magnitude(self):
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self, other):
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

    def __mul__(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k  # Dot product

    def __neg__(self):
        return Vector(-self.i, -self.j, -self.k)

# Creating objects
v1 = Vector(3, 2, 1)
v2 = Vector(1, -4, 2)

v1.display()
v2.display()

v3 = v1 + v2
print("Addition of Vectors:")
v3.display()

v4 = v1 - v2
print("Subtraction of Vectors:")
v4.display()

print("Dot Product:", v1 * v2)

print("Negation of v1:")
v5 = -v1
v5.display()

print("Magnitude of v1:", v1.magnitude())
