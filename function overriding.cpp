#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    // Virtual function to be overridden
    virtual void sound() {
        cout << "Animal makes a sound" << endl;
    }
};

// Derived class
class Dog : public Animal {
public:
    // Override the sound function
    void sound() override {
        cout << "Dog barks" << endl;
    }
};

// Derived class
class Cat : public Animal {
public:
    // Override the sound function
    void sound() override {
        cout << "Cat meows" << endl;
    }
};

int main() {
    Animal* animal;

    // Create objects of derived classes
    Dog dog;
    Cat cat;

    // Pointing to Dog object
    animal = &dog;
    animal->sound();  // Calls Dog's overridden sound()

    // Pointing to Cat object
    animal = &cat;
    animal->sound();  // Calls Cat's overridden sound()

    return 0;
}
