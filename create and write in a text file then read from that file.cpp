#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Creating and opening a file to write
    ofstream outFile("example.txt");

    if (!outFile) {
        // If the file is not created/opened successfully
        cout << "Error opening the file for writing!" << endl;
        return 1;
    }

    // Writing data to the file
    outFile << "This is the first line in the file." << endl;
    outFile << "This is the second line in the file." << endl;
    outFile << "C++ File handling is quite easy!" << endl;

    // Closing the file after writing
    outFile.close();

    // Opening the file to read the data
    ifstream inFile("example.txt");

    if (!inFile) {
        // If the file is not found or cannot be opened
        cout << "Error opening the file for reading!" << endl;
        return 1;
    }

    string line;
    cout << "Reading from file:" << endl;

    // Reading each line from the file and displaying it
    while (getline(inFile, line)) {
        cout << line << endl;
    }

    // Closing the file after reading
    inFile.close();

    return 0;
}
