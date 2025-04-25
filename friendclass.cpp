#include <iostream>
using namespace std;

class B;  // Forward declaration of class B to be used in class A

class A {
    int x;  // Private member variable

public:
    A(int value) {  // Constructor to initialize x
        x = value;
    }

    // Declare class B as a friend so it can access private members of A
    friend class B;
};

class B {
public:
    void display(A &a) {
        // Since B is a friend of A, it can access the private member 'x'
        cout << "Value of x is: " << a.x << endl;
    }
};

int main() {
    A a(5);  // Create object of class A and initialize x using constructor
    B b;     // Create object of class B
    b.display(a);  // Call display function of class B

    return 0;
}
