# Practical 4.5
# Title: Practical 4.5 - Create a class Vector and overload == and != operators

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and self.k == other.k

    def __ne__(self, other):
        return not self == other

# Creating objects
v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 3)
v3 = Vector(4, 5, 6)

print("v1 == v2:", v1 == v2)
print("v1 != v3:", v1 != v3)
