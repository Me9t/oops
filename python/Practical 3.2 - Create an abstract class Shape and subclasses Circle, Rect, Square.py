# Practical 3.2
# Title: Practical 3.2 - Create an abstract class Shape and subclasses Circle, Rect, Square

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def display(self):
        print(f"Circle with radius: {self.r}")

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r * self.r

class Rect(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def display(self):
        print(f"Rectangle with length: {self.l}, breadth: {self.b}")

    def perimeter(self):
        return 2 * (self.l + self.b)

    def area(self):
        return self.l * self.b

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def display(self):
        print(f"Square with side: {self.s}")

    def perimeter(self):
        return 4 * self.s

    def area(self):
        return self.s * self.s

# Testing
c = Circle(7)
c.display()
print("Perimeter:", c.perimeter())
print("Area:", c.area())

r = Rect(4, 6)
r.display()
print("Perimeter:", r.perimeter())
print("Area:", r.area())

s = Square(5)
s.display()
print("Perimeter:", s.perimeter())
print("Area:", s.area())
