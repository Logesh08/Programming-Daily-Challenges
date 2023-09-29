// Python - C - 006

// Please convert the following Python code to C so that the C program executes successfully passing the test cases.

// #Length of strVal is always less than or equal to 100
// strVal = input().strip()
// #X is always less than Y
// X, Y = [int(val) for val in input().split()]
// print(strVal[:X])
// print(strVal[X:Y])
// print(strVal[-Y:])
 



// Max Execution Time Limit: 1000 millisecs


#include<stdio.h>
#include<stdlib.h>

int main()
{
    char str[101],temp;
    int x,y;
    scanf("%s\n",str);
    scanf("%d %d\n",&x,&y);
    
    temp = str[x];
    str[x] = '\0';
    printf("%s\n",str);
    str[x] = temp;
    
    temp = str[y];
    str[y] = '\0';
    printf("%s\n",&str[x]);
    str[y] = temp;
    
    printf("%s",&str[strlen(str)-y]);
}