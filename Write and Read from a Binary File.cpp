#include <iostream>
#include <fstream>
using namespace std;

struct Person {
    char name[50];
    int age;
    float salary;
};

void writeToFile(const char* filename) {
    // Create and open a binary file to write data
    ofstream outFile(filename, ios::binary);

    if (!outFile) {
        cout << "Error opening file for writing!" << endl;
        return;
    }

    Person person1 = {"Alice", 30, 50000.0};
    Person person2 = {"Bob", 25, 40000.0};

    // Write data to the file in binary mode
    outFile.write(reinterpret_cast<char*>(&person1), sizeof(person1));
    outFile.write(reinterpret_cast<char*>(&person2), sizeof(person2));

    // Close the file after writing
    outFile.close();
    cout << "Data written to file successfully." << endl;
}

void readFromFile(const char* filename) {
    // Open the binary file to read data
    ifstream inFile(filename, ios::binary);

    if (!inFile) {
        cout << "Error opening file for reading!" << endl;
        return;
    }

    Person person;
    // Read data from the file
    while (inFile.read(reinterpret_cast<char*>(&person), sizeof(person))) {
        cout << "Name: " << person.name << ", Age: " << person.age << ", Salary: " << person.salary << endl;
    }

    // Close the file after reading
    inFile.close();
}

int main() {
    const char* filename = "people.dat";

    // Write data to the binary file
    writeToFile(filename);

    // Read data from the binary file
    readFromFile(filename);

    return 0;
}
