// function getTotalPrice
// The function/method getTotalPrice accepts an argument str representing a text. The text contains the prices of some items as floating point values.

// The function/method getTotalPrice must return a floating point value representing the total price of the items mentioned in the text.

// Your task is to implement the function getTotalPrice so that the program runs successfully.

// Note: The total price will be printed with the precision up to 2 decimal places.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// Cost of 5 pens is 50.98 rupees. Cost of a pencil is 4.25.

// Output:
// 55.23

// Explanation:
// There are two prices (50.98 and 4.25) mentioned in the given text.
// So their sum is 55.23 which is printed as the output.

// Example Input/Output 2:
// Input:
// A is 5.60, B is 2.14, C is 100.58 and D is 50.6.

// Output:
// 158.92






#include <stdio.h>
#include <stdlib.h>
int isIntChar(char c){
    return (c>='0'&&c<='9')?1:0;
}
double getTotalPrice(char *str)
{
    int i=0,ind=0,set=0,floatFound=0;
    char temp[999999];
    float price = 0.0;
    while(str[i]!='\0'){
        char c=str[i];
        if(isIntChar(c)||(c=='.'&&isIntChar(str[i-1])&&str[i+1]!='\0'&&isIntChar(str[i+1]))){
            temp[ind++]=str[i];
            if(c=='.') floatFound=1;
            set = 1;
        }else{
            if(set){
                temp[ind]='\0';
                if(floatFound){
                    price += atof(temp);
                    floatFound=0;
                }
                ind=0;
                set=0;
            }
        }
        i++;
    }
    if(floatFound){
        temp[ind]='\0';
        price += atof(temp);
        
    }
    return price;
}
int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    double totalPrice = getTotalPrice(str);
    printf("%.2lf", totalPrice);
    return 0;
}