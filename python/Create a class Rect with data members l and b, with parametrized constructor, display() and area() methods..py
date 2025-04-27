# Practical 1.1
# Title: Create a class Rect with l and b, with display() and area() methods

class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def display(self):
        print(f"Length = {self.l}, Breadth = {self.b}")

    def area(self):
        return self.l * self.b

# Creating two objects
r1 = Rect(4, 8)
r2 = Rect(3, 9)

# Testing methods
r1.display()
print("Area is:", r1.area())
r2.display()
print("Area is:", r2.area())
