#include<iostream>
using namespace std;

class Rectangle {
private:
    float breadth;
    float length;

public:
    // Function to get input from user
    void getInput() {
        cout << "Enter the length: ";
        cin >> length;
        cout << "Enter the breadth: ";
        cin >> breadth;
    }

    // Function to calculate area
    float calculateArea() {
        return length * breadth;
    }

    // Function to calculate perimeter
    float calculatePerimeter() {
        return 2 * (length + breadth);
    }

    // Function to display results
    void displayValue() {
        cout << "Area of the rectangle is: " << calculateArea() << endl;
        cout << "Perimeter of the rectangle is: " << calculatePerimeter() << endl;
    }
};

int main() {
    Rectangle rect;
    rect.getInput();
    rect.displayValue();
    return 0;
}
