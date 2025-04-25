#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Create and open a file "example.txt" to write data
    ofstream outFile("example.txt");

    // Check if the file is opened successfully
    if (!outFile) {
        cout << "Error opening the file for writing!" << endl;
        return 1;  // Return with an error code
    }

    // Writing text into the file
    outFile << "Hello, this is a text written to the file." << endl;
    outFile << "This is another line of text." << endl;
    outFile << "File handling in C++ is quite easy to understand!" << endl;

    // Close the file after writing
    outFile.close();

    // Now open the file to read and display its contents
    ifstream inFile("example.txt");

    // Check if the file is opened successfully
    if (!inFile) {
        cout << "Error opening the file for reading!" << endl;
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

