#include <iostream>
using namespace std;

// Abstract class with a pure virtual function
class Shape {
public:
    // Pure virtual function
    virtual void draw() = 0; // No implementation here

    // Regular function (can be used directly)
    void display() {
        cout << "Displaying shape" << endl;
    }
};

// Derived class that overrides the pure virtual function
class Circle : public Shape {
public:
    // Implementation of the pure virtual function
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
};

// Another derived class that overrides the pure virtual function
class Square : public Shape {
public:
    // Implementation of the pure virtual function
    void draw() override {
        cout << "Drawing Square" << endl;
    }
};

int main() {
    // Shape s; // This will give an error because Shape is an abstract class

    // Create objects of derived classes
    Circle c;
    Square s;

    // Call the overridden draw function
    c.draw();  // Calls Circle's draw function
    s.draw();  // Calls Square's draw function

    // Call the regular function from the base class
    c.display();
    s.display();

    return 0;
}
