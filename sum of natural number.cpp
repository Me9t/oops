#include <iostream>
using namespace std;

class Natural {
private:
    int number[100];
    int n;

public:
    void getNumber() {
        cout << "Enter how many natural numbers to sum: ";
        cin >> n;

        while (n <= 0) {
            cout << "Enter number larger than 0: ";
            cin >> n;
        }

        for (int i = 0; i < n; i++) {
            number[i] = i + 1;
        }
    }

    int calculateSum() {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += number[i];
        }
        return sum;
    }

    void display() {
        cout << "Sum is: " << calculateSum() << endl;
    }
};

int main() {
    Natural obj;
    obj.getNumber();
    obj.display();
    return 0;
}
