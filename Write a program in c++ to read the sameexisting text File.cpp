#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Open the file "example.txt" to read data
    ifstream inFile("example.txt");

    // Check if the file is opened successfully
    if (!inFile) {
        cout << "Error opening the file!" << endl;
        return 1;  // Return with an error code
    }

    // Read and display the content of the file
    string line;
    cout << "Contents of the file:" << endl;
    while (getline(inFile, line)) {
        cout << line << endl;
    }

    // Close the file after reading
    inFile.close();

    return 0;
}
