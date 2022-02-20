// Evaluate Expression - Operators as Words
// The program must accept a string S representing an arithmetic expression. The expression contains the integer values and the operators in words (plus for +, minus for -, multiply for * and divide for /). The program must evaluate the expression from left to right and print the resulting integer value as the output.

// Note: The divide operator (/) must return the quotient when the numerator is divided by the denominator.

// Boundary Condition(s):
// 8 <= Length of S <= 1000
// 1 <= Each integer value <= 100

// Input Format:
// The first line contains S.

// Output Format:
// The first line contains an integer value representing the resulting integer.

// Example Input/Output 1:
// Input:
// 10 plus 20 minus 5 multiply 4 divide 50

// Output:
// 2

// Explanation:
// S = 10 plus 20 minus 5 multiply 4 divide 50
// = 10 + 20 - 5 * 4 / 50
// = 30 - 5 * 4 / 50
// = 25 * 4 / 50
// = 100 / 50
// = 2

// Example Input/Output 2:
// Input:
// 50 multiply 3 plus 21 plus 13 divide 3

// Output:
// 61







// s=input().replace('plus','+').replace('minus','-').replace('multiply','*').replace('divide','//').split()
// for i in range(1,len(s),2):
//     s[i+1]=str(eval(s[i-1]+s[i]+s[i+1]))
// print(s[-1])












// function addTrailingZeroes
// The function/method addTrailingZeroes accepts two arguments - SIZE and arr. The integer SIZE represents the size of the integer array arr.

// The function/method addTrailingZeroes must find the number of digits K in the largest integer in the given array. Then the function must add the trailing zeroes to the integers so that each integer in the array contains K digits. Finally, the function must print the sum of N revised integers.

// Your task is to implement the function addTrailingZeroes so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4
// 12 506 7 6893

// Output:
// 20153

// Explanation:
// Here N = 4.
// The largest integer among the 4 integers is 6893.
// The number of digits in 6893 is 4.
// After adding the trailing zeroes to the integers based on the given conditions, the integers become
// 1200 5060 7000 6893
// The sum of the 4 revised integers is 20153 which is printed as the output.

// Example Input/Output 2:
// Input:
// 5
// 600 12 40 78 147

// Output:
// 2047

// Example Input/Output 3:
// Input:
// 6
// 9 99 999 1 10 100

// Output:
// 3189











#include <stdio.h>
#include <stdlib.h>
#include<string.h>
void addTrailingZeroes(int SIZE, int arr[])
{
    int len = 0,i=0,sum=0;
    for(;i<SIZE;i++){
        char temp[1000001];
        sprintf(temp,"%d\0",arr[i]);
        int t = strlen(temp);
        if(len<t) len = t;
    }
    for(i=0;i<SIZE;i++){
        char temp[1000001];
        sprintf(temp,"%d\0",arr[i]);
        while(strlen(temp)!=len) strcat(temp,"0");
        sum+=atoi(temp);
    }
    printf("%d",sum);
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    addTrailingZeroes(N, arr);
    return 0;
}