// C++ - Class Method Definition Calculator add
// Fill in the missing lines of code to define the class Calculator along with the method add so that the program accepts two integers as input and prints their sum as the output.










#include <iostream>
using namespace std;
class Calculator{
    public:
    int x,y;
    Calculator(int a,int b){
        x=a; y=b;
    }
    int add(){
        return x + y;
    }
};

int main()
{
    int a,b;
    cin >> a;
    cin >> b;
    Calculator calc{a,b};
    cout << calc.add();
    return 0;
}