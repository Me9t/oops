#include <iostream>
using namespace std;

class Calculator {
public:
    // Overloaded function to add two integers
    int add(int a, int b) {
        return a + b;
    }

    // Overloaded function to add three integers
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded function to add two floating-point numbers
    float add(float a, float b) {
        return a + b;
    }
};

int main() {
    Calculator calc;  // Create an object of Calculator class

    // Using the overloaded functions
    int sum1 = calc.add(5, 10);            // Calls add(int, int)
    int sum2 = calc.add(1, 2, 3);          // Calls add(int, int, int)
    float sum3 = calc.add(1.5f, 2.5f);     // Calls add(float, float)

    // Output results
    cout << "Sum of two integers: " << sum1 << endl;
    cout << "Sum of three integers: " << sum2 << endl;
    cout << "Sum of two floating-point numbers: " << sum3 << endl;

    return 0;
}
