#include <iostream>
using namespace std;

class Circle {
private:
    double radius;  // Private member to store radius

public:
    // Constructor to initialize the radius
    Circle(double r) {
        radius = r;
    }

    // Friend function declaration
    friend double calculateArea(Circle c);  // Friend function to calculate area
};

// Friend function definition
double calculateArea(Circle c) {
    // Accessing private member of the Circle class
    return 3.14159 * c.radius * c.radius;  // Area of a circle = p * radius^2
}

int main() {
    // Creating an object of Circle class with radius 5.0
    Circle circle1(5.0);

    // Calling the friend function to calculate the area
    double area = calculateArea(circle1);  // Calculate area of the circle

    // Display the result
    cout << "The area of the circle is: " << area << endl;

    return 0;
}
