#include <iostream>
using namespace std;

// Global variable
int value = 100;

class ScopeExample {
private:
    int value;  // Class-level variable

public:
    void setValue(int value) {
        this->value = value;  // 'this->value' refers to class variable, 'value' is parameter
    }

    void showValues() {
        int value = 10;  // Local variable

        // Displaying values from different scopes
        cout << "Local value: " << value << endl;
        cout << "Class-level value (this->value): " << this->value << endl;
        cout << "Global value (::value): " << ::value << endl;
    }
};

int main() {
    ScopeExample obj;
    obj.setValue(50);  // Set class-level value
    obj.showValues();  // Display all values
    return 0;
}
