#include <iostream>
using namespace std;

// Base class 1 (for Multilevel Inheritance)
class Animal {
public:
    void sound() {
        cout << "Animals make sounds" << endl;
    }
};

// Base class 2 (for Multiple Inheritance)
class Bird {
public:
    void fly() {
        cout << "Birds can fly" << endl;
    }
};

// Derived class 1 (Multilevel Inheritance)
class Dog : public Animal {
public:
    void bark() {
        cout << "Dog barks: Woof Woof!" << endl;
    }
};

// Derived class 2 (Multiple Inheritance)
class Bat : public Animal, public Bird {
public:
    void hangUpsideDown() {
        cout << "Bats hang upside down" << endl;
    }
};

// Derived class (Hybrid Inheritance) - combining both
class Hybrid : public Dog, public Bat {
public:
    void display() {
        cout << "Hybrid class is using both Dog and Bat features." << endl;
        
        // Resolve ambiguity by specifying which base class method to use
        Dog::sound();           // From Animal class (inherited by Dog)
        bark();                 // From Dog class
        Bat::fly();             // From Bird class (inherited by Bat)
        hangUpsideDown();       // From Bat class
    }
};

int main() {
    Hybrid h;
    h.display(); // Show all features of the Hybrid class
    return 0;
}
