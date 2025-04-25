#include<iostream>
using namespace std;

class Maths {
private:
    int matrix1[10][10];
    int matrix2[10][10];
    int result[10][10];
    int rows, cols;

public:
    // Function to input matrices
    void getInput() {
        cout << "Enter number of rows (max 10): ";
        cin >> rows;

        cout << "Enter number of columns (max 10): ";
        cin >> cols;

        cout << "Enter elements for Matrix 1:\n";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << "Element [" << i << "][" << j << "]: ";
                cin >> matrix1[i][j];
            }
        }

        cout << "Enter elements for Matrix 2:\n";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << "Element [" << i << "][" << j << "]: ";
                cin >> matrix2[i][j];
            }
        }
    }

    // Function to add the matrices
    void calculateMatrix() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
    }

    // Function to display the result matrix
    void display() {
        cout << "Result =\n";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << result[i][j] << "\t";
            }
            cout << endl;
        }
    }
};

// Main function
int main() {
    Maths obj;
    obj.getInput();
    obj.calculateMatrix();
    obj.display();
    return 0;
}

