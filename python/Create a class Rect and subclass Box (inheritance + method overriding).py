
class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def display(self):
        print(f"Length = {self.l}, Breadth = {self.b}")

    def area(self):
        return self.l * self.b

class Box(Rect):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.h = h

    def display(self):
        print(f"Length = {self.l}, Breadth = {self.b}, Height = {self.h}")

    def area(self):
        return 2 * (self.l * self.b + self.b * self.h + self.h * self.l)

# Creating two Rect objects
r1 = Rect(4, 5)
r2 = Rect(6, 3)

r1.display()
print("Area of Rectangle:", r1.area())
r2.display()
print("Area of Rectangle:", r2.area())

# Creating two Box objects
b1 = Box(4, 5, 6)
b2 = Box(3, 7, 2)

b1.display()
print("Total Surface Area of Box:", b1.area())
b2.display()
print("Total Surface Area of Box:", b2.area())
