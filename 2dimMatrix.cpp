#include<iostream>
using namespace std;
class Maths{
	private:
		int matrix1[10][10];
		int matrix2[10][10];
		int result[10][10];
		int rows , cols;
		
	public:
		void getInput()
		{
			cout<<"Enter number of rows (max10)"<<endl;
			cin>>rows;
			
			cout<<"Enter number of colms (max10)"<<endl;
			cin>>cols;
			
			cout<<"Enter number for matrix 1 ";
			for(int i=0; i<rows;i++)
			{
				for(int j=0;j<cols;j++)
				{
					cout << "Element [" << i << "][" << j << "]: ";
					cin>>matrix1[i][j];
				}
			}
			
			cout<<"Enter number for matrix 2 ";
			for(int i=0; i<rows;i++)
			{
				for(int j=0;j<cols;j++)
				{
					cout << "Element [" << i << "][" << j << "]: ";
					cin>>matrix2[i][j];
				}
			}
	}
		
		void calculateMatrix()
		{	for(int i=0; i<rows;i++)
			{
				for(int j=0;j<cols;j++)
				{
						result[i][j]= matrix1[i][j] + matrix2[i][j];
				}
			}
		
		}
		 
		void display()
		{
			cout<<"result = \n";
			for(int i=0; i<rows;i++)
			{
				for(int j=0;j<cols;j++)
				{
					cout<<result[i][j]<<"\t";
				}
			cout<<endl;
			}
			
		}
		
};

int main()
{
Maths obj;
obj.getInput();
obj.calculateMatrix();
obj.display();
return 0;
}
