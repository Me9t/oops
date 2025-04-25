#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Open the file "example.txt" in append mode to add data to the file
    ofstream outFile("example.txt", ios::app);

    // Check if the file is opened successfully
    if (!outFile) {
        cout << "Error opening the file for appending!" << endl;
        return 1;  // Return with an error code
    }

    // Writing additional lines to the file
    outFile << "This is an appended line 1." << endl;
    outFile << "This is an appended line 2." << endl;
    outFile << "File handling in C++ can be done with append mode." << endl;

    // Close the file after appending
    outFile.close();

    cout << "Lines have been appended to the file successfully!" << endl;

    return 0;
}
