
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, classs, rollno):
        super().__init__(name, age)
        self.classs = classs
        self.rollno = rollno

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Class: {self.classs}, Roll No: {self.rollno}")

# Creating two Person objects
p1 = Person("Amit", 45)
p2 = Person("Neha", 30)

p1.display()
p2.display()

# Creating two Student objects
s1 = Student("Ravi", 18, "FYBSc CS", 101)
s2 = Student("Priya", 19, "FYBSc CS", 102)

s1.display()
s2.display()
