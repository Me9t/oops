

class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def display(self):
        print(f"{self.h}:{self.m}:{self.s}")

    def seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

# Creating two objects
t1 = Time(10, 30, 10)
t2 = Time(30, 12, 56)

# Testing methods
t1.display()
print("Time in seconds:", t1.seconds())
t2.display()
print("Time in seconds:", t2.seconds())
