#include<iostream>
using namespace std;
class Rectangle{
    private:
        float breath;
        float length;
    
    public:
    void getInput(){
        cout<<"Enter A Length: ";
        cin>>length;
        cout<<"Enter a breath: ";
        cin>>breath;
    }
    
    float calculateArea(){
        return length*breath;
    }
    
    float calculatePerimeter(){
        return 2 * (length+breath);
    }
    
    void displayValue(){
        cout<<"Area of the rectangle is " <<calculateArea()<<endl;
        cout<<"Perimeter of the rectangle is "<<calculatePerimeter()<<endl;
    }
};



int main(){
    Rectangle rect;
    rect.getInput();
    rect.displayValue();
}