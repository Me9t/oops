#include <iostream>
using namespace std;

class Box {
private:
    double length;
    double width;
    double height;

public:
    // Constructor to initialize the box dimensions
    Box(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Friend function declaration
    friend double calculateVolume(Box b);
};

// Friend function definition
double calculateVolume(Box b) {
    // Accessing private members of Box class
    return b.length * b.width * b.height;
}

int main() {
    // Creating an object of Box class with dimensions
    Box box1(3.0, 4.0, 5.0);

    // Calling the friend function to calculate volume
    double volume = calculateVolume(box1);
    
    // Display the result
    cout << "The volume of the box is: " << volume << endl;

    return 0;
}
