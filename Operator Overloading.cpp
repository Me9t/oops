#include <iostream>
using namespace std;

class Complex {
private:
    float real;
    float imag;

public:
    // Constructor to initialize real and imaginary parts
    Complex(float r = 0, float i = 0) {
        real = r;
        imag = i;
    }

    // Overload the '+' operator to add two complex numbers
    Complex operator+(const Complex& other) {
        Complex temp;
        temp.real = real + other.real;  // Add real parts
        temp.imag = imag + other.imag;  // Add imaginary parts
        return temp;
    }

    // Function to display the complex number
    void display() {
        if (imag >= 0)
            cout << real << " + " << imag << "i" << endl;
        else
            cout << real << " - " << -imag << "i" << endl;
    }
};

int main() {
    // Create two complex number objects
    Complex c1(3.5, 2.5), c2(1.5, 1.5);

    // Add two complex numbers using overloaded '+' operator
    Complex c3 = c1 + c2;

    // Display the result
    cout << "Result of c1 + c2: ";
    c3.display();

    return 0;
}
