#include <iostream>
using namespace std;

int main() {
    int num = 10;        // A regular integer variable
    int* ptr = &num;     // Pointer ptr holds the address of num

    // Display the address of num using the address-of operator (&)
    cout << "Address of num: " << &num << endl;

    // Display the value of num using the pointer (dereferencing the pointer using *)
    cout << "Value of num using pointer: " << *ptr << endl;

    // Display the address stored in ptr (which is the address of num)
    cout << "Address stored in ptr: " << ptr << endl;

    // Display the value of num using the pointer ptr
    cout << "Value of num using pointer ptr: " << *ptr << endl;

    // Modify the value of num using the pointer ptr
    *ptr = 20;  // Dereferencing ptr to change the value of num

    // Display the new value of num
    cout << "New value of num after modification: " << num << endl;

    return 0;
}
