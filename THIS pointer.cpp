#include <iostream>
using namespace std;

class Box {
private:
    double length;
    double width;
    double height;

public:
    // Constructor to initialize values
    Box(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Function to calculate volume
    double volume() {
        // Using the 'this' pointer to access member variables
        return this->length * this->width * this->height;
    }

    // Function to compare volumes of two boxes
    bool isEqual(Box& b) {
        // Using 'this' pointer to compare with another object
        return this->volume() == b.volume();
    }

    // Display box details
    void display() {
        cout << "Length: " << length << ", Width: " << width << ", Height: " << height << endl;
    }

    // Function to modify dimensions using the 'this' pointer
    void setLength(double length) {
        this->length = length;  // Using 'this' to distinguish from parameter
    }
    void setWidth(double width) {
        this->width = width;
    }
    void setHeight(double height) {
        this->height = height;
    }
};

int main() {
    // Create two objects of Box
    Box box1(3.5, 4.0, 5.0);
    Box box2(3.5, 4.0, 5.0);

    // Display volume and check if they are equal
    cout << "Volume of Box 1: " << box1.volume() << endl;
    cout << "Volume of Box 2: " << box2.volume() << endl;

    if (box1.isEqual(box2)) {
        cout << "The two boxes have the same volume." << endl;
    } else {
        cout << "The two boxes have different volumes." << endl;
    }

    // Modify the dimensions of box1 using 'this' pointer
    box1.setLength(4.0);
    box1.setWidth(4.5);
    box1.setHeight(6.0);

    cout << "Modified Box 1 details: ";
    box1.display();

    return 0;
}
