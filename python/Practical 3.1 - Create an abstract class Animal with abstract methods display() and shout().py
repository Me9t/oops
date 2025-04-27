# Practical 3.1
# Title: Practical 3.1 - Create an abstract class Animal with abstract methods display() and shout()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def shout(self):
        pass

class Dog(Animal):
    def display(self):
        print("This is a Dog.")

    def shout(self):
        print("Dog says: Bhaw Bhaw!")

class Cat(Animal):
    def display(self):
        print("This is a Cat.")

    def shout(self):
        print("Cat says: Meow Meow!")

# Creating objects
d = Dog()
c = Cat()

d.display()
d.shout()
c.display()
c.shout()
