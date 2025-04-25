#include <iostream>
using namespace std;

// Function to swap values using call by reference (using pointers)
void swap(int *a, int *b) {
    int temp;
    temp = *a;   // Dereferencing the pointer to get the value of a
    *a = *b;     // Dereferencing the pointer to assign the value of b to a
    *b = temp;   // Dereferencing the pointer to assign the value of temp to b
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

    // Calling the swap function (Call by Reference using pointers)
    swap(&x, &y);  // Passing the addresses of x and y

    // Displaying the values after swapping
    cout << "After swap - x: " << x << ", y: " << y << endl;

    return 0;
}
