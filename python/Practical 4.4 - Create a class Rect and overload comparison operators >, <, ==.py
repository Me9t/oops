# Practical 4.4
# Title: Practical 4.4 - Create a class Rect and overload >, <, == operators based on area

class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

# Creating objects
r1 = Rect(5, 4)
r2 = Rect(6, 3)

print("Rect1 > Rect2:", r1 > r2)
print("Rect1 < Rect2:", r1 < r2)
print("Rect1 == Rect2:", r1 == r2)
