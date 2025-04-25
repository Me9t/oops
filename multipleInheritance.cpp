#include <iostream>
using namespace std;

// Base class 1
class Animal {
public:
    void sound() {
        cout << "Animals make sounds" << endl;
    }
};

// Base class 2
class Bird {
public:
    void fly() {
        cout << "Birds can fly" << endl;
    }
};

// Derived class (Multiple Inheritance)
class Bat : public Animal, public Bird {
public:
    void hangUpsideDown() {
        cout << "Bats hang upside down" << endl;
    }
};

int main() {
    Bat b;
    b.sound();          // Inherited from Animal
    b.fly();            // Inherited from Bird
    b.hangUpsideDown(); // Specific to Bat class
    return 0;
}
