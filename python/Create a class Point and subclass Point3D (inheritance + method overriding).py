# Practical 2.2
# Title: Create a class Point and subclass Point3D with display() and distance() methods using Inheritance

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"({self.x}, {self.y})")

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# Creating two Point objects
p1 = Point(3, 4)
p2 = Point(5, 12)

p1.display()
print("Distance from Origin:", p1.distance())
p2.display()
print("Distance from Origin:", p2.distance())

# Creating two Point3D objects
p3 = Point3D(3, 4, 5)
p4 = Point3D(5, 12, 13)

p3.display()
print("Distance from Origin:", p3.distance())
p4.display()
print("Distance from Origin:", p4.distance())
