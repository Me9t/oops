# Practical 3.3
# Title: Practical 3.3 - Create an abstract class Maruti and subclasses Zen and Swift

from abc import ABC, abstractmethod

class Maruti(ABC):
    @abstractmethod
    def display(self):
        pass

class Zen(Maruti):
    def display(self):
        print("This is a Maruti Zen.")

class Swift(Maruti):
    def display(self):
        print("This is a Maruti Swift.")

# Creating and testing objects
z = Zen()
s = Swift()

z.display()
s.display()
