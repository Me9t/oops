
import math

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def display(self):
        print(f"i = {self.i}, j = {self.j}, k = {self.k}")

    def magnitude(self):
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)

# Creating two objects
v1 = Vector(2, 3, 6)
v2 = Vector(1, 4, 2)

# Testing methods
v1.display()
print("Magnitude is:", v1.magnitude())
v2.display()
print("Magnitude is:", v2.magnitude())
