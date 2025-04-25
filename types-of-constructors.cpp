#include <iostream>
using namespace std;

class Demo {
private:
    int x;

public:
    // 1. Default Constructor
    Demo() {
        x = 0;
        cout << "Default Constructor called. x = " << x << endl;
    }

    // 2. Parameterized Constructor
    Demo(int val) {
        x = val;
        cout << "Parameterized Constructor called. x = " << x << endl;
    }

    // 3. Copy Constructor
    Demo(const Demo &obj) {
        x = obj.x;
        cout << "Copy Constructor called. x = " << x << endl;
    }

    // Function to display x
    void display() {
        cout << "Value of x = " << x << endl;
    }

    // 4. Destructor
    ~Demo() {
        cout << "Destructor called for x = " << x << endl;
    }
};

int main() {
    cout << "Creating obj1 using Default Constructor" << endl;
    Demo obj1;

    cout << "\nCreating obj2 using Parameterized Constructor" << endl;
    Demo obj2(50);

    cout << "\nCreating obj3 using Copy Constructor (copy of obj2)" << endl;
    Demo obj3 = obj2;

    cout << "\n---Displaying all values---" << endl;
    obj1.display();
    obj2.display();
    obj3.display();

    cout << "\n---End of main()---" << endl;

    return 0;
}
