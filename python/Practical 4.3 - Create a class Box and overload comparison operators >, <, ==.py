# Practical 4.3
# Title: Practical 4.3 - Create a class Box and overload >, <, == operators based on volume

class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def volume(self):
        return self.l * self.w * self.h

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

# Creating objects
b1 = Box(2, 3, 4)
b2 = Box(3, 3, 3)

print("Box1 > Box2:", b1 > b2)
print("Box1 < Box2:", b1 < b2)
print("Box1 == Box2:", b1 == b2)
