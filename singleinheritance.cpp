#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    void sound() {
        cout << "Animals make sounds" << endl;
    }
};

// Derived class (Single Inheritance)
class Dog : public Animal {
public:
    void bark() {
        cout << "Dog barks: Woof Woof!" << endl;
    }
};

int main() {
    Dog d;
    d.sound(); // function from base class
    d.bark();  // function from derived class
    return 0;
}