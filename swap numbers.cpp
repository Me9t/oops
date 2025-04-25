#include <iostream>
using namespace std;

// Function to swap values using call by value
void swap(int a, int b) {
    int temp;
    temp = a;
    a = b;
    b = temp;

    // Displaying the swapped values inside the function
    cout << "After swap function - a: " << a << ", b: " << b << endl;
}

int main() {
    int x, y;

    // Taking input for two integers
    cout << "Enter the value of x: ";
    cin >> x;
    cout << "Enter the value of y: ";
    cin >> y;

    // Displaying the values before swapping
    cout << "Before swap - x: " << x << ", y: " << y << endl;

    // Calling the swap function (Call by Value)
    swap(x, y);

   

    return 0;
}
