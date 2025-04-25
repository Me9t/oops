#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    void sound() {
        cout << "Animals make sounds" << endl;
    }
};

// Derived class 1
class Dog : public Animal {
public:
    void bark() {
        cout << "Dog barks: Woof Woof!" << endl;
    }
};

// Derived class 2
class Cat : public Animal {
public:
    void meow() {
        cout << "Cat meows: Meow Meow!" << endl;
    }
};

int main() {
    Dog d;
    Cat c;

    d.sound();   // Inherited from Animal
    d.bark();    // Specific to Dog class

    c.sound();   // Inherited from Animal
    c.meow();    // Specific to Cat class

    return 0;
}
