#include <iostream>
using namespace std;

int main() {
    int num = 5;           // Regular integer variable
    int *ptr = &num;       // Pointer to store address of num
    int **ptr2 = &ptr;     // Pointer to pointer to store address of ptr

    // Display the value of num using different levels of pointers
    cout << "Value of num: " << num << endl;             // Direct access
    cout << "Value of num using ptr: " << *ptr << endl;  // Using pointer ptr
    cout << "Value of num using ptr2: " << **ptr2 << endl; // Using pointer to pointer ptr2

    // Display the address of num using different levels of pointers
    cout << "Address of num: " << &num << endl;           // Direct address
    cout << "Address of num using ptr: " << ptr << endl;  // Using pointer ptr
    cout << "Address of num using ptr2: " << *ptr2 << endl; // Using pointer to pointer ptr2

    return 0;
}
