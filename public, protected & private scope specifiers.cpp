#include <iostream>
using namespace std;

// Creating a class to show public, private, and protected
class Example {
private:
    int a;  // private variable, used only inside class

protected:
    int b;  // protected variable, used inside class and derived class

public:
    int c;  // public variable, can be used anywhere

    // function to set values
    void setData() {
        a = 10;
        b = 20;
        c = 30;
    }

    // function to show values
    void showData() {
        cout << "Private value a = " << a << endl;
        cout << "Protected value b = " << b << endl;
        cout << "Public value c = " << c << endl;
    }
};

// child class to show use of protected and public
class Child : public Example {
public:
    void showChildData() {
        // cout << a;  // Not allowed because 'a' is private
        cout << "Accessing protected value b in child = " << b << endl;
        cout << "Accessing public value c in child = " << c << endl;
    }
};

int main() {
    Example obj;
    obj.setData();       // setting values
    obj.showData();      // showing values

    Child c1;
    c1.setData();        // child can also use public function
    c1.showChildData();  // child shows protected and public

    // Access outside class
    // cout << obj.a;     // Not allowed
    // cout << obj.b;     // Not allowed
    cout << "Accessing public value c from main = " << obj.c << endl;

    return 0;
}
