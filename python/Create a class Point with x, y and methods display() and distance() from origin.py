
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"x = {self.x}, y = {self.y}")

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

# Creating two objects
p1 = Point(4, 3)
p2 = Point(3, 12)

# Testing methods
p1.display()
print("Distance from Origin:", p1.distance())
p2.display()
print("Distance from Origin:", p2.distance())
