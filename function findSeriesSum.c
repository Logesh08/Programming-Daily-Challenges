// function findSeriesSum
// The function/method findSeriesSum accepts an argument str representing a string value. The string str contains a series of integers but some integers are denoted by their binary representations.

// The function/method findSeriesSum must find the decimal value for each binary representation in the given string. Then the function must return an integer representing the sum of all the integers present in the given series.

// Your task is to implement the function findSeriesSum so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Each integer value in the series <= 10^7

// Example Input/Output 1:
// Input:
// 45 32 1010 5 10111 60

// Output:
// 175

// Explanation:
// In the given series, two integers are denoted by their binary representations.
// 1010 -> 10
// 10111 -> 23
// Sum = 45 + 32 + 10 + 5 + 23 + 60 = 175.

// Example Input/Output 2:
// Input:
// 10 111 1005 1114 101

// Output:
// 2133




#include <stdio.h>
#include <stdlib.h>
#include<string.h>



int binaryTodecimal(char* bin_num)  
{  
    int val=0;
    for(int i=strlen(bin_num)-1;i>=0;i--){
        if(bin_num[i]=='1'){
            val+= pow(2,strlen(bin_num)-i-1);
        }
    }
    return val;
}  
 
int findSeriesSum(char *str)
{
    int sum=0;
    char *token = strtok(str," ");
    while(token!=NULL){
        int i=0,bol=1;
        while(token[i]!='\0'){
            if(token[i]!='0'&&token[i]!='1'){
                bol=0;
                break;
            }
            i++;
        }
        if(bol==1){
            sum+=binaryTodecimal((token));
        }else{
            sum+=atoi(token);
        }
        token=strtok(NULL," ");
    }
    return sum;
}

int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    printf("%d", findSeriesSum(str));
    return 0;
}