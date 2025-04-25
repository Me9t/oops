#include <iostream>
using namespace std;

class VolumeCalculator;  // Forward declaration of the second class

class Box {
private:
    double length;
    double width;
    double height;

public:
    // Constructor to initialize the dimensions of the box
    Box(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Friend function declaration
    friend double calculateVolume(Box b, VolumeCalculator v);
};

class VolumeCalculator {
private:
    double multiplier;

public:
    // Constructor to set multiplier
    VolumeCalculator(double m) {
        multiplier = m;
    }

    // Friend function declaration
    friend double calculateVolume(Box b, VolumeCalculator v);
};

// Friend function to calculate the volume
double calculateVolume(Box b, VolumeCalculator v) {
    return b.length * b.width * b.height * v.multiplier;  // Formula for volume
}

int main() {
    // Create Box object with dimensions (length=3.0, width=4.0, height=5.0)
    Box box1(3.0, 4.0, 5.0);

    // Create VolumeCalculator object with multiplier 1.2
    VolumeCalculator calculator(1.2);

    // Call the friend function to calculate volume
    double volume = calculateVolume(box1, calculator);

    // Output the result
    cout << "The volume of the box is: " << volume << endl;

    return 0;
}
