#include <iostream>
using namespace std;

// Base class
class LivingThing {
public:
    void live() {
        cout << "Living things are alive" << endl;
    }
};

// First derived class
class Animal : public LivingThing {
public:
    void eat() {
        cout << "Animals eat food" << endl;
    }
};

// Second derived class (child of Animal)
class Dog : public Animal {
public:
    void bark() {
        cout << "Dog barks loudly!" << endl;
    }
};

int main() {
    Dog d;
    d.live(); // from LivingThing class
    d.eat();  // from Animal class
    d.bark(); // from Dog class
    return 0;
}
