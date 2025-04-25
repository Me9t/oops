#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    Animal() {
        cout << "Animal constructor called!" << endl;
    }

    void sound() {
        cout << "Animals make sounds!" << endl;
    }
};

// Derived class
class Dog : public Animal {
public:
    // Constructor of derived class
    Dog() {
        cout << "Dog constructor called!" << endl;
    }

    void bark() {
        cout << "Dog barks: Woof Woof!" << endl;
    }
};

int main() {
    // Creating an object of the derived class
    Dog d;

    d.sound();  // Inherited function from Animal class
    d.bark();   // Function specific to Dog class

    return 0;
}
