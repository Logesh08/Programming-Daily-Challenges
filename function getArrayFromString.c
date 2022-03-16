// function getArrayFromString
// The function/method getArrayFromString accepts two arguments str and K representing a string value and an integer value respectively. The string str contains only digits.

// The function/method getArrayFromString must form K-digit integers from the given string based on the following conditions.
// - For every K digits in the given string, the function must form an integer. If there are leading zeroes in the K digits, then the function must move those leading zeroes to the end and form the integer.
// Then the function must return an array containing those K-digit integers.

// Note:
// - The length of the string is always divisible by K.
// - There will be at least one nonzero digit in every K digits.

// Your task is to implement the function getArrayFromString so that it passes all test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     int *arr;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 121021562005468058
// 3

// Output:
// 121 210 562 500 468 580

// Explanation:
// Here the given string is 121021562005468058 and the value of K is 3.
// The 3-digit integers formed from the string are given below.
// 121 -> 121
// 021 -> 210
// 562 -> 562
// 005 -> 500
// 468 -> 468
// 058 -> 580

// Example Input/Output 2:
// Input:
// 50000004
// 4

// Output:
// 5000 4000







#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

int getLen(int n){
    int lenght = 0;
    while(n>0){
        lenght++;
        n/=10;
    }
    return lenght;
}

boundedArray* getArrayFromString(char *str, int K)
{
    boundedArray *barr = malloc(9999999);
    barr-> arr = malloc(9999999);
    char tem[K+2];
    tem[0]='\0';
    int count = 0,ind = 0;
    for(int i=0;str[i]!='\0';i++){
        if(count==K){
            tem[count]='\0';
            int x = atoi(tem);
            while(getLen(x)!=K){
                x*=10;
            }
            barr->arr[ind++] = x;
            count=0;
        }
        tem[count++]=str[i];
    }
    int x = atoi(tem);
    while(getLen(x)!=K) x*=10;
    barr->arr[ind++]=x;
    barr->SIZE = ind;
    return barr;
}

int main()
{
    char str[101];
    int K;
    scanf("%s\n%d", str, &K);
    boundedArray *bArr = getArrayFromString(str, K);
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}